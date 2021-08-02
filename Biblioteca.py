#Biblioteca

#(Se omiten las tildes y la ñ para evitar problemas de condificación)

#Tipado de la función

def organizador(libro1: dict, libro2: dict, libro3:dict, libro4: dict)-> str:
    
    #obtención de los valores de las llaves de cada diccionario
    nombre_libro1= libro1["nombre"]
    codigo_libro1= libro1["codigo"]
    autor_libro1= libro1["autor"]
    anio_publicación_libro1= libro1["anio_publicacion"]
    costo_libro1= libro1["costo"]
    precio_libro1= libro1["precio"]
    
    nombre_libro2= libro2["nombre"]
    codigo_libro2= libro2["codigo"]
    autor_libro2= libro2["autor"]
    anio_publicación_libro2= libro2["anio_publicacion"]
    costo_libro2= libro2["costo"]
    precio_libro2= libro2["precio"]
    
    nombre_libro3= libro3["nombre"]
    codigo_libro3= libro3["codigo"]
    autor_libro3= libro3["autor"]
    anio_publicación_libro3= libro3["anio_publicacion"]
    costo_libro3= libro3["costo"]
    precio_libro3= libro3["precio"]
    
    nombre_libro4= libro4["nombre"]
    codigo_libro4= libro4["codigo"]
    autor_libro4= libro4["autor"]
    anio_publicación_libro4= libro4["anio_publicacion"]
    costo_libro4= libro4["costo"]
    precio_libro4= libro4["precio"]
    
    #Calculo de la ganancia por unidad para cada libro
    ganancia_libro1= precio_libro1- costo_libro1
    ganancia_libro2= precio_libro2- costo_libro2
    ganancia_libro3= precio_libro3- costo_libro3
    ganancia_libro4= precio_libro4- costo_libro4
    
    libro_mayor_ganancia={}
    
    #Obtener el par de libros de cada grupo con mayor ganancia por unidad
    mayor1= mayor(ganancia_libro1, ganancia_libro2, 1, 2)["ganancia"]
    mayor2= mayor(ganancia_libro3, ganancia_libro4, 3, 4)["ganancia"]
    
    #Comporbar el par de libros de cada grupo con mayor ganancia por unidad
    if mayor1 > mayor2:
        libro_mayor_ganancia= mayor(ganancia_libro1, ganancia_libro2, 1, 2)
    
    else:
        libro_mayor_ganancia= mayor(ganancia_libro3, ganancia_libro4, 3, 4)
        
        verificador= False #Se inicializa la variable con valor falso por defcto por si ningunga condición se cumple
        
    #Comprobar que el libro seleccionado, con mayor ganancia, cumpla la segunda condición de tener mas de 100 solicitudes
    if libro_mayor_ganancia["id"]== 1 and libro1["cantidad"] >= 100 and libro_mayor_ganancia["ganancia"] > 14000:
       
        #se crea una variable verificadora para la segunda condicion
        verificador=True
        
    elif  libro_mayor_ganancia["id"]== 2 and libro2["cantidad"] >= 100 and libro_mayor_ganancia["ganancia"] > 14000:
       
        verificador=True
        
    elif  libro_mayor_ganancia["id"]== 3 and libro3["cantidad"] >= 100 and libro_mayor_ganancia["ganancia"] > 14000:
       
        verificador=True
        
    elif  libro_mayor_ganancia["id"]== 4 and libro4["cantidad"] >= 100 and libro_mayor_ganancia["ganancia"] > 14000:
       
        verificador=True
    
    #Se procede a verificar Si el libro tiene mas de 800 solicitudes o unidades requeridas
        if libro_mayor_ganancia["id"]== 1 and libro1["cantidad"] >= 800:
            
            libro1["precio"] += libro1["precio"] * 0.1
            
        elif libro_mayor_ganancia["id"] == 2 and libro2["cantidad"] >= 800:
            
            libro2["precio"] += libro2["precio"] * 0.1
            
        elif libro_mayor_ganancia["id"] == 3 and libro3["cantidad"] >= 800:
            
            libro3["precio"] += libro3["precio"] * 0.1
            
        elif libro_mayor_ganancia["id"] == 4 and libro4["cantidad"] >= 800:
            
            libro4["precio"] += libro4["precio"] * 0.1
            
    #Determinar si el libro cumple todas las condiciones
    if libro_mayor_ganancia["id"] == 1 and verificador == True:
        
        mensaje = f"El libro {nombre_libro1} escrito por {autor_libro1} en el año {anio_publicación_libro1} con el código {codigo_libro1} y precio de {precio_libro1} es la mejor opción a vender"
        
    if libro_mayor_ganancia["id"] == 2 and verificador == True:
        
        mensaje = f"El libro {nombre_libro2} escrito por {autor_libro2} en el año {anio_publicación_libro2} con el código {codigo_libro2} y precio de {precio_libro2} es la mejor opción a vender"
        
    elif libro_mayor_ganancia["id"] == 3 and verificador == True:
        
        mensaje = f"El libro {nombre_libro3} escrito por {autor_libro3} en el año {anio_publicación_libro3} con el código {codigo_libro3} y precio de {precio_libro3} es la mejor opción a vender"
    
    elif libro_mayor_ganancia["id"] == 4 and verificador == True:
        
        mensaje = f"El libro {nombre_libro4} escrito por {autor_libro4} en el año {anio_publicación_libro4} con el código {codigo_libro4} y precio de {precio_libro4} es la mejor opción a vender"
    
    #Si ninguno de los libros cumple la condicion 2 entonces:
    else: 
        
        mensaje= "Ninguno de los libros es la mejor opción para ser vendido"
        
    return mensaje

#Para esta solución se tulizo una función extra para determinar la ganancia mayor

def mayor(a,b, id_libroa, id_librob):
    
    #Esta función calcula la mayor ganancia y a que libro le corresponde
    
    if a > b:
        
        mayor = {"ganancia": a, "id": id_libroa}
        
    else:
        
        mayor = {"ganancia": b, "id": id_librob}  
        
    return mayor

#Casos a evaluar

libro1={"nombre": "Harry Potter y la piedra filosofal", "codigo": "HPJE1997", "autor": "J.K.Rowling", "anio_publicacion": 1997, "cantidad":  200, "precio": 25000 , "costo":  9000}
libro2={"nombre": "Los juegos del Hambre", "codigo": "JHSC2008", "autor": "Suzanne Collins", "anio_publicacion": 2008, "cantidad":  20, "precio": 27000 , "costo":  12000}
libro3={"nombre": "El Hobbit", "codigo": "EHJR1937", "autor": "J.R.R.Tolken", "anio_publicacion": 1937, "cantidad":  100, "precio": 35000 , "costo":  15000}
libro4={"nombre": "Hamlet", "codigo": "HWS1589", "autor": "William Shakespeare", "anio_publicacion": 1589, "cantidad":  20, "precio": 26000 , "costo":  13000}
libro5={"nombre": "Mehtods of mathematical physics", "codigo": "MOF2900", "autor": "Richard Courant", "anio_publicacion": 1924, "cantidad":  50, "precio": 25000 , "costo":  9000}
libro6={"nombre": "Electrodinamica clasica", "codigo": "ECA2100", "autor": "John David Jackson", "anio_publicacion": 1962, "cantidad":  20, "precio": 32000 , "costo":  9000}
libro7={"nombre": "A Student's Guide to the Schrödinger Equation", "codigo": "EQA2222", "autor": "Daniel A.Fleisch", "anio_publicacion": 2019, "cantidad":  90, "precio": 40000 , "costo":  9000}
libro8={"nombre": "The Feynman Lectures on Physics (The Feynman Lectures)", "codigo": "FEY2312", "autor": "Matthew Sands, Richard Feyman y Robert B.Leighton", "anio_publicacion": 1963, "cantidad":  50, "precio": 23000 , "costo":  9000}

print(organizador(libro1, libro2, libro3, libro4))
print(organizador(libro5, libro6, libro7, libro8))

