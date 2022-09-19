"""
# SORU: sözlük uygulaması olsun Tr-Eng
#       sözlük={"siyah":"black"...}
#       kullanıcı 4 seçenekli bir menü verelim
#          1-Arama
2-Çıkarma
3-Listeleme
4-Çıkış
Kullanıcı 1'e basarsa ->
- Aranacak kelimeyi giriniz:
- Bu kelime dict varsa english karşılığını yazılır.
- Yoksa uygulamayı geliştirmek istermisiniz?
    - E ise bu kelimenin ingilizce karşılığını alırız ve sözlüğe eklenir.
    - H ise Peki..
Kullanıcı 2'e basarsa ->
- Çıkarılmak istenen kelime:
- Kelime sözlükte varsa çıkartılır.
- Yoksa uyarı verilir.
Kullanıcı 3'e basarsa ->
- Tum key value lar listenilir.
- KEY -> VALUE
Kullanıcı 4'e basarsa ->
- Döngü sonlanır..
"""
import time
listKey = list()
listValue = list()
sozluk={"siyah":"black"}
while True:
    secim = input("1 Arama\n2.Çıkarma\n3.Listeleme\n4.Çıkış\n")

    if secim =="1":
        ara = str(input("Aranacak kelimeyi söyleyiniz\n"))
        if ara in sozluk.keys():
            print(f"{ara} isimli kelimenin ingilizce karşılığı {sozluk[ara]} olarak gösteriliyor ")
            ara_secim = input("Uygulamaya devam etmek için (E) çıkmak için (Q) tuşuna basınız\n")
            if ara_secim == "E":
                continue
            elif ara_secim == "Q":
                print("Uygulama kapatılıyor,yine bekleriz.....")
                time.sleep(3)
                break
            else:
                print("Geçersiz işlem,yine bekleriz....")
                time.sleep(3)
                break

        else:
            sozluk_gelistirme = input("Uygulamayı geliştirmek istermisiniz? (E) or (H)\n").upper()
            if sozluk_gelistirme == "E":

                sozluk_gelistirme_secim_key = input("Lütfen eklemek istediğiniz kelimenin türkçesini yazınız\n").lower()
                sozluk_gelistirme_secim_value = input("Lütfen eklemek istediğiniz kelimenin ingilizce karşılığını yazınız\n").lower()
                listKey.append(sozluk_gelistirme_secim_key)
                listValue.append(sozluk_gelistirme_secim_value)
                for key in listKey:
                    for value in listValue:
                        sozluk[key] = value
                print("Yeni kelimenin ingilizce kavramsal karşılığı sözlüğe kaydedildi. Teşekkür ederiz\n")
                secim_iki = input("Uygulamayı geliştirmeye devam etmek ister misiniz? Evet için (E) tuşuna Çıkmak için (H) tuşuna basınız\n").upper()
                if secim_iki == "E":
                    print("2nci denemede ana menüye aktarılacaksınız\n")
                    sozluk_gelistirme_secim_key = input(
                        "Lütfen eklemek istediğiniz kelimenin türkçesini yazınız\n").lower()
                    sozluk_gelistirme_secim_value = input(
                        "Lütfen eklemek istediğiniz kelimenin ingilizce karşılığını yazınız\n").lower()
                    listKey.append(sozluk_gelistirme_secim_key)
                    listValue.append(sozluk_gelistirme_secim_value)
                    for key in listKey:
                        for value in listValue:
                            sozluk[key] = value
                elif secim_iki == "H":
                    continue
                else:
                    print("Geçersiz işlem,uygulama kapatılıyor....")
                    time.sleep(3)
                    break


            elif sozluk_gelistirme == "H":
                secim_uc = input("Uygulamadan çıkmak için (Q) uygulamaya devam etmek için (E) tuşuna basınız\n").upper()
                if secim_uc == "E":
                    continue
                else:
                    break
            else:
                print("Geçersiz işlem,uygulama kapatılıyor........")
                time.sleep(2)
                break
    elif secim == "2":
        print(sozluk)
        ara_iki = input("Lütfen sözlükten çıkarılacak kelimeyi giriniz\n")
        if ara_iki in sozluk:
            sozluk.pop(ara_iki)
            print(f"{ara_iki} kelimesi sözlükten çıkarıldı test etmek için (Q) tuşuna bas ve (Listeleme) seçeneğine odaklan\n")
            komut = input("").upper()
            if komut == "Q":
                continue
            else:
                print("Yanlış tuşa bastın")
                komut_bir = input("Lütfen (Q) tuşuna bas ve (Listeleme) seçeneğine odaklan\n").upper()
                if komut_bir == "Q":
                    continue
                else:
                    print("geçersiz işlem,uygulama kapatılıyor....")
                    time.sleep(3)
                    break

        else:
            print("Böyle bir kelime sözlükte yok")
            sozluk_cikar = input("Sözlükten çıkmak için (Q) devam etmek için (E) tuşuna basınız\n").upper()
            if sozluk_cikar == "E":

                ara_uc = input("Lütfen sözlükten çıkarılacak kelimeyi giriniz\n")
                if ara_uc in sozluk:
                    sozluk.pop(ara_uc)
                else:
                    print("Geçersiz işlem,uygulama kapatılıyor......")
                    time.sleep(2)
                    break
            elif sozluk_cikar == "Q":
                continue
            else:
                print("Geçersiz işlem,uygulama kapatılıyor......")
                time.sleep(3)
                break
    elif secim == "3":
        for x in sozluk.items():
            print(x)
        liste_dongu = input("Ana menuye dönmek için (E) tuşuna Programı kapatmak için (Q) tuşuna basınız\n")
        if liste_dongu == "E":
            continue
        elif liste_dongu == "Q":
            break

    elif secim == "4":
        print("Sözlük uygulaması kapatılıyor....")
        time.sleep(2)
        print("Yine bekleriz...")
        break















