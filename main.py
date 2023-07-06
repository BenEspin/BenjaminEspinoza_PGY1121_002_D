
import numpy as np
from entrada import*
from Funcion import*

arreglo = np.full((10, 10), '---')
list_audiencia = []
ciclo=True


def AgregarAudiencia(List_Audiencia, num_asiento):
    a = asistencias()

    a.rut = int(input("Ingrese su rut"))
    a.nombre = int(input("Ingrese el Nombre"))
    a.apellido = int(input("Ingrese su Apellido"))
    a.edad = int(input("Ingrese su edad"))
    a.num_asiento = num_asiento
    if num_asiento>=1 and num_asiento<=20:
        a.valor=120000
    if num_asiento>=21 and num_asiento<=50:
        a.valor=80000
    if num_asiento>=51 and num_asiento<=100:
        a.valor=50000
    print("La operacion se realizo con exito")
    list_audiencia.append(a)

def CompraAsiento(arreglo,list_audiencia):
    try:
        lugar = int(input("Ingresar la cantidad de audiencia"))
        if lugar>=1 and lugar<=3:
            compra=0
            while compra<lugar:
                mostrar(arreglo)
                num_asiento = int(input("Numero de Puesto"))
                if num_asiento >=1 and num_asiento <= 100:
                    disponible = ComprobarLugar(arreglo, num_asiento)
                    if disponible == True:
                        AgregarAudiencia(list_audiencia, num_asiento)
                        compra(arreglo, num_asiento)
                        compra = compra + 1
                    else:
                        print("No se encuentra Disponible")
                else:
                    print("Solo disponible de 1 a 100")
        else:
            print("ubicaciones entre 1 a 100")
    except BaseException as error:
        print(f"Error:{error}")

def Salir():
    print("Gracias por preferir")
    return False

llenar(arreglo)


def listAudiencia(list_audiencia)
    for a in list_audiencia:
        print(f"Nombre:{a.nombre}{a.apellido}\n Valor: ${a.valor} lugar {a.num_asiento}")

def Totales(List_Audiencia):
    platino=0
    gold=0
    silver=0
    total_plati=0
    total_gold=0
    total_silver=0
    for asi in list_audiencia:
        if int(asi.valor) == 120000:
            platino = platino + 1
            total_plati = total_plati + 120000
        if int(asi.valor) == 80000:
            gold = gold + 1
            total_gold = total_gold + 80000
        if int(asi.valor) == 50000:
            silver = silver + 1
            total_silver = total_silver + 50000

while ciclo:
    print("Creativos.cl")
    print("1) Compra Entradas")
    print("2) Mostrar Ubicacion")
    print("3) Ver Listado asistente")
    print("4) Total de Ganancias")
    print("5) Salir")
    op=int(input("Seleccione (1-5):"))
    match op:
        case 1:
            CompraAsiento()
        case 2:

        case 3:

        case 4:
            
        case 5:
            ciclo = False