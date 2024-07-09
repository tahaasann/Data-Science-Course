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
# Python'da kullanılan birden çok veri yapısı vardır: Listeler, tupplelar, dictonary vb... en sık kullanılan veri yapısı listelerdir.
# Listeler değiştirilebilir, kapsayıcıdır (farklı tipte verileri tutabilir), sıralıdır.
# []
# list()

notlar = [90,80,70,50]
type(notlar) # list

liste = ["a", 19.3, 90]
liste2 = ["a", 19.3, 90, notlar] 

len(liste2) # 4

#-------------------------------------------------



































































