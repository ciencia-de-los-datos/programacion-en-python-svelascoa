"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

archivo=open("data.csv")

data=archivo.readlines()
archivo.close()
   
matrix=[]
for ind in range(0,len(data)):
   matrix.append(data[ind].split("\t"))




def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma=0
    for i in range(0,len(matrix)):
        suma += int(matrix[i][1])
        
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    letras=[]
    for i in range(0,len(matrix)):
        if  matrix[i][0] not in letras:
            letras.append(matrix[i][0])

    letras=sorted(letras)
    Rta=[]
    for i in range(0, len(letras)):
        cont=0
        for j in range(0,len(matrix)):
            if letras[i]==matrix[j][0]:
                cont += 1
        Rta.append((letras[i], cont))    

    
    
    return Rta


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    letras=[]
    for i in range(0,len(matrix)):
      if  matrix[i][0] not in letras:
        letras.append(matrix[i][0])

    letras=sorted(letras)
    Rta=[]
    for i in range(0, len(letras)):
        suma=0
        for j in range(0,len(matrix)):
            if letras[i]==matrix[j][0]:
                suma += int(matrix[j][1])
        Rta.append((letras[i], suma))
    

    
    return Rta


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    Meses=[]
    for i in range(0,len(matrix)):
        mes=matrix[i][2]
        if mes[5:7] not in Meses:
          Meses.append(mes[5:7])
    Meses=sorted(Meses)

    Rta=[]
    for i in range(0,len(Meses)):
        cont=0
        for j in range(0, len(matrix)):
            mes=matrix[j][2]
            if Meses[i]==mes[5:7]:
               cont += 1
        Rta.append((Meses[i],cont))        

    
    return Rta


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    letras=[]
    for i in range(0,len(matrix)):
        if matrix[i][0] not in letras:
           letras.append(matrix[i][0]) 
    letras=sorted(letras)

    Rta=[]
    for i in range(0,len(letras)):
        valetras=[]
        for j in range(0,len(matrix)):
            if letras[i]==matrix[j][0]:
                valetras.append(int(matrix[j][1]))
        Rta.append((letras[i],max(valetras),min(valetras)))

        
    return Rta


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    claves=[]
    for i in range(0,len(matrix)):
        clave=matrix[i][4]
        j=0
        k=0
        while k+5<len(clave):
            k=clave.find(":",j)
            key=clave[j:k]
            valor=int(clave[k+1:clave.find(",",j)])
            j=clave.find(",",j)+1
            claves.append((key,valor))    
        
    claves=sorted(claves)

    keys=[]
    for i in range(0,len(claves)):
        if claves[i][0] not in keys:
            keys.append(claves[i][0])

    rta=[]
    for i in range(0,len(keys)):
        valr=[]
        for j in range(0,len(claves)):
           if keys[i]==claves[j][0]:
               valr.append(claves[j][1])
        rta.append((keys[i],min(valr),max(valr)))


    
    
    return rta


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    ValUnic=[]
    for i in range(0,len(matrix)):
        if matrix[i][1] not in ValUnic:
            ValUnic.append(matrix[i][1])
          
    ValUnic=sorted(ValUnic)

    Rta=[]
    for i in range(0, len(ValUnic)):
        letras=[]           
        for j in range(0, len(matrix)):
            if ValUnic[i]==matrix[j][1]:
                letras.append(matrix[j][0])
                
        Rta.append((int(ValUnic[i]),letras))    

    
    
    return Rta


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    ValUnic=[]
    for i in range(0,len(matrix)):
        if matrix[i][1] not in ValUnic:
            ValUnic.append(matrix[i][1])
          
    ValUnic=sorted(ValUnic)

    Rta=[]
    for i in range(0, len(ValUnic)):
        letras=[]           
        for j in range(0, len(matrix)):
            if ValUnic[i]==matrix[j][1] and matrix[j][0] not in letras :
               letras.append(matrix[j][0])
        letras=sorted(letras)        
        Rta.append((int(ValUnic[i]),letras))    

    
    return Rta


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    diccol5=[]       
    for i in range(0, len(matrix)):
        clave=matrix[i][4]
        k=0
        j=0
        while k+5<len(clave):
            k=clave.find(":",j)
            key=clave[j:k]
            valor=int(clave[k+1:clave.find(",",j)])
            j=clave.find(",",j)+1
            diccol5.append((key,valor)) 
         
    col5u=[]
    for i in range(0,len(diccol5)):
         if diccol5[i][0] not in col5u:
             col5u.append(diccol5[i][0])

    col5u=sorted(col5u)

    list=[]
    for i in range(0,len(col5u)):
        cont=0
        for j in range(0, len(diccol5)):
             if col5u[i]==diccol5[j][0]:
                 cont+=1
        list.append((col5u[i],cont))
             
    Rta=dict(list)

    
    return Rta


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    Rta=[]
    for i in range(0,len(matrix)):
        col4=matrix[i][3].split(",")
        col5=matrix[i][4].split(",")
        Rta.append((matrix[i][0],len(col4),len(col5)))
    

    
    return Rta


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    col4=[]
    for i in range(0,len(matrix)):
        if matrix[i][3][:1] not in col4:
            col4.append(matrix[i][3][:1])

    col4=sorted(col4)

    rta=[]
    for i in range(0,len(col4)):
        sumcol2=0
        for j in range(0,len(matrix)):
            a=[]
            a=matrix[j][3].split(",")
            for k in range(0,len(a)):
                if col4[i]==a[k]:
                  sumcol2=sumcol2+int(matrix[j][1])
               
        rta.append((col4[i], sumcol2))

    
    return dict(rta)


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    coln1=[]
    for i in range(0,len(matrix)):
        if matrix[i][0] not in coln1:
           coln1.append(matrix[i][0])
           
    coln1=sorted(coln1)

    Rta=[]
    for i in range(0,len(coln1)):
        valor=0
        for j in range(0, len(matrix)):
            if coln1[i]==matrix[j][0]:
               coln5=matrix[j][4].split(",")
               for k in range(0,len(coln5)):
                   valor +=int(coln5[k][coln5[k].find(":")+1:])
        Rta.append((coln1[i],valor))       


    return dict(Rta)
