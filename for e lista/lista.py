
#1- crio uma lista com 5 objetos
objetos = ["mesa", "ventilador", "caneta", "cadeira", "garrafa"]

#2- adiciono mais um objeto na lista
objetos.append("ar - condicionado")

#3- acessei o segundo objeto
print(objetos[1])

#4- removi um objeto da lista e exibi
removido = objetos.pop(2)
print(removido)

#5- exibir o tamanho da lista
print("")
print(len(objetos))
print("")

#6-mostrei o itebs com o for
for objeto in objetos:
    print(objeto)
    
#7-verifiquei a cadeira na lista e coloquei que se estiver remove se não adiciono
if "cadeira" in objetos:
    objetos.remove("cadeira")
else:
    objetos.append("cadeira")

#8- ordenei a lista em ordem alfabética e exibi antes e o depois
print(objetos)
objetos.sort()
print(objetos)

#9- exibi o primeiro e o ultimo
print(objetos[0])
ultimo_elemento = objetos.pop()
objetos.append(ultimo_elemento)

#10- limpei a lista
objetos.clear()
