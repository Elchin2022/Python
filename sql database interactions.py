#-------------------------------------------------------------------149. Database Bağlantısı


import mysql.connector

mydb=mysql.connector.connect(host='localhost',
    user='root',
    password='qwer',r:
    print(i)

mycursor.execute("CREATE TABLE test1 (name VARCHAR(255),adress VARCHAR(45))")


#---------------------------------------------------150. Uygulama: School Database0

import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='qwer')




#------------------------------------------------------151. Insert: Veri Ekleme




import mysql.connector


def insrt():
    cnctn=mysql.connector.connect(host='localhost',user='root',
        password='qwer',
        database='schooldb')
    crsr=cnctn.cursor()

    sql_c="INSERT INTO new_table(stno,name,gender) VALUES(%s,%s,%s)"
    vls=(109,'elcin','k')
    crsr.execute(sql_c,vls)

    try:
        cnctn.commit()
    except mysql.connector.Error as err:
        print('hata:',err)
    finally:
        cnctn.close()
        print('process ended sucesfully ivjjj')
insrt()







#-input

def insert(stno,name,gender):

    cnctn=mysql.connector.connect(host='localhost',user='root',password='qwer',database='schooldb')
    mycrsr=cnctn.cursor()
    sql_c='INSERT INTO new_table(stno,name,gender) VALUES(%s,%s,%s)'
    vls=(stno,name,gender)
    mycrsr.execute(sql_c,vls)

    try:
        cnctn.commit()
    except mysql.connection.Error as err:
        print('hata:',err)
    finally:
        cnctn.close()
        print('sucesfully completed')

stno=int(input('numara:'))
name=input('ad:')
gender=input('c:')


insert(stno,name,gender)





#--while
def insert(list):

    cnctn=mysql.connector.connect(host='localhost',user='root',password='qwer',database='schooldb')
    mycrsr=cnctn.cursor()
    sql_c='INSERT INTO new_table(stno,name,gender) VALUES(%s,%s,%s)'
    vls=list
    mycrsr.executemany(sql_c,vls)

    try:
        cnctn.commit()
        print(f'{mycrsr.rowcount} eded veri')
        print(f'son eklenen kaydin id numarasi{mycrsr.lastrowid}')
    except mysql.connection.Error as err:
        print('hata:',err)
    finally:
        cnctn.close()
        print('sucesfully completed')


list=[]
while True:
    stno=int(input('numara:'))
    name=input('ad:')
    gender=input('c:')
    list.append((stno,name,gender))
    print('would u like to continue?')
    a=input('yes or no:')
    if a=='no':
        print('your datas loading...')
        print(list)
        insert(list)
        break
    

# ----------------------------------------------------------------------152. Uygulama: Veri Ekleme






import mysql.connector



liste=[(1,'elcin','k'),(2,'james','f')]


cnctn=mysql.connector.connect(host='localhost',user='root',password='qwer',database='schooldb')
mycrsr=cnctn.cursor()

sql_c="INSERT INTO new_table(stno,name,gender) VALUES(%s,%s,%s)"
vls=liste

mycrsr.executemany(sql_c,vls)      # must be many!!!!

try:
    cnctn.commit()
    print(f'{mycrsr.rowcount} eded veri eklendi')
except mysql.connector.Error as err:
    print('hatali islem:',err)
finally:

    print(f'son eklenen kaydin id numarasi:{mycrsr.lastrowid}')
    cnctn.close()                   #close it always!!!!!!!
    print('process ended')


#by class


import mysql.connector

from connection import cnctn


class student:

    connection=cnctn            #bunlar her nesne icin ortakdir so isnt  included in _init_
    mycursor=cnctn.cursor()

    def __init__(self,stno,name,gender):
        self.s=stno
        self.n=name
        self.g=gender

    def savestudent(self):
        sql_c="INSERT INTO new_table(stno,name,gender) VALUES(%s,%s,%s)"
        vls=(self.s,self.n,self.g)
        student.mycursor.execute(sql_c,vls)

        try:
            student.connection.commit()
            print(f'{student.mycursor.rowcount} eded veri eklendi')
        except mysql.connector.Error as err:
            print('hatali islem:',err)
        finally:
            print(f'son eklenen kaydin id numarasi:{student.mycursor.lastrowid}')
            student.connection.close()                   #close it always!!!!!!!
            print('process ended')


ahmet=student(100,'ahmet','e')
ahmet.savestudent()




    @staticmethod #oldugu icin self parametresi vermiyoruz,for ex students-i veriyoruz 
    def savestudents(students):
        sql_c="INSERT INTO new_table(stno,name,gender) VALUES(%s,%s,%s)"
        vls=students
        student.mycursor.executemany(sql_c,vls)



        try:
            student.connection.commit() print(f'{student.mycursor.rowcount} eded veri eklendi') except mysql.connector.Error as err: print('hatali islem:',err) finally: print(f'son eklenen kaydin id numarasi:{student.mycursor.lastrowid}')
            student.connection.close()                   #close it always!!!!!!!
            print('process ended')


ogrenciler=[(1,'elcin','k'),(2,'james','f')]
student.savestudents(ogrenciler)








#------------------------------------------------------153.Verileri getirme:


import mysql.connector

def getproducts():
    cnctn=mysql.connector.connect(host='localhost',user='root',password='qwer',database='schooldb')
    mycrsr=cnctn.cursor()

    #mycrsr.execute('Select * From new_table') # '*' represents columns
    mycrsr.execute('Select name,stno from new_table')

    # r=mycrsr.fetchall()
    # print(r)

    # for i in r:
    #     print(f'adi:{i[0]} numarasi:{i[1]}')



    r=mycrsr.fetchone()

    print(f'adi:{r[0]} numarasi:{r[1]}')


getproducts()


# 154. ------------------------------Where: Kayıt Filtreleme
# import mysql.connector

def getproducts():
    cnctn=mysql.connector.connect(host='localhost',user='root',password='qwer',database='schooldb')
    mycrsr=cnctn.cursor()
    #mycrsr.execute('Select * From new_table Where name="elcin" and stno=109')
    # mycrsr.execute('Select * From new_table Where name LIKE "%elcin%" and stno=109 ')
    mycrsr.execute('Select * From new_table Where id =1')

    r=mycrsr.fetchone() #fetchall(liste) we need for loop but fetchone(tuple)

    print(f'adi:{r[2]} numarasi:{r[1]}')

    # for std in r:
    #     print(f'adi:{std[2]} numarasi:{std[1]}')

getproducts()






#MORE NET VERSION

def getproducts(id):
    cnctn=mysql.connector.connect(host='localhost',user='root',password='qwer',database='schooldb')
    mycrsr=cnctn.cursor()

    sql_c='Select * From new_table Where id =%s'
    vl=(id,)                                            #WHY ,,,,,,,,,,,,,,,,,, AFTER ID ?????????????????????????????????????????????????

    mycrsr.execute(sql_c,vl)

    r=mycrsr.fetchone()

    print(f'id:{r[0]},adi:{r[1]} numarasi:{r[2]}')


getproducts(1)






#--------------------------------------# 155. OrderBy: Kayıt Sıralama


import mysql.connector

def getproducts():
    cnctn=mysql.connector.connect(host='localhost',user='root',password='qwer',database='schooldb')
    mycrsr=cnctn.cursor()
    mycrsr.execute('Select * From new_table ORDER BY name,stno')


    r=mycrsr.fetchall()

    try:
        r=mycrsr.fetchall()
        for i in r:
            print(f'adi:{i[2]} numarasi:{i[1]}')
    except mysql.connector.Error as err:
        print('hatali islem:',err)
    finally:
        cnctn.close()
        print('islem ended...')
        cnctn.close()
getproducts()      



# 156.---------------------------------------------Aggregate Fonksiyonları:Count(), Avg(), Sum(), Min(), Max()





import mysql.connector

def getproducts():
    cnctn=mysql.connector.connect(host='localhost',user='root',password='qwer',database='schooldb')
    mycrsr=cnctn.cursor()
    # sql_c='Select COUNT(*) from new_table'
    # sql_c='Select AVG(stno) from new_table'
    # sql_c='Select SUM(stno) from new_table'
    sql_c='select name,stno from new_table where stno=(Select MAX(stno) from new_table)'
    mycrsr.execute(sql_c)
    r=mycrsr.fetchone()

    print(f'result:{r[0]} {r[1]}')

getproducts()

    



# -----------------------------------------------------------------------------------157. Uygulama: Veri Seçme

import mysql.connector
from connection import cnctn


class student:

    cnctn=cnctn
    crsr=cnctn.cursor()

    @staticmethod
    def stdinfo():
        # sql_c='select stno,name from new_table'
        # sql_c='select name,stno from new_table where gender="k"'
        # sql_c='select count(*) from new_table where gender="k"'
        sql_c='select * from new_table where gender="k" order by stno'
        student.crsr.execute(sql_c)

        try:
            r=student.crsr.fetchall()
            print(r)
            # for i in r:
            #     print(i[1])
            #     # print(f'{i[0]} {i[1]}') 
        except mysql.connector.Error as err:
            print('hatali!!!',err)
        finally:
            student.cnctn.close()


student.stdinfo()



# 158.----------------------------------------------------------------------Update: Kayıt Güncelleme


import mysql.connector


def updprd():
    cnctn=mysql.connector.connect(host='localhost',user='root',password='qwer',database='schooldb')
    crsr=cnctn.cursor()

    sql_c='update new_table set name="jamie" where id=1 '
    crsr.execute(sql_c)

    try:
        cnctn.commit()
        print(f'{crsr.rowcount} tane kayit guncellendi')
    except mysql.connector.Error as err:
        print('hatali!!!',err)
    finally:
        cnctn.close()

updprd()

#---------------------------------------------------------------- 159. Delete: Kayıt Silme

import mysql.connector


def delprd(id):
    cnctn=mysql.connector.connect(host='localhost',user='root',password='qwer',database='schooldb')
    crsr=cnctn.cursor()

    sql_c='delete from new_table where id=%s'
    vl=(id,)
    crsr.execute(sql_c,vl)

    try:
        cnctn.commit()
        print(f'{crsr.rowcount} tane kayit silindi')
    except mysql.connector.Error as err:
        print('hatali!!!',err)
    finally:
        cnctn.close()

delprd(12)




#--------------------------------------------------------------160. Uygulama: Kayıt Güncelleme


import mysql.connector



#basic

def getst(id):
    cnctn=mysql.connector.connect(host='localhost',user='root',password='qwer',database='schooldb')
    crsr=cnctn.cursor()

    sql_c='select * from new_table where id=%s'
    vl=(id,)

    crsr.execute(sql_c,vl)

    r=crsr.fetchone()

    print(f'numara {r[1]},ad {r[2]}')

getst(1)

def updt(id):
    cnctn=mysql.connector.connect(host='localhost',user='root',password='qwer',database='schooldb')
    crsr=cnctn.cursor()

    sql_c='update new_table set stno="160107019" where id=%s'
    vl=(id,)

    crsr.execute(sql_c,vl)


    try:
        cnctn.commit()
        print(f'{crsr.rowcount} tane kayit guncellendi')
    except mysql.connector.Error as err:
        print('hatali!!!',err)
    finally:
        cnctn.close()


updt(1)






#by class methods>>

class student:

    cnctn=mysql.connector.connect(host='localhost',user='root',password='qwer',database='schooldb')

    crsr=cnctn.cursor()

    @staticmethod
    def stdinfo(id):
       
        sql_c='select * from new_table where id=%s'
        vl=(id,)
        student.crsr.execute(sql_c,vl)

        try:
            # return student.crsr.fetchone()

            obj=student.crsr.fetchone()
            return student(obj[0],obj[1],obj[2],obj[3])
        except mysql.connector.Error as err:
            print('hatali!!!',err)


# student.stdinfo()


    def __init__(self,id,stno,name,gender):
        if id is None:
            self.id=0

        else:
            self.id=id

        # self.id=id
    
        self.s=stno
        self.n=name
        self.g=gender





    def updt(self):
        cnctn=mysql.connector.connect(host='localhost',user='root',password='qwer',database='schooldb')
        crsr=cnctn.cursor()

        sql_c='update new_table set stno=%s,name=%s where id=%s'
        vl=(self.stno,self.name,self.id)

        student.crsr.execute(sql_c,vl)


        try:
            student.cnctn.commit()
            print(f'{student.crsr.rowcount} tane kayit guncellendi')
        except mysql.connector.Error as err:
            print('hatali!!!',err)


# obj=student.stdinfo(13)
# print(obj)
# st=student(obj[0],obj[1],obj[2],obj[3])



# st=student.stdinfo(23)


# st.name='james'
# st.stno='160107018'

# st.updt()




    @staticmethod
    def stdgndr(gender):
       
        sql_c='select * from new_table where gender=%s'
        vl=(gender,)
        student.crsr.execute(sql_c,vl)

        try:
            return student.crsr.fetchall() #it fetchs list to us
        except mysql.connector.Error as err:
            print('hatali!!!',err)




    @staticmethod
    def updtss(liste):
        cnctn=mysql.connector.connect(host='localhost',user='root',password='qwer',database='schooldb')
        crsr=cnctn.cursor()

        sql_c='update new_table set stno=%s,name=%s where id=%s'
        vl=[]
        order=[1,2,0]

        for item in liste:
            item=[item[i] for i in order]
            vl.append(item)

        student.crsr.executemany(sql_c,vl)


        try:
            student.cnctn.commit()
            print(f'{student.crsr.rowcount} tane kayit guncellendi')
        except mysql.connector.Error as err:
            print('hatali!!!',err)



sl=student.stdgndr('k')
print(sl)


l=[]
for s in sl:
    s=list(s)
    s[2]='Mr.'+s[2]
    s[1]=16010700+s[1]
    l.append(s)

student.updtss(l)