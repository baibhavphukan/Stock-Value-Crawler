import re
import urllib.request
#https://www.google.com/finance?q=
url = "https://finance.yahoo.com/quote/"
stock = input("Enter your stock:")
url = url + stock

from urllib.request import Request, urlopen
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#print(url)
data = urlopen(req).read()
data1 = data.decode("utf-8")
m = re.search("currentPrice",data1)
start = m.start()
end = start + 50
new = data1[start:end]
#print(new)
m = re.search('"fmt":"',new)
start = m.end()
new2 = new[start:]
#print(new2)
m = re.search('}',new2)
start = 0
end = m.end()-2
final = new2[0:end]
print("The value of",stock ,"is",final )
