> [!WARNING]
> `apps.txt` içerisinde yer alan paketler internet üzerindeki kullanıcıların sildiği paketlerdir. Cihazınızda oluşacak herhangi bir arıza/brick durumundan kullanıcın kendisi sorumludur.

# HyperOS deBloater
> Cihazına değer verenlerin tercihi...

## 📋 Proje Hakkında

HyperOS deBloater, Xiaomi HyperOS işletim sistemini kullanan Android cihazlardan gereksiz ön yüklü uygulamaları (bloatware) temizlemek için geliştirilmiş otomatik bir Python aracıdır.

### ✨ Özellikler

- ✅ **ADB Entegrasyonu** - Android Debug Bridge ile güvenli bağlantı
- ✅ **Root Desteği** - Rootlu ve rootsuz cihazlarda çalışır
- ✅ **Akıllı Silme** - Sistem korumalı paketler için alternatif yöntemler
- ✅ **Renkli Çıktı** - Terminalde görsel geri bildirim
- ✅ **Güvenli Kontrol** - Kritik Google bileşenleri korunur
- ✅ **Hata Yönetimi** - Başarısız işlemler raporlanır

### 🎯 Projenin Amacı

HyperOS işletim sistemini kullanan cihazları günlük hayatta kullanılmayan uygulamalardan arındırarak:
- 📱 Cihaz performansını artırmak
- 🔋 Pil ömrünü uzatmak
- 💾 Depolama alanı kazanmak
- 🚀 Sistem kaynaklarını optimize etmek

## 🚀 Kurulum

### Gereksinimler

- ✅ USB hata ayıklama açık olmalıdır
- ✅ Android Platform Tools (ADB)
- ✅ Python 3.x

### Kurulum Adımları

```bash
# Bağımlılıkları yükle
pip install -r requirements.txt

# Programı çalıştır
python3 main.py
```

### Kullanım

1. Cihazınızı USB ile bilgisayara bağlayın
2. USB hata ayıklamayı onaylayın
3. Script'i çalıştırın
4. Root desteği varsa belirtin
5. Listeyi kontrol edin ve onaylayın
6. Program otomatik olarak uygulamaları kaldırır

## 📦 Kaldırılabilecek Paketler

Aşağıdaki tabloda `apps.txt` dosyasında bulunan tüm paketler ve açıklamaları yer almaktadır:

| Paket Adı | Açıklama | Kategori |
|-----------|----------|----------|
| `com.miui.powerkeeper` | MIUI Güç Yöneticisi - Pil optimizasyonu | MIUI Sistem |
| `com.android.browser` | Varsayılan Android Tarayıcı | Tarayıcı |
| `com.miui.hybrid` | MIUI Hibrit Motor - Hızlı Uygulamalar | MIUI Sistem |
| `com.android.emergency` | Acil Durum Bilgileri | Sistem |
| `com.android.soundrecorder` | Ses Kaydedici | Multimedya |
| `com.google.android.apps.docs` | Google Docs | Google |
| `com.android.providers.downloads.ui` | İndirilenler Yöneticisi UI | Sistem |
| `com.miui.notes` | MIUI Notlar | MIUI Uygulama |
| `com.miui.screenrecorder` | MIUI Ekran Kaydedici | Multimedya |
| `com.android.dreams.phototable` | Fotoğraf Ekran Koruyucu | Tema |
| `com.xiaomi.glgm` | Xiaomi Oyun Servisi | Oyun |
| `com.android.calendar` | Android Takvim | Takvim |
| `com.miui.calculator` | MIUI Hesap Makinesi | Araçlar |
| `com.google.android.apps.maps` | Google Maps | Google |
| `com.miui.android.fashiongallery` | MIUI Moda Galerisi | Tema |
| `com.android.wallpaper.livepicker` | Canlı Duvar Kağıdı Seçici | Tema |
| `com.miui.compass` | MIUI Pusula | Araçlar |
| `com.mi.android.personalassistant` | Mi Kişisel Asistan | MIUI Uygulama |
| `com.android.stk` | SIM Araç Kiti | Sistem |
| `com.miui.player` | MIUI Müzik Çalar | Multimedya |
| `com.xiaomi.discover` | Xiaomi Keşfet | Xiaomi Servis |
| `com.android.cellbroadcastreceiver` | Acil Uyarı Mesajları | Sistem |
| `com.google.android.feedback` | Google Geri Bildirim | Google |
| `com.miui.bugreport` | MIUI Hata Raporu | MIUI Sistem |
| `com.miui.weather2` | MIUI Hava Durumu | MIUI Uygulama |
| `com.android.email` | Android E-posta | E-posta |
| `com.xiaomi.mipicks` | Mi Seçimleri - Uygulama Önerileri | Xiaomi Servis |
| `com.mi.android.fileexplorer` | Mi Dosya Yöneticisi | Araçlar |
| `com.android.htmlviewer` | HTML Görüntüleyici | Sistem |
| `com.miui.fm` | MIUI FM Radyo | Multimedya |
| `com.miui.fmservice` | MIUI FM Radyo Servisi | Multimedya |
| `com.miui.backup` | MIUI Yedekleme | MIUI Sistem |
| `com.miui.cloudbackup` | Mi Cloud Yedekleme | MIUI Sistem |
| `com.android.internal.cutout.emulation.corner` | Ekran Çentik Emülasyonu (Köşe) | Tema |
| `com.android.internal.display.cutout.emulation.tall` | Ekran Çentik Emülasyonu (Uzun) | Tema |
| `com.miui.touchassistant` | MIUI Dokunmatik Asistan - Kayan Düğme | MIUI Uygulama |
| `com.google.android.tts` | Google Metin Okuyucu | Google |
| `com.google.android.syncadapters.contacts` | Google Kişiler Senkronizasyonu | Google |
| `com.google.android.syncadapters.calendar` | Google Takvim Senkronizasyonu | Google |
| `com.xiaomi.scanner` | Mi Scanner - QR/Barkod Okuyucu | Araçlar |
| `com.android.providers.userdictionary` | Kullanıcı Sözlüğü | Sistem |
| `com.android.bips` | Varsayılan Yazdırma Servisi | Sistem |
| `com.miui.yellowpage` | MIUI Sarı Sayfa - Arama Kimlik | MIUI Uygulama |
| `com.android.printspooler` | Yazdırma Kuyruğu Yöneticisi | Sistem |
| `com.android.dreams.basic` | Temel Ekran Koruyucu | Tema |
| `com.android.systemui.theme.dark` | Sistem UI Karanlık Tema | Tema |
| `com.miui.global.packageinstaller` | MIUI Global Paket Yükleyici | MIUI Sistem |
| `com.android.deskclock` | Android Saat/Alarm | Araçlar |
| `com.miui.analytics` | MIUI Analitik - Kullanım İstatistikleri | MIUI Sistem |
| `com.android.egg` | Android Easter Egg | Sistem |
| `com.dsi.ant.server` | ANT+ Kablosuz Servis | Sistem |
| `com.miui.audioeffect` | MIUI Ses Efektleri | Multimedya |
| `com.aura.oobe.xiaomi` | Xiaomi İlk Kurulum Deneyimi | MIUI Sistem |
| `com.android.bookmarkprovider` | Tarayıcı Yer İmleri Sağlayıcı | Sistem |
| `com.android.chrome` | Google Chrome | Tarayıcı |
| `com.miui.qr` | MIUI QR Kod Tarayıcı | Araçlar |
| `com.android.providers.partnerbookmarks` | Ortak Yer İmleri | Sistem |
| `com.android.sharedstoragebackup` | Paylaşılan Depolama Yedekleme | Sistem |
| `com.android.wallpaperbackup` | Duvar Kağıdı Yedekleme | Sistem |
| `com.android.wallpapercropper` | Duvar Kağıdı Kırpıcı | Tema |
| `com.mfashiongallery.emag` | Moda Galerisi | Tema |
| `com.miui.antispam` | MIUI Anti-Spam | MIUI Sistem |
| `com.miui.extraphoto` | MIUI Fotoğraf Düzenleyici Eklentileri | Multimedya |
| `com.miui.smsextra` | MIUI SMS Eklentileri | MIUI Sistem |
| `com.miui.translation.kingsoft` | Kingsoft Çeviri Servisi | MIUI Sistem |
| `com.miui.translation.xmcloud` | Xiaomi Cloud Çeviri | MIUI Sistem |
| `com.miui.translation.youdao` | Youdao Çeviri Servisi | MIUI Sistem |
| `com.miui.translationservice` | MIUI Çeviri Servisi | MIUI Sistem |
| `com.qti.dpmserviceapp` | Qualcomm Veri Performans Yöneticisi | Sistem |
| `com.qualcomm.embms` | Qualcomm eMBMS (Multicast) | Sistem |
| `com.xiaomi.joyose` | Xiaomi Joyose Servisi | Xiaomi Servis |
| `com.google.android.apps.tachyon` | Google Duo | Google |
| `com.facebook.system` | Facebook Sistem Servisleri | Facebook |
| `com.facebook.appmanager` | Facebook Uygulama Yöneticisi | Facebook |
| `com.facebook.services` | Facebook Servisleri | Facebook |
| `com.google.android.gm` | Gmail | Google |
| `com.google.android.apps.photos` | Google Fotoğraflar | Google |
| `com.google.android.play.games` | Google Play Oyunlar | Google |
| `com.google.android.videos` | Google Play Filmler | Google |
| `com.google.android.music` | Google Play Müzik (YouTube Music) | Google |
| `com.xiaomi.mirecycle` | Mi Recycle - Geri Dönüşüm | Xiaomi Servis |
| `com.miui.hybrid.accessory` | MIUI Hibrit Aksesuar | MIUI Sistem |
| `com.caf.fmradio` | CAF FM Radyo | Multimedya |
| `com.miui.videoplayer` | MIUI Video Oynatıcı | Multimedya |
| `com.duokan.phone.remotecontroller` | Mi Uzaktan Kumanda | Araçlar |
| `com.miui.virtualsim` | MIUI Sanal SIM | MIUI Sistem |
| `com.xiaomi.payment` | Mi Ödeme | Xiaomi Servis |
| `com.xiaomi.midrop` | Mi Drop - Dosya Paylaşımı | Araçlar |
| `com.mipay.wallet.in` | Mi Pay Cüzdan (Hindistan) | Xiaomi Servis |
| `com.my.games.vendorapp` | My Games - Oyun Merkezi | Oyun |
| `com.miui.msa.global` | MIUI Reklam Servisi (MSA) | MIUI Sistem |
| `com.mi.globalTrendNews` | Mi Trend Haberleri | Xiaomi Servis |
| `com.netflix.partner.activation` | Netflix Aktivasyon Ortağı | Üçüncü Taraf |
| `com.duokan.phone.remotecontroller.peel.plugin` | Peel Uzaktan Kumanda Eklentisi | Araçlar |
| `com.google.android.printservice.recommendation` | Google Yazdırma Önerisi | Google |
| `com.fingerprints.sensortesttool` | Parmak İzi Sensör Test Aracı | Sistem |
| `com.google.android.marvin.talkback` | Android TalkBack - Ekran Okuyucu | Erişilebilirlik |
| `com.milink.service` | Mi Link Servisi - Cihaz Bağlantısı | MIUI Sistem |
| `com.miui.vsimcore` | MIUI Sanal SIM Çekirdeği | MIUI Sistem |
| `com.qualcomm.wfd.service` | Qualcomm Wi-Fi Display Servisi | Sistem |

## ⚠️ Önemli Uyarılar

- ❌ **Google Play Store** (`com.android.vending`) - Listeden çıkarıldı (kritik)
- ❌ **Gboard** (`com.google.android.inputmethod.latin`) - Listeden çıkarıldı (kritik)
- ❌ **Google App** (`com.google.android.googlequicksearchbox`) - Listeden çıkarıldı (kritik)
- ⚠️ Yanlış paket silinmesi cihazınızı kullanılamaz hale getirebilir
- ⚠️ İşlem öncesi yedek almak önerilir
- ⚠️ Sistem uygulamaları için root gerekebilir

## 🔄 Geri Yükleme

Silinen bir uygulamayı geri yüklemek için:

```bash
adb shell cmd package install-existing <paket_adı>
```

## 📝 Lisans

Bu proje topluluk katkısıyla geliştirilmiştir. Kullanıcılar kendi sorumluluğundadır.
