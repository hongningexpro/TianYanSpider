# 天眼查企业数据爬虫

- 本程序基于基于python3版本编写，需要安装pymysql requests模块
- core目录下的db.py程序中需要修改本地mysql数据库连接信息
- bin目录下的为可以执行程序manage.py,python3 manage.py --help可以查看支持的命令行参数
- 目前还有功能不完善，批量企业数据爬取不支持，由于没带上cookies，只能爬取模糊数据

- 仅仅只是一个爬虫示例，好久之前写的，偶然间看到在电脑上，就保存到github吧。目前的url解析好多失效了，需要修改
- 需要修改的内容为core目录下 TYSpider.py文件中的 analyse_* 开头的方法
