from googletrans import Translator

translator = Translator(service_urls=['translate.googleapis.com'])
result = translator.translate(text='ciao come stai?', dest='en')

print(result.src)
print(result.dest)
print(result.origin)
print(result.text)
print(result.pronunciation)