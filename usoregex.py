#En este programa tuvimos que hacer una pregunta hasta que la pregunta fuera correcta

def main():
  while True:
    strRFC = input("Dame el RFC: ")
    coincide = ("^[A-Z]{4}-[0-9]{6}-[A-Z0-9]{3}$", strRFC)
    if (coincide):
      print("RFC Correcto!")
      break
    else:
      print("RFC incorrecto. Intenta de nuevo.")
