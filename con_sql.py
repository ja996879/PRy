import sqlite3

class Sql3:
  
   def __init__(self):
       self.conn = sqlite3.connect('PRy.sqlite')
       
       
   def s_sql(self,s_str):
        
        s_cursor = self.conn.execute(s_str)
        return s_cursor
     

      
   def i_sql(self, i_str , *args):
      if len(args)==2:
       try: 
        u_coursor = self.conn.execute(i_str ,(args[0],args[1]))
        self.conn.commit()
        return True
       except sqlite3.Error:
        return False
       
       
   def u_sql(self,u_str , *args):
      try: 
        u_coursor = self.conn.execute(u_str ,(args[0],args[1]))
        self.conn.commit()
      except sqlite3.Error:
        print("update error")

   def d_sql(self,d_str, *args):
      try:
      
        d_coursor = self.conn.execute(d_str , [args[0]])
        self.conn.commit()
      except:
        print("delete error")
       
   def del_con(self):
      self.conn.close()
      
   def t_s(self):
      print("success")




'''
x=Sql3()
cursor=x.s_sql("SELECT * from products;")
for row in cursor:
      print("id=" , row[0])
      print ("name=",row[1])

cursor=x.u_sql("update user set name='yayahello' where name='lin'")
cursor=x.d_sql("delete from user where id=2")
for row in cursor:
    print("id=" , row[0])
    print ("name=",row[1])
'''