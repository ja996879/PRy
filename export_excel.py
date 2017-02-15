# coding=UTF-8
import os
import xlsxwriter
from datetime import datetime
from con_sql import Sql3
class EXport_excel:
    
   def __init__(self):
       self.today_dt = datetime.now().strftime('%Y-%m-%d')
       self.us = os.getlogin()
          
   def w_excel(self):       
       
       workbook = xlsxwriter.Workbook("C:\\Users\\%s\\Desktop\\%s.xlsx" % (self.us,self.today_dt))
          
       worksheet = workbook.add_worksheet()


       worksheet.set_column('A:D', 20)
   
       xa=Sql3()
       xa_all=xa.s_sql("select a.pro_name,p.p_name,p.price from allpro as a inner join products as p on a.id=p.pn_name")
       
       z=0
       y=0
       for row in xa_all:
          worksheet.write(z, y, row[0])
          worksheet.write(z, y+1, row[1])
          worksheet.write(z, y+2, row[2])
          z+=1
       workbook.close()
       xa.del_con
   def ExExcel(self,e_info):
       print(e_info)
       z=0
       y=0
       e_workbook = xlsxwriter.Workbook("C:\\Users\\%s\\Desktop\\%s.xlsx" % (self.us,self.today_dt))
       ew_workbook = e_workbook.add_worksheet()
       ew_workbook.set_column('A:D', 20)
       for k,v in e_info.items():
          ew_workbook.write(z,y,k)
          ew_workbook.write(z,y+1,v[0])
          ew_workbook.write(z,y+2,v[1])
          z+=1
       e_workbook.close
         

'''
 
       a=EXport_excel()
       b={"a":[1,2]}
       a.ExExcel(b)
'''     

