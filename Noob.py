#LESONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\\22
def cem(a,b):
    return a+b
a=cem(4,8)
print(a)
#or
def cem(a,b):
    print(a+b)
cem(5,6)
###
print(type(a))
print(type(cem))

#
def kv(a):
    return a**2
a=kv(7)
print(a)
#or
print(kv(9))

###
#this makes our work easier(avoiding repeating of code)
def inform(name,no):

    print("""ad.{}               #without repeating
il.{}.""".format(name,no))

inform("elcin","1998")
inform("jack","1999")
##
def show(name,no):
    print("""ad:{},nomre:{}""".format(name,no))

show("elcin","1998")
#IF U dont want to use print)))
def fn():
    print("yazi")
fn()
#

#################LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\\23
def func():
    l=[x for x in range(0,100) if x%5==0]
    print(l)
func()


#
def func(smth):
    ll=[x for x in range(0,100) if x%smth==0]
    print(ll)

func(6)

####
"""def func(unknown):
    l3=[x for x in range(0,100)if unknown%7==0]
    print(l3)
func("elcin")"""
# above "smth" must be int otherwise it gives "type error"
#option to avoid this:
def func(deyer):
    try:

        l5=[x for x in range(0,100)if deyer%7==0]
        print(l5)
    except TypeError:
        print("hatali deyer")

func("elcin")

###
def funk(*args):  #*makes to get chrs as it is in tuple
    toplam=0
    for i in args:
        toplam+=i
    return toplam
print(funk(1,2,3,4,5,6,7,8,9))



#if u dont want use print))
def yazdir(*yazi):
    for i in yazi:
        print(i)
yazdir("elchin","b")

#
def s(r,p=3.14):
    return p*(r**2)
print(s(5))
#if u want to change p:
def s(r,p=3.14):

    return p*(r**2)
print(s(5,p=3))

#
print("ee","ll",sep="--",end="..")
print("ch","in",sep="--")
print("1998","10","12",sep=".")

#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN/24
c=7 #(global)
def vur(a,b):
    c=9
    print(c)#prints global c
    return a*b
print(c) #nonglobal(belongs to def)
print(vur(1,5))

##
c=8
def vur(a,b):
    global c #to use global c directly
    return a*b*c
print(vur(2,3))

#
def power(a,b):
    return a**b
print(power(5,2))
#we can write it in one raw>>>>>
p=lambda a,b:a**b
print(p(2,5))

#
tekcut=lambda x:x%2==0
print(tekcut(9))
#
y_n=lambda x:x%7==0 #bolunurse bura true olur
r=int(input("eded"))
if y_n(r):          #ve bura kecerek yes yazdirir
    print("yes")
else:
    print("no")#false olsa else-ye kecirr ve no



#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN/25
def bolenler(eded):
    l=list()
    for i in range(1,eded+1):
        if eded%i==0:
            l.append(i)
    return l
print(bolenler(45)) #this will be equal to "l"(liste) actually

#
def sade(eded):
    for i in range(2,eded):
        if eded%i==0:
            return False
        return True     #else:      #or can do using else
                           #return True
print(sade(12))


###
def sade(eded):
    for i in range(2,eded):
        if eded%i==0:
            return False
    return True     #else:      #or can do using else
                           #return True

while True:
    eded=int(input("write"))
    if sade(eded):
        print("yes")
    else:
        print("no")
    cixis=int(input("x to stop"))
    if cixis==x:
        break


##LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN/26
def ekob(a,b):
    big=max(a,b)
    l=list()
    for i in range(big,a*b+1):
        if i%a==0 and i%b==0:
            l.append(i)
    l.sort()
    return l[0]
print(ekob(3,5))

####
def ebob(a,b):
    sm=min(a,b)
    l=list()
    for i in range(1,sm+1):
        if a%i==0 and b%i==0:
            l.append(i)
            l.sort(reverse=True)
    return l[0]
print(ebob(18,42))


 #LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\\27


import math
print(dir(math))
#
print(math.ceil(2.1))
print(math.sqrt(25))
print(type(math))
print(math.factorial(5))

from math import*
a=factorial(6)
print(a)

#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN//28
#import game
#game.oyunabasla()  ####look again codes of game!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN//29
l=[1,2,3]
print(type(l))
###
class car():
    color="red"
    model="niva"
    s="motor"
car1=car()
print(car1.color,car1.model)

#
print(dir(car1))

##
class car():

    def __init__(self):
        print("nesne olusturuldu")

car1=car()

print("nesne olusmustu")

###

class car():

    def __init__(self,color,silindr,model):
        self.c=color
        self.s=silindr
        self.m=model

car1=car("blue",4,"rena") #car1=self(phyton use self because it doesnt know about car1 (beforehand))

car2=car("red",1,"niva")
print(car1.c,car1.s,car1.m)
print(car2.c,car2.s,car2.m)

####
class car():

    def __init__(self,color="yoxdu",silindr="idk",model="x"):#otherwise it cant print car3
        self.c=color
        self.s=silindr
        self.m=model
car3=car()
print(car3.c,car3.m)

car4=car(color="black")
print(car4.c)

#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN//30
class holding():

    def __init__(self,noofworkers,nameofHolding,patron,assistant,activity):

        self.w=noofworkers
        self.n=nameofHolding
        self.p=patron
        self.a=assistant
        self.ac=activity

    def buy_w(self,num):
        self.w+=num
    def fire_w(self,num):
        self.w-=num
    def changename(self,name):
        self.n=name
    def batir(self,name):
        self.ac=False
    def addpatron(self,name):
        self.p.append(name)
    def show(self):
        print("name:{}\nworkers:{}\npatrons:{}\nassistants:{}\nactivity:{}".format(self.n,self.w,self.p,self.a,self.ac))



mmc=holding(55,"unknown",["acun,huseyn"],["serdar,mustafa"],True)
mmc.show()
mmc.buy_w(10)
mmc.show()
mmc.addpatron("aydin")
mmc.show()

#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN//31
class isci():
    def __init__(self,salary,name,age):
        self.s=salary
        self.n=name
        self.a=age
    def goster(self):
        print("name:{}\nage:{}\nsalary:{}".format(self.n,self.a,self.s))

class yonetici(isci):
    pass

y1=yonetici("cem",1111,99)
y1.goster()
i1=isci("ali",100,21)
i1.goster()

#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN//32
##look again for incorrect codes and COMPLETE!!!!!!!!!!!!!!!!!!!!!!!!!!



import time
import random

class hit():
    def __init__(self,songs=[]):
        self.s=songs
        self.durum=True
        self.sound=100
        self.playingsong=""
    def volumeup(self):
        if(self,sound>=95):
            pass
        else:
            print("increasingvolume")
            time.sleep(2)
            self.sound+=5
            print("increaedvolume:{}".format(self.sound))

    def vol_down(self):
        if(self.sound<6):
            sel.s=0
        else:
            print("decreasing.V")
            time.sleep(2)
            print("decreased.V={}".format(self.sound))
            self.s-=5
    def addsong(self,song):
        self.s.append(song)
    def songlist(self):
        print(self.s)
    def choose_song(self):
        sayac=1
        for i in self.s:
            print("{}.{}".format(sayac,i))
        choose=int(input("song no:"))
        print("changing")
        sleep.time(2)
        self.playingsong=self.songs[choose-1]
        print("changed song={}".format(self.playingsong))
    def random_song(self):
        random_no=random.randint(0,len(self.s))
        self.playingsong=self.s[random_no]
    def off(self):
        self.durum=False
    def delete(self):
        choose=int(input("which one u wanna delete"))
        self.s.pop(choose-1)





o1=hit(songs=["kale-we go"])
while o1.durum:
    choose=int(input("no:"))
    if(choose==1):
        o1.choose_song()
    elif(choose==2):
        o1.volumeup()
    elif(choose==3):
        o1.vol_down()
    elif(choose==4):
        o1.random_song()
    elif(choose==5):
        o1.addsong()
    elif(choose==6):
        o1.delete()
    else:
        o1.off()
        
#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN//34


class country():
    pass
turkey=country()
print(dir(turkey))
print(turkey)
##
class country():
    def __init__(self,name,population):
        self.n=name
        self.p=population

    def __str__(self):
        return "c:{} p:{}".format(self.n,self.p)

    def __len__(self):
        return self.p
    def builder(self):
        return "MKA"



    pass
turkey=country("TURKEY",76000)
print(turkey)
print(len(turkey))
print(turkey.builder())

##del turkey #isnt defined
#print(turkey.builder())

#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN///35
try:
    fnum=int(input("firstnum:"))
    snum=int(input("secondnum:"))
    print("{}+{}={}".format(fnum,snum,fnum+snum))
except ValueError:
    print("qaqa adam kimi reqem yaz!")

##
while True:

    try:
        control=input("q to exit")
        if control=="q":
            break
        fnum=int(input("firstnum:"))
        snum=int(input("secondnum:"))
        print("{}/{}={}".format(fnum,snum,fnum/snum))
    except (ValueError,ZeroDivisionError):
        print("qaqa sifra bolme dana!")
##
try:
    fnum=int(input("firstnum:"))
    snum=int(input("secondnum:"))
    print("{}+{}={}".format(fnum,snum,fnum+snum))
except:
    print("something went wrong")#for all kinda errors
finally:
    print("finally bloku herturlu calisir")

#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN///35

def sum(a):
    if type(a)==list or type(a)==tuple:
        sum=0
        for i in a:
            sum+=i
        return sum
    else:
        raise ValueError("must enter list or tuple")
b=sum([1,2,3,4])
print(b)

try:
    c=sum(7)
    print(a)
except ValueError:
    print("liste ve ya demet giriniz")


#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN//36

dosya=open("reminder.txt","w")
print(type(dosya))

dosya.write("hhhhhhhh")
dosya.close()


dosya1=open("reminder1.txt","a")     #"w" eger dosya varsa siliyor ve tekrar yartiyor eger dosya yoka kendi basdan yartiyor zaten
                                    #"a" eger dosya vardisa ekleme yapiyor yoksa yaratiyor
print(type(dosya1))                #a kipi dosyayi editi engellemek icin
                                   #w kipi whatever dosyayi tekrar olusturmak icin


dosya1=open("C:/Users/Elchin/Desktop/usb/a.sd/LOST.DIR/here/reminder.txt","a")

##
while True:
    yazi=input("q to exit and smth to write:")
    if yazi=="q":
        break
    dosya1.write("\n{}".format(yazi))
dosya1=open("reminder.txt","a")


##
while True:
    yazi=input("q to exit and smth to write:")
    if yazi=="q":
        break
    dosya1.write("\n{}".format(yazi))
##
while True:
    yazi=input("q to exit and smth to write:")
    if yazi=="q":
        break
    dosya1.write("\n{}".format(yazi))

dosya1.close()



#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN///37




folder=open("elcin.txt","r") #r=read
folder.read()
dosya.close()


try:
    folder=open("elcin.txt","r") #r=read
    folder.read()
    folder.close()
except FileNotFoundError:
    print("yoxdu qaqa")


#then i created "elcin"txt=no error anymore

##

try:
    folder=open("elcin.txt","r")
    for i in folder:
        print(i)
except FileNotFoundError:
    print("yoxdu qaqa")

folder.close()




try:
    folder=open("elcin.txt","r")
    icerik=folder.read()
    print(icerik)
    icerik2=folder.read()
    print(icerik2)
#after this code it doest make it write 2 time because inlec en axrda durur ve sorasi bos odugu icin yazdirmir

except FileNotFoundError:
    print("yoxdu qaqa")



try:
    folder=open("elcin.txt","r")
    print(folder.readline(),end="")#end=without bosluk aralarda
    print(folder.readline(),end="")

except FileNotFoundError:
    print("yoxdu qaqa")



try:
    folder=open("elcin.txt","r")
    siyahikimi=folder.readlines()
    print(siyahikimi)

    for i in siyahikimi:
        print(i)

except FileNotFoundError:
    print("yoxdu qaqa")

folder.close()


#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN//37

with open("elcin.txt","r") as folder:
    folder.read()
#these codes are the same but above u dont need to close very time as below
folder=open("elcin.txt","r")
folder.read()
folder.close()



try:
    with open("babayev.txt","r") as f:
        f.read()
except FileNotFoundError:
    print("yok boyle dosya")


try:
    with open("babayev.txt","r") as f:
        a=f.read()
        print(a)
        b=f.read()
        print(b)        #doest print b becasue of inlec's place

except FileNotFoundError:
    print("yok boyle dosya")



try:
    with open("babayev.txt","r") as f:
        print(f.tell()) # tell-shows inlec's place
        f.read()
        print(f.tell()) #at the end

        f.seek(5)  #seek-put inlec desired byte
        print(f.tell())
        b=f.read()
        print(b)

except FileNotFoundError:
    print("yok boyle dosya")



#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN///38

with open("babayev.txt","r+") as fol: #r+>>will print (6) byte

    a=fol.read(6)
    fol.write("elchin")
    print(a)



with open("babayev.txt","a") as fol: #r+>>will print (6) byte
    fol.write("elchin\n")



with open("babayev.txt","r+ ") as fol:
    icerik=fol.read()
    icerik="ELCH\n"+icerik
    fol.seek(0)
    fol.write(icerik)



with open("babayev.txt","r+") as fol:
    a=fol.readlines()
    a.insert(2,"engineering\n")
    fol.seek(0)
    for i in a:
        fol.write(i)

#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN//39

def sq(x):
    return x**2

print(list(map(sq,[1,2,3])))
#wee could do this like:longwayyyyy
def sq(liste):
    newlist=list()
    for i in liste:
        newlist.append(i**2)
    return newlist
print(sq([12,3,4]))

#
a=list(map(lambda x: x**2,[1,2,3,4,5,6]))
print(a)


#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN//40
from functools import reduce
a=reduce(lambda x,y: x+y,(1,2,3,4,5))
print(a)

#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN///41

liste=[12,34,56,78,44]
print(min(liste))
print(max(234,543))

#
worker=["calamity","me","you","we"]
maas=[1,22,23,43,41]
print(list(zip(worker,maas)))
#below the same but longer:
def pair(liste1,liste2):
    liste=list()
    for i in range(len(liste1)):
        liste.append((liste1[i],liste2[i]))
    return liste
words=["calamity","squender","pauper","prosecute"]

defn=["trouble","spendharshly","extrpoor","follow up"]

print(pair(words,defn))

#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN//42
def enumyapma(liste):
    bliste=list()
    for i in range(len(liste)):
        bliste.append((i,liste[i]))
    return bliste
print(enumyapma(["wail","pauper","fierce"]))

#same but shorter
for i,j in enumyapma(["matrimony","fugitive","bigamy","homecide"]):
    print("{}indexde,{} var".format(i,j))
#shortest way:enumerate
a=list(enumerate(["compel","awkward","venture","awesome"]))
print(a)


#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN//43
a=list(filter(lambda x:x%2==0,[x for x in range(100)]))
print(a)
#by list-compression:for simple works
a=[x for x in range(100) if x%2==0]
print(a)

#
def sade_di(x):
    for i in range(2,x):
        if x%i==0:
            return False

    return True
print(sade_di(19))
##
a=filter(sade_di,[x for x in range(1000)])
print(list(a))

#LESSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN///44
def degerdondur(x):
    for i in x:
        if not i:           #in this case ,not true=false,then it goes to 'return false'
            return False
    return True
liste=[True,True,True,True]  #true>>return true

print(degerdondur(liste))

#easy way for this:
liste=[True,True,True,False,True]
print(all(liste))
print(any(liste))                     #'all' means all have to be 'true' to be true,otherwise itll be 'false'
                                      #'any' if any of them is true,itll be true
