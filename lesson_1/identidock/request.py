import requests

url = 'https://speech.googleapis.com/v1p1beta1/speech:recognize'
audio_path = '/home/boozzee/Загрузки/Telegram Desktop/20181019102516.mp3'

params = {
    "audio": {
    "content": audio_path
  },
  "config": {
    "enableAutomaticPunctuation": True,
    "encoding": "LINEAR16",
    "languageCode": "ru-RU",
    "model": "default"
  }
}

resp = requests.get(url=url, params=params)
data = resp.json()
