from pymysql import *

g_db = None

def db_connect():
    """
    功能:连接数据库接口
    """
    global g_db
    g_db = connect(host = "localhost",port=3306,user="root",password="hongning",database="TYSpiderDB",charset="utf8")
    if not g_db:
        print("database connect failed") 
    else:
        cur = g_db.cursor()
        cur.execute('create table if not exists company_info(id int primary key auto_increment,name varchar(30),tel varchar(15),\
                                                             email varchar(40),website varchar(40),address varchar(100))')
        cur.close()

def select_all():
    """
    功能:返回数据库表中所有数据
    """
    cur = g_db.cursor()
    cur.execute('select * from company_info')
    return cur.fetchall() 

def insert(name,tel,email,website,address):
    """
    功能:插入数据到数据库表
    """
    cur = g_db.cursor()
    sql_str = """insert into company_info  (name,tel,email,website,address) values("%s","%s","%s","%s","%s")"""%(name,tel,email,website,address)
    cur.execute(sql_str)
    g_db.commit()
    cur.close()

def clear():
    cur = g_db.cursor()
    cur.execute("delete from company_info")
    g_db.commit()
    cur.close()

if __name__ == "__main__":
    db_connect()
    clear()
    g_db.close()
