from flask import Flask, render_template
import requests
import random # Rastgele sayı üretmek için bunu ekledik

app = Flask(__name__)

@app.route('/')
def index():
    # --- YENİ MANTIK ---
    # 1. Toplam 826 karakter var. Rastgele 4 tane ID seçelim.
    # random.sample, 1 ile 826 arasından tekrar etmeyen 4 sayı seçer.
    rastgele_idler = random.sample(range(1, 827), 4)
    
    # 2. Bu ID'leri virgülle birleştirip API linki yapalım (Örn: "1,15,200,555")
    idler_string = ",".join(map(str, rastgele_idler))
    url = f"https://rickandmortyapi.com/api/character/{idler_string}"
    
    karakterler = []
    try:
        # API'ye özel isteği atıyoruz
        response = requests.get(url)
        # Birden fazla ID istediğimizde API bize direkt liste döner (data['results'] gerekmez)
        karakterler = response.json()
    except:
        # Hata olursa boş liste dönsün, site çökmesin
        pass

    return render_template('index.html', karakterler=karakterler)

if __name__ == '__main__':
    # Konteyner içinde 0.0.0.0 şart
    app.run(host='0.0.0.0', port=5000)
