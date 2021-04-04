import pymysql
import argparse

# 输入参数，参数定义
def cli_parser():# 传参函数
    parser = argparse.ArgumentParser(description=__doc__)#变量名parser，
    parser.add_argument('-addValue', help='The VALUE you want to insert')#添加接口

    return parser

parser = cli_parser()
args = parser.parse_args()
Values = list(args.addValue)

db = pymysql.connect(host="localhost",user="root",password="19970125",database="POTTERY")
cursor = db.cursor()
sql = "INSERT INTO EXAMPLE(Registration_Number,Excavation_Site_Number,\
                SoilLayer_Coding,SoilLayer,Assumable_Year,Stages,Porcelain_TYPE,\
                General_Description,Specific_Feature,Porcelain_Dimensions,\
                Porcelain_Ornamentation,Porcelain_Glaze_Color,Porcelain_Glaze)  \
                VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

try:
    cursor.execute(sql,tuple(Values))
    db.commit()
except:
    db.rollback()

db.close()