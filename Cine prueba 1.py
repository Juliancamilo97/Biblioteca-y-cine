def calcular_costo_boletas(info_cine: dict)->int:
    
    cantidad_boletas=info_cine['cantidad_boletas']
    tipo_sala=info_cine['tipo_sala']
    hora_pico=info_cine['hora_pico']
    pago_tarjeta_cinema=info_cine['pago_tarjeta_cinema']
    reserva=info_cine['reserva']
    
    dinamix=18800
    d2=11300
    d3=15500 
    total=0
    descnopico=0
    tarjeta=0
    
    if tipo_sala=='2D':
        total= d2
    elif tipo_sala=='3D':
        total= d3
    else:
        total= dinamix
    
    if hora_pico==False:
      descnopico= total*0.1
      if info_cine['cantidad_boletas']>=3:
          descnopico= descnopico+500
    elif hora_pico==True:
        if tipo_sala== '2D':
            total=d2*1.25
        if tipo_sala=='3D':
            total=d3*1.25
        if tipo_sala=='Dinamix':
            total= dinamix*1.5
            
    if pago_tarjeta_cinema== True and tipo_sala=='2D':
        tarjeta=d2*0.05
    if pago_tarjeta_cinema== True and tipo_sala=='3D':
        tarjeta=d3*0.05
    if pago_tarjeta_cinema== True and tipo_sala=='Dinamix':
        tarjeta=dinamix*0.05

    total=total-descnopico-tarjeta
    
    if reserva==True:
        total=total+2000
    
    total= int(total*cantidad_boletas)
    
    return total            
             
             
caso1= {'cantidad_boletas': 3, 'tipo_sala': '2D', 'hora_pico': True, 'pago_tarjeta_cinema': True, 'reserva': False}
caso2= {'cantidad_boletas': 4, 'tipo_sala': '3D', 'hora_pico': True, 'pago_tarjeta_cinema': False, 'reserva': True}
caso3= {'cantidad_boletas': 5, 'tipo_sala': 'Dinamix', 'hora_pico': False, 'pago_tarjeta_cinema': True, 'reserva': False}
caso4= {'cantidad_boletas': 2, 'tipo_sala': '2D', 'hora_pico': False, 'pago_tarjeta_cinema': False, 'reserva': True}

print(calcular_costo_boletas(caso1))
print(calcular_costo_boletas(caso2))
print(calcular_costo_boletas(caso3))
print(calcular_costo_boletas(caso4))