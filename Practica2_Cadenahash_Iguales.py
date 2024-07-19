import hashlib

def comparar_cadenas_md5(cadena1, cadena2):
  """
  Compara dos cadenas utilizando el algoritmo MD5 y devuelve True si son iguales, False en caso contrario.

  Parámetros:
    cadena1 (str): La primera cadena a comparar.
    cadena2 (str): La segunda cadena a comparar.

  Devuelve:
    bool: True si las cadenas son iguales, False en caso contrario.
  """
  hash1 = hashlib.md5(cadena1.encode()).hexdigest()
  hash2 = hashlib.md5(cadena2.encode()).hexdigest()

  return hash1 == hash2

# Ejemplo de uso
cadena1 = "Hola!"
cadena2 = "Hola!"

resultado = comparar_cadenas_md5(cadena1, cadena2)

if resultado:
  print("Las cadenas son iguales")
else:
  print("Las cadenas no son iguales")