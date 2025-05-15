
luta = int (input ("qual luta?, 1karate,2muay thay,3box?"))
peso = input ("qual peso?")
nome = input ("qual é o seu nome?")
if luta == 1:
    print ("seu estilo de luta é karate")
    print ("peso da pessoa:", peso)
    print ("nome do lutador:", nome)

elif luta == 2 :
    print("seu estilo de luta muay thay")
    print ("peso da pessoa:",peso )
    print("nome do lutador:", nome)
elif luta == 3:
    print ("seu estilo de luta é box")
    print ("peso da pessoa:", peso)
    print ("nome do lutador: ", nome)
 


else:
    print (f"peso da pessoa:", {peso})
    print(f"nao tem estilo de luta")
    print (f"nome do lutador:", {nome})

