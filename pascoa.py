tamanho = input("Informe o tamanho\n 1-grande\n 2-médio\n 3-pequeno:\n ")
sabor = input("Informe o sabor:\n  1-Chocolate preto\n 2-Chocolate branco\n  3-Chocolate ao leite\n  ")
recheio = input("Qual é o recheio desejado:\n 1-Chocolate preto\n 2-Chocolate branco\n 3-Os dois ")


if tamanho == 1 or tamanho == "pequeno":
  valor = valor + 7.80 

elif tamanho == 2 or tamanho == "médio" :
  valor = valor + 12.90

else :
  valor = valor + 23.90


if sabor == 1 or sabor== "Chocolate preto":
  valor = valor + 9.67

elif sabor == 2 or sabor == "chocolate branco" :
  valor = valor + 4.50

else  :
      valor = valor + 9.32 

if recheio == 1 and recheio == "Chocolate preto":
    valor = valor +4.83

elif recheio == 2 and recheio == "chocolate branco" :
    valor = valor + 2.25

else:
    valor = valor + 4.83


