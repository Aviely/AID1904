import pymysql

#连接数据库
db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user = "root",
                     passwd = "123456",
                     database = "dict",
                     charset = "utf8")
#获取游标对象(用于进行数据操作的对象，承载操作结果)
cur = db.cursor()

# with open("linux.jpg","rb") as fd:
#     data = fd.read()
#     try:
#         sql = "insert into image (id,filename,data) values(1,'circle.jpg',%s)"
#         cur.execute(sql,[data])
#         db.commit()
#     except Exception as e:
#         db.rollback()
#         print(e)
sql = "select * from image where filename='circle.jpg'"
cur .execute(sql)
image = cur.fetchone()
with open(image[1],"wb") as f:
    f.write(image[2])
cur.close()
db.close()
