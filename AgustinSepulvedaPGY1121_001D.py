

listaTipo = ['SOBRE']
listaNombre = ['JUAN']
listaRut = ['11531416-9']
listaPeso = [9]
listaPrecio = [49999]
listaDestino = ['Concepcion']

def grabar():
        while True:
            try:
                tipo=input("Ingrese el tipo de encomienda: 'SOBRE' o 'PAQUETE' " )
                if tipo == "SOBRE" or tipo == "PAQUETE":
                    listaTipo.append(tipo)
                    break
                else:
                    print("INVALIDO, solo acepta SOBRE o PAQUETE")
            except:
                print("Invalido 1")
        while True:
            try:
                nom=input("Ingrese el nombre del destinatario: " )
                if len(nom) >= 2 and len(nom) <= 30:
                    listaNombre.append(nom)
                    break
                else:
                    print("Nombre muy corto o superior a 30 caracteres")
            except:
                print("Invalido 2")
        while True:
            try:
                rut=input("Ingrese el rut del destinatario")
                if len(rut) >= 9 and rut[-2] == '-' :
                    listaRut.append(rut)
                    break
                else:
                    print("Rut ingresado no valido ")
            except:
                print("Invalido 3")
        while True:
            try:
                peso=int(input("Ingrese el peso del producto "))
                if peso >=1:
                    listaPeso.append(peso)
                    break
                else:
                    print("Peso Invalido")
            except:
                print("Invalido 4")
        while True:
            try:
                precio=int(input("Ingrese el precio del producto"))
                if precio >= 2000:
                    listaPeso.append(precio)
                    break
                else:
                    print("Precio muy bajo tiene que ser mayor a 2000")
            except:
                print("Invalido 5")
        while True:
            try:
                city=input("Ingrese la Ciudad de destino " )
                if len(city) > 3:
                    listaDestino.append(city)
                    break
                else:
                    print("Nombre de destino muy corto")
            except:
                print("Invalido 6")
# FIN FUNCION AGREGAR

def buscarPedido():
    run=input("Ingrese el rut a buscar")
    print(f"Lista del rut: {run}")
    for i in range(len(listaRut)):
        if run==listaRut[i]:
            print(f"{i+1}|{listaRut[i]:12s}|{listaNombre[i]:31s}|{listaTipo[i]:9s}|{listaPeso[i]:5d}|{listaPrecio[i]:7d}|{listaDestino[i]:30s}")
    print(f"Total de encomiendas {i+1}")
# FIN FUNCION BUSCAR
def listarEncomiendas():
    print("Lista de Encomiendas")
    print("N°| RUT         | NOMBRE                        | TIPO     |PESO | PRECIO | DESTINO                              ")
    for i in range(len(listaRut)):
        print(f"{i+1}|{listaRut[i]:12s}|{listaNombre[i]:31s}|{listaTipo[i]:9s}|{listaPeso[i]:5d}|{listaPrecio:7d}|{listaDestino[i]:30s}")
# FIN FUNCION LISTAR

menu =""""
    Caracol Express
        Opciones
    1. Grabar encomienda
    2. Buscar encomienda
    3. Listar encomiendas   
    4. Salir 
    Ingrese una opcion \n"""

#INICIO MENU PRINCIPAL
while True:
        try:
            opc=int(input(menu))
            if opc == 4:
                input("Gracias por usar el programa... realizado por Agustin Sepulveda")
                break
            elif opc == 1:
                grabar()
                input("enter para continuar")
            elif opc == 2:
                buscarPedido()
                input("enter para continuar")
            elif opc == 3:
                listarEncomiendas()
                input("Enter para continuar")
        except:
            print("error menu [%s]")
