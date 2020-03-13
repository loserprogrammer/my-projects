f = open("hitori_bulmaca.txt","r")     # BU PROGRAMLA AYNI KLASÖRDE BULUNAN TXT DOSYAMIZI OKUMA MODUNDA AÇMA İŞLEMİ
ilksatır = f.readline()                # N*N LİK FORMATTA OLAN BULMACA SAYILARIMIZIN İLK SATIRINI OKUMA İŞLEMİ. KAÇ SATIR OKUMAMIZ GEREKTİĞİNİ İLK SATIRDAKİ ELEMAN SAYISINA GÖRE BELİRLEDİĞİM İÇİN ÖNCE SADECE İLK SATIRI ALDIK
ilksatır = ilksatır[0:len(ilksatır)-1]  # SATIRIN SONUNDAKİ \N KARAKTERİNİ SİLİYORUZ
dizi = ilksatır.split(" ")              # İLKSATIR STRİNGİNİ BOŞLUK KARAKTERİNE GÖRE AYIRIP DİZİYE ATIYORUZ
sayılar = []                            # N ELEMANLI DİZİLERİ İÇİNE EKLEYECEĞİMİZ İKİ BOYUTLU DİZİ
sayılar.append(dizi)
for i in range(1,len(dizi)):            # YUKARDAKİ İŞLEMLERİ DİĞER SATIRLAR İÇİN YAPAN FOR DÖNGÜSÜ
    satır = f.readline()
    satır = satır[0:len(satır)-1]
    array  = satır.split(" ")
    sayılar.append(array)
f.close()    #DOSYAYLA İŞİMİZ BİTTİ. DOSYAYI KAPATIYORUZ

tablodizisi = []    # OYUNDA BOŞ/DOLU OLARAK İŞARETLENEN VEYA NORMAL SAYILARIMIZI TUTAN , OYUNUN GÜNCEL HALİNİ TUTAN İKİ BOYUTLU DİZİMİZ
for i in range(len(dizi)):  # OYUN BAŞLANGICINDA BÜTÜN SAYILAR İŞARETSİZ OLARAK BAŞLAYACAĞIMIZ İÇİN SAYILAR DİZİSİNİ BU DİZİYE AKTARIYORUZ
    adizi = []
    for j in range(len(dizi)):
        adizi.append(0)
        adizi[j] = "-"+sayılar[i][j]+"-"
    tablodizisi.append(adizi)

def doluindex():    #TABLODİZİSİNDEKİ BOŞ OLARAK İŞARETLİ OLMAYAN VE İLK KARŞIMIZA ÇIKAN İNDEXİ DÖNDÜREN METHOD. BFS'ÜN HANGİ İNDEXTEN BAŞLAYACAĞINI BELİRLEMEK İÇİN
    for i in range(len(tablodizisi)):
        for j in range(len(tablodizisi)):
            if (tablodizisi[i][j] != "-X-"):
                return i * len(tablodizisi) + j

def oyuntablosu():  # TABLODİZİSİNİ EKRANA YAZDIRAN METHOD
    print(" ",end="")
    for i in range(len(tablodizisi)):
        print(" ",i+1,end="")
    print()
    for i in range(len(tablodizisi)):
        for j in range(len(tablodizisi)):
            if(j==0):
                print(i+1,end=" ")
            print(tablodizisi[i][j],end="")
        print()

def oyunBittiMi():  # OYUNUN BİTMESİ İÇİN GEREKEN 3 KURALI KONTROL EDİP OYUN BİTMEMİŞ DURUMDAYSA FALSE,BİTMİŞSE TRUE DÖNDÜREN METHOD
    for i in range(len(tablodizisi)):       # BURADA SATIRDA BİR SAYININ BİRDEN FAZLA OLUP OLMADIĞINI KONTROL ETTİK
        for j in range(len(tablodizisi)-1):
            eleman  = tablodizisi[i][j]
            if(eleman != "-X-"):
                for k in range(j + 1, len(tablodizisi)):
                    if (eleman[1] == tablodizisi[i][k][1]):
                        return False

            else:
                if(eleman == tablodizisi[i][j+1] ):
                    return False

    for i in range(len(tablodizisi)-1):  # BURADA SÜTUNLARDA BİR SAYININ BİRDEN FAZLA OLUP OLMADIĞINI KONTROL ETTİK
        for j in range(len(tablodizisi)):
            eleman = tablodizisi[i][j]
            if (eleman != "-X-"):
                for k in range(i+1,len(tablodizisi)):
                    if(eleman[1] == tablodizisi[k][j][1]):
                        return False

            else:
                if(eleman == tablodizisi[i+1][j]):
                    return False
    #AŞAĞIDAKİ KISIMDA 3.KURALIN SAĞLANIP SAĞLANMADIĞINI BREADTH FİRST SEARCH İLE KONTROL ETTİK
    komşuluktablosu = []  #TABLODİZİMİZDE BOŞ OLMAYAN BİR ELEMANIN KOMŞU OLDUĞU ELEMANLARI TRUE OLMADIKLARINI FALSE OLARAK ATAYARAK OLUŞTURDUĞUMUZ (N^2)*(N^2) LİK DİZİ
    for i in range(len(tablodizisi) * len(tablodizisi)): #BURDA İ DEĞERLERİ HER BİR ELEMANI TEMSİL EDECEK.ÖRNEĞİN 3*3 LÜK TABLO DİZİSİNİN [2][1] ELEMANI 7.ELEMANIMIZDIR
        dizi = []
        for j in range(len(tablodizisi) * len(tablodizisi)): # J DEĞERLERİ İSE İ.ELEMANA KOMŞULUĞU OLUP OLMADIĞINI BELİRLEMEK İÇİNDİR
            dizi.append(False) #BAŞTA DEFAULT OLARAK FALSE ATADIK.
            if(tablodizisi[int(i/len(tablodizisi))][i%len(tablodizisi)] != "-X-"): #İ.ELEMANIMIZ TABLO DİZİSİNDE HANGİ İNDEXE DENK GELDİĞİNİ BELİRLEDİK VE O ELEMANIN BOŞ DEĞİLSE KOMŞULARINI AŞAĞIDA TRUE YAPTIK
                if (i % len(tablodizisi) == len(tablodizisi) - 1): #İ.ELEMANIMIZIN TABLODİZİSİNİN SON SÜTUNUNDAYSA BU DURUMA GİRER VE J.ELEMAN KOMŞUSUYSA VE BOŞ DEĞİLSE TRUE YAPTIK
                    if ((j == i + len(tablodizisi) or j == i-1 or j == i-len(tablodizisi)) and tablodizisi[int(j / len(tablodizisi))][j % len(tablodizisi)] != "-X-"):
                        dizi[j] = True

                elif (i %len(tablodizisi) == 0): #İ.ELEMANIMIZ TABLODİZİSİNİN İLK SÜTUNUNDAYSA BU DURUMA GİRER
                    if ((j == i + 1  or j == i-len(tablodizisi) or j == i+len(tablodizisi))and tablodizisi[int(j / len(tablodizisi))][j % len(tablodizisi)] != "-X-"):
                        dizi[j] = True

                elif (j == i + 1 or j == i + len(tablodizisi) or j == i-1 or j == i-len(tablodizisi)): #YUKARDAKİ DURUMLAR HARİCİNDE BURAYA GELİNİR VE J DEĞERİ İ.ELEMANIMIZIN KOMŞUSUYSA VE BOŞ DEĞİLSE TRUE YAPTIK
                    if (tablodizisi[int(j / len(tablodizisi))][j % len(tablodizisi)] != "-X-"):
                        dizi[j] = True

        komşuluktablosu.append(dizi) # OLUŞAN N^2 ELEMALI BOOLEAN DİZİSİNİ KOMŞULUKTABLOSU DİZİSİNE EKLEDİK

    visited = []  #TABLODİZİSİNDEKİ ELEMANLARI BFS YAPILIRKEN EĞER ZİYARET EDİLDİYSE , O İNDEXE TRUE DEĞERİNİ ATAYAN VE BİR DAHA KUYRUĞA EKLENMEMESİNİ SAĞLAYAN N^2 ELEMANLI BOOLEAN DİZİ
    for i in range(len(tablodizisi)*len(tablodizisi)): #BAŞTA TÜM ELEMANLAR ZİYRET EDİLMEDİĞİ İÇİN HEPSİNE FALSE ATADIK
        visited.append(False)

    kuyruk = [] #BFS YAPILIRKEN ELEMAN EKLEYECEĞİMİZ VE ÇIKARIP YERİNE KOMŞULARINI KOYACAĞIMIZ KUYRUK DİZİMİZ
    startindex = doluindex() #BREADTH FİRST SEARCH ÜN BAŞLAYACAĞI İNDEX.EĞER 0.İNDEXTEN BAŞLASAYDIK VE BOŞ OLSAYDI BFS GERÇEKLEŞEMEZDİ.

    kuyruk.append(startindex) #BAŞLANGIÇ OLARAK KUYRUĞA BAŞLANGIÇ İNDEXİNİ EKLEDİK
    visited[startindex] = True #ZİYARET EDİLDİ OLARAK İŞARETLEDİK
    sayac = 0 #ZİYARET EDİLEN ELEMAN SAYISINI TUTAN SAYACIMIZ

    while(len(kuyruk)!=0): #KUYRUK BOŞALANA YANİ ZİYARET EDİLECEK İNDEX KALMAYINCAYA KADAR DÖNGÜ DEVAM EDER
        eleman = kuyruk.pop(0) #KUYRUK DZİMİZİN EN BAŞINDAKİ ELEMANI HER DÖNÜŞTE KUYRUKTAN SİLDİK VE DEĞİŞKENE ATADIK
        sayac+=1 # KUYRUKTAN HER ELEMAN SİLİNDİĞİNDE SAYACI ARTTIRDIK.BÖYLECE TOPLAMDA KAÇ ELEMAN ZİYARET EDİLDİ BELİRLEMİŞ OLDUK
        for i in range(len(komşuluktablosu)):
            if(komşuluktablosu[eleman][i] and (not visited[i])):#KUYRUKTAN ATTIĞIMIZ ELEMAN ,BİZE BULUNDUĞUMUZ İNDEXİ VERİR.KOMŞULUK TABLOSUNDA BULUNDUĞUMUZ İNDEXİN KOMŞULARI TRUE DEĞERİNDE OLDUĞU İÇİN EĞER BULUNDUĞUMUZ İNDEXİN KOMŞUSU ZİYARET EDİLMEDİYSE BURAYA GİRER
                kuyruk.append(i) #BULUNDUĞUMZ İNDEXİN KOMŞU İNDEXLERİNİ KUYRUĞA EKLEDİK
                visited[i] = True #ZİYARET EDİLDİ OLARAK İŞARETLEDİK

    count = 0  #TABLODİZİSİNDEKİ BOŞ OLMAYAN ELEMANLARIN SAYISINI TUTAN SAYAC
    for i in range(len(tablodizisi)):
        for j in range(len(tablodizisi)):
            if(tablodizisi[i][j] != "-X-"):
               count+=1

    if(sayac != count): #EĞER BFS YAPARAK ZİYARET ETTİĞİMİZ ELEMAN SAYISI OYUNUMUZDAKİ BOŞ OLMAYAN ELEMAN SAYISINA EŞİT DEĞİLSE TÜM ELEMANLARI GEZEMEMİŞİZ , DOLAYISIYLA DA BÜTÜN ELEMANLAR BİRBİRİYLE BAĞLANTILI DEĞİL DEMEKTİR
        return False

    return True #YUKARIDAKİ HİÇ BİR DURUMA GİRMEZSE OYUNUMUZUN BÜTÜN KURALLARI SAĞLANMIŞ DEMEKTİR.YANİ OYUNUN BİTMESİ GEREKİR

while(not oyunBittiMi()): #OYUNBİTTİMİ METODU FALSE DÖNDÜRDÜĞÜ SÜRECE OYUN DEVAM EDER
    oyuntablosu() #EN BAŞTA OYUN TABLOMUZUN GÜNCEL HALİNİ YAZDIRIYORUZ
    print("Satır numarasını ( 1 -",len(sayılar),"), sütun numarasını ( 1 -",len(sayılar),") ve işlem kodunu (B:boş, D:dolu, N:normal/işaretsiz) aralarında boşluk bırakarak giriniz:")
    girdi = input()
    girdi = girdi.split(" ")#OYUNCUDAN ALINAN GİRDİ BOŞLUKLU OLMASI GEREKTİĞİİÇİN SPLİT METODUYLA AYIRIP AYNI İSİMLİ DİZİYE ATIYORUZ
    while((len(girdi)!=3) or (girdi[0] not in ["1","2","3","4","5","6","7","8","9"])or (girdi[1] not in ["1","2","3","4","5","6","7","8","9"]) or  #HATA KONTROLLERİNİ YAPIYORUZ
              (int(girdi[0])>len(sayılar)) or (int(girdi[0])<1) or (int(girdi[1])>len(sayılar)) or (int(girdi[1])<1) or
              (girdi[2] not in ["B","D","N"] )):
        print("Hatalı giriş yaptınız!Satır numarasını ( 1 -", len(sayılar), "), sütun numarasını ( 1 -", len(sayılar),
                      ") ve işlem kodunu (B:boş, D:dolu, N:normal/işaretsiz) aralarında boşluk bırakarak giriniz:")
        girdi = input()
        girdi = girdi.split(" ")
    girdi = [int(girdi[0]),int(girdi[1]),girdi[2]] #ALIĞIMIZ GİRDİ DİZİSİNİN İLK 2 ELEMANINI İNT TİPİNE ÇEVİRİP TEKRAR DİZİYE ATIYORUZ
    #AŞAĞIDAKİ İŞLEMLERDE TABLODİZİSİNİ ALINAN GİRDİYE GÖRE GÜNCELLİYORUZ
    if(girdi[2] == "B"):
        tablodizisi[girdi[0]-1][girdi[1]-1] = "-X-"

    elif(girdi[2] == "N"):
        tablodizisi[girdi[0]-1][girdi[1]-1] = "-"+sayılar[girdi[0]-1][girdi[1]-1]+"-"

    else:
        tablodizisi[girdi[0]-1][girdi[1]-1] = "(" + sayılar[girdi[0]-1][girdi[1]-1] + ")"

oyuntablosu() #WHİLEDAN ÇIKILDIYSA BULMACA ÇÖZÜLMÜŞ DEMEKTİR OYUNUMUZUN SON HALİNİ YAZDIRIYORUZ
print("Tebrikler, bulmacayı çözdünüz! ")
