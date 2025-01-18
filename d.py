import re
texto = "Hola mundo"
resultado = re.search("mundo", texto)
print(resultado)  # Devuelve un objeto de coincidencia