frace= input( "ingrese una frace")
palabra= input("ingrese una palabra de la frace")

lista= frace.lower()
lista = frace.split("\n" )
lista= frace.split(" ")

cant=0
print(lista)
for clave in lista : 
    if( palabra in clave):
        cant +=1
print(cant)
