import requests
from lxml import etree
from core import db
#import db

class TYSpider(object):
    """
    功能:天眼查数据爬取爬虫
    """
    def __init__(self):
        """
        功能:初始化方法
        """
        self.url = "https://www.tianyancha.com"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safa    ri/537.36"}

    def request_search(self,company_name):
        """
        功能:http请求方法
        参数:company_name 搜索的公司名称
        """
        url = self.url + "/search?"
        params = dict()
        params["key"] = company_name
        response = requests.get(url,headers = self.headers,params = params)
        if response:
            return response.content.decode()
        else:
            return None

    def analyse_search_res(self,html_str):
        """
        功能:分析传入的html内容，找出对应公司id
        参数:html_str 传入的html文本
        返回值:有对应公司id则返回对应公司id，没有就返回None
        """
        html = etree.HTML(html_str)
        return html.xpath("//div[@class='result-list sv-search-container']/div/div/@data-id")

    def request_detail(self,company_id):
        """
        功能:请求详细公司信息
        参数:company_id 搜索请求爬取到的对应公司id
        """
        url = self.url + "/company/" + company_id
        response = requests.get(url,headers = self.headers) 
        if response:
            return response.content.decode()
        else:
            return None

    def analyse_detail(self,html_str):
        """
        功能:分析对应公司页面信息
        参数:html_str 对应公司html页面
        """
        company_name = ""
        phone = ""
        email = ""
        website = ""
        address = ""

        try:
            html = etree.HTML(html_str)
            company_name = html.xpath("//div[@class='header']/h1/text()")
            ret = html.xpath("//div[@class='in-block sup-ie-company-header-child-1']")
            phone = ret[0].xpath("./span[@onclick='openPhonePopup(this)']/text()")
            email = ret[1].xpath("./span[@onclick='openEmailPopup(this)']/text()")
            website = ret[2].xpath("./a/text()")
            address = ret[3].xpath("./text()")
        except Exception:
            pass
        #以下是使用三目运算符对数据进行处理
        company_name = company_name[0] if len(company_name) else ""
        phone = phone[0] if len(phone) else ""
        email = email[0] if len(email) else ""
        website = website[0] if len(website) else ""
        address = address[0] if len(address) else ""
        return company_name,phone,email,website,address

    def run(self,mode,company):
        """
        功能:爬虫运行方法
        参数:mode 爬取数据模式 1:爬取指定公司 2:从excel中导入公司名称爬取
             company 公司相关信息参数
        """
        if mode == 1:
            html = self.request_search(company) 
            id_list = self.analyse_search_res(html)
            print(id_list)
            for id in id_list:
                detail_html = self.request_detail(id)
                data = self.analyse_detail(detail_html)
                db.insert(data[0],data[1],data[2],data[3],data[4])
        elif mode == 2:
            for c in company:
                html = self.request_search(c) 
                id_list = self.analyse_search_res(html)
                for id in id_list:
                    detail_html = self.request_detail(id)
                    data = self.analyse_detail(detail_html)
                    db.insert(data[0],data[1],data[2],data[3],data[4])


if __name__ == "__main__":
    #db.db_connect()
    t = TYSpider()
    t.run(1,"江苏睿希")
