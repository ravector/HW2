from pandas import DataFrame 
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties 

myfont = FontProperties(fname="C:\Windows\Fonts\msyh.ttc", size=14)
url='https://quality.data.gov.tw/dq_download_csv.php?nid=72460&md5_url=d5052e0d88dd5f4e2d8683f657c5557d'
data = pd.read_csv(url)
print(data)
# x = []
# for i in range(len(data['鄉鎮別'])-1):
#     x.append(data['鄉鎮別'][i])
    
x = list(data['鄉鎮別'][0:13])
# y = []
#for i in range(len(data['人口數'])-1):
#    y.append(data['人口數'][i])

y = list(data['人口數'][0:13])


# for i in data['鄉鎮別']:
#     x.append(i)
# print(x)

print(data['人口數'][0:13])

df = DataFrame(y,x) 
ax = df.plot(kind = 'bar', rot = 0,legend=False) 
for label in ax.get_xticklabels() :
    label.set_fontproperties(myfont)
# plt.title("籌碼",fontproperties=myfont)
plt.xlabel('鄉鎮',fontproperties=myfont)
plt.ylabel('人口數',fontproperties=myfont)


plt.show()

