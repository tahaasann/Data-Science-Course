# SAYILAR VE STRINGLERE GIRIS
# istatistik açısından (sayısal değişken)
9 #integer - kesikli
9.2 #float - sürekli
9+9
9*9

# stringler (karakter dizileri)
# String olduğu bilgisini vermek için " - çift tırnak veya ' - tek tırnak kullanılmalıdır.
print('HELLO AI ERA') # İçine yazdığımız ifadeyi konsol ekranına yazdırır.
"HELLO AI ERA"

# python programlama dilinde oluşturduğumuz her şeye nesne adı verilir(nesne yönelimli programlama prensipleri). 

type(9) # herhangi bir nesnenin tipini belirlemek için
type(9.2)
type("HELLO AI ERA")

#----------------------------------------------

# STRING-KARAKTER DİZİLERİNİ YAKINDAN TANIYALIM
## Genellikle veri yapılarında, elde tutmuş olduğumuz veriler ve üzerinde çalışıyor olduğumuz veriler genelde STRİNG yapıda olabiliyorlar.

""
''

123
type(123) # integer
"123"
type('123') # string

# en kapsayıcı olarak '' tek tırnak kullanılması önerilir
"a" + "b" # ab
'a'' b'   #ab
"a" + "-b" # Stringler bir araya getirmek amaçlı kullanılır.
"a" - "b" # TypeError: 2 string birbirinden çıkarılamaz
"a"*3 # aaa
"a "*3 # a a a  Bir araya getirmek amaçlı
"a"/3 # TypeError

#-----------------------------------------------

# UZUNLUK(ELEMAN SAYISI) BİLGİSİNE ERİŞMEK: len METODU
# Metodlar, veri yapıları veya belirli yapılara uygulanan çeşitli fonksiyonlardır. 
## len(sadece stringlere özel bir metod değildir. Birçok veri yapısıyla kullanılabilen bir metod/fonksiyondur.)

gel_yaz = "gelecegi_yazanlar"
#del mvk

a = 9
b = 10

a*b

len(gel_yaz)
len("gelecegi_yazanlar")

#------------------------------------------------
# BÜYÜK/KÜÇÜK HARF DÖNÜŞÜMLERİ: UPPER & LOWER METODLARI
# Bir string ifadeyi komple büyük veya küçük hale getirir. Elimizde özellikle yapısal olmayan veriler, metinler olduğunda; bu metinleri belirli düzende yapısal formlara getirmek istediğimizde çok sık kullanılan yapılardır.
# Kullanıcının girdiği String ifadeleri standartize etmek için kullanılan yapılardır.
# Değişken ve dosya isimlerini stardartize haline getirmek için kullanılır.

gel_yaz.upper() # 'GELECEGI_YAZANLAR'
gel_yaz.lower() # 'gelecegi_yazanlar'

gel_yaz.islower() # lower mı öğrenmek için
B = gel_yaz.upper()

B.isupper() # True
B.islower() # False

#-------------------------------------------------
# REPLACE (YER DEĞİŞTİRME) METODU
# Elimizdeki stringdeki karakterleri değiştirmek istediğimizde kullanılır.

gel_yaz.replace("e", "a") # galacagi_yazanlar

gel_yaz.replace("a", "i") # gelecegi_yizinlir

#-------------------------------------------------
# KARAKTER KIRPMA İŞLEMLERİ(STRİP METODU)
gel_yaz = " gelecegi_yazanlar "
gel_yaz.strip() # 'gelecegi_yazanlar'

gel_yaz = "*gelecegi_yazanlar*"
gel_yaz.strip("*")

gel_yaz = "lgelecegi_yazanlarl"
gel_yaz.strip("l")

#-------------------------------------------------
# METODLARA GENEL BAKIŞ
## Python'da üzerinde çalışıyor olduğumuz veri tipine uygulanabilecek olan methodları görmek için dir fonksiyonunu kullanabiliriz.
gel_yaz = "gelecegi_yazanlar"

dir(gel_yaz)
dir(str)

#-------------------------------------------------
# KARAKTER DİZİLERİNDE ALTKÜME İŞLEMLERİ(SUBSTRINGS)
gel_yaz[0] # 'g'

gel_yaz[20] # IndexError: Verilmiş aralık, indexin dışında.

gel_yaz[0:3] # 'gel'

gel_yaz[3:7] # 'eceg'

#--------------------------------------------------
# DEĞİŞKENLER

a = 99999 # atama işlemi sonunda oluşan nesne bir değişkendir. Her değişkenin bir tipi vardır. a değişkeninin tipi integer'dır.
b = "ali_uzaya_git"
c = a*2

a/c
a*c
a*5

type(100) #integer
type(100.2) #float
type(1+2j) #complex

a = 100.2

#--------------------------------------------------
# TİP(TYPE) DÖNÜŞÜMLERİ
## Bazı durumlarda değişkenlerin tipleri arasında dönüşümler yapmak gerekir. String -> İnteger || Integer -> Float gibi

# Mesela kullanıcıdan alınan iki ifadenin çarpımını hesaplamak istediğimizi düşünelim. Kullanıcının girdiği ifadeler genel olarak string olarak alınır. Ardından bu string değişkenlerin tipini integer çevirmemiz gerekir.

toplama_bir = input() # input() fonksiyonu kullanıcıdan bilgi almak için kullanılır.
toplama_iki = input()

type(toplama_bir) # str

toplama_bir + toplama_iki # 57

int(toplama_bir) + int(toplama_iki) # 12

int(11.0) # 11

float(12) # 12.0

type(str(12)) # str

#--------------------------------------------------
#KOD ÇIKTISINI EKRANA YAZDIRMAK: PRINT

print("HELLO AI ERA")

print("gelecegi","yazanlar") # gelecegi yazanlar

print("gelecegi","yazanlar", sep = "_") # gelecegi_yazanlar
# Ayrıca birleştireceğimiz iki stringin aralarına eklemek istediğimiz herhangi bir şey varsa sep = "istediğimiz herhangi bir sembol veya boşluk"  ekleyebiliriz.
#* Fonksiyonların genel amaçlarını biçimlendirmek için kullanılan alt görev belirticilere *argüman* denir. Bu mantığa göre "sep" bir argümandır. Printin ana amacını sep ile biçimlendirdik.

#-------------------------------------------------
# VERI YAPILARI - LISTE OLUSTURMA
# Python'da kullanılan birden çok veri yapısı vardır: Listeler, tuplelar, dictonary vb... en sık kullanılan veri yapısı listelerdir.
# Listeler değiştirilebilir, kapsayıcıdır (farklı tipte verileri tutabilir), sıralıdır.
# []
# list()

notlar = [90,80,70,50]
type(notlar) # list

liste = ["a", 19.3, 90]
liste2 = ["a", 19.3, 90, notlar] 

len(liste2) # 4

#-------------------------------------------------
# LİSTE İÇİ TİP SORGULAMA

type(liste2[0]) #str
liste2[0] # 'a'
liste2[3] # [90, 80, 70, 50]

tum_liste = [liste, liste2] # [['a', 19.3, 90], ['a', 19.3, 90, [90, 80, 70, 50]]]

#del tum_liste # tum_listeyi bellekten siler

#-------------------------------------------------
# LİSTE ELEMANLARINA ERİŞMEK

liste = [10, 20, 30, 40, 50]

liste[0]
liste[1]

liste[6] # IndexError

liste[0:2] # [10, 20]
liste[:2] # [10, 20]
liste[2:] # [30, 40, 50]

yeni_liste = ["a", 10, [20, 30, 40, 50]]
yeni_liste

yeni_liste[2] # [20, 30, 40, 50]

yeni_liste[0:2] # ['a', 10]

yeni_liste[2][1] # 30
 
#-------------------------------------------------
#LİSTELERE ELEMAN EKLEME, DEĞİŞTİRME, SİLME İŞLEMLERİ
#Eleman değiştirme
liste = ["ali","veli","berkcan","ayse"]
liste # ['ali', 'veli', 'berkcan', 'ayse']

liste[1] = "velinin_babası"
liste # ['ali', 'velinin_babası', 'berkcan', 'ayse']

liste[1]= "veli"
liste[0:3] = "alinin_babasi", "velinin_babasi", "berkcanin_babasi"

liste # ['alinin_babasi', 'velinin_babasi', 'berkcanin_babasi', 'ayse']

liste = ["ali","veli","berkcan","ayse"]

liste = liste + ["kemal"]

liste # ['ali', 'veli', 'berkcan', 'ayse', 'kemal']

# del liste[2] # listedeki 2. indeksi siler

liste # ['ali', 'veli', 'ayse', 'kemal']

#-------------------------------------------------
# METODLAR İLE ELEMAN EKLEME & SİLME: (append & remove)
liste = ["ali", "veli", "isik"]

dir(liste)

liste # ['ali', 'veli', 'isik']

#append
liste.append("berkcan") # bu metod kalıcı değişikliğe sebep oldu. bazı metodlar kalıcı değişikliğe yol açmaz.
liste # ['ali', 'veli', 'isik', 'berkcan']

liste.remove("berkcan")
liste # ['ali', 'veli', 'isik']

#-------------------------------------------------
# INDEKSE GÖRE ELEMAN EKLEME & SİLME: insert & pop
liste

## insert
liste.insert(0, "ayse")
liste # ['ayse', 'ali', 'veli', 'isik']

liste.insert(2, "mehmet")
liste # ['ayse', 'ali', 'mehmet', 'veli', 'isik']

liste.insert(5, "berk")
liste # ['ayse', 'ali', 'mehmet', 'veli', 'isik', 'berk']

liste.insert(len(liste), "beren")
liste # ['ayse', 'ali', 'mehmet', 'veli', 'isik', 'berk', 'beren']

##pop
liste.pop(0)
liste # ['ali', 'mehmet', 'veli', 'isik', 'berk', 'beren']

liste.pop(4)
liste # ['ali', 'mehmet', 'veli', 'isik', 'beren']

#-------------------------------------------------
# DİĞER LİSTE METODLARI

liste = ["ali","veli","isik","ali","veli"]

# count
liste.count("ali") # 2
liste.count("veli") #2
liste.count("isik") #1

#copy
liste_yedek = liste.copy()

#extend
liste.extend(["a","b",10])
liste # ['ali', 'veli', 'isik', 'ali', 'veli', 'a', 'b', 10]

#index
liste.index("ali") # 0

#reverse()
liste.reverse()
liste # [10, 'b', 'a', 'veli', 'ali', 'isik', 'veli', 'ali']

#sort()
liste.sort() # TypeError: Listede hem str hem de int değerler olduğu için sıralayamıyor

liste = [10,40,5,90]
liste.sort()
liste # [5, 10, 40, 90]

#clear
liste.clear()
liste # []

#-------------------------------------------------
# TUPLE(DEMET) OLUŞTURMA
# Tuple'lar kapsayıcıdır(birbirinden farklı veri tiplerini barındırabilirler), sıralıdır(içerisinde indeks işlemleri yapılabilir) fakat listelerden farklı olarak değiştirilemezlerdir(tuple oluştuktan sonra değişemez).

t = ("ali","veli",1,2,3.2,[1,2,3,4])
dir(t)

t = "ali","veli",1,2,3.2,[1,2,3,4]

#tuple() fonksiyon ile de tuple oluşturulabilir
t = ("eleman") # str döndü, tek elemanlı tuple oluştururken elemanın sonuna virgül atmak gerekir.
type(t) #str

t = ("eleman",)
type(t) #tuple

#-------------------------------------------------
# TUPLE(DEMET) ELEMAN İŞLEMLERİ
t = ("ali","veli",1,2,3,[1,2,3,4])
t # ('ali', 'veli', 1, 2, 3, [1, 2, 3, 4])

#tuple elemanlarına erişmek, liste elemanlarına erişmek gibidir. İndeks üzerinden elemanlara erişilebilir.
t[1] # 'veli'
t[0:3] # ('ali', 'veli', 1)

t[2] = 99 # TypeError, tuple nesnesi atama işlemine izin vermez.

# bazı durumlarda veri yapıları sabit dursun ve değişmeyeceğine emin olmak istediğimiz durumlarda tuple kullanılır.

#-------------------------------------------------
# SÖZLÜK(DİCTİONARY) OLUŞTURMA - VERİ YAPILARI
# Sözlükler, Kapsayıcıdır, Sırasızdır, Değiştirilebilir
# Anahtar ifadeler(key) ve bu anahtar ifadelerin karşılıklarının(value) bir arada tutulduğu veri yapılarıdır. Referanslı bir veri yapısıdır.
# Listelerde ve Tuplelarda olduğu gibi index işlemleri yapılamaz. 

sozluk = {
        "REG" : "Regresyon Modeli",
        "LOJ" : "Lojistik Regresyon",
        "CART": "Classification and Reg"
    }

len(sozluk) # 3

sozluk = {
        "REG" : 11,
        "LOJ" : 22,
        "CART": 33
    }

sozluk = {
        "REG" : ["RMSE",11],
        "LOJ" : ["MSE",22],
        "CART": ["SSE",33]
    }

sozluk

#-------------------------------------------------
# SÖZLUK(DİCTİONARY) ELEMAN SEÇME İŞLEMLERİ

sozluk = {
        "REG" : "Regresyon Modeli",
        "LOJ" : "Lojistik Regresyon",
        "CART": "Classification and Reg"
    }

sozluk[0] # KeyError: İndekslenemez(Sırasız) olduğu için bu hatayı aldık

sozluk["REG"] # 'Regresyon Modeli'

sozluk = {
        "REG" : ["RMSE",11],
        "LOJ" : ["MSE",22],
        "CART": ["SSE",33]
    }

sozluk["REG"] # ['RMSE', 11]

sozluk = {
        "REG" : {"RMSE": 10,
                 "MSE": 20,
                 "SSE": 30},
        "LOJ" : {"RMSE": 10,
                 "MSE": 20,
                 "SSE": 30},
        "CART": {"RMSE": 10,
                 "MSE": 20,
                 "SSE": 30}
    }

sozluk # {'REG': {'RMSE': 10, 'MSE': 20, 'SSE': 30}, 'LOJ': {'RMSE': 10, 'MSE': 20, 'SSE': 30}, 'CART': {'RMSE': 10, 'MSE': 20, 'SSE': 30}}

sozluk["REG"]["SSE"] # 30
 
#-------------------------------------------------
# SÖZLÜK(DİCTİONARY) ELEMAN EKLEME & DEĞİŞTİRME
sozluk = {
        "REG" : "Regresyon Modeli",
        "LOJ" : "Lojistik Regresyon",
        "CART": "Classification and Reg"
    }

sozluk["GBM"] = "Gradient Boosting Mac"

sozluk # {'REG': 'Regresyon Modeli',
       # 'LOJ': 'Lojistik Regresyon',
       # 'CART': 'Classification and Reg',
       # 'GBM': 'Gradient Boosting Mac'}

sozluk

sozluk["REG"] = "Çoklu Doğrusal Regresyon"

sozluk # {'REG': 'Çoklu Doğrusal Regresyon',
       # 'LOJ': 'Lojistik Regresyon',
       # 'CART': 'Classification and Reg',
       # 'GBM': 'Gradient Boosting Mac'}
       
# Eğer sözlük ifadesini yazdıktan sonra köşeli parantez içerisine olmayan bir key yazıldığında, program onu "benim sözlüğümde böyle bir key yok, o zaman bu verilen key için yeni bir değer oluşturayım" der ve yeni key-value çifti oluşturur. 

dir(sozluk)  

sozluk[1] # KeyError - Böyle bir ifade yok hatası aldık

sozluk[1] = "Yapay Sinir Ağları"

sozluk # {'REG': 'Çoklu Doğrusal Regresyon',
         #'LOJ': 'Lojistik Regresyon',
         #'CART': 'Classification and Reg',
         #'GBM': 'Gradient Boosting Mac',
         #1: 'Yapay Sinir Ağları'}

l = [1] # yeni bir liste

sozluk[l] = "yeni bir şey" # TypeError - Sözlüklerde key değerleri ancak sabit veri yapılarıyla oluşturulabilir(stringler, sayılar vb.). 
# Key'ler sabitliğinden endişe etmeyeceğimiz referans değerlerdir. Value'lar değişebilir, sorun değil.

t = ("tuple",) # tuple, sabit veri yapısır

sozluk[t] = "yeni bir şey"

sozluk # {'REG': 'Çoklu Doğrusal Regresyon',
       #'LOJ': 'Lojistik Regresyon',
       #'CART': 'Classification and Reg',
       #'GBM': 'Gradient Boosting Mac',
       #1: 'Yapay Sinir Ağları',
       #('tuple',): 'yeni bir şey'}

#-------------------------------------------------
#SET(KÜME) OLUŞTURMA
# Sırasızdır, Değerleri eşsizdir(unique), Değiştirilebilirdir, Farklı tipleri barındırabilir.
# Performans odaklı bir veri yapısıdır. Eşsiz değerler istediğimizde kullanırız.

s = set()
s

l = [1, "a", "ali", 123]
s = set(l)
s # {1, 123, 'a', 'ali'}

t = ("a", "ali")
s = set(t)
s # {'a', 'ali'}

ali = "lutfen_ata_bakma_uzaya_git"
type(ali)

s = set(ali)
s # {'_', 'a', 'b', 'e', 'f', 'g', 'i', 'k', 'l', 'm', 'n', 't', 'u', 'y', 'z'} tüm karakterler tek bir defa yazılmış

# Set oluşturma aşamasında verdiğimiz şeyler eğer birden çok sayıda ise, set bunları tek ve unique olacak şekilde düzenler

l = ["ali","lütfen","ata","bakma","uzaya","git","git","ali","git"]
l
s = set(l)
s # {'ali', 'ata', 'bakma', 'git', 'lütfen', 'uzaya'}

len(s) # 6

l[0] # 'ali'

s[0] # TypeError: set nesnesi index işlemini desteklemiyor

#-------------------------------------------------
# SETLERDE ELEMAN EKLEME & ÇIKARMA
l = ["gelecegi","yazanlar"]

s = set(l)
s # {'gelecegi', 'yazanlar'}

dir(s)

s.add("ile")
s # {'gelecegi', 'ile', 'yazanlar'}

s.add("gelecege_git")
s # {'gelecege_git', 'gelecegi', 'ile', 'yazanlar'}

# add ile setimize yeni değerler eklediğimizde, yeni gelen değerler sette rastgele bir yere gidebilir.

s.add("ile")
s

s.remove("ile")
s

s.remove("ile") # KeyError, bu şeyi bulamadım
s

s.discard("ali") # Bu hata vermez ama bir işlemde de bulunmaz

#-------------------------------------------------
 #SETLERDE FARK İŞLEMLERİ: difference & symmetric_difference
#======================================================
#  difference() ile iki kumenin farkını yada "-" ifadesi
#  intersection() iki küme kesişimi yada "&" ifadesi
#  union() iki kümenin birleşimi
#  symmetric_difference() ikisinde de olmayanları.
#======================================================
 
# difference
set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2) # 5  set1'de olup set2'de olmayan değerler

set2.difference(set1) # 2  set2'de olup set1'de olmayan değerler

# symmetric_difference
set1.symmetric_difference(set2) # {2, 5} ikisinde de olmayanlar

set1 - set2 # {5}
set2 - set1 # {2}

# intersection
set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2) # {1, 3} iki kümenin kesişimi
set2.intersection(set1) # {1, 3}

set1 & set2 # {1, 3}

# union
birlesim = set1.union(set2) # {1, 2, 3, 5}
birlesim

set1.intersection_update(set2) # set1'in set2'yle kesişim kümesi set1'in yeni hali olur.
set1 # {1, 3}

#-------------------------------------------------
# SETLERDE SORGU İŞLEMLERİ
# Kod akışı içerisinde kümülatif bazı işlemler gerçekleşirken setler arasında kesişimin boş olup olmadığını sorgulamak gibi, bir set diğer seti kapsar mı? gibi sorgulamaların fonksiyonel anlamda yapıldığı işlemlerdir.

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])


# iki kümenin kesişiminin boş olup olmadığının sorgulanması
set1.isdisjoint(set2) # False   İki kümenin kesişimi boş mu?

# Bir kümenin bütün elemanlarının başka bir küme içerisinde yer alıp almadığı
set1.issubset(set2) # True, set1 set2'nin alt kümesidir

# Bir küme diğer kümeyi kapsıyor mu?
set2.issuperset(set1) # True, evet set2 set1'i kapsıyor

#-------------------------------------------------
# FONKSİYONLARA GİRİŞ VE FOKSİYON OKURYAZARLIĞI
# Fonksiyon ve döküman okuryazarlığı bir yazılımcının en önemli özelliklerindendir.

print("merhaba", "dünya", sep="_")
#?print # fonksiyon hakkında bilgi verir
print()

len("a")

#?len
#-------------------------------------------------
# FONKSİYONLAR NASIL YAZILIR?
# Matematiksel işlemler
4*4 # 16
4/4 # 1.0
5-1 # 4
6+3 # 9
3**2 # 9
3**3 # 27

# Kendi fonksiyonunu hazırla
def kare_al(x):
    print(x**2)
    

kare_al(3) # 9
#-------------------------------------------------
#11-07-2024
# BİLGİ NOTUYLA ÇIKTI ÜRETMEK

def kare_al(x):
    print("Girilen sayının  karesi: " + x**2)

kare_al(3) # TypeError, String ifadeler sadece string ifadeler ile birleştirilebilir.

def kare_al(x):
    print("Girilen sayının  karesi: " + str(x**2))

kare_al(3) # Girilen sayının  karesi: 9

def kare_al(x):
    print("Girilen sayı: " + str(x) +  
          ", Karesi: " + str(x**2))

kare_al(3) # Girilen sayı: 3, Karesi: 9

#-------------------------------------------------
# İKİ ARGÜMANLI FONKSİYON TANIMLAMAK

def carpma_yap(x, y):
    print(x*y)

carpma_yap(3, 5) # 15

#-------------------------------------------------
# ÖN TANIMLI ARGÜMANLAR
# Kullanıcıların hata yapma ihtimallerini önlemek adına, bazı argümanları ön tanımlı olarak veririz.

def carpma_yap(x, y):
    print(x*y)

carpma_yap(3) # TypeError, gereken bir argüman yok 'y'

def carpma_yap(x, y = 1):
    print(x*y)

carpma_yap(3) # 3

carpma_yap(3, 4) # 12, argümanda 1 verdik diye her zaman 1 olmaz.  Ön tanımlı değeri göz ardı eder.

# Argümanların Sıralaması
def carpma_yap(x, y = 1):
    print(x*y)
    print("X'in değeri: " + str(x) + " Y'nin değeri: " + str(y))

carpma_yap(y = 2, x = 3) # 6 X'in değeri: 3 Y'nin değeri: 2, Argümanların isimlerini biliyoruz fakat sıralarını bilmiyorsak önemli değil, sıralamadan bağımsız olarak argümanlara değer verebiliriz.

#-------------------------------------------------
# NE ZAMAN FONKSİYON YAZILIR?
# Fonksiyonlar, tekrar eden görevleri yerine getirmek ve var olan işleri daha programatik şekilde gerçekleştirmek için kullanılır. Sık tekrar eden veya uzun işlemlerden kurtulmak adına fonksiyonları kullanırız.

# isi, nem, sarj
(40+25)/90 # 0.7222222222222222

def direk_hesap(isi, nem, sarj): # ihtiyaca fonksiyon giydirmek
    print((isi + nem) / sarj)

direk_hesap(25, 40, 70) # 0.9285714285714286

#-------------------------------------------------
# FONKSİYON ÇIKTILARINI GİRDİ OLARAK KULLANMAK: return

def direk_hesap(isi, nem, sarj): 
    print((isi + nem) / sarj)

cikti = direk_hesap(25, 40, 70) # NoneType Object
cikti # cikti
print(cikti) # none, direk_hesap'ın çıktısını işleyemedik

direk_hesap(25, 40, 70) * 9 # TypeError

def direk_hesap(isi, nem, sarj): 
    return (isi + nem) / sarj

direk_hesap(25, 40, 70) # 0.9285714285714286, çıktı hesabı yine geldi

cikti = direk_hesap(25, 40, 70) * 9 # 8.357142857142858 bu sefer hata vermedi, çünkü return kullandık
cikti # 8.357142857142858
print(cikti) # 8.357142857142858

# Eğer bir fonksiyonun çıktısını başka bir fonksiyonun veya işlemin girdisi olarak kullanmak istiyorsak, bu durumda return ifadesini kullanılırız.

#-------------------------------------------------
# LOCAL VE GLOBAL DEĞİŞKENLER
# Ana çalışma alanımızdaki değişkenler global değişkenlerdir, lokal değişkenler fonksiyonların etki alanlarında tanımlanmış değişkenlerdir

x = 10 # global değişkenlerdir
y = 20 # global değişkenlerdir

def carpma_yap(x = 2, y = 1): # x ve y lokal değişkenlerdir
    return x*y

carpma_yap(2, 3) # 6

#-------------------------------------------------
# LOCAL ETKİ ALANINDAN GLOBAL ETKİ ALANINI DEĞİŞTİRME
# Tanımlamış olduğumuz bir fonksiyon ya da yazıyor olduğumuz bir döngü içerisinde global değişkenlerin değerlerinde bir değişiklik yapmak istersek ne yapacağız?

x = []

def eleman_ekle(y):
    x.append(y) # liste'ye y'yi ekle
    print(str(y) + " ifadesi eklendi")

eleman_ekle(5)
x # [5]
eleman_ekle('a')
x # [5, 'a']

x = []

# del x

def eleman_ekle(y):
    x.append(y) # liste'ye y'yi ekle
    print(str(y) + " ifadesi eklendi")

eleman_ekle(5) # NameError: X bulunamadı. Çünkü x'i sildik.

#-------------------------------------------------
# TRUE-FALSE SORGULAMALARI - KARAR-KONTROL YAPILARI
#True-false sorgu mekanizmalarıdır
sinir = 5000

sinir == 4000 # False

sinir == 5000 # True

5 == 4 # False

5 == 5 # True

#-------------------------------------------------
# İF

sinir = 50000 # Geliri 50000 TL'den düşük olan mağazaları kapat.

gelir = 40000

gelir < sinir # True

if gelir < sinir: 
    print("Gelir sinirdan küçük")
    print(gelir*2)

gelir = 60000

gelir < sinir # False

if gelir < sinir: 
    print("Gelir sinirdan küçük") # False geldiği için bir çıktı vermedi.
    
if gelir > sinir: 
    print("Gelir sinirdan büyük") # Gelir sinirdan büyük
    
#-------------------------------------------------
# ELSE

sinir = 50000
gelir = 35000

if gelir > sinir: 
    print("Gelir sinirdan büyük")
else:
    print("Gelir sinirdan küçük") # Gelir sinirdan küçük

sinir = 50000
gelir = 51000

if gelir == sinir: 
    print("Gelir sinira eşittir")
else:
    print("Gelir sinira eşit değildir") # Gelir sinira eşit değildir

sinir = 50000
gelir = 50000

if gelir == sinir: 
    print("Gelir sinira eşittir")
else:
    print("Gelir sinira eşit değildir") # Gelir sinira eşittir

#-------------------------------------------------
# ELİF
sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000

if gelir1 > sinir: 
    print("Tebrikler. Prim kazandınız.") # Tebrikler. Prim kazandınız
elif gelir1 < sinir:
    print("Daha karlı satışlar yapmalısınız.")
else:
    print("Denetime devam edelim.") 


if gelir2 > sinir: 
    print("Tebrikler. Prim kazandınız.") 
elif gelir2 < sinir:
    print("Daha karlı satışlar yapmalısınız.")
else:
    print("Denetime devam edelim.") # Denetime devam edelim.


if gelir3 > sinir: 
    print("Tebrikler. Prim kazandınız.") 
elif gelir3 < sinir:
    print("Daha karlı satışlar yapmalısınız.")
else:
    print("Denetime devam edelim.")  # Daha karlı satışlar yapmalısınız.

#-------------------------------------------------
# UYGULAMA (İF VE İNPUT İLE KULLANICI ETKİLEŞİMLİ PROGRAM)
sinir = 50000
magaza_adi = input("Magaza adi nedir? ")
gelir = int(input("Gelirinizi Giriniz: ")) # str olarak alındığı için TypeError hatası verdi.

if gelir > sinir:
    print("Tebrikler! " + magaza_adi + " İyi gidiyorsunuz")
elif gelir < sinir:
    print("Biraz daha gayret edin " + str(gelir) + " ile zarardasınız") # Print fonksiyonunda string, int ile birleşemiyor. Bunun için intleri string çevirmek zorundayız.
else:
    print("Ha gayret. Neredeyse kar edeceksiniz.")

#-------------------------------------------------
# FOR DÖNGÜLERİ
# İteratif işlemleri yerine getirmek için kullandığımız yapılardır.

ogrenci = ["ali", "veli", "isik", "berk"]

ogrenci[0] # ali 
ogrenci[1] # veli 
# peki ya elimizde 1000 tane veri olsa hepsini teker teker yazmak zorunda mıyız? Hayır değiliz.

for i in ogrenci: # for döngüsü
    print(i)    #ali
                #veli
                #isik
                #berk

#-------------------------------------------------
# FOR - ÖRNEK

maaslar = [1000,2000,3000,4000,5000]

maaslar[0]
maaslar[1]
maaslar[2]
maaslar[3]
maaslar[4]

for maas in maaslar:
    print(maas*2) #2000
                  #4000
                  #6000
                  #8000
                  #10000

for i in maaslar:
    print(i)

toplam_maas = 0
for i in maaslar:
    toplam_maas += i
    print(toplam_maas) # 15000

#-------------------------------------------------
# DÖNGÜ VE FONKSİYONLARIN BİRLİKTE KULLANIMI

def kare_al(x):
    print(x**2)
    
kare_al(2)

maaslar = [1000,2000,3000,4000,5000]

for i in maaslar:
    print(i)

# Maaşlara yüzde 20 zam yapılacak. Gerekli kodları yazınız.

maaslar[0] * 20 / 100 + maaslar[0]
maaslar[1] * 20 / 100 + maaslar[1]
# Binlerce kişinin maaşı bu şekilde hesaplanamaz. Bir döngü yazılması gerekli ve fonksiyon yazılmalı.

def zamli_maas(x):
    print(x)

zamli_maas(4) # 4

def zamli_maas(x):
    print(x * 20 / 100 + x)

zamli_maas(1000) # 1200 . Bu yöntem hala yeterli değil

for i in maaslar:
    zamli_maas(i) #1200.0
                  #2400.0
                  #3600.0
                  #4800.0
                  #6000.0

#-------------------------------------------------
# İF, FOR VE FONKSİYONLARIN BİRLİKTE KULLANIMI

# Maaşı 3000'den az olanlara %20, 3000'den fazla olanlara %10 zam yapacağız.
maaslar = [1000,2000,3000,4000,5000]

def maas_ust(x):
    print(x*10/100+x)

def maas_alt(x):
    print(x*20/100+x)

for i in maaslar:
    if i >= 3000:
        maas_ust(i)
    else:
        maas_alt(i)
#-------------------------------------------------
# BREAK & CONTİNUE
# Döngüler içerisinde bazen belirli bir şartı sağlayan elemanlar yakalandığında(ifler ile yakalanır), döngü bitirilmek istenebilir yada bu şartı sağlayan eleman görmezden gelinmek istenebilir. İşte bu durumlarda break & continue ifadeleri kullanılır.

maaslar = [8000,5000,2000,1000,3000,7000,1000]

dir(maaslar)

maaslar.sort()
maaslar

for i in maaslar:
    if i == 3000:
        print("kesildi")
        break
    print(i) # 1000
             # 1000
             # 2000
             # kesildi

for i in maaslar:
    if i == 3000:
        continue
    print(i) # 1000
             # 1000
             # 2000
             # 5000
             # 7000
             # 8000

#-------------------------------------------------
# WHİLE
# While, bu şart sağlandığı sürece demektir.

sayi = 1

while sayi < 10:
    print(sayi) # 1 2 3 4 5 6 7 8 9
    sayi += 1 
    
#12-07-2024
#-------------------------------------------------
# NESNE YÖNELİMLİ PROGRAMLAMA
# SINIFLARA(CLASS) GİRİŞ VE SINIF TANIMLAMAK

# Class(Sınıf) nedir? Benzer özellikler, ortak amaçlar taşıyan, içerisinde metod ve değişkenler olan yapılardır.

#class VeriBilimci():
#    print("Bu bir siniftir")    

#-------------------------------------------------
# SINIF ÖZELLİKLERİ(CLASS ATTRİBUTES)

class VeriBilimci():
    bolum = ''
    sql = 'Evet' # Ön kabul evet
    deneyim_yili = 0
    bildigi_diller = []

# Siniflarin özelliklerine erismek
VeriBilimci.bolum
VeriBilimci.sql

# Sınıfların özelliklerini değiştirmek
VeriBilimci.sql = "Hayir"
VeriBilimci.sql # 'Hayır'

#-------------------------------------------------
# SINIF ÖRNEKLENDİRMESİ(INSTANTİATİON)

ali = VeriBilimci()

ali.sql # 'Hayir'
ali.deneyim_yili # 0
ali.bolum # ''
ali.bildigi_diller.append("Python") 
ali.bildigi_diller # ['Python']

veli = VeriBilimci()
veli.sql # 'Hayir'

veli.bildigi_diller # ['Python'] ali.bildigi_diller.append("Python") # Burada yapılan değişiklik tüm sınıfa mal oldu

#-------------------------------------------------




























