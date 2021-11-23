import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime #de biet khi nao thi crawl data
import matplotlib.pyplot as plt
import matplotlib.animation as animation #Ve hinh data trong real time
from matplotlib import style
import json, time
#soup = bs4.BeautifulSoup(r.text, "html.parser")
#soup.find_all('div',{'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})                                          

# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=False, indent=4)
#     print(text)
# jprint(response.json())
# data = json.dumps(df, sort_keys=True, indent=4)pi
# with open('Hose data.json','w') as outfile:
#     outfile.write(data)
#Giu lai time, 
#a: ma co phieu 
#b (gia dong cua: closed price), 
#v (gia cao nhat: highest price), 
#w (lowest price), 
#n(khoi luong giao dich trong phien)
#FPT, MWG(TGDD), CMG (CMC), LC


url_hose = ('https://banggia.cafef.vn/stockhandler.ashx?center=1')
response_hose = requests.get(url_hose)
hose = pd.DataFrame.from_dict(pd.json_normalize(response_hose.json()), orient='columns')
hose = hose[['Time','a','b','c','d','v','w','n']]
hose = hose.nlargest(100, 'n')
print(hose)
hose.to_csv('./Source Code/Data/Hose data.csv', mode = 'a', header = False)

url_upcom = ('https://banggia.cafef.vn/stockhandler.ashx?center=9')
response_upcom = requests.get(url_upcom)
upcom = pd.DataFrame.from_dict(pd.json_normalize(response_upcom.json()), orient='columns')
upcom = upcom[['Time','a','b','c','d','v','w','n']]
upcom = upcom.nlargest(100, 'n')
print(upcom)
upcom.to_csv('./Source Code/Data/Upcom data.csv', mode = 'a', header = False)

url_hnx = ('https://banggia.cafef.vn/stockhandler.ashx?center=2')
response_hnx = requests.get(url_hnx)
hnx = pd.DataFrame.from_dict(pd.json_normalize(response_hnx.json()), orient='columns')
hnx = hnx[['Time','a','b','c','d','v','w','n']]
hnx = hnx.nlargest(100, 'n')
print(hnx)
hnx.to_csv('./Source Code/Data/HNX data.csv', mode = 'a', header = False)


    
