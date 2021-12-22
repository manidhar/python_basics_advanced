# create table inside database manidhar

import mysql.connector as mysqlconnect

class CreateTable:
    mysqldb=""
    
    def connectToDB(self,hostname,username,password):
        try:
            self.mysqldb=mysqlconnect.connect(host=hostname,user=username,passwd=password,use_pure=True) 
        except Exception as e:
            print("Error connecting to DB : ",str(e))
    
    def showDatases(self):
        try:
            print(self.mysqldb)
            cursor=self.mysqldb.cursor()
            cursor.execute("SHOW DATABASES")
            for db in cursor:
                print(db)
        except Exception as e:
            print("Error connecting to DB : ",str(e))
    
    def createTable(self,dbName,tablename,columns):
        try:
            cursor=self.mysqldb.cursor()
            query1="use "+dbName
            cursor.execute(query1)
            query="create table if not exists "+tablename+"("+columns+")"
            cursor.execute(query)
            self.mysqldb.commit()
        except Exception as e:
            print("Error connecting to DB : ",str(e))
    
    def insertData(self,dbName,tablename,columns,values):
        try:
            cursor=self.mysqldb.cursor()
            query1="use "+dbName
            cursor.execute(query1)
            query="insert into "+tablename+"("+columns+") values("+values+")"
            cursor.execute(query)
            self.mysqldb.commit()
        except Exception as e:
            print("Error inserting data : ",str(e))
    
    def fetchData(self,dbName,tablename,columns,condition):
        try:
            cursor=self.mysqldb.cursor()
            query1="use "+dbName
            cursor.execute(query1)
            query="select "+columns+" from "+tablename+" where "+condition
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("Error fetching data : ",str(e))
    
    def deleteData(self,dbName,tablename,condition):
        try:
            cursor=self.mysqldb.cursor()
            query1="use "+dbName
            cursor.execute(query1)
            query="delete from "+tablename+" where "+condition
            cursor.execute(query)
            self.mysqldb.commit()
        except Exception as e:
            print("Error deleting data : ",str(e))
    
    def deleteTable(self,dbName,tablename):
        try:
            cursor=self.mysqldb.cursor()
            query1="use "+dbName
            cursor.execute(query1)
            query="drop table "+tablename
            cursor.execute(query)
            self.mysqldb.commit()
        except Exception as e:
            print("Error deleting table : ",str(e))

    
    def closeConnection(self):
        try:
            self.mysqldb.close()
        except Exception as e:
            print("Error closing connection : ",str(e))