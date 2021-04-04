import pymysql
import argparse

# 输入参数，参数定义
def cli_parser():# 传参函数
    parser = argparse.ArgumentParser(description=__doc__)#变量名parser，
    parser.add_argument('-Match', help='The INDEX you want to select')#添加接口
    parser.add_argument('-Value', help='The VALUE of matches ')#添加接口

    return parser

parser = cli_parser()
args = parser.parse_args()
Index = str(args.Match)
Values = str(args.Value)

db = pymysql.connect(host="localhost",user="root",password="19970125",database="POTTERY")
cursor = db.cursor()
sql = "SELECT * FROM EXAMPLE WHERE "+Values+" like "+Matches

try:
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        Rnumber = row[0]
        Enumber = row[1]
        Scoding = row[2]
        Slayer = row[3]
        Ayear = row[4]
        Stages = row[5]
        Ptype = row[6]
        Gdescription = row[7]
        Sfeature = row[8]
        Pdimensions = row[9]
        POrnamentation = row[10]
        Pglazecolor = row[11]
        Pglaze = row[12]

        print("Rnumber=%s,Enumber=%s,Scoding=%s,Slayer=%s,Ayear=%s,Stages=%s,Ptype=%s,Gdescription=%s,\
                Sfeature=%s,Pdimensions=%s,POrnamentation=%s,Pglazecolor=%s,Pglaze=%s"%
              (Rnumber,Enumber,Scoding,Slayer,Ayear,Stages,Ptype,Gdescription,Sfeature,Pdimensions,\
               POrnamentation,Pglazecolor,Pglaze))
except:
    print("Error:unable to fentch data")

db.close()