# coding=UTF-8
import urllib.request
import urllib
from bs4 import BeautifulSoup
from d_help import s_Help
from export_excel import EXport_excel

class Y_sea:
  def __init__(self,ya_price,ya_word,ya_m_price):
     self.yh_price = ya_price
     self.yh_word = ya_word
     self.yhm_price = ya_m_price
     self.qs=urllib.parse.quote(self.yh_word)
     print(self.yh_price)
     print(self.yh_word)
     print(str(self.yhm_price))
  def ssprint(self):
     i=0
     y_page = 1
     y_limit = 0
     y_limit_add = 60
     y_dict = {}
     y_price = self.yhm_price
     hisa = int(self.yh_price)
     print(y_price)
     print("https://tw.search.bid.yahoo.com/search/auction/product?p=%s&qt=product&kw=%s&cid=0&clv=0&acu=0&property=auction&sub_property=auction&srch=product&aoffset=%s&poffset=0&pg=%s&sort=-curp&nst=1&act=srp&rescheck=1" %(self.qs,self.qs,y_limit,y_page))

     while i < 3:
       x = urllib.request.urlopen("https://tw.search.bid.yahoo.com/search/auction/product?p=%s&qt=product&kw=%s&cid=0&clv=0&acu=0&property=auction&sub_property=auction&srch=product&aoffset=%s&poffset=0&pg=%s&sort=-curp&nst=1&act=srp&rescheck=1" %(self.qs,self.qs,y_limit,y_page))
       
       #x = urllib.request.urlopen("https://tw.search.bid.yahoo.com/search/auction/product?p=intel+i3-6100&qt=product&kw=intel+i3-6100&cid=0&clv=0&acu=0&property=auction&sub_property=auction&srch=product&aoffset=0&poffset=0&pg=1&sort=-curp&nst=1&act=srp&rescheck=1")
       html = x.read()
       soup = BeautifulSoup(html,"html.parser")
       #print(soup.find_all('em',limit=60))
       
       
       #y_price = self.yhm_price
       #hisa = int(self.yh_price)
       yp_limit_top = y_price+hisa
       yp_limit_bottom = y_price-hisa
       q=0
       s_ar = soup.find_all('em',limit=60)

       c_ar = soup.select('.srp-pdtitle > a',limit=60)
       for x in c_ar:
         price = s_Help.Conver(s_ar[q].string)
         ypi=int(price)
         y_hisa=s_Help.Total(int(price),y_price)
         if  ypi >= yp_limit_bottom and ypi <= yp_limit_top :
            #print("產品:"+x.string+"\n價格:"+price+"\n差額:"+str(y_hisa))
            #print('------------------------------')
            y_dict[x.string]=[ypi,y_hisa]
         q+=1
       print("=====================================")
       print(y_dict)
       y_page+=1
       y_limit+=60
       i+=1
     
     yx = EXport_excel()
     yx.ExExcel(y_dict,hisa,y_price)
     

#露天 http://search.ruten.com.tw/search/s000.php?enc=u&searchfrom=searchf&k=arduino+mega&t=0&p=2   p is page_will
#yahoo https://tw.search.bid.yahoo.com/search/auction/product?p=amd+a6-3650&qt=product&kw=amd+a6-3650&cid=0&clv=0&acu=0   
#('kw','kw','省略幾筆','pg')
'''
ax=Y_sea()
ax.ssprint()
'''
