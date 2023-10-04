# Sağ Tuş ile Pdf'i Açmadan Resime Dönüştürün
Pdf dosyalarını farenin sağ tuşundan bat dosyasına gönderin, uygulama açılan inputa girdiğiniz sayfa numarasının resmini kaydeder ve clipboard'a kopyalar

Python kurmak istemeyenler için Build.7z dosyasını indirip aşağıdaki gif gibi farenin sağ tuşuna ekleme metoduyla veya pdf dosyasını app.exe'nin üstüne sürükleyerek kullanabilirisiniz. Hareketli görüntüde tüm dosyaların sağ tuşuna ekleme görülmekte.

![Kullanım Şekli](https://github.com/matasoy/rigthclick_pdftoimg/blob/97c3a8dc18f85ac6cbd8003a7a4f468311b537c9/pdftopng.gif)

Sadece PDF dosyalarına eklemek isterseniz regeditte "HKEY_CLASSES_ROOT\SystemFileAssociations\.pdf\shell" yoluna aşağıdaki resimdeki gibi BAT dosyasını veya EXE dosyasının yolunu girmeniz yeterlidir.

![Sağ Klik Menüsüne Yerleştirme](https://github.com/matasoy/rigthclick_pdftoimg/blob/main/sag_klik.jpg)


Python ile kullanmak isteyenler öncelikle aşağıdaki kütüphaneleri kurun
- pip install pywin32
- pip install pdf2image
- pip install tk

pdf2img kütüphanesi poppler kütüphanesine ihtiyaç duyuyor. Windowsa kurmak için https://github.com/oschwartz10612/poppler-windows/releases/latest adresinde gidin. Zip dosyasını indirin. Zipten çıkartarak bilgisayarınızda sabit bir yere taşıyın (Ben python klasörünün yanına koydum). C:\Users\%username%\AppData\Local\Programs\Python\poppler-23.08.0 . Daha sonra bin klasörünü PATH e eklemeniz lazım. Bunun için Sistem->Gelişmiş Sistem Ayarları->Ortam Değişkenleri->Kullanıcı Değişkenleri->Path e tıklayın ve düzenle diyerek yeni bir satır olarak ekleyin. Açıksa command panellerinizi kapatın, proppler yeni açtığınız cmd ekranlarında çalışacaktır.

- Bat dosyasının adını istediğiniz gibi değiştirin ve şuraya atın C:\Users\%username%\AppData\Roaming\Microsoft\Windows\SendTo
- Bat dosyası içindeki app.py dosya yolunu kendinize göre güncelleyin ve tamamdır.
