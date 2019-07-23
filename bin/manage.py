import sys
import os
import getopt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import db,TYSpider

def usage():
    print("manage.py [--help] [--signel:company name] [--multiple] [--show] [--truncate]")

def help():
    print("--signel:parse designated company infomation")
    print("--multiple:parse company infomation depend on config")
    print("--show:show company infomations")
    print("--truncate:delete all existed company infomations")

def main(argv):
    try:
        opts,args = getopt.getopt(argv,"",["help","signel=","multiple","show","truncate"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    db.db_connect()
    spider = TYSpider.TYSpider()
    for opt,arg in opts:
        if opt == "--help":
            help()
        elif opt == "--signel":
            spider.run(1,arg)
        elif opt == "--multiple":
            pass
        elif opt == "--show":
            res = db.select_all()
            if len(res):
                for r in res:
                    print(r)
            else:
                print("there is no company infomation")
        elif opt == "--truncate":
            db.clear()



if __name__ == "__main__":
    main(sys.argv[1:])
