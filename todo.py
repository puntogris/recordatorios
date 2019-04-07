#programa de recordatorios
import pickle
import os

#crea lista vacia en un archivo llamada outfile con pickle si no exite uno
#de lo contrario abre el creado previamente
if os.path.isfile('./outfile') == False:
    recordatorios = []
    with open('outfile', 'wb') as fp:
        pickle.dump(recordatorios, fp)
else:
    with open ('outfile', 'rb') as fp:
        recordatorios = pickle.load(fp)

#opciones para elejir
print('Opciones:')
print('\
    1 - Ver recordatorios\n\
    2 - Agregar items\n\
    3 - Quitar items\n\
    4 - Salir\
    ')
#muestra la lista en forma vertical y numera los items
def mostrar_items(lista):
    print("Recordatorios:")
    for lugar,line in enumerate(lista):
        print("   ",lugar + 1,'-' , line)

#funcion main con codigo de las oredenes
def main():
    ordenes = int(input('Que queres hacer?... '))
    if ordenes == 1:
        if recordatorios == []:
            print("No tenes recordatorios.")
            main()
        else:
            mostrar_items(recordatorios)
            main()
    elif ordenes == 2:
        agregar_recordar = input('Ingresa de lo que queres que te recuerde... ')
        recordatorios.append(agregar_recordar.capitalize())
        mostrar_items(recordatorios)
        main()
    elif ordenes == 3:
        mostrar_items(recordatorios)
        item = int(input('Ingresa el numero de item a eliminar: '))
        del recordatorios[item - 1]
        mostrar_items(recordatorios)
        main()
    elif ordenes == 4:
        with open('outfile', 'wb') as fp:
            pickle.dump(recordatorios, fp)
        quit('Adios!')
    else:
        print('Error, intenta de nuevo.')
        main()
main()
