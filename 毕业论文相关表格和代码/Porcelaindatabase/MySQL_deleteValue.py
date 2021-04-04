import pymysql
import argparse

# 输入参数，参数定义
def cli_parser():# 传参函数
    parser = argparse.ArgumentParser(description=__doc__)#变量名parser，
    parser.add_argument('- deleteValue', help='The matches you want to delete')#添加接口

    return parser

parser = cli_parser()
args = parser.parse_args()
Values = str(args.deleteValue)

db = pymysql.connect(host="localhost",user="root",password="19970125",database="POTTERY")
cursor = db.cursor()
sql = "DELETE FROM EXAMPLE WHERE"+Values

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()