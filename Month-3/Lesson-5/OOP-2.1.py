# Python package ga poisk bersa kerakli kutubxonani ornatib beradi
# Ornatilgan modulni korish uchun terminalga "pip list" deb yozish kerak

from gtts import gTTS
from playsound import playsound  # playsouund funksiyasi pythonda ozida ovoz beradi
# Google Text To Speech => textni ovozga aylantirib beradi
# Voice Recognization => ovozni textga aylantirib beradi

# tts = gTTS('hello')
# tts.save('Hello.mp3')  # moy computerdagi papkadan koriladi

# text = input()
# tts = gTTS(text, lang='fr', tld='fr')
# tts.save(text[:5] + '.mp3')

# text = input()
# tts = gTTS(text, lang='en', tld='us')
# tts.save(text[:5] + '.mp3')

text = input()
tts = gTTS(text, lang='en', tld='us')
filename = text[:5] + '.mp3'
tts.save(filename)
playsound(filename)

##########################################################
## "python -m venv venv" => venv papkasini ochish uchun terminalga xuddi shunaqa deb yoziladu
## Windowsda: "venv/ Scripts/activate" => yozilib enter bosiladi terminalda
## Linux va Macos da => ". venv/bin/activate" => yoziladi

# pip freeze => orqali ornatilgan filelarni korish mumkin terminalda
# pip freeze > requirements.txt  => pythonda ornatilgan modullarni fileni yaratib beradi
