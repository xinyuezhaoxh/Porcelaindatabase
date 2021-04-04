import pymysql
db = pymysql.connect(host="localhost",user="root",password="19970125",database="POTTERY")
cursor = db.cursor()
#cursor.execute("SELECT VERSION()")
#data = cursor.fetchone()
#print ("Database vision : %s" % data)
cursor.execute("DROP TABLE IF EXISTS  EXAMPLE")
sql = """CREATE TABLE EXAMPLE(
         Registration_Number CHAR (100) NOT NULL,
         Excavation_Site_Number CHAR (100),
         SoilLayer_Coding CHAR (100),
         SoilLayer CHAR (100),
         Assumable_Year CHAR (100),
         Stages CHAR (100),
         Porcelain_TYPE CHAR (100),
         General_Description TEXT,
         Specific_Feature CHAR (100),
         Porcelain_Dimensions CHAR (100),
         Porcelain_Ornamentation CHAR (100),
         Porcelain_Glaze_Color CHAR(100),
         Porcelain_Glaze CHAR(100)
         )"""
cursor.execute(sql)
db.close()