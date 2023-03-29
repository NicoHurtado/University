from crearPacientes import *
from neuronal_net import *
import matplotlib.pyplot as plt

def Simulacion1():
    lista = creacionPacientes(50000)
    categorizar(lista)
    print("\n")
    print("----------------ANALISIS DE DATOS HOSPITAL 1----------------"+"\n")
    print("---> A continuacion La lista de pacientes categorizada por en que estado se encuentran (TRIAJE - PREDIAGNOSTICO - EXAMENES - TRATAMIENTO) \n")
    print('''---> Cada lista esta organizada de la siguiente manera:  
        Pacientes en TRIAJE estan organizados de menos tiempo a mas en Triaje
        Pacientes en PREDIAGNOSTICO esta organizado de menor a mayor depende del tiempo que lleva en PreDiagnostico
        Pacientes en EXAMENES esta organizado de menor a mayor depende del tiempo que lleva en Examenes
        Pacientes en TRATAMIENTO esta organizado de menor a mayor depende del tiempo que lleva en Tratamiento
        ''')

    
    triajeOrd = OrdenarEstados(triaje)

    
    PreOrd = OrdenarEstados(Prediagnostico)
    
    
    ExamsOrd = OrdenarEstados(Examenes)
    
    
    
    TratOrd = OrdenarEstados(Tratamiento)


    Pacientes_Pasados_por_triaje = PreOrd + ExamsOrd + TratOrd
    Pacientes_Pasados_por_Prediagnostico = ExamsOrd + TratOrd
    Pacientes_Padados_por_Examenes = TratOrd
    Pacientes_Pasados_por_Tratamiento = TratOrd

    Prom_Triaje = promedioTiempos(Pacientes_Pasados_por_triaje, "t1")
    Prom_Pre = promedioTiempos(Pacientes_Pasados_por_Prediagnostico, "t2")
    Prom_Examenes = promedioTiempos(Pacientes_Padados_por_Examenes, "t3")
    Prom_Tratamiento = promedioTiempos(Pacientes_Pasados_por_Tratamiento, "t4")

    estados = ['TRIAJE', 'PREDIAGNOSTICO', 'EXAMENES', 'TRATAMIENTO']
    cantidades = [len(triajeOrd), len(PreOrd), len(ExamsOrd), len(TratOrd)]
    plt.bar(estados, cantidades)
    plt.xlabel('Estados')
    plt.ylabel('Cantidad de pacientes')
    plt.title('Simulación 1')
    plt.show()

    print("--"*20 + "PROMEDIOS" + "--"*20 + "\n")
    print(f'Tiempo Promedio de pacientes en Triaje: {Prom_Triaje}')
    print(f'Tiempo Promedio de pacientes en Prediagnostico: {Prom_Pre}')
    print(f'Tiempo Promedio de pacientes en Examenes: {Prom_Examenes}')
    print(f'Tiempo Promedio de pacientes en Tratamiento: {Prom_Tratamiento}')

    print('\n')
    
    proms = Promedios_tiempoEnEstadosTriaje(lista)

    print(f"Promedio de tiempo de personas con nivel de urgencia 1 en el triaje: Numero De Personas: {proms[0][0]} | Promedio Tiempo: {proms[1][0]} min")
    print(f"Promedio de tiempo de personas con nivel de urgencia 2 en el triaje: Numero De Personas: {proms[0][1]} | Promedio Tiempo: {proms[1][1]} min")
    print(f"Promedio de tiempo de personas con nivel de urgencia 3 en el triaje: Numero De Personas: {proms[0][2]} | Promedio Tiempo: {proms[1][2]} min")
    print(f"Promedio de tiempo de personas con nivel de urgencia 4 en el triaje: Numero De Personas: {proms[0][3]} | Promedio Tiempo: {proms[1][3]} min")
    print(f"Promedio de tiempo de personas con nivel de urgencia 5 en el triaje: Numero De Personas: {proms[0][4]} | Promedio Tiempo: {proms[1][4]} min")
    print("\n")

    print('''Los tiempos predetermindados para cada nivel de emergencia (TRIAJE) son:
             - 1 (Codigo Rojo): Atencion Inmediata
             - 2 (Codigo Naranja): 10-15 min
             - 3 (Codigo Amarillo): 60 min
             - 4 (Codigo Verde): 120 min
             - 5 (Codigo Azul): 240 min \n
             
             El tiempo recomendados para (PREDIAGNOSTICO) es de 30 min
             El tiempo recomendados para (EXAMENES) es de 120 min
             El tiempo recomendados para (TRATAMIENTO) es de 120 min \n ''')

    print('''A continuacion haremos el analisis dado el conjunto de datos para saber en cual cada servicio fallo, luego el conteo de errores
        - Si fallo (Se exedio el tiempo) en el triaje sera un 1 
        - Si fallo (Se exedio el tiempo) en el Prediagnostico sera un 2 
        - Si fallo (Se exedio el tiempo) en el Examenes sera un 3
        - Si fallo (Se exedio el tiempo) en el Tratameinto sera un 4
        - Si El servicio estuvo o esta dentro de los parametros de tiempo y urgencia sera un 5 \n''')

    ListaAnalisis = SalidaParaAnalisis(Servicios)
    uno = ListaAnalisis.count(1)
    dos = ListaAnalisis.count(2)
    tres = ListaAnalisis.count(3)
    cuatro = ListaAnalisis.count(4)
    cinco = ListaAnalisis.count(5)

    conteos = {'#De Fallas en el Triaje': uno, '#De Fallas en el Prediagnostico': dos, '#De Fallas en Exmanes': tres, '#De Fallas en el Tratamiento': cuatro, '#De Servicios EXitosos': cinco}
    print(f'Conteos: {conteos}')
    print('\n')
    categoria_maxima = max(conteos, key=conteos.get)
    print(f"La categoría con mayor conteo es {categoria_maxima} con un total de {conteos[categoria_maxima]} Fallas \n")
    print(f'''El analisis Final es que Como la categoria con mayores fallas es --> {categoria_maxima} <--, Hay que agilizar el proceso en esta etapa \n''')
    print('''Ahora Con ayuda de una Red Neuronal vamos a ver si el servicio En general del hospital fue bueno o malo
            Entregaremos a la red neuronal una lista tal que asi [0,1,1,0,0,....] Donde cada uno y cero es un servicio
            - 0 Significa que el servicio exedio tiempo (Mal servicio)
            - 1 Significa que el servicio esta dentro de los rangos (Buen servicio) \n''')
    
    DatosSalida_RedNeuronal(Servicios)
    print('Si el resultad de la red esta por debajo de 0.5 El Resultado General Fue Malo. Mientras que es mayor a 0.5 El Resultado General Fue Bueno \n')

    resultado = Red_Neuronal2(Servicios, SalidaRedNeuronal)
    if resultado >= 0.5:
        funcionamiento = 'Bueno'
    else: 
        funcionamiento = 'Malo'

    print(f'Resultado de la red neuronal {resultado:.2f}, Por lo Tanto el funcionamiento del Hospital Fue {funcionamiento}. \n')
    print('fin..')
    

def Simulacion2():
    lista = creacionPacientes(50)
    #verLista(lista) Si desea Ver la lista Completa sin categorizar
    categorizar(lista)
    print("\n")
    print("----------------ANALISIS DE DATOS HOSPITAL 2----------------"+"\n")
    print("---> A continuacion La lista de pacientes categorizada por en que estado se encuentran (TRIAJE - PREDIAGNOSTICO - EXAMENES - TRATAMIENTO) \n")
    print('''---> Cada lista esta organizada de la siguiente manera:  
        Pacientes en TRIAJE estan organizados de menos tiempo a mas en Triaje
        Pacientes en PREDIAGNOSTICO esta organizado de menor a mayor depende del tiempo que lleva en PreDiagnostico
        Pacientes en EXAMENES esta organizado de menor a mayor depende del tiempo que lleva en Examenes
        Pacientes en TRATAMIENTO esta organizado de menor a mayor depende del tiempo que lleva en Tratamiento
        ''')

    print(("--"*20)+"Pacientes En TRIAJE"+("--"*20))
    triajeOrd = OrdenarEstados(triaje)
    verLista(triajeOrd)

    print(("--"*20)+"Pacientes En PREDIAGNOSTICO"+("--"*20))
    PreOrd = OrdenarEstados(Prediagnostico)
    verLista(PreOrd)
    
    print(("--"*20)+"Pacientes En EXAMENES"+("--"*20))
    ExamsOrd = OrdenarEstados(Examenes)
    verLista(ExamsOrd)
    
    print(("--"*20)+"Pacientes En TRATAMIENTO"+("--"*20))
    TratOrd = OrdenarEstados(Tratamiento)
    verLista(TratOrd)


    Pacientes_Pasados_por_triaje = PreOrd + ExamsOrd + TratOrd
    Pacientes_Pasados_por_Prediagnostico = ExamsOrd + TratOrd
    Pacientes_Padados_por_Examenes = TratOrd
    Pacientes_Pasados_por_Tratamiento = TratOrd

    Prom_Triaje = promedioTiempos(Pacientes_Pasados_por_triaje, "t1")
    Prom_Pre = promedioTiempos(Pacientes_Pasados_por_Prediagnostico, "t2")
    Prom_Examenes = promedioTiempos(Pacientes_Padados_por_Examenes, "t3")
    Prom_Tratamiento = promedioTiempos(Pacientes_Pasados_por_Tratamiento, "t4")

    estados = ['TRIAJE', 'PREDIAGNOSTICO', 'EXAMENES', 'TRATAMIENTO']
    cantidades = [len(triajeOrd), len(PreOrd), len(ExamsOrd), len(TratOrd)]
    plt.bar(estados, cantidades)
    plt.xlabel('Estados')
    plt.ylabel('Cantidad de pacientes')
    plt.title('Simulación 1')
    plt.show()

    print("--"*20 + "PROMEDIOS" + "--"*20 + "\n")
    print(f'Tiempo Promedio de pacientes en Triaje: {Prom_Triaje}')
    print(f'Tiempo Promedio de pacientes en Prediagnostico: {Prom_Pre}')
    print(f'Tiempo Promedio de pacientes en Examenes: {Prom_Examenes}')
    print(f'Tiempo Promedio de pacientes en Tratamiento: {Prom_Tratamiento}')

    print('\n')
    
    proms = Promedios_tiempoEnEstadosTriaje(lista)

    print(f"Promedio de tiempo de personas con nivel de urgencia 1 en el triaje: Numero De Personas: {proms[0][0]} | Promedio Tiempo: {proms[1][0]} min")
    print(f"Promedio de tiempo de personas con nivel de urgencia 2 en el triaje: Numero De Personas: {proms[0][1]} | Promedio Tiempo: {proms[1][1]} min")
    print(f"Promedio de tiempo de personas con nivel de urgencia 3 en el triaje: Numero De Personas: {proms[0][2]} | Promedio Tiempo: {proms[1][2]} min")
    print(f"Promedio de tiempo de personas con nivel de urgencia 4 en el triaje: Numero De Personas: {proms[0][3]} | Promedio Tiempo: {proms[1][3]} min")
    print(f"Promedio de tiempo de personas con nivel de urgencia 5 en el triaje: Numero De Personas: {proms[0][4]} | Promedio Tiempo: {proms[1][4]} min")
    print("\n")

    print('''Los tiempos predetermindados para cada nivel de emergencia (TRIAJE) son:
             - 1 (Codigo Rojo): Atencion Inmediata
             - 2 (Codigo Naranja): 10-15 min
             - 3 (Codigo Amarillo): 60 min
             - 4 (Codigo Verde): 120 min
             - 5 (Codigo Azul): 240 min \n
             
             El tiempo recomendados para (PREDIAGNOSTICO) es de 30 min
             El tiempo recomendados para (EXAMENES) es de 120 min
             El tiempo recomendados para (TRATAMIENTO) es de 120 min \n ''')

    print('''A continuacion haremos el analisis dado el conjunto de datos para saber en cual cada servicio fallo, luego el conteo de errores
        - Si fallo (Se exedio el tiempo) en el triaje sera un 1 
        - Si fallo (Se exedio el tiempo) en el Prediagnostico sera un 2 
        - Si fallo (Se exedio el tiempo) en el Examenes sera un 3
        - Si fallo (Se exedio el tiempo) en el Tratameinto sera un 4
        - Si El servicio estuvo o esta dentro de los parametros de tiempo y urgencia sera un 5 \n''')
    
        #Si desea ver la lista de Datos, Quite el comentario en las siguientes lineas
    #print(Servicios)
    #print('\n')

        #Si desea ver la lista con la clasificacion de cada servicio, Quite el comentario en las siguientes lineas
    #print(SalidaParaAnalisis(Servicios))
    #print('\n')

    ListaAnalisis = SalidaParaAnalisis(Servicios)
    uno = ListaAnalisis.count(1)
    dos = ListaAnalisis.count(2)
    tres = ListaAnalisis.count(3)
    cuatro = ListaAnalisis.count(4)
    cinco = ListaAnalisis.count(5)

    conteos = {'#De Fallas en el Triaje': uno, '#De Fallas en el Prediagnostico': dos, '#De Fallas en Exmanes': tres, '#De Fallas en el Tratamiento': cuatro, '#De Servicios EXitosos': cinco}
    print(f'Conteos: {conteos}')
    print('\n')
    categoria_maxima = max(conteos, key=conteos.get)
    print(f"La categoría con mayor conteo es {categoria_maxima} con un total de {conteos[categoria_maxima]} Fallas \n")
    print(f'''El analisis Final es que Como la categoria con mayores fallas es --> {categoria_maxima} <--, Hay que agilizar el proceso en esta etapa \n''')
    print('''Ahora Con ayuda de una Red Neuronal vamos a ver si el servicio En general del hospital fue bueno o malo
            Entregaremos a la red neuronal una lista tal que asi [0,1,1,0,0,....] Donde cada uno y cero es un servicio
            - 0 Significa que el servicio exedio tiempo (Mal servicio)
            - 1 Significa que el servicio esta dentro de los rangos (Buen servicio) \n''') 
    
    DatosSalida_RedNeuronal(Servicios)

        # Si desea ver la lista de [0,1,1,0,1,0,0,....], Quite el comentario de la siguiente linea 
    #print(SalidaRedNeuronal)
    
    print('Si el resultad de la red esta por debajo de 0.5 El Resultado General Fue Malo. Mientras que es mayor a 0.5 El Resultado General Fue Bueno \n')

    resultado = Red_Neuronal1(Servicios, SalidaRedNeuronal)
    if resultado >= 0.5:
        funcionamiento = 'Bueno'
    else: 
        funcionamiento = 'Malo'

    print(f'Resultado de la red neuronal {resultado:.2f}, Por lo Tanto el funcionamiento del Hospital Fue {funcionamiento}. \n')
    print('fin..')


def SalidaParaAnalisis(lista):

    #1: Mejorar Triaje
    #2: Mejorar Prediagnostico
    #3: Mejorar Examenes
    #4: Mejorar Tratamiento
    #5: Servicio Funciono bien
    
    listaSalida_Red_Neuronal = []
    for paciente in lista: 
        if (paciente[0] == 1 and paciente[1] >= 5) or (paciente[0] == 2 and paciente[1] > 15) or (paciente[0] == 3 and paciente[1] > 60) or (paciente[0] == 4 and paciente[1] > 120):
            listaSalida_Red_Neuronal.append(1)
        elif paciente[2] > 30:
            listaSalida_Red_Neuronal.append(2)
        elif paciente[3] > 120:
            listaSalida_Red_Neuronal.append(3)
        elif paciente[4] > 120:
            listaSalida_Red_Neuronal.append(4)
        else:
            listaSalida_Red_Neuronal.append(5)

    return listaSalida_Red_Neuronal

def Promedios_tiempoEnEstadosTriaje(lista):
    conteos = [0, 0, 0, 0, 0]
    sumas = [0, 0, 0, 0, 0]
    for i in lista:
        if i.clasTriaje >= 1 and i.clasTriaje <= 5:
            indice = i.clasTriaje - 1 
            conteos[indice] += 1
            sumas[indice] += i.t1
    promedios = [suma / conteo if conteo > 0 else None for suma, conteo in zip(sumas, conteos)]
    return (conteos, promedios)


def promedioTiempos(lista, tiempo):
    promedio_tiempo = 0
    lenght = len(lista)
    while lenght != 0:
        if tiempo == 't1':
            for i in lista:
                promedio_tiempo = promedio_tiempo + i.t1
        if tiempo == 't2':
            for i in lista:
                promedio_tiempo = promedio_tiempo + i.t2
        if tiempo == 't3':
            for i in lista:
                promedio_tiempo = promedio_tiempo + i.t3
        if tiempo == 't4':
            for i in lista:
                promedio_tiempo = promedio_tiempo + i.t4
        return promedio_tiempo/lenght
    return None
        
SalidaRedNeuronal = []

def DatosSalida_RedNeuronal(lista):
    # 0 Servicio Fallo (Excedio lo estimado)
    # 1 Servicio Exitoso 
    for paciente in lista: 
        if (paciente[0] == 1 and paciente[1] >= 5) or (paciente[0] == 2 and paciente[1] > 15) or (paciente[0] == 3 and paciente[1] > 60) or (paciente[0] == 4 and paciente[1] > 120) or\
            paciente[2] > 30 or \
            paciente[3] > 120 or \
            paciente[4] > 120:
            SalidaRedNeuronal.append(0)
        else:
            SalidaRedNeuronal.append(1)
    return SalidaRedNeuronal


if __name__ == "__main__":
    Simulacion2()
    #Simulacion1()
