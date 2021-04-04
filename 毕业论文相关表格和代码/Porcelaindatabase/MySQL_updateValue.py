import pymysql
import argparse

# 输入参数，参数定义
def cli_parser():# 传参函数
    parser = argparse.ArgumentParser(description=__doc__)#变量名parser，
    parser.add_argument('-updataValue', help='The VALUE you want to updata')#添加接口
    parser.add_argument('-matchValue', help='The VALUE of matches ')#添加接口

    return parser

parser = cli_parser()
args = parser.parse_args()
Values = str(args.updataValue)
Matches = str(args.matchValue)

db = pymysql.connect(host="localhost",user="root",password="19970125",database="POTTERY")
cursor = db.cursor()
sql = "UPDATE EXAMPLE SET "+Values+"WHERE"+Matches

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()