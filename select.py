import urllib.request
from bs4 import BeautifulSoup
x = urllib.request.urlopen('https://tw.search.bid.yahoo.com/search/auction/product?p=amd+a6-3650&qt=product&kw=amd+a6-3650&cid=0&clv=0&acu=0')
html = x.read()

soup = BeautifulSoup(html,"html.parser")
print(soup.find_all('em',limit=5))

s_ar=soup.find_all('em',limit=5)
for i in s_ar:
   print(i.string)
c_ar=soup.select('.srp-pdtitle > a',limit=5)
for x in c_ar:
   q=0
   print("產品:"+x.string+"\n價格:"+s_ar[q].string)
   q+=1
#露天 http://search.ruten.com.tw/search/s000.php?enc=u&searchfrom=searchf&k=arduino+mega&t=0&p=2   p is page_will
#yahoo https://tw.search.bid.yahoo.com/search/auction/product?p=amd+a6-3650&qt=product&kw=amd+a6-3650&cid=0&clv=0&acu=0   
