import sys
import io
import re

global x, flag
soma = 0
flag = True

def soma_numeros(entrada):
  global flag, soma
  for elemento in entrada.split():
    if re.match(r"\d+", elemento):
      if flag:
        soma += int(elemento)
    elif re.match(r"on", elemento, re.IGNORECASE):
      flag = True
    elif re.match(r"off", elemento, re.IGNORECASE):
      flag = False
    else:
      pass

  return soma


# Exemplo de uso
entrada = """12 off 123 45 on 
8 off 29 on 10 40 OFF 20 ON 45 """
soma = soma_numeros(entrada)
print(f"Soma dos números: {soma}")
