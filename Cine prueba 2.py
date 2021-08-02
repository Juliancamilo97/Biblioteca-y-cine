#Boletas de cine

#(Se omiten las tildes y la ñ para evitar problemas de condificación)

#Tipado de la función
def calcular_costo_boletas(info_cine:dict)->int:
    
    #Varibales indicadas en el contexto del ejercicio
    sala_dx=18800
    sala_3d=15500
    sala_2d=11300
    sala_dx_inc=28200
    sala_3d_inc=19375
    sala_2d_inc=14125
    total=0
    
    #Varibles con los valores del diccionario
    cantidad_boletas=info_cine['cantidad_boletas']
    tipo_sala=info_cine['tipo_sala']
    hora_pico=info_cine['hora_pico']
    pago_tarjeta_cinema=info_cine['pago_tarjeta_cinema']
    reserva=info_cine['reserva']
    
    #Revisar si es hora pico
    if hora_pico==False:
        
        #Comprobar cada caso de cantidad de boletas, pago con tarjeta y reserva para calcular el valor a pagar en hora no pico
        
        if cantidad_boletas >=3 and pago_tarjeta_cinema== True and reserva ==True:
            
            if tipo_sala == '2D':
                
                total= (((sala_2d*0.9-500)-(sala_2d*0.05))+2000)*cantidad_boletas
                
            elif tipo_sala == '3D':
                
                total= (((sala_3d*0.9-500)-(sala_3d*0.05))+2000)*cantidad_boletas
                 
            else:
                
                total= (((sala_dx*0.9-500)-(sala_dx*0.05))+2000)*cantidad_boletas
        
        elif cantidad_boletas >= 3 and pago_tarjeta_cinema == False and reserva ==True:
            
            if tipo_sala == '2D':
                
                total= ((sala_2d*0.9-500)+2000)*cantidad_boletas
                
            elif tipo_sala== '3D':
                
                total= ((sala_3d*0.9-500)+2000)*cantidad_boletas
            
            else:
                
                total= ((sala_dx*0.9-500)+2000)*cantidad_boletas
        
        elif cantidad_boletas >= 3 and pago_tarjeta_cinema == True and reserva == False:
            
            if tipo_sala == '2D':
                
                total= (((sala_2d* 0.9-500)-(sala_2d*0.05)))*cantidad_boletas
        
            elif tipo_sala == '3D':    
                
                total= (((sala_3d* 0.9-500)-(sala_3d*0.05)))*cantidad_boletas
            
            else:
                
                total= (((sala_dx* 0.9-500)-(sala_dx*0.05)))*cantidad_boletas
                
        elif cantidad_boletas >=3 and pago_tarjeta_cinema == False and reserva== False:
                    
            if tipo_sala == '2D':
                
                total= (sala_2d*0.9-500)*cantidad_boletas
                
            elif tipo_sala == '3D':
                
                total= (sala_3d*0.9-500)*cantidad_boletas
                
            else:
                
                total= (sala_3d*0.9-500)*cantidad_boletas
        
        elif cantidad_boletas < 3 and pago_tarjeta_cinema == False and reserva == True:
            
            if tipo_sala== '2D':
                
                total= ((sala_2d*0.9)+2000)* cantidad_boletas
            
            elif tipo_sala=='3D':
                
                total= ((sala_3d*0.9)+2000)* cantidad_boletas    
                 
            else:
                
                total= ((sala_dx*0.9)+2000)* cantidad_boletas
                
        elif cantidad_boletas<3 and pago_tarjeta_cinema==True and reserva==False:
            
            if tipo_sala == '2D':
                
                total = (((sala_2d*0.9)-(sala_2d*0.05)))*cantidad_boletas
            
            elif tipo_sala== '3D':
                
                total = (((sala_3d*0.9)-(sala_3d*0.05)))*cantidad_boletas
                
            else:
                
                total = (((sala_dx*0.9)-(sala_dx*0.05)))*cantidad_boletas
                
        elif cantidad_boletas < 3 and pago_tarjeta_cinema==True and reserva==True:
            
            if tipo_sala == '2D':
                
                total=(((sala_2d*0.9)-(sala_2d*0.05))+2000)*cantidad_boletas
                
            elif tipo_sala== '3D':
                
                total=(((sala_3d*0.9)-(sala_3d*0.05))+2000)*cantidad_boletas
            
            else:
                 
                total=(((sala_dx*0.9)-(sala_dx*0.05))+2000)*cantidad_boletas
            
        elif cantidad_boletas < 3 and pago_tarjeta_cinema == False and reserva== False:
            
            if tipo_sala == '2D':
                
                total= (sala_2d*0.9)* cantidad_boletas   
            
            elif tipo_sala == '3D':
                
                total= (sala_3d*0.9)* cantidad_boletas 
                
            else: 
                
                total= (sala_dx*0.9)* cantidad_boletas   
    
    #Revisar si es hora pico
    elif hora_pico == True:
        
        # Comprobar cada caso de cantidad de boletas, pago con tarjeta y reserva para calcular el valor a pagar en hora pico
        if pago_tarjeta_cinema== True and reserva ==True:
            
            if tipo_sala == '2D':
                
                total= (((sala_2d_inc)-(sala_2d*0.05))+2000)*cantidad_boletas
                
            elif tipo_sala == '3D':
                
                total= (((sala_3d_inc)-(sala_3d*0.05))+2000)*cantidad_boletas
                 
            else:
                
                total= (((sala_dx_inc)-(sala_dx*0.05))+2000)*cantidad_boletas
        
        elif pago_tarjeta_cinema == True and reserva ==False:
            
            if tipo_sala == '2D':
                
                total= (sala_2d_inc-sala_2d*0.05)*cantidad_boletas
            
            elif tipo_sala == '3D':
                
                total= (sala_3d_inc-sala_3d*0.05)*cantidad_boletas
            
            else:
                
                total= (sala_dx_inc-sala_dx*0.05)*cantidad_boletas    
            #Aqui voy    
        elif pago_tarjeta_cinema== False and reserva== True:
            
            if tipo_sala == '2D':
                
                total= (sala_2d_inc+2000)*cantidad_boletas
            
            elif tipo_sala == '3D':
                
                total= (sala_3d_inc+2000)*cantidad_boletas
            
            else:
                
                total= (sala_dx_inc+2000)*cantidad_boletas 
        
        elif pago_tarjeta_cinema == False and reserva == False:
            
            if tipo_sala == '2D':
                
                total= (sala_2d_inc)*cantidad_boletas
            
            elif tipo_sala == '3D':
                
                total= (sala_3d_inc)*cantidad_boletas
                
            else:
                
                total= (sala_dx_inc)*cantidad_boletas
                
    return round(total)

#Casos a evaluar

caso1= {'cantidad_boletas': 3, 'tipo_sala': '2D', 'hora_pico': True, 'pago_tarjeta_cinema': True, 'reserva': False}
caso2= {'cantidad_boletas': 4, 'tipo_sala': '3D', 'hora_pico': True, 'pago_tarjeta_cinema': False, 'reserva': True}
caso3= {'cantidad_boletas': 5, 'tipo_sala': 'Dinamix', 'hora_pico': False, 'pago_tarjeta_cinema': True, 'reserva': False}
caso4= {'cantidad_boletas': 2, 'tipo_sala': '2D', 'hora_pico': False, 'pago_tarjeta_cinema': False, 'reserva': True}

caso5= {'cantidad_boletas': 10, 'tipo_sala': '2D', 'hora_pico': True, 'pago_tarjeta_cinema': True, 'reserva': True}
caso6= {'cantidad_boletas': 3, 'tipo_sala': 'Dinamix', 'hora_pico': False, 'pago_tarjeta_cinema': False, 'reserva': False}
caso7= {'cantidad_boletas': 4, 'tipo_sala': 'Dinamix', 'hora_pico': True, 'pago_tarjeta_cinema': False, 'reserva': False}
caso8= {'cantidad_boletas': 6, 'tipo_sala': '3D', 'hora_pico': False, 'pago_tarjeta_cinema': True, 'reserva': False}

print(calcular_costo_boletas(caso1))

