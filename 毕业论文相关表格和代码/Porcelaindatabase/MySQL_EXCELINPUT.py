
import pymysql
import xlrd
import argparse

# 输入参数，参数定义
def cli_parser():# 传参函数
    parser = argparse.ArgumentParser(description=__doc__)#变量名parser，
    parser.add_argument('-Excel_file', help='The input file, The path to the excel file.')#添加接口

    return parser

parser = cli_parser()#执行上方函数
args = parser.parse_args()#读出上方函数输出
file = str(args.Excel_file)

# 连接数据库
db = pymysql.connect(host="localhost",user="root",password="19970125",database="POTTERY")
cursor = db.cursor()

sql = "INSERT INTO EXAMPLE(Registration_Number,Excavation_Site_Number,\
                SoilLayer_Coding,SoilLayer,Assumable_Year,Stages,Porcelain_TYPE,\
                General_Description,Specific_Feature,Porcelain_Dimensions,\
                Porcelain_Ornamentation,Porcelain_Glaze_Color,Porcelain_Glaze)  \
                VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

# 读取Excel
data = xlrd.open_workbook(file)
for s in data.sheet_names():
    table = data.sheet_by_name(s)

    # 读取已有数据的行数
    cursor.execute("SELECT COUNT(*) FROM EXAMPLE")
    row_num = cursor.fetchone()[0]#数据库的行数
    for r in range(1,table.nrows):#把excel里面的每一行读进来
        Values = table.row_values(r)
        Values = ['无' if i == '' else i for i in Values]
        cursor.execute(sql,tuple(Values))#从list转化成数组
        db.commit()

db.close()