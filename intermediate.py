#62/Nesne Tabanlı Programlama: Class--------------------------------------------------------------------------------
class Person:
    pass

p1=Person()
p2=Person()

print(p1)
print(p2)
print(type(p1))


##

class Person:
    #class attributes
    address='no info'

    #object attributes:
    #constructor(yapici method adlanir ve init otomotik calisir
    #cagirmaya gerek kalmadan)
    def __init__(self,ad,yil):  #self =p1 or p2
        self.name=ad
        self.year=yil
        print('init metodu calisti')

p1=Person('elcin',1998)
p2=Person('ali',1999)

#updating:
p1.name='babayev'
p1.address='zaqa'


#accessing object attrbts:
print(f"adi:{p1.name} tev:{p1.year} adrsi:{p1.address}")
print(f"adi:{p2.name} tev:{p2.year} adresi:{p2.address}")



#63. Nesne Tabanlı Programlama: Methods-----------------------------------------
class Person:
    #class attributes
    address='no info'


    #constructor(yapici method)
    def __init__(self,ad,yil):

        #object attributes:
        self.name=ad
        self.year=yil


    #instance method
    def intro(self):
        print(f"hi my name is "+self.name)

    def age(self):

        return 2021-self.year





p1=Person('elcin',1998)
p2=Person('ali',1999)

#p1.intro()
#p2.intro()



print(f"my name is {p1.name} and i am {p1.age()} years old")





#cevre hesaplamalari



class circle:
    #class object attribute
    pi=3.14

    def __init__(self,radius=1):
        self.r=radius

    #methods
    def l(self):
        return 2*self.pi*self.r

    def s(self):
        return self.pi*(self.r**2)

c1=circle() #r=1
c2=circle(5)

print(f"c2in alani={c1.s()} ve cevresi={c1.l()}")
print(f"c2in alani={c2.s()} ve cevresi={c2.l()}")



#64. Nesne Tabanlı Programlama:Inheritance (Kalıtım)
class person():
    def __init__(self):
        print('person created')

class student(person):
    pass

p1=person()
s1=student()

#
class person():
    def __init__(self):
        print('person created')

class student(person):
    def __init__(self):
        person.__init__(self) #will print also 'person created'
        print('student created')


#p1=person()

s1=student()

#
class person():
    def __init__(self,fname,lname):
        self.f=fname
        self.l=lname
        print('person created')

class student(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname) #will print also 'person created'
        print('student created')


p1=person('ali','A')

s1=student('elchin','B')

print(s1.f+" "+s1.l)
print(p1.f+' '+p1.l)

#
class person():
    def __init__(self,fname,lname):
        self.f=fname
        self.l=lname
        print('person created')
    def who(self):
        print('i am a person')
    def eat(self):
        print('i am eating')

class student(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname) #will print also 'person created'
        print('student created')


p1=person('ali','A')

s1=student('elchin','B')


p1.who()
s1.who()
p1.eat()
s1.eat()
#
class person():
    def __init__(self,fname,lname):
        self.f=fname
        self.l=lname
        print('person created')
    def who(self):
        print('i am a person')
    def eat(self):
        print('i am eating')

class student(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname) #will print also 'person created'
        print('student created')

    #override:
    def who(self):
        print('i am student actually')


p1=person('ali','A')

s1=student('elchin','B')



p1.who()
s1.who()


#
class person():
    def __init__(self,fname,lname):
        self.f=fname
        self.l=lname
        print('person created')
    def who(self):
        print('i am a person')
    def eat(self):
        print('i am eating')

class student(person):
    def __init__(self,fname,lname,number):
        self.n=number
        person.__init__(self,fname,lname) #will print also 'person created'
        print('student created')

    #override:
    def who(self):
        print('i am student actually')

    #method for just student:
    def h(self):
        print('helo i am a student')


p1=person('ali','A')

s1=student('elchin','B',1256)


print(s1.f+" "+s1.l+' '+str(s1.n))
print(p1.f+' '+p1.l)

s1.h()


#
class person():
    def __init__(self,fname,lname):
        self.f=fname
        self.l=lname
        print('person created')
    def who(self):
        print('i am a person')
    def eat(self):
        print('i am eating')

class student(person):
    def __init__(self,fname,lname,number):
        self.n=number
        person.__init__(self,fname,lname) #will print also 'person created'
        print('student created')

    #override:
    def who(self):
        print('i am student actually')

    #method for just student:
    def h(self):
        print('helo i am a student')

class teacher(person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.b=branch

    def who(self):
        print('i am a teacher')




p1=person('ali','A')

s1=student('elchin','B',1256)


t1=teacher('mellim','ov','math')
t1.who()
print(t1.f+" "+t1.l+' '+t1.b)






#--------------------------------65. Nesne Tabanlı Programlama: Özel Metodlar

class movie:
    def __init__(self,title,director,duration):
        self.t=title
        self.dr=director
        self.d=duration
        print('init works as usual;)')
m=movie('film','yonetmen','sure')
print(m)
print(str(m))


#

class movie:
    def __init__(self,title,director,duration):
        self.t=title
        self.dr=director
        self.d=duration
        print('init works as usual;)')

    def __str__(self):
        return f"{self.t} filmi by {self.dr}"
m=movie('BMS','NBC','sure')
print(m)
print(str(m))
print(len(m))



#
class movie:
    def __init__(self,title,director,duration):
        self.t=title
        self.dr=director
        self.d=duration
        print('init works as usual;)')

    def __str__(self):
        return f"{self.t} filmi by {self.dr}"

    def __len__(self):
        return self.d



m=movie('BMS','NBC',150)

print(len(m))


#
class movie:
    def __init__(self,title,director,duration):
        self.t=title
        self.dr=director
        self.d=duration
        print('init works as usual;)')

    def __str__(self):
        return f"{self.t} filmi by {self.dr}"

    def __len__(self):
        return self.d

    def __del__(self):
        print('movie silindi')


m=movie('BMS','NBC',150)

#del m    #even without del object will be deleted after a while:

print(m)



#66--------------------------------------------------------------quiz uygulamasi
class Question:
    def __init__(self,text,choices,answer):
        self.t=text
        self.c=choices
        self.a=answer

    def ca(self,answer):            #check_answer
        return self.a==answer

q1=Question('best prg_lang?',['py','java','c'],'py')
q2=Question('most popular?',['java','py','c'],'py')
q3=Question('benefitful?',['c','py','java'],'py')

print(q1.ca('py'))
print(q1.ca('c'))



class Quiz:
    def __init__(self,ql):

        self.q=ql
        self.i=0 #i=question_index
        self.s=0 #s=score
    def get_whole_questionl(self):           #instead of>>>sual=kuiz.q[kuiz.i]
        return self.q[self.i]

    def displayquestion(self):       #instead of>>sual=kuiz.getquestion()
        question=self.get_whole_questionl()  #>>>>>>>>>>>>print(sual.t)
        print(f"{self.i+1}ci soru>>>{question.t}")

        for i in question.c:
            print('-'+i)

        answer=input('cevabiniz:')
        self.guess(answer)
        self.load_question()

    def guess(self,answer):
        question=self.get_whole_questionl()

        if question.ca(answer):
            self.s+=1
        self.i+=1

    def load_question(self):
        if len(self.q)==self.i:
            print('quiz tamamlandi')
            self.show_score()
        else:
            self.displayprogress()
            self.displayquestion()

    def show_score(self):
        print(f'skorunuz:{self.s}')

    def displayprogress(self):
        total=len(self.q)
        num=self.i+1

        if num>total:
            print("quiz bitdi")
        else:
            print(f"question {num} of {total}".center(100,'*'))
q1=Question('Best prgogramming language?',['py','java','c','c++','c#'],'py')
q2=Question('most popular?',['java','py','c','c++','c#'],'py')
q3=Question('benefitful?',['c','py','java','c++','c#'],'py')
ql=[q1,q2,q3]

kuiz=Quiz(ql)

#sual=kuiz.q[kuiz.i]
#sual=kuiz.getquestion()
#print(sual.t)

kuiz.load_question()












#Section 9: Pythonda Modüller
#67. Bölüm Hakkında
#68. Modüle Nedir ?



#69. Hazır Modül Kullanımı - Math Modülü



import math

#value=dir(math)
#print(value)
#a=help(math)
#b=help(math.factorial)
#print(b)
s=math.sqrt(49)
print(s)
#
import math as m
a=m.factorial(5)
print(a)

#
from math import * #we imported eveything from math so dont need to write math anymore
a=sqrt(25)
print(a)

b=ceil(6.8)
print(b)



#or we can import what we want exactly:
from math import sqrt,factorial
a=sqrt(64)
print(a)

b=ceil(6.8) #so,not defined
print(b)

#>>
from math import sqrt,factorial

def sqrt(x):
    print('eger bu kod calisiyorsa bizim fonksiyonumuz math kutubhanesini ezmisdir ve mathin icinde tanimlanmisidr:'+str(x**2))

s=sqrt(9)
print(s)

#but
def sqrt(x):
    print('eger bu kod calisiyorsa bizim fonksiyonumuz math kutubhanesini ezmisdir ve mathin icinde tanimlanmisidr:'+str(x**2))
from math import sqrt,factorial
s=sqrt(9)
print(s)

#ayni isimli fonksiyuonlardan en son tanimlanan fonkisyon calisyor(otekini ezioyr=override)


#70. Hazır Modül Kullanımı ----------------------------------------Random Modülü
import random
r=random.random() #random float between 0 and 1
re=random.random()*100

print(r)
print(re)

a=random.uniform(10,50)
print(a)


b=int(random.uniform(10,50))
print(b)
#instead of:
c=random.randint(1,11)
print(c)

words=['keen','gallant','peril','recline','shriek','conceal','frigid']
rw=words[random.randint(0,len(words)-1)]
print(rw)
#but short way:
rw1=random.choice(words)
print(rw1)

#
word='wager(bet)'
a=random.choice(word)
print(a)

#
liste=list(range(10))
print(liste)
random.shuffle(liste)
print(liste)



#71--------------------------------------------------Kendi Modüllerimizi Yazalım
#in nmod.py....
import mod

#it diddnt work because i couldnt do it via atom



#**************************Section 10: Pythonda Hatalar & Hata Yönetimi************
#72. Bölüm Hakkında


#73.-----------------------------------------------Hata ve Hata Yönetimi Nedir ?


#74------------------------------

try:

    x=int(input('x:'))
    y=int(input('y:'))
    print(x/y)

except (ZeroDivisionError):
    print('0-a bolmek olmaaz,bele birsey mumkun deyil')
except (ValueError):
    print('herfsiz!!!')

#

try:

    x=int(input('x:'))
    y=int(input('y:'))
    print(x/y)

except (ZeroDivisionError,ValueError) as e:
    print('0-a boldun ya da herf  yazdin-_-')
    print(e)

#
try:

    x=int(input('x:'))
    y=int(input('y:'))
    print(x/y)
except:
    print('0-a boldun ya da herf  yazdin-_-')


#
try:

    x=int(input('x:'))
    y=int(input('y:'))
    print(x/y)
except:
    print('0-a boldun ya da herf yazdin-_-')
else:
    print('bu defe duzgun yazdin)')

#
while True:

    try:
        x=int(input('x:'))
        y=int(input('y:'))
        print(x/y)
    except Exception as err:
        print('0-a boldun ya da herf  yazdin-_-.tezeden yaz !!!\nsehvin:',err)
    else:
        break
    finally:
        print('try except sonlandi ve bu blok herzaman calisir\namma else blokuysa yalniz except calismazsa calisir')



#75. --------------------------------------------------Raising an Exception
x=11

if x>5:

    raise Exception('5den buyuk olmasn')


#>>>>>>>>>
def check_password(p):
    import re
    if len(p)<8:
        raise Exception('en az 8 karakter giriniz!')
    elif not re.search('[a-z]',p):
        raise Exception('kucuk harf icermelidir')
    elif not re.search('[A-Z]',p):
        raise Exception('buyuk harf icermelidir')
    elif not re.search('[0-9]',p):
        raise Exception('rakam icermelidir')
    elif re.search('!@$%^&*()_+',p):
        raise Exception('simvol icermemelidir ')
    elif re.search('\s',p):
        raise Exception('bosluk icermemelidir')
    else:
        print('sifre onaylandi by function')

password=input('parolayi giriniz:')

try:
    check_password(password)
except Exception as ex:
    print('yanlis oldu. hata ismi: ',ex)
else:
    print('sifre onaylandi by try-except')
finally:
    print('finally validation tamamlandi')


#>>>
class person:
    def __init__(self,name,year):
        if len(name)>10:
            raise Exception('10dan fazla karakter iceriyor!')
        else:
            self.n=name
            print(f'onaylandi {self.n}')

p1=person('elcin',1998)



#76-----------------------------------------------------Uygulama: Hata Yönetimi
liste=['1','2','5a','10b','abc','10','50']


#1.my way:
for i in liste:
    import re

    if not re.search('[a-z]',i):
        print('sayisal degerler:'+i)

#1
for x in liste:
    try:
        result=int(x)
        print(f'{result} ededdir')
    except:
        print(f'{x} eded deyil')
#1best
for x in liste:
    try:
        result=int(x)
        print(result)
    except ValueError:
        continue


#>>2

while True:
    a=input('sayi giriniz ve ya cikmak icin q tusuna basiniz:')
    if a=='q':
        break

    try:
        a=int(a)
        print('gecerli sayi ve islem sona erdi')
        break
    except:
        print('lutfen rakam girininz')

#3
p=input("password:")
tk='ü,ö,ğ,ı,ə,ç,ş'

for i in tk:
    if i==p:
        raise TypeError('parolada turkce karakter olmaaz)')
#or
p=input("password:")
tk='ü,ö,ğ,ı,ə,ç,ş'

for i in p:
    if i in tk:
        raise TypeError('parolada turkce karakter olmaaz)')
print('gecerli parola')

#or2

def chpswrd(p):
    tk='ü,ö,ğ,ı,ə,ç,ş'

    for i in p:
        if i in tk:
            raise TypeError('parolada turkce karakter olmaaz)')
    print('gecerli parola')

p=input("password:")
try:
    chpswrd(p)
except TypeError as err:
    print(err)






#

def fac(x):
    x=int(x)
    if x<0:
        raise ValueError('negativ olmamali')

    r=1
    for i in range(1,x+1):
        r*=i
    return r

for x in [5,10,11,-3,'e']:
    try:
        a=fac(x)
    except ValueError as err:
        print(err)
        continue

    print(a)


#

def fac(x):
    x=int(x)
    if x<0:
        raise ValueError('negativ olamaz')


    r=1
    for i in range(1,x+1):
        r*=i
    return r

for x in [5,10,11,-3,'3e']:
    try:
        a=fac(x)
    except ValueError:
        print('error verdi')
        continue

    print(a)



#????????????????????????????????????????????????????????????????????????????
def fac(x):
    x=int(x)
    if x<0 or x==str(x):
        raise ValueError('negativ sayi girdiniz ve ya girdiyiniz tam olarak sayi deyil')

    r=1
    for i in range(1,x+1):
        r*=i
    return r

for x in [5,10,11,-3,'e']:
    try:
        a=fac(x)
    except ValueError as err:
        print(err)
        continue
    print(a)

#why it doesnt defines 'invalid literal for int() with base 10: 'e'' error
#as valueerror and it doesnt print 'negativ sayi girdiniz ve ya girdiyiniz tam olarak sayi deyil'





#******************Section 11: Pythonda Dosya Yönetimi**************************
#77.---------------------------------------------------------Dosya Açma ve Yazma
file=open('newfile.txt','w')
#print(file)
file.close()

#
file=open("C:/Users/TOSHIBA/Desktop/elchinpy.txt","w") #but here location is noted as u see
print(file)


file=open("newfile.txt","w") #automaticly it will open and writes to dosya which is in the same location with beginner8.py
file.write('asdf')
file.close()

#so "w">>write yazma modu:dosyayi konumda olusturur ve dosyanin onceki icerigini silerek son yazilani ekler
#eger fayli acarak hicbirsey yazmadan close edib yeniden acarsaniz hersey silinmis olur>>>#file.write('asdf')

#>>>a
file=open('newfile.txt',"a")
file.write("qwertyy")
file.close

#>>x creates dosya eger zaten dosya varsa erorr verir:
file=open('newfile2.txt',"x")
file.close()


#78.---------------------------------------------------------------- Dosya Okuma
#file=open("newfile1.txt") #mode "r" is default dont need to write :File=open("newfile","r")
#print(file) #u see mode is "r"

#"r" read mode arises error if file isnt existed already
#we can handle this error:
try:
    file=open("newfile1.txt","r")
    print(file)
except FileNotFoundError:
    print('dosya okuma hatasi:lutfen once dosyayi olusturunuz')
finally:
    print('dosya kapandi')
    file.close()




#
file=open("newfile.txt","r")

for i in file:
    #print(i) #print yazdirdikdan sonra bos satir birakiyor
    print(i,end="")
file.close()

file=open("newfile.txt")
#instead of for,we can read to read)
content=file.read()
print(content)
file.close()

#inlecin mentiqi:
file=open('newfile.txt')

content1=file.read()
print("content1:")
print(content1)

content2=file.read()
print('content2:')
print(content2) #so it doesnt read anything cunki inlec zaten en sondaydi okunacak birsey kalmamisdi
file.close()


#but if u close file before reading second time:
file=open('newfile.txt')

content1=file.read()
print("content1:")
print(content1)
file.close()

file=open('newfile.txt') # also open it again to read
content2=file.read()
print('content2:')
print(content2)
file.close()

#>>>
file=open('newfile.txt')
print('readden sonra yazdigin qeder karakter(byte) oxuyur ')
content=file.read(3)
content=file.read(5) #sonra oxudugu her defede imlecin qaldigi yerden davam edib oxuyur:
content=file.read(6)
print(content)
file.close



#>>>>>>>>readline fonksiyonu
file=open('newfile.txt')


print('just one line:')
content=file.readline()
print(content)
file.close()


#short way:
print('just one line:')
print(file.readline())
print(file.readline())
print(file.readline()) #as above it will becoe  to read from cursors last position
file.close()


#>
print('just one line:')
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline()) #okunacak file bitdikden sonra bosluklar olustururlar:
print(file.readline()) #egre yukardaku gibi end="" diyilse
print(file.readline())
file.close()



#>>>>>readlines:lineleri listeye cevirir:
l=file.readlines()
print(l)
print(l[2])
print(l[1])
file.close()



#79. Dosya Okuma Fonksiyonları:
#noneed for 'file.close':
with open('newfile.txt','r') as file:
    content=file.read()
    print(content)
#
    print(file.tell()) #tells cursors location



#>
with open('newfile.txt','r') as file:
    content=file.read(10)
    print(content)
    file.seek(3) #sends cursor to defined location
    print(file.tell())
    print(file.read())


#----------------------------------------------------80. Dosyada Güncelleme Yapma
with open('newfile.txt','r+') as file: #r+ hem dosyayi acmak hemde okumka icin kullanlir
    file.write('aaaaa')
    print(file.read())

with open('newfile.txt','r+') as file:
    print(file.read())

#
with open('newfile.txt','r+') as file: #r+ hem dosyayi acmak hemde okumka icin kullanlir

    file.seek(7)
    file.write('aaaaa')
    print(file.read())

with open('newfile.txt','r+') as file:
    print(file.read())


#>>>>append>>>en sona guncelleme
with open("newfile.txt","a") as file:
    file.write("\nappend en sona yazdirir ve ya ekleme yapar")

with open("newfile.txt","r") as file:
    print(file.read())


#EN BASA guncelleme
with open("newfile.txt",'r+') as file:
    content=file.read()
    content='en bas\n'+content
    file.seek(0)
    file.write(content)
with open("newfile.txt","r") as file:
    print(file.read())

#ortada guncelleme:also will be written with writelines method below

with open('newfile.txt','r+') as file:
    liste=file.readlines()
    liste.insert(3,'\nortaya\n\n')
    file.seek(0)
    for i in liste:
        file.write(i)

with open('newfile.txt','r') as file:
    print(file.read())



#writelines method:
with open('newfile.txt','r+') as file:
    liste=file.readlines()
    liste.insert(3,'ELCHINN\n')
    file.seek(0)
    file.writelines(liste)

with open('newfile.txt','r') as file:
    print(file.read())





#----------------------------------------------81.uygulama dosya yonetimi


def not_hsp(satir):          #[:-1] it takes all elemnts but last one
                              #and here it means "I'm pretty sure that line ends with a newline and I want to strip it"
    satir=satir[:-1]
    liste=satir.split(':')
    print(liste[0])
    print(liste[1])
    print(liste)

    ogrenci=liste[0]
    nots=liste[1].split(',')

    not1=int(nots[0])
    not2=int(nots[1])
    not3=int(nots[2])

    avg=not1+not2+not3

    if avg>=90:
        harf='AA'
    elif avg>=85:
        harf='BA'
    elif avg>=65:
        harf='CC'
    else:
        harf='FF'

    return ogrenci+':'+harf+'\n'

def ort_oku():
    with open('exam_notes.txt','r') as file:
        for satir in file:
            print(not_hsp(satir))

def not_gir():
    ad=input('adi:')
    soyad=input('soyadi:')
    not1=input('not1:')
    not2=input('not2:')
    not3=input('not3:')

    with open('exam_notes.txt','a') as file:
        file.write(ad+' '+soyad+' '+':'+not1+','+not2+','+not3+'\n')


def not_kayit():
    with open('exam_notes.txt','r') as file:
        liste=[]

        for i in file:
            liste.append(not_hsp(i))


        with open('results.txt','w') as file2:
            for i in liste:
                file2.write(i)

while True:
    islem=input('1-notlari oku\n2-gir\n3-kaydet\n4-cik\n')

    if islem=='1':
        ort_oku()
    elif islem=='2':
        not_gir()
    elif islem=='3':
        not_kayit()
    else:
        break




#************************Section 12: Pythonda Fonksiyonların********************
#İleri Seviye Özellikleri

#----------------------------------------------------------82. İç içe Fonksiyon Kullanımı

def greeting(name):
    print('hello',name)
#print(greeting('ali'))
#print(greeting)

s=greeting
#burda iki objeyi birbirine atama yapdigimiz zaman aslindam atama islemi bilginin
#tutuldugu yerdeki data deyil de datanin adresine atama islemi yapmis oluyoruz

#print(s)
#print(greeting)

#so no difference between:
#print(greeting('ali'))
#print(s('ali'))

del s #burda s-i sildiyimzde ilgili adresdeki data silinmez so:
print(greeting)
 #but print(s) isnt defined of course
 

 #>>>>

def outer(num1):
    print('gorduyunuz gibi sadece outer calisti')
    def inner(num1):
        print('inner zaten calismaz(')
        return num1+1

outer(10)


#encapsulation-icdeki func kendine bir scope yani calisma alani tanimliyor ve disda donen islem icdeki funcnu ilgilendirmiyor

def outer(num1):
    print('gorduyunuz gibi outer calisti')
    def inner(num1):
        print('inner de calisti cunki biz inneri outerin icerisinde cagiryoruz:)')
        return num1+1
    n1=inner(num1)
    print(n1,num1)

outer(10)
#inner(10)>>>calismaz cunki sadece outer kapsaminda calisir

#>>>
def fac(number):
    if not isinstance(number,int):
        raise TypeError('must be int')

    if not number>=0:
        raise ValueError('musnt be neg')

    def innerfac(number):
        if number<=1:
            return 1
        return number*innerfac(number-1)
    return innerfac(number)

try:
    print(fac('l'))
except Exception as ex:
    print(ex)



#---------------------------------------------83. Fonksiyondan Fonksiyon Döndürme


def usalma(num):

    def inner(power):
        return num**power

    return inner

two=usalma(2)
print(two(3))

#funny but also works:)
print(usalma(2)(5))



#>>>>

def yetkisorgula(page):

    def inner(role):
        if role=='admin':
            return '{} rolu {} sayfasina ulasabilir'.format(role,page)
        else:
            return '{} rolu {} sayfasina ulasamaz'.format(role,page)
    return inner

user1=yetkisorgula('edit')
print(user1('admin'))

print(user1('just user'))


#

def islem(islem_adi):
    def topla(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam

    def carp(*args):
        carpma=1
        for i in args:
            carpma*=i
        return carpma

    if islem_adi=='toplama':
        return topla
    else:
        return carp

t=islem('toplama')
print(t(1,2,3))

c=islem('carpma')
print(c(2,4,6))

#84---------------------------------functions as parameters

def toplama(a,b):
    return a+b

def cikma(a,b):
    return a-b

def bolme(a,b):
    return a/b


def islem(f1,f2,f3,islemadi):
    if islemadi=='toplama':
        print(f1(1,8))
    elif islemadi=='cikarma':
        print(f2(10,4))
    elif islemadi=='bolme':
        print(f3(12,4))

islem(toplama,cikma,bolme,'toplama')

#85. -------------------------------------------------Decorator Fonksiyonlar


def decorator(func):
    def wrapper():
        print('fonsiyondan onceki islemler')
        func()
        print('fonksiyondan sonraki islemler')
    return wrapper




@decorator
def sayhallo():
    print('hello')

def greet():
    print('greeting')


sayhallo=decorator(sayhallo)
sayhallo()

greet=decorator(greet)
greet()

#real and short way:
def decorator(func):
    def wrapper():
        print('fonsiyondan onceki islemler')
        func()
        print('fonksiyondan sonraki islemler')
    return wrapper



@decorator
def sayhallo():
    print('hello')
sayhallo()

#>>>
def decorator(func):
    def wrapper(name):
        print('fonsiyondan onceki islemler')
        func(name) #because it is also sayhallo func
        print('fonksiyondan sonraki islemler')
    return wrapper




@decorator
def sayhallo(name):
    print('hello',name)
sayhallo('ali')




#>>>>>>>
import math
import time


def usalma(a,b):
    start=time.time()
    time.sleep(1)
    print(math.pow(a,b))
    finish=time.time()
    print('fonksiyon'+str(finish-start)+'saniye surdu')
def fakt(num):
    start=time.time()
    time.sleep(1)
    print(math.factorial(num))
    finish=time.time()
    print('fonksiyon'+str(finish-start)+'saniye surdu')

usalma(2,3)
fakt(5)


#>>>>>>>unikal way:her bir fonlsiyon kendi isini yapsin
#ve zaman hesaplamak icin baska bir fonksiyon
#bu sayede kod tekrarinin da onune gecilir

def ctime(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish=time.time()
        print('fonksiyon'+func.__name__+' '+str(finish-start)+'saniye surdu')
    return inner


@ctime
def usalma(a,b):
    print(math.pow(a,b))


@ctime
def fak(num):
    print(math.factorial(num))

usalma(2,3)
fak(5)
 


#**************Section 13: Pythonda Iterators***********************************


#--------------------------------------------86. Iterators
liste=[1,2,3,4,5]


iterator=iter(liste)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))



#>>>>>>>
for i in liste:
    print(i)

iterator=iter(liste)

#how 'for' works:
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
 


 #>>>>>why do we need(for ex to make our own class ):
class Mynumbers:
    def __init__(self,start,stop):
        self.st=start
        self.sp=stop

    def __iter__(self):
        return self



    def __next__(self):
       if self.st<=self.sp:
           x=self.st
           self.st+=1
           return x
       else:
           raise StopIteration

list=Mynumbers(10,20)

#for
for i in list:
    print(i)

#without for:
myiter=iter(list)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#with while:
myiter=iter(list)
while True:
    try:
        element=next(myiter)
        print(element)
    except StopIteration:
        break





#-----------------------------------------87.generators.
def cube():
    result=[]
    for i in range(5):
        res ult.append(i**3)
    return result
print(cube())

#bellek uzerinde yer tutmayan:
def cube():
    for i in range(5):
        yield i**3 #yieldin gonderdiyi deger biryerde saklanmiyor uretildiyi anda ekrana yazdirmak icin kullanilir

kupler=cube()
print(kupler) #return dan farkli olarak deyerler gondermez(burda kup fonksiyonunu calistirmis olmuyoruz)
#onun yerine uzerinde dolasa bileceyimiz iterable objesi gonderiyor


#ve iterable obje uzerinde de next fonksiyonu sayesinde dolasa biliyoruz:

generator=cube()
iterator=iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))


#
#yield ile dondurduyumuz fonksiyon iterable bir obje getiriyor
#zaten generator iterable olan objeyi iteratora ceviriyor ve itere ihtiyacimiz yok aslinda:
generator=cube()
print(next(generator))
print(next(generator))
print(next(generator))


#
iterator=cube()
for i in  iterator:
    print(i)

#or:
for i in cube():
    print(i)


#>>>>>list compression
liste=[i**3 for i in range(5)]
print(liste)

#generator seklinde dondurtmek icin use () instead of []:
gen=(i**3 for i in range(5))
print(next(gen))
print(next(gen))
print(next(gen))

#
for i in gen:
    print(i)





#***********Section 15: Advanced Python Modülleri & Web Scraping

#------------------------------------------88. Datetime Module
from datetime import datetime

simdi=datetime.now()
print(datetime.now())
print(datetime.now().year)
print(simdi.month)
print(simdi.hour)

#
print(datetime.ctime(simdi))

##
print(datetime.strftime(simdi,'%Y')) #yil
print(datetime.strftime(simdi,'%X')) #saat
print(datetime.strftime(simdi,'%d')) #day
print(datetime.strftime(simdi,'%A')) #day of week(str)
print(datetime.strftime(simdi,'%B')) #month(str)
print(datetime.strftime(simdi,'%d %X %A'))


###
tme='21 march 2021'
gun,ay,yil=tme.split()
print(gun)
print(ay)
print(yil)

###short and cool way:
t='15 march 2021 hour 12:29:00'
result=datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
r=result.year
r1=datetime.strftime(result,'%Y')

print(result)
print(r)
print(r1)


#

birthday=datetime(1988,12,28,12,20,11) #yil,ay,gun,saat
print(birthday)

result=datetime.timestamp(birthday) #tarih objesi saniyeyle ifade olunur
print(result)

r=datetime.fromtimestamp(result) #saniye to datetime=saniyeden tarih bilgisine
r1=datetime.fromtimestamp(0) #milad time for comps)

print(r)
print(r1)


##
birthday=datetime(1988,12,28,12,20,11)
simdi=datetime.now()
d=simdi-birthday
rd=d.days
print(d)
print(rd)


#>>>>>
from datetime import timedelta   #or just Import datetime

simdi=datetime.now()
print(simdi)
result=simdi+timedelta(days=10)
print(result)

#------------------------------------------------------------------------89. Os Module

import os

r=dir(os)
r=os.name


#DIZIN DEGISTIRME

#os.chdir('C:\\')

#bir ust duzine birbasa gecmek icin:
#os.chdir('..')
#os.chdir('..')

#>>or instead of two chdir('..')
#os.chdir('..//..')


#DIZIN OYRENME
r=os.getcwd()


#KLASOR OLUSTURMA
#os.mkdir('smt')

#>dizin icinde dizn olusturma
#os.makedirs('smth/any')
#os.rename('smth','something')

#LISTELEME:
r=os.listdir()
#r=os.listdir('C:\\') #herhanci bir konumda listeleme

#FILTRELEME
for dosya in os.listdir():
    if dosya.endswith('.py'):
        print(dosya)


print(r)



#
#import datetime
#r=os.stat("newfile.txt")
#r=r.st_size/1024
#r=r.st_ctime
#r=datetime.datetime.fromtimestamp(r.st_ctime)

#print(r)


#>>
#os.system('notepad.exe')


#PATH
#r=os.path.abspath('newfile.txt') #tam konum
#r=os.path.dirname('C:/Users/TOSHIBA/.atom/packages/contrast-syntax\newfile.txt') #dizin ismi
#r=os.path.dirname(os.path.abspath('newfile.txt'))


#r=os.path.exists('newfile.txt')



#clasormu deylmi?>>>>isdir
#r=os.path.isdir('newfile.txt')
#r=os.path.isdir('C:/Users/TOSHIBA/.atom/packages')

#faylmi
#r=os.path.isfile('newfile.txt')

#
r=os.path.join('C:\\','test','mest') #dizinleri birlesdirir
r=os.path.split('C:\\fest') #bolur


r=os.path.splitext('newfile.txt') #ismiyle uzantisini ayirir


print(r)



#----------------------------------------------90   RE
#import re

#r=dir(re)

#str='Python theKursu:Python Pytmmn Proglamlama Rehberiniz| all 40 saat'

#r=re.findall('Python',str)
#r=len(r)

#r=re.split(' ',str)

#r=re.sub(' ','*****',str)

r=re.search('Python',str)
#yukardaki searchin gonderdiyi match objesi uzerinden asagidaki islemleri yapabiliriz
#r=r.span()
#r=r.start()
#r=r.end()
#r=r.group()
#r=r.string



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#r=re.findall('[abc]',str)
#r=re.findall('[pytn]',str)
#r=re.findall('[a-e]',str)
#r=re.findall('[a-z]',str)
#r=re.findall('[0-5]',str)
#note [0-39]>>>[01239]



#
#[^abc]>besides abc
#[^0-9]>besids numbers
#r=re.findall('[^abc]',str)
#r=re.findall('[^0-9]',str)


#>>>
#r=re.findall('...',str)
#r=re.findall('Pyt..n',str)

#>>>
#r=re.findall('^a',str)
#r=re.findall('^P',str)


#>>>
#r=re.findall('a$',str)
#r=re.findall('t$',str)


#>>>
#r=re.findall('sa*t',str) # * sifr ve ya daha fazla
#r=re.findall('sa+t',str) # + bir ve ya daha fazla
#r=re.findall('sa?t',str) #? sifir ve ya bir kere


#>>>
#al{2,3}=>a-dan sonra en az 2 en fazla 3 l
#[0-9]{2,4}=>en az 2 en cok 4 basamakli sayilar
#r=re.findall('al{2}',str)
#r=re.findall('[0-9]{2}',str)

#print(r)


#------------------------------------------------------------------------91 json
#import json

#ps='{"name":"elcin","lang":["python","java"]}'



#json to dic
r=json.loads(ps)


print(type(r ))
print(r)

#>>>fayli okuma
with open('person.jso') as f:
    data=json.load(f)
    print(data["name"])





#>>>dic to str
ps1={"name":"elcin","lang":["python","java"]}
r=json.dumps(ps1)
print(r)
print(type(r))



#fayla yazdirma yeni bilgi
pd={"name":"elcinnnnnzs","lang":["python","java"]}
with open('person.jso','w') as f:
    json.dump(pd,f)


#>>>jsondan dicta gecerek okunakli sekilde yazdirma
ps='{"name":"elcin","lang":["python","java"]}'
perdic=json.loads(ps)
r=json.dumps(perdic,indent=4,sort_keys=True)
#print(perdic)
print(r)



#-------------------------------------------------------------------93. Requests
import requests
import json

r=requests.get("https://jsonplaceholder.typicode.com/todos")
r=json.loads(r.text)

#r=r.text

print(r[0]["title"])
print(r[0])
print(type(r))


print(r)
#>>>
for i in r:
    print(i['title'])

print(type(r))




#------------------------------------------94. Exchange Api ile Döviz Uygulaması
import requests
import json

b=input('bozulan doviz turu:')
a=input('alinan doviz turu:')

h=int(input('NE KADAR PARA CEVIRMESI GERCEKLESTIRILICEK?:'))


link='https://api.exchangeratesapi.io/latest?base='
r=requests.get(link+b)
r=json.loads(r.text)


print(f"1{b}={r['rates'][a]}{a}")
print(f"{h}{a}={h*r['rates'][a]}{a}")

#print(r)







#-------------------------------------------------95. Github Rest Api Kullanımı
import requests

class Github:
    def __init__(self):
        self.api_url='https://api.github.com'
        self.token='2a0cebe35888589a756953098fb345a5c26fc79b'
    def getuser(self,username):
        response=requests.get(self.api_url+'/users/'+username)
        return response.json()
    def getrepositories(self,username):
        response=requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()

    def cr_repos(self,name):
        response=requests.post(self.api_url+'/user/repos/?access_token='+self.token,json={
            "name":"xello",
            "description":"okayyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
            "homepage":'https://github.com',
            "private":False,
            "has_issues":True,
            "has_projects":True,
            "has_wiki":True
        })

        return response.json()

gthb=Github()


while True:
    secim=input('1-find user\n2-get repositories\n3-create repository\n4-exit\nseciminiz: ')

    if secim=='4':
        break
    elif secim=='1':
        username=input('Enter username please:')
        result=gthb.getuser(username)
        #print(result)
        print(f"NAME:{result['name']} PUBLIC REPOLARI:{result['public_repos']} IZLEYICILERI:{result['followers']}")
    elif secim=='2':
        username=input('Enter username please:')
        result=gthb.getrepositories(username)
        for repo in result:
            print(repo['name'])
    elif secim=='3':
        name=input('enter repo name:')
        result=gthb.cr_repos(name)
        print(result)

    else:
        print('gecersiz islems...(ERRORS ZBAB IVJJJ)')


#----------------------------------------------------------------96
import requests

class mdb:
    def __init__(self):
        self.api_url='https://api.themoviedb.org/3/'
        self.api_key='886b68b2eecce2aa4a03257255614f1f'

    def getpop(self):
        response=requests.get(self.api_url+'movie/popular?api_key='+self.api_key+'&language=en-US&page=1')
        return response.json()

    def srch(self,keyword):
        response=requests.get(self.api_url+'search/company?api_key='+self.api_key+'&query='+keyword+'&page=1')
        return response.json()



mv=mdb()
while True:
    secim=input('1-popoular/n2-search/n3-exit/n: ')

    if secim=='3':
        break
    elif secim=='1':
        r=mv.getpop()
        for movie in r['results']:
            print(movie['title'])

    elif secim=='2':

        kywrd=input('keyword: ')
        r=mv.srch(kywrd)
        for movie in r['results']:
            print(movie['name'])




#---------------------------------------------------97
