# Validação de Senha 
# peça ao usuario para digitar uma senha e valida a senha o codigo nao deve parar caso o usuario digite a senha incorreta 


print("digite a sua senha: ")

senha = float(input())

while senha != 1234:
    print("senha incorreta")

    senha = float(input("digite a sua senha novamente: "))

    
print("senha correta")