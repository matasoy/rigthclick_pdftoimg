# rigthclick_pdftoimg
Pdf dosyalarını farenin sağ tuşu ile resme dönüştürüp kaydeden ve ilk sayfanın resmini clipboard'a kopyalayan uygulama

Öncelikle aşağıdaki kütüphaneleri kurun
pip install pywin32
pip install pdf2image

pdf2img kütüphanesi poppler kütüphanesine ihtiyaç duyuyor. Windowsa kurmak için https://github.com/oschwartz10612/poppler-windows/releases/latest adresinde gidin. Zip dosyasını indirin. Zipten çıkartarak bilgisayarınızda sabit bir yere taşıyın (Ben python klasörünün yanına koydum). C:\Users\%username%\AppData\Local\Programs\Python\poppler-23.08.0 . Daha sonra bin klasörünü PATH e eklemeniz lazım. Bunun için Sistem->Gelişmiş Sistem Ayarları->Ortam Değişkenleri->Kullanıcı Değişkenleri->Path e tıklayın ve düzenle diyerek yeni bir satır olarak ekleyin. Açıksa command panellerinizi kapatın, proppler yeni açtığınız cmd ekranlarında çalışacaktır.
