from googletrans import Translator

translator = Translator()
user = input("Enter message to be translated to english: ")
result = translator.translate(user, dest = 'en')
print(result.text)