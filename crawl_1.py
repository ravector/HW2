import  matplotlib.pyplot as plt
import pandas as pd

url='https://quality.data.gov.tw/dq_download_csv.php?nid=72493&md5_url=9a518478ce5e43d6e9129cf9c044d9be'
data = pd.read_csv(url)
print(data)

plt.figure(figsize=(10, 5))

x = []
for i in range(len(data['年度'])):
    x.append(data['年度'][i])
y = []
for i in range(len(data['總人口數'])):
    y.append(data['總人口數'][i])

plt.plot(x,y,color='orange',linewidth=2.0,linestyle='-')
plt.show()

