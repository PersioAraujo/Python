print("\n ********** Calculadora Python **********\n")

def soma(priNum,segNum):
    valor = priNum + segNum
    return(valor)

def subt(priNum,segNum):
    valor = priNum - segNum
    return(valor)

def divs(priNum,segNum):
    valor = priNum / segNum
    return(valor)

def mult(priNum,segNum):
    valor = priNum * segNum
    return(valor)
    
selecione = int(input("Escolha a opção: \n\n 1 - Soma \n 2 - Subtração \n 3 - Divisão \n 4 - Multiplicação \n\n Digite a sua opção => "))
  
if selecione == 1:
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        print("O Resultado da operação é: ",soma(valor1,valor2))    
elif selecione == 2:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print("O Resultado da operação é: ",subt(valor1,valor2))
elif selecione == 3:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print("O Resultado da operação é: ",divs(valor1,valor2))
elif selecione == 4:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print("O Resultado da operação é: ",mult(valor1,valor2))
else:
    print("\nOpção Invalida!!")
        
  
    