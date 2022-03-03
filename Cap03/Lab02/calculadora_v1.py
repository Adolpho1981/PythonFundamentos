# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")
print('Digite: 1(soma), 2(subtração), 3(produto) ou 4(quociente)')
operacao = input('Qual operação gostaria de executar?: ')
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if operacao == "1":
             soma = num1 + num2
             print ("A soma desses número é: ", soma)
elif operacao == "2":
             diferenca = num1-num2
             print ('A subtração desses números é: ', diferenca)
elif operacao == "3":
             produto = num1*num2
             print ('O produto desses números é: ', produto)
elif operacao == "4":
             quociente = num1/num2
             print( 'O quociente desses números é: ', quociente)
else:
             print('Essa operação não está determinada!')
