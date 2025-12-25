from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Rick and Morty API'sine bağlan
    url = "https://rickandmortyapi.com/api/character"
    try:
        response = requests.get(url)
        data = response.json()
        karakterler = data['results']
    except:
        karakterler = [] # Hata olursa boş liste dönsün, site çökmesin

    return render_template('index.html', karakterler=karakterler)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
