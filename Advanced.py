
#------------------------------------------------------------------------98. Beatifulsoup Kullanımı

from bs4 import BeautifulSoup

s=BeautifulSoup(htmldoc,'html.parser')
r=s.prettify()
r=s.title
r=s.head
r=s.body

r=s.title.name
r=s.title.string

r=s.h1
r=s.h2 #first h2
r=s.h2.string
r=s.h1.string

#findall all h2-s:
r=s.find_all('h2')
r=s.find_all('h2')[0] #first h2
r=s.find_all('h2')[1] #second h2

#same for div:
r=s.div
r=s.find_all('div')[1]
r=s.find_all('div')[1].ul
r=s.find_all('div')[1].ul.li
r=s.find_all('div')[1].ul.find_all('li')



#
r=s.div.findChildren()

#
r=s.div.findNextSibling()
r=s.div.findNextSibling().findNextSibling()
r=s.div.findNextSibling().findNextSibling()
r=s.div.findPreviousSibling().findNextSibling()



print(r)



#-----------------------------------------------------------------------99. Web Scraping: imdb
from bs4 import BeautifulSoup
import requests

url='https://www.imdb.com/chart/top/?ref_=nv_mv_250'

response=requests.get(url)
c=response.content
print(c)
#insetead of above one
h=requests.get(url).content

s=BeautifulSoup(h,'html.parser')
list=s.find('tbody',{'class':'lister-list'}).find_all('tr',limit=5)

for tr in list:
    title=tr.find('td',{'class':'titleColumn'}).find('a').text
    year=tr.find('td',{'class':'titleColumn'}).find('span').text.strip('()')
    print(title,year)




    rating=tr.find('td',{'class':'ratingColumn imdbRating'}).find('strong').text
    print(rating)
#print(list)



#-----------------------------------------------------------------------100. Web Scraping: n11
from bs4 import BeautifulSoup
import requests

url='https://www.n11.com/bilgisayar/dizustu-bilgisayar'
h=requests.get(url).content

s=BeautifulSoup(h,'html.parser')


#sadece bir urun icin bilgi elde edilir
f1=s.find('li',{'class':'column'}).find('div',{'class':'proDetail'}).find_all('a')[0].text.strip().strip('TL')
f2=s.find('li',{'class':'column'}).find('div',{'class':'proDetail'}).find_all('a')[1].text.strip().strip('TL')


n=s.find('li',{'class':'column'}).find('div',{'class':'pro'}).find('a').find('h3',{'class':'productName'}).text.strip()
print(n)
print(f1)
print(f2)

print(f"\nurun ismi:{n}\nfiyat:{f1}tl\nindirimli fiyat:{f2}tl")





#for dongusuyle tum urunler icin bilgi elde edile bilir
list=s.find_all('li',{'class':'column'},limit=2)

for l in list:
    name=l.div.a.h3.text.strip()
    link=l.div.a.get('href')
    #print(name)
    #print(link)
    op=l.find('div',{'class':'proDetail'}).find_all('a')[0].text.strip().strip('TL')
    np=l.find('div',{'class':'proDetail'}).find_all('a')[1].text.strip().strip('TL')
    #print(op)

    print(f"\nurun ismi:{name}\nfiyat:{op}tl\nindirimli fiyat:{np}")

#---------------------------------------------------------------------Section 16: Python ile Bot Yazımı

#---------------------------------------------------------------101. Selenium Nedir ve Nasıl Kurulur



#-----------------------------------------------------------102. Selenium Temelleri

from selenium import webdriver
import time

url='https://instagram.com/'

driver=webdriver.Chrome()
driver.get(url)

time.sleep(1)
driver.maximize_window()

print(driver.title)

time.sleep(2)
driver.close()
#-----------------------------------------------=---------------///////////////////Section 19: Veri Analizi: Numpy


120. Uygulama: Numpy






#----------------------------------116. Numpy Nedir ?


import numpy as np

#python list
py_list=[1,2,3,4,5,6]


#numpy_array
np_array=np.array([1,2,3,4,5,6,7,8,9])


multi_py=[[1,2,3],[4,5,6],[7,8,9]]
multi_np=np_array.reshape(3,3)
print(multi_np)
print(multi_py)

print(np_array.ndim)
print(multi_np.ndim)

print(np_array.shape)
print(multi_np.shape)
print('hi')



#-----------------------------------------------117. Numpy Dizileri ile Çalışma

r=np.array([1,2,3,4,5,6,7,8,9])
r=np.arange(1,10)
r=np.arange(1,10,3)
r=np.zeros(5)
r=np.ones(5)

r=np.linspace(0,10,5)

r=np.random.randint(0,10)
r=np.random.rand(3)
r=np.random.randn(3)


np_array=np.arange(50)
np_multi=np_array.reshape(5,10)


print(np_multi)
print(np_multi.sum(axis=1))
print(np_multi.sum(axis=0))


rnd=np.random.randint(10,100,10)print(rnd)
print(rnd.max())
print(rnd.mean())
r=rnd.argmax()


print(r)


#----------------------------------------118. Numpy Dizilerinin Indekslenmesi
n=np.array([0,5,10,15,20,25,50,75])
r=n[5]
r=n[0:3]
r=n[:3]
r=n[::-2]

n2=np.array([[0,5,10],[15,20,25],[50,75,85]])
#print(n2)
r=n2[2]
r=n2[2,1]
r=n2[:,1]
r=n2[:,0:2]
r=n2[-1:,0:2]
r=n2[-1,:]
r=n2[:3,:3]


#arr1=np.arange(0,10)
arr2=arr1   #reference>biz burda arr1in adresinin kopyasini arr2e vermis oluyoruz
            #ayni adresi gosteren iki farkli yapi olmus oluyor


arr2[0]=20
print(arr1)
print(arr2)#ayni adresde tutulduklaari icin ikis de guncellendi

#>>
arr2=arr1.copy() #arr2 farkli bir adresdeki bir liste oluyor
arr2[0]=20
arr1[0]=30
print(arr1)
print(arr2)




print(r)

#-----------------------------------119. Numpy Dizi Operasyonları

n1=np.random.randint(10,100,6)
n2=np.random.randint(10,100,6)

print(n1)
print(n2)

r=n1+n2
r=n1+10
r=n1*n2
r=np.sin(n1)
r=np.sqrt(n1)


mn1=n1.reshape(2,3)
mn2=n2.reshape(2,3)
#print(mn1)
#print(mn2)
r=np.vstack((mn1,mn2))



r=n1>=5
r=n1%2==0

print(n1[r])


print(r)



#--------------------------------------------------------------120.numpy demo

n=np.array([10,15,30,45,60])
n=np.arange(5,15)
n=np.arange(50,100,5)
n=np.zeros(10)
n=np.ones(10)
n=np.linspace(0,100,5)
print(n)
n=np.random.randint(10,30,5)
n=np.random.rand(10)
print(n)


mn=np.random.randint(10,50,15).reshape(3,5)
print(mn)
#n=n.sum(axis=0)

#print(mn)
n=mn.max()
#11> n=mn.()

n=mn.argmin()
print(n)


#13>
n=np.arange(10,20)
#n=n[:3]


n=n[::-1]


print(mn)
n=mn[0]
n=mn[1,2]
n=mn[0:3,0]
n=mn**2


mn=np.random.randint(-50,50,15).reshape(3,5)
print(mn)
n=mn>0
r=mn%2==0




print(n)
print(r)
c=r*n
print(mn[c])


#----------------------------122. Pandas Serileri
import pandas as pd
import numpy as np


n=[20,30,40,50]
l=['a','b','c','d']
d={'a':10,'b':20,'c':30,'d':40}

rn=np.random.randint(10,100,6)


ps=pd.Series(n)
ps=pd.Series(l)
ps=pd.Series(5,[1,2,3])
ps=pd.Series(d)
ps=pd.Series(rn)
print(ps)

ps=pd.Series([20,30,40,51],['a','b','c','d'])

r=ps[0]
r=ps[-1]
r=ps[-2:]
r=ps['a']
r=ps[['a','c']]

r=ps.ndim
r=ps.dtype
r=ps.shape
r=ps.sum()
r=ps+ps
r=ps+50
r=np.sqrt(ps)
r=ps>=50

r=ps%2==0


print(ps)
print(r)


opel2018=pd.Series([20,30,40,10],['astra','corsa','mokka','insignia'])
opel2019=pd.Series([20,30,40,10],['astra','corsa','Grandland','insignia'])

print(opel2018)
print(opel2019)

total=opel2018+opel2019
print(total['astra'])

#-------------------------123. Pandas DataFrame
import pandas as pd

s1=pd.Series([3,2,0,1])
s2=pd.Series([0,3,7,2])

data=dict(apples=s1,oranges=s2)

df=pd.DataFrame(data)

print(df)


#df=pd.DataFrame()


data=[['ahmet',50],['ali',60],['yagmur',70],['cinar',80]]
dic={'Name':['ahmet','ali','yagmur','cinar'],'Grade':[50,60,70,80]}
dic_list=[{'name':'met','grade':'50'},

{'name':'ahmet','grade':'50'},
{'name':'ahme','grade':'5'},
{'name':'ahm','grade':'0'}]

df=pd.DataFrame(data,columns=['name','grade'],index=[1,2,3,4],dtype=float)
df=pd.DataFrame(dic,index=[1,2,3,4])
df=pd.DataFrame(dic_list,index=[1,2,3,4])


print(df)



#-------------------------124. Pandas ile Farklı Dosya Tiplerinden Veri Okuma
import pandas as pd

df=pd.read_csv('sample.csv')
df=pd.read_json('sample.json')
df=pd.read_excel('sample.xlsx')

print(df)




#-------------------125. Pandas DataFrame ile Satır Sütun Seçimleri
import pandas as pd
from numpy.random import randn

df=pd.DataFrame(randn(3,3),index=['A','B','C'],columns=['column1','column2','column3'])
print(df)
print('\n')
r=df['column1']
r=df[['column1','column2']]


#loc('row','column')>>loc(':','column')
r=df.loc['A']
r=df.loc[:,'column2']
r=df.loc[:,:'column2']
r=df.loc['A':'B',:'column2']
r=df.iloc[2]
r=df.loc['A','column3']
r=df.loc[['A','B'],['column1','column2']]
df['column4']=pd.Series(randn(3),['A','B','C'])
df['column5']=df['column1']+df['column3']



#r=df.drop('column5',axis=1)
r=df.drop('column5',axis=1,inplace=False)


print(df)



print(r)
#print(df)


#--------------------------------------------126. Pandas DataFrame ile Filtreleme

import pandas as pd
import numpy as np

data=np.random.randint(10,100,75).reshape(15,5)
df=pd.DataFrame(data,columns=['column1','column2','column3','column4','column5'])

r=df.columns
r=df.head()
r=df.tail(8)

r=df['column1'].tail()
r=df.column1.head()
r=df[['column1','column2']].tail(3)
r=df[5:15][['column1','column2']].tail()

r=df>50


r=df[df['column1']>50][['column1','column2']]
r=df[(df['column1']>50) & (df['column2']<70)][['column1','column2']]
r=df[(df['column1']>50)|(df['column2']<70)][['column1','column2']]
r=df.query('column1>50 & column1%2==0')



print(r)

#----------------------------------128. Pandas DataFrame ile Groupby Kullanımı
import pandas as pd
import numpy as np

personeller={
    'calisan':['ahmet yilmaz','can erturk','hasan korkmaz','cenk saymaz','ali turan','rza erturk','mustafa can'],
    'departman':['insan kay','bilgi islem','muh','insan kay','bilgi islem','muh','insan kay'],
    'yas':[30,25,45,50,23,34,42],
    'semt':['kd','tz','mltp','tz','mltp','tz','kd'],
    'maas':[5000,3000,4000,3500,2750,6500,4500]
}

df=pd.DataFrame(personeller)
r=df['maas'].sum()
r=df.groupby('departman').groups
r=df.groupby(['departman','semt']).groups




semtler=df.groupby('semt')

for nme,grp in semtler:
    print(nme)
    print(grp)




r=df.groupby('semt').get_group('kd')

r=df.groupby('departman').sum()

r=df.groupby('departman')['maas'].mean()

r=df.groupby('semt')['yas'].mean()
r=df.groupby('semt')['calisan'].count()
r=df.groupby('departman')['maas'].min()
r=df.groupby('departman')['maas'].max()['muh']

r=df.groupby('departman').agg(np.mean)
r=df.groupby('departman')['maas'].agg([np.sum,np.mean,np.max])
r=df.groupby('departman')['maas'].agg([np.sum,np.mean,np.max]).loc['muh']
print(r)


#----------------------------------------------129. Pandas ile Kayıp ve Bozuk Veri Analizi
import pandas as pd
import numpy as np

data=np.random.randint(10,100,15).reshape(5,3)

df=pd.DataFrame(data,index=['a','c','e','f','h'],columns=['column1','column2','column3'])
df=df.reindex(['a','b','c','d','e','f','g','h'])
r=df

newcolumn=[np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df['column4']=newcolumn

r=df.drop('column1',axis=1)
r=df.drop(['column1','column2'],axis=1)
r=df.drop('a')
r=df.drop(['a','b','c'],axis=0)

r=df.isnull()
r=df.notnull()
r=df.notnull().sum()
r=df.isnull().sum()
r=df['column1'].isnull().sum()
r=df[df['column1'].isnull()]['column1']
r=df[df['column1'].notnull()]['column1']


r=df.dropna() #axis=0 by default
r=df.dropna(how='all')
r=df.dropna(subset=['column1','column2'],how='all')
r=df.dropna(thresh=2)
r=df.dropna(thresh=4) #en az sayoda noraml veri



r=df.size
r=df.isnull().sum().sum()
r=df.sum().sum()

def ortalama(df):
    toplam=df.sum().sum()
    adet=df.size-df.isnull().sum().sum()
    return toplam/adet

r=df.fillna(value=ortalama(df))


print(r)



#----------------------------------130. Pandas ile String Fonksiyonları Kullanımı
import pandas as pd
data=pd.read_csv('nba.csv')
data.dropna(inplace=True)

print(data.columns)



data['Player']=data['Player'].str.upper()
data['Player']=data['Player'].str.lower()


data['index']=data['Player'].str.find('a')
data=data[data.Player.str.contains('jordan')]
#data=data.Player.str.replace(' ','#')


data[['frst','last']]=data['Player'].loc[data['Player'].str.split().str.len()==2].str.split(expand=True)

#print(data)
print(data.head(10))


#---------------------------------131. Pandas ile Join ve Merge
import pandas as pd

customers={
    'ci':[1,2,3,4],
    'fn':['a','b','c','d'],
    'ln':['q','w','a','a'],

}

orders={
    'oi':[10,11,12,13],
    'ci':[1,2,5,7],
    'od':[2010,11,12,13]
}

df_c=pd.DataFrame(customers,columns=['ci','fn','ln'])
df_o=pd.DataFrame(orders,columns=['oi','ci','od'])

print(df_c)
print(df_o)

r=pd.merge(df_c,df_o,how='inner') #intersection of ci-s
r=pd.merge(df_c,df_o,how='left')  #according to left one
r=pd.merge(df_c,df_o,how='outer') #union

print(r)


r=pd.concat([df_a,df_b])#axis=0 by default>>satira gore alt alta birlesdirir
r=pd.concat([df_a,df_b,axis=1])#colonlar yan yana birlesdirilir



#-----------------------------------132. Pandas ile DataFrame Metotları
import pandas as pd
import numpy as np

data={
    'column1':[1,2,3,4,5],
    'column2':[10,20,13,45,20],
    'column3':['abccc','bcac','adeccc','cbcca','deca']
}





df=pd.DataFrame(data)
r=df
r=df['column2'].unique()
r=df['column2'].nunique()
r=df['column2'].value_counts()



def kare(x):
    return x*x

k2=lambda x:x*x

r=df['column1'].apply(kare)
r=df['column1'].apply(k2)
r=df['column1'].apply(lambda x:x*x)


r=df['column3'].apply(len)


r=len(df.columns)
r=df.info

r=df.sort_values('column3')
print(r)




df=pd.DataFrame(unwriten_data)
df=df.pivot_table(index='Ay',columns='Kategori',values='Gelir')




#----------------------------------133. Uygulama: Nba Oyuncularının Veri Analizi

import pandas as pd


df=pd.read_csv('nba.csv')


r=df.head(10)
r=len(df.index)

r=df['height'].mean()
r=df['height'].max()
#r=df['Player']['height'].max()
r=df[df['height']==df['height'].max()]['Player']


r=df[df['Player']=='Cliff Barker']['height'].iloc[0]

r=df.groupby('birth_city').mean()['height']

r=df['birth_city'].nunique()
r=df.groupby('birth_city')
r=len(r)

r=df['birth_state'].value_counts()




df=df.dropna()
r=df['Player'].str.contains('and')
r=df[r]

print(r)


#===========================134.ygulama: Youtube İstatistik Verilerinin Analizi


def function_that_prints():
    print("I printed")

def function_that_returns():
    print('**')
    return "I returned"

f1 = function_that_prints()
f2 = function_that_returns()
print("Now let us see what the values of f1 and f2 are")
print(f1)
print(f2)







#------------------------------------------136. Matplotlib ile Grafik Oluşturma
#Plot, SubPlot ve Axes
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4]
y=[1,4,9,16]
plt.plot(x,y,'o--r')
plt.axis([0,6,0,20])

plt.title('taytls')
plt.xlabel('x leybls')
plt.ylabel('y leybls')
plt.show()



x=np.linspace(0,2,100)

plt.plot(x,x,label='linear',color='black')
plt.plot(x,x**2,label='square')
plt.plot(x,x**3,label='cubic')

plt.legend()

plt.show()



x=np.linspace(0,2,100)

fig,axs=plt.subplots(2)

axs[0].plot(x,x,color='green')
axs[0].set_title('lin')
axs[1].plot(x,x**2,color='orange')
axs[1].set_title('sq')
plt.tight_layout()
plt.show()



x=np.linspace(0,2,100)
fig,axs=plt.subplots(2,2)
fig.suptitle('Graphs')


axs[0,0].plot(x,x,color='red')
axs[0,1].plot(x,x**2,color='blue')
axs[1,0].plot(x,x**3,color='green')
axs[1,1].plot(x,x**0.5,color='pink')

plt.show()


import pandas as pd
df=pd.read_csv('nba.csv')
print(df)

df=df.drop(labels=df.columns[0],axis=1).groupby('birth_state').mean()
df.plot(subplots=True)

plt.show()



#--------------------------------------------137. Matplotlib ile Figure Oluşturma
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-10,9,20)
y=x**3
z=x**2


f=plt.figure()

axes=f.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y,color='b')
axes.set_xlabel('xin labeli')
axes.set_ylabel('yini labeli')
axes.set_title('CUBE')



axes2=f.add_axes([0.15,0.6,0.25,0.25])

axes2.plot(x,z)
axes2.set_xlabel('xl')
axes2.set_ylabel('yl')
axes2.set_title('titless')

plt.show()




x=np.linspace(-10,9,20)
y=x**3
z=x**2

f=plt.figure()
axs=f.add_axes([0,0,1,1])
axs.plot(x,z,label='sq')
axs.plot(x,y,label='cube')
axs.legend(loc=4)
plt.show()



x=np.linspace(-10,9,20)
y=x**3
z=x**2

fig,axes=plt.subplots(2,1,figsize=(8,8))

axes[0].plot(x,y)
axes[0].set_title('zbab0')
axes[1].plot(x,z)
axes[1].set_title('zbab1')
plt.tight_layout()
plt.show()



#-------------------------------------138. Matplotlib ile Grafik Türler
import matplotlib.pyplot as plt

yil=[2011,2012,2013,2014,2015]

oyuncu1=[8,10,12,7,9]
oyuncu2=[7,12,5,15,21]
oyuncu3=[18,20,22,25,19]

plt.plot([],[],color='y',label='o1')
plt.plot([],[],color='r',label='o2')
plt.plot([],[],color='b',label='o3')


plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=['y','r','b'])
plt.legend()
plt.xlabel('yil')
plt.ylabel('gol sayi')
plt.title('dlssdfjdgmb')
plt.show()


goal_types='pen','sut','f'

goals=[12,5,7]
colors=['y','r','b']

plt.pie(goals,labels=goal_types,colors=colors,shadow=True,explode=(0.05,0.05,0.7),autopct='%1.1f%%')

plt.show()

