from translate import Translator

# Crear una instancia del traductor
translator = Translator(from_lang='spanish', to_lang='english')

# Solicitar al usuario que ingrese el texto a traducir
txt = input('¿Qué quieres traducir? ')

# Traducir el texto
res = translator.translate(txt)

# Imprimir el resultado de la traducción
print(f"Texto traducido: {res}")
