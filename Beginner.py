#-----------------------------14
p=3.14
r=float(input("radius:"))
l=2*p*r
print(type(l))

A=p*r**2
print(type(A))

print("uzunlugu:"+str(l)+"\nsahesi:"+str(A))



#_===========================================16. Pythonda String Formatlama



result=200/700
print("result is {}".format(result))
print("result is {:1.4}".format(result))
print("result is {:99.4}".format(result))

#f instead of format
print(f"result is {result}")



y



#-----------------------17===isalpha,split,strip,center,replace,find
word=" warden is guardiane of jail.Emerge is coming to orta"
print(word)

word=word.strip()
print(word)


#word=word.split()
#print(word)



word=word.split(".")
print(word)

word=".".join(word)
print(word)

index=word.find("jail")  #finds index of first ch of words
print(index)

word=word.replace('j','w')
print(word)

word=word.center(20,'*')
print(word)

word=word.lstrip("war")
print(word)

result=word.isalpha()
print(result)

print("temp")



#LESSON 18 important!!!

#-------------------------------------------------------------21

l=[1,2,3,4,5,6,7]
print(l)
l.insert(4,59)
print(l)

#-----------------------------------------------------------26(demo dictionary)


dics={}

w=input("soz:")
syn=input("sinonimi:")
ant=input("antonimi:")

dics.update({w:{"synonim":syn,"antonim":ant}})
print(dics)

#another way:
w=input("soz:")
syn=input("sinonimi:")
ant=input("antonimi:")

dics[w]={"s":syn,"a":ant}
print(dics)

#

wrd=input("w:")
dic=dics[wrd]
print(dic)

print(f"{wrd} sozunun sinonimi:{dic['synonim']} ve antonimi:{dic['antonim']}")





dics={}
w=input("soz=")
s=input("sinonimi=")
a=input("antonimi:")

dics.update({w:{'syn':s,'ant':a}})
print(dics)

w=input("soz=")
s=input("sinonimi=")
a=input("antonimi:")
dics[w]={"syn":s,"ant":a}
print(dics)

a=input("which word:")
dic=dics[a]
print(dic)

print(f"{a} sozunun sinonimi {dic['syn']} ve antonimi {dic['ant']}-dir")


#----------------------------------------------------------------------------------------27(sets)
#search about it(differnce between lists and sets)!!!!!!!!!!!!!!!!
#sets are like lists but indexlenmir and  i think no repetable objects are allowed in sets...



#------------------------------------------------28(Pythonda Value & Referans Veri Tipleri)

#search!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#value:string,number


x=6
y=4
print(x,y)
x=y
print(x,y)
y=8 #doesnt affect x
print(x,y)

#reference:lists
a=[1,2,3,4,5]
b=[11,12,13,14,15]
print(a,b)
a=b
print(a,b)
b[0]=22 #it affected a
print(a,b)


#----------------------------------------------------------------------------------30. Atama Operatörleri
x,y,z=5,10,20
print(x,y,z)
x,y=y,x
print(x,y,z)
#x=x+5 or x+=5

values=1,2,3
print(type(values))
x,y,z=values
print(x,y,z)

valuess=1,2,3,4,5,6,7,8
x,*y,z=valuess
print(x,y,z)


#---------------------------------------------------33. Karşılaştırma(comparison) Operatörleri

#clclte average

vize1=int(input("vize1 notu:"))
vize2=int(input("vize2 notu:"))
vize3=int(input("vize3 notu:"))

final=int(input("final notu:"))

average=(vize1+vize2+vize3)/3*0.6+final*0.4
print(f'averagepoint={average} and passed:{average>=51}')


#tekcift

eded=int(input("sayi giriniz:"))
r=eded%2==0
print(f"cut eded:{r}")


#pos or neg

sayi=int(input(":"))
r=sayi>0
print(f"eded positivdir:{r}")


#

ml=input("write your mail:")
psw=input("write your password:")

mail="elcin@mail.com"
password="abc"

m=ml.lower().strip()==mail
p=psw.strip()==password
print(f"girdiniz mail adresi:{m} ve sifre:{p}-dir ")



#logical operators--------------------------------------------------------34-35


x=6
r=(x>5 and x<10) and x%2==0
print(r)



sayi=int(input("sayi:"))
r=sayi>0 and sayi<100
print(r)


##

vize1=int(input("vize1 notu:"))
vize2=int(input("vize2 notu:"))
vize3=int(input("vize3 notu:"))

final=int(input("final notu:"))

average=(vize1+vize2+vize3)/3*0.6+final*0.4
result=average>51 and final>50
print(f'averagepoint={average}\npassed:{result}')


##

name=input("ad:")
k=int(input("kilo:"))
l=int(input("boy:"))

i=k/l**2

z=i>0 and i<18
print(f"zayif:{z}")

n=i>18 and i<25
print(f"normal:{n}")

s=i>25
print(f"sisman:{s}")



#------------------------------------36. Diğer Python Operatörleri

x=y=[1,2,3]
z=[1,2,3]

print(x==y)
print(x==z)
print(x is z)


#

x=[1,2,3]
y=[2,4]

del x[2]
y[1]=1
y.reverse()

print(x==y)
print(x is y)


#37. Bölüm Hakkında----------------------------38 Koşullu Durum Blokları - If ve Else Blokları
#-------------------------------------------39Koşullu Durum Blokları - If - Elif - Else

#---------------------------------------40. Uygulama-1: Koşullu İfadeler


#prava1

n=input("isminiz:")
a=int(input("yas:"))
e=input("egitim dereceniz(lise,uni,etc)")

if a>18 and (e=="lise" or e=="uni"):
    print("okey")

else:
    print("not enough age or education")

##prava2


n=input("isminiz:")
a=int(input("yas:"))
e=input("egitim dereceniz(lise,uni,etc)")


if a>18:
    if e=="uni" or e=="lise":
        print(f"MR.{n} enough age and enough education.Able to get prava:)")
    else:
        print(f"MR.{n} enough age but not enough education")
elif (a<=18) and (e=="uni" or e=="lise"):
    print(f"sorry {n} enough education but not enough age")

else:
    print(f"sorry {n},not enough age and education")



#sozlu yazili exam


n=input("adiniz:")
y1=int(input("yazili_1:"))
y2=int(input("yazili_2:"))
s=int(input("sozlu:"))

a=(y1+y2)/2*0.6+s*0.4

if a<=50:
    print("failed!")
elif a<=71:
    print(f"Dear {n},notunuz{a}=3")
elif a>71 and a<=90:
    print(f"Dear {n},notunuz{a}=4")
elif a>90 and a<=100:
    print(f"Dear {n},notunuz{a}=5")
else:
    print(f"Dear {n},something went wrong!")





import datetime

d=int(input("driving days:"))
a=datetime.now()-2018/8/1
if d<=365:
    print("light service")
elif d>365:
    print("normal service ")



import datetime
t=input("araciniz ne zaman trafige cikdi? ")
t=t.split('/')
trf=datetime.datetime(int(t[0]),int(t[1]),int(t[2]))

simdi=datetime.datetime.now()
fark=simdi-trf
days=fark.days

if days<=365:
    print("1ci servis")
elif days>365 and days<=365*2:
    print("2ci servis")
elif days>365*2 and days<=365*3:
    print("3cu servis")
else:
    print("4cu servis")


#41-----------------------------if else(demo2)

#0-100
sayi=int(input("sayiniz:"))
if sayi>=0 and sayi<=100:
    print("sayi 0-100 arsindadir")
else:
    print("0-100 arasinda bir sayi giriniz!!!")


#pos cift sayi:
s=int(input("sayiniz:"))

if s>0 and s%2==0:
    print("sayi cift ve pozitiv")
elif s>0 and s%2==1:
    print("positiv ama cift deyil")
else:
    print("sayiniz ne cift ne de pozitiv")



#reg control


ml=input("mailiniz:")
psw=input("sifreniz:")

m="e"
p="abc"

if ml==m:
    if psw==p:
        print("giris dogrulandi")
    elif psw!=p:
        print("yanlis sifre grdiniz!!!")
else:
    print("bu mailde bir kullanici yok:REG NOW!")




#comparis of a b c
a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))

if a>b and a>c:
    print('a')
elif b>a and b>c:
    print('b')
else:
    print('c')



#TMS1

v1=int(input("vize1 notu:"))
v2=int(input("vize2 notu:"))

f=int(input("final notu:"))

a=(v1+v2)/2*0.6+f*0.4

if (f>70) or (a>=51 and f>=34):
    print(f'{a} passed')
else:
    print(f'{a}failed')


###TMS2
v1=int(input("vize1 notu:"))
v2=int(input("vize2 notu:"))

f=int(input("final notu:"))


average must be at least 51 and final 34but if final is 70 or more
student passes regardless to average point

a=(v1+v2)/2*0.6+f*0.4

if a>=51 and f>=34 and f<70:
    print(f"{a}good average and final")
elif f<34:
    print(f"{a}failed...low final note!")
elif f>=70 and f<=100:
    print(f'{a}passed with high final note')

else:
    print(f'{a} isnt reasonable point!!!')


#tms a:

v1=int(input("vize1 notu:"))
v2=int(input("vize2 notu:"))

f=int(input("final notu:"))

a=(v1+v2)/2*0.6+f*0.4

if a>50:
    if f>=50:
        print(f'{a}:passed')
    else:
        print(f'{a}:failed;final must be at least 50')
else:
    print(f'{a}:failed,low average')

#tms b:

v1=int(input("vize1 notu:"))
v2=int(input("vize2 notu:"))

f=int(input("final notu:"))

a=(v1+v2)/2*0.6+f*0.4

if a>=50:
    print(f'{a} passed:good average')
else:
    if f>=70:
        print(f'{a} passed:only high final')
    else:
        print(f'{a} failed')







#42. Bölüm Hakkında---------------------------------------43. Pythonda For Döngüleri
tuple=[(1,2),(3,4),(5,6)]
for i in tuple:
    print(i)
#
for i,x in tuple:
    print(i,x)

d={'k1':1,'k2':2,'k3':3}
for item in d:
    print(item) #keys

for i in d.items():
    print(i)


##
for key,value in d.items():
    print(key)

for a,b in d.items():
    print(a) #same and shows keys


#---------------------------------------------44(for dongu demo)
#
s=[1,3,5,7,9,12,19,21]

for i in s:
    if i%3==0:
        print(i)

t=0 #toplam
for i in s:
    t+=i
print(f'toplam={t}')

for i in s:
    if i%2==1:
        sq=i**2
        print(f'squares of odds={sq}')

#
w=['jail','warden','pledge','pursue','wail']
for i in w:
        if len(i)<=5:
            print(i)

#kitle indexi app

name=input("ad:")
k=int(input("kilo:"))
l=float(input("boy:"))

i=k/l**2

if i>0 and i<=18.4:
    print(f'{name} {i} damn you thin bro')
elif i>18.4 and i<=24.9:
    print(f'{name} {i}:you are in good shape')
else:
    print(f' {name} {i} fitness wouldnt hurt')






#phones
phs=[
{'name':'s6','price':'700'},
{'name':'s','price':'700'},
{'name':'mi','price':'350'},
{'name':'redmi','price':'350'},
{'name':'iphone','price':'1000'}
]

t=0
for i in phs:
    a=int((i['price']))
    t+=a
print('toplam=',t)

#
for i in phs:
    if int(i['price'])<=500:
        print(i['name'])




#----------------------45.WHILE

x=1
while x<=100:

    if x%2==0:
        print(f'cift sayi {x}')
    else:
        print(f'tek sayi{x}')

    x+=1


print('bitdi...')


#

name='' #false
while not name.strip(): #means 'while True'
    name=input("nameiniz:")
print(f"hi dear,{name}")




#-------------------------46. Uygulama: While Döngüleri

#SAYILAR WHILE

#s=[1,3,5,7,9,12,19,21]

i=0
while i<=s.index(21):
    print(s[i])
    i+=1

#SAME:
i=0
while i<len(s):
    print(s[i])
    i+=1




#bas aradaki sayilar bit
bas=int(input('baslangic:'))
bit=int(input('bitis:'))

i=bas
while i<bit:
    print(i)
    i+=1

#tek sayilar
bas=int(input('baslangic:'))
bit=int(input('bitis:'))

i=bas
while i<bit:
    if i%2==1:

        print(i)
    i+=1



#1-100

i=100
while i>0:
    print(i)
    i-=1

##
l=[]
i=0
while i<5:
    n=int(input('sayiniz:'))
    l.append(n)
    i+=1
l.sort()
print(l)


##urunlerrr
urunler=[]
num=int(input('kac urun:'))

i=0
while i<num :
    nm=input('adi:')
    p=int(input('fiyati:'))

    urunler.append({'ad':nm,'fiyat':p})
    print(urunler)
    i+=1

for urun in urunler:
    print(f'urun ismi:{urun["ad"]} ve fiyati:{urun["fiyat"]}')



#------------------------------------------------47. Break ve Continue İfadeleri

x=1
t=0
while x<=100:
    t+=x
    x+=1
print(f'toplam={t}')

#
x=0
t=0
while x<=10:
    x+=1
    if x%2==0:
        continue
    t+=x

print(f'toplam={t}')

#------------------------------48.dongu metotlari:
range__


for i in range(11,110,20):
    print(i)

print(list(range(12,200,7)))

#
index=0
greeting='hello'

for i in greeting:
    print(f'{index}:deki harf {i}-dir')
    index+=1


#same:

index=0
greeting='hello'

for i in greeting:
    print(f'{index}:deki harf {greeting[index]}-dir')
    index+=1

#enumerate:
greeting='hello'

for index,item in enumerate(greeting):
    print(f'{index}:deki harf {item}-dir')

for item in enumerate(greeting):
    print(item)


zip:

l1=[1,2,3,4,5]
l2=['a','b','c','d','e']
l3=[100,200,300,400,500]

print(list(zip(l1,l2,l3)))

for item in zip(l1,l2,l3):
    print(item)
for a,b,c in zip(l1,l2,l3):
    print(a,b,c)

#----------------------------------49.list comp.
l=[]

for x in range(10):
    l.append(x**2)
print(l)

#with list comp:
l=[x**2 for x in range(10)]
print(l)


#!!look @ if temasinin evvelde ve sonda olmasina
n=[x*x for x in range(11) if x%3==0]
print(n)

n=[x*x  if x%3==0 else '3e bolunmur'  for x in range(11) ]
print(n)





#
g='hello'
l=[]

for i in g:
    l.append(i)
print(l)

#with l/c:
w=[i for i in g]
print(w)


##
il=[1998,2003,1995,1975,1983]

yas=[2021-i for i in il ]
print(yas)



#
r=[]
for x in range(3):
    for y in range(3):
        r.append((x,y))
print(r)


n=[(x,y) for x in range(3) for y in range(3)]
print(n)
#
n=[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(n)


#--------------------------50. Uygulama: Sayı Tahmin Uygulaması



#mine

import random
hak=int(input('kac hakda bulacacksin:'))
a=random.randint(0,100)
i=0
while hak>i:
    i+=1
    s=int(input(('sayi giriniz:')))

    if s>a:
        print('asagi:')
    elif s<a:
        print('yukari')

    else:
        print('tebrikler buldunuz')
        break



#hak=5
import random
r=random.randint(1,10)
hak=5
sayac=0

while hak>0:
    hak-=1
    sayac+=1
    t=100-(sayac-1)*20
    s=int(input('tahmininiz:'))


    if r==s:
        print(f'Tebrikler!!!{sayac} defada bildiniz!\ntoplam puaniniz{t}')
        break
    elif r>s:
        print('yukari')
    else:
        print('asagi')

#hak=input
import random
r=random.randint(1,10)
can=int(input('kac hakda bulacacksin:'))
hak=can

sayac=0

while hak>0:
    hak-=1
    sayac+=1
    t=100-100/can*(sayac-1)
    s=int(input('tahmininiz:'))


    if r==s:
        print(f'Tebrikler!!!{sayac} defada bildiniz!\ntoplam puaniniz{t}')
        break
    elif r>s:
        print('yukari')
    else:
        print('asagi')



#-------------------------------51.demo asal sayi

s=int(input('sayi giriniz:'))


if s==1:
    print('1 isnt defined yet as asal or nonasal')

for i in range(2,s):
    if s%i==0:
        print('asal deyil')
        break

    else:
        print('asal')
        break


s=int(input('sayi giriniz:'))
asalmi=True

if s==1:
    asalmi=False

for i in range(2,s):
    if s%i==0:
        asalmi=False
        break

if asalmi:
    print('sayi asal')
else:
    print('sayi asal deyil')


#52. Bölüm Hakkında-53. Pythonda Metotlar----------------------54. Fonksiyon Kullanımı
def grt(name='user'):
    print('hello '+name)
grt()
grt('elcin')



def grt(name):
    return 'hello '+name #in thus case when u use return the last one will work

msg=grt('Elchin')
msg=grt('Babayev')   #the last one will work

print(msg)

#
def total(n1,n2):
    return n1+n2
t=total(10,20)
t=total(10,22)
t1=total(99,1) #this will always work
t2=total(999,77) #also this)
print(t,t1)
print(t1)
print(t2)


#emekliliyekacyil kaldi:
def y(tev):
    return 2021-tev
yas=y(1998)
print(yas)

def emk(tev,ad):


    #DOCsTRING:tevelludunuze gore ememkliliyine ne kadar kaldigini hesaplar
    #INPUt:dogum yili
    #OUTPUT:kac yilin kaldigi

    yas=y(tev)
    kaldi=65-yas
    if kaldi>0:
        print(f'{ad} emekliliyinize {kaldi} yil kaldi')
    else:
        print(f'{ad} zaten emeklisiniz')
emk(1998,'elchin')
emk(1975,'someone')

print(help(emk))




#------------------------------55. Fonksiyon Parametreleri
#value type
def changeword(n):
    n='revive'

word='commence'
changeword(word)
print(word)

#reference type:
def chwords(n):

    n[0]='revive'
words=['commence','prohibit','solitary']

chwords(words)
print(words)
#(adres kopyalamasi+edit)=refernce type,in a word it is like n=words:

n=words
n[1]='molest'
print(words)
print(n)

#not adres kopyalamasi but smth like value type:
words=['resent','denounce','postpone']
n=words[:]   #slicing makes different lists without changing original lists
n[0]='angry'
print(words)
print(n)

#so words doesnt change:
def chwords(n):
    n[0]='revive'

chwords(words[:])
print(n)
print(words)




#
def add(a,b):
    return sum((a,b))

a=add(10,20)
print(a)
#or
print(add(10,40))
print(add(100,10))

#for 3 and 2 parameters
def add(a,b,c=0):
    return sum((a,b,c))

print(add(11,22,33))
print(add(22,222))

#for all number of parameters:
def add(*params):
    print(params) #so params is list
    return sum(params)
print(add(1,2,3,4))
print(add(4,5,6))


#alternative:
def add(*params):
    sum=0
    for i in params:
        sum+=i
    return sum
print(add(1,2,3,4))
print(add(4,5,6))



#indor to make dictioanry for users differnt type of infos:
def dicuser(**args):
    print(type(args))
    for key,value in args.items():
        print('{} is {}'.format(key,value))
dicuser(name='Elchin',age=22,city='zaqatala') #these will be in form of dict.
dicuser(name='Elch',age=23,city='zaqa',mail='@GMAIl')


##
def func(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
func(1,2,3,4,5,6,7,k1='defraud',k2='thorough')

#__________________________________________56(demo)

#1.
def yazdir(kelime,adet):
    print(kelime*adet)
f=yazdir('defraud\n',5)

#2.#!!!!!!!!!!!!!!difference of return and return + tab!!!search return!1!1!
def l(*args):
    liste=[]
    for i in args:
        liste.append(i)
    return liste   #!!!!!!!!!!!!!!difference of return and return + tab!!!search return!1!1!

f=l('a','b','c','d',1,2,3)
print(f)



#.3(asal sayi)!!!!!!!!!else-for temasi(else clause in for loop)!!!!!!!!!!!!!!!!!!


def asal(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi>1:
            for i in range(2,sayi):
                if (sayi%i==0):
                    break
            else:
                print(sayi)
sayi1=int(input('sayi1:'))
sayi2=int(input('sayi2:'))
asal(sayi1,sayi2)


#4.
def tb(sayi):
    l=[]
    for i in range(1,sayi+1):
        if sayi%i==0:
            l.append(i)
    return l

print(tb(20))



#---------------------57.Lambda Expressions, Map ve Filter
def sq(n): return n**2
r=print(sq(2))

#list(map)
def sq(n): return n**2
l=[1,2,3,4,5]
r=list(map(sq,l))  #map(func u use,list or array u use)
print(r)

#for map                #we use list or for to get output of map func
for i in map(sq,l):
    print(i)



#lambda:
n=[3,4,5,6,7]

r=list(map(lambda a:a**2,n))
print(r)

#
n=[3,4,5,6,7]
f=lambda a:a**2

r=list(map(f,n)) #or promoy) r=list(map(lambda a:a**2,n))
print(r)
#and
q=f(5) #we can use it as basic func
print(q)



#FILTER
def cut(n):return n%2==0
l=[11,12,13,14,16,17,18,22]
#res=list(filter(cut,l))
res=list(filter(lambda b:b%2==0,l))
print(res)
#
def cut(n):return n%2==0
l=[11,12,13,14,16,17,18,22]
c=lambda b:b%2==0
result=list(filter(c,l))
print(result)

p=c(l[2]) #it is 13
print(p)

#---------------------------58.Fonksiyonların Kapsamı : Global ve Yerel Değişkenler
x='global x'

def func():
    x='local x'
    print(x)

func()
print(x)


#
word='global string'
def wrd():
    word='Burden'
    def verb():
        print('to '+word)
    verb()
wrd()

#
word='global string'
def wrd():
    word='Burden'
    def verb():
        word='evade'
        print('to '+word)
    verb()
wrd()

#word='global string'
def wrd():
    #word='Burden'
    def verb():
        #word='evade'
        print('to '+word)
    verb()
wrd()


#
x=50
def test(x):
    print(f'x:{x}')

    x=100
    print(f'x changed to {x}')
test(x)

print(x)

#
x=50
def test():
    global x         #every operation to glb x in def test(),also affecs disardaki x
    print(f'x:{x}')  #because disardaki is global actually

    x=100 #also changes global x(disardaki)
    print(f'x changed to {x}')
test()

print(x) #globalx =100



#---------59. Uygulama: Bankamatik

EH={
'ad':'elcin',
'hesapno':'1234567',
'bakiye':3000,
'ek':2000
}
                  #EH and BH are refernce typesayni adresi temsil eder ve biz adrese gondermis oluyoruz
                  #
                  #bakiye ve s uzerindeki guncellemler disradaki objler uzerindde de guncellme yapar
                  #but if we had used; ad="ali",hesap='12345' vs bunlar value tip olucakdi ki
                  #there is  no affect of guncelleme.ve fonk icerisinde sadece kopyalama islemi yapilir
                  #
BH={
'ad':'babayev',
'hesapno':'98765432',
'bakiye':2000,
'ek':1000
}

def pcek(hesap,miktar):
    print(f"merhaba {hesap['ad']}")
    parasorgula(hesap)

    if hesap['bakiye']>=miktar:
        hesap['bakiye']-=miktar
        print('pullar hazirlanir')
    else:
        toplam=hesap['bakiye']+hesap['ek']

        if toplam>=miktar:
            ekh=input('ek hesapdan cekilsinmi?E(evet) or anybutton(hayir)...')
            if ekh=='e':
                ekhdan_cekilecek=miktar-hesap['bakiye']
                hesap['ek']-=ekhdan_cekilecek
                print(f"pullar hazirlanir...")
                parasorgula(hesap)
            else:
                print(f"canceled by user no:{hesap['hesapno']}\nToplam bakiye:{toplam}")
                parasorgula(hesap)
        else:
            print(f'sorry...yeterli paraniz yok{toplam}')



def parasorgula(hesap):
    print(f"{hesap['hesapno']} nolu hesabinizda\nbakiye:{hesap['bakiye']}\nekpara:{hesap['ek']}")


pcek(EH,3000)
pcek(EH,1000)



v1=float(input("vize1 notu:"))
v2=float(input("vize2 notu:"))

fn=float(input("final notu:"))

av=(v1+v2)/2*0.6+(fn*0.4)

a=(av>=50) and (fn>=50)

print(f"ortalamaniz:{av}  gecme durumunuz {a}")



if a>50:
    if f>=50:
        print(f'{a}:passed')
    else:
        print(f'{a}:failed;final must be at least 50')
else:
    print(f'{a}:failed,low average')
