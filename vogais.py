# Contar vogais em uma string 
# Enunciado: 
# Peça ao usuário uma palavra e conte quantas vogais ela contém. 




palavra = input("Digite uma palavra: ")

vogais = "aeiouAEIOU"

contador = 0

for letra in palavra :
    if letra in vogais :
        contador += 1 

print("O numero de vogais na palavra é: ", contador) 