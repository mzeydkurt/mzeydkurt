import yt_dlp
user_input = input("İndirmek İstediğiniz Videonun Linkini Giriniz : ")

try:
    # İndirme ayarlarını tanımla
    ydl_opts = {
        'format': 'best', #en yüksek kalite için bestvideo+bestaudio/best
        'outtmpl': '%(title)s.%(ext)s',
    }

    # Video indirme
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([user_input])
    print("Video başarıyla indirildi!")
except Exception as e:
    print("Hata Oluştu ", e)