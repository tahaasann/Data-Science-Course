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












































