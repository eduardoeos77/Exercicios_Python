def bin_dec():
    n = input('Digite um número binário: \n> ')
    soma = 0

    for i in range(len(n)):
        soma += int(n[len(n)-(i+1)]) * 2**i
 
    print("Decimal: " + str(soma))

def dec_bin():
    n = int(input("Digite um número decimal para converter em binário: \n> "))
    resto = ''

    while n != 0 and n != 1:
        resto += str(n % 2)
        n = int(n / 2)

    resto += str(n)
    resto = resto[::-1]

    print('Binário: ' + resto)

print("O que você deseja converter?")
print("1 - Binário para decimal")
print("2 - Decimal para binário")
entrada = input('> ')

if entrada == '1':
    bin_dec()
elif entrada == '2':
    dec_bin()
else:
    print("Opção inválida")
  

