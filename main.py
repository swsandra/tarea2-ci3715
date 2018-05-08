from datetime import datetime, date, time
from tarifa import tarifa
from tiempoDeTrabajo import tiempoDeTrabajo
from math import ceil

def calcularPrecio(tarifa, tiempoDeServicio):
    
    #Assert de los tipos
    
    
    
    inicio=tiempoDeServicio[0]
    fin=tiempoDeServicio[1]
    
    #Vemos la cantidad de dias
    dias_totales=((fin.fecha-inicio.fecha).days)-1 #Para no contar el primer y ultimo dia, porque probablemente no se cubren completos
    
    #Horas del primer dia
    horasInicio=inicio.tiempo.tm_hour+(inicio.tm_min/60) #Agrega los minutos a la hora
    horasInicio=24-horasInicio
    
    #Horas del ultimo dia
    horasFin=fin.tiempo.tm_hour+(fin.fecha.tm_min/60) #Agrega los minutos a la hora
    horasFin=0+horasFin
    
    #date.isoweekday()
    if(dias_totales>7): #Fueron mas de 7 dias
        print("Error: el servicio duro mas de 7 dias.")
        exit()
    elif(dias_totales==-1): #Fue el mismo dia, -1 porla resta
        horas_totales=horasFin-horasInicio
        if(horas_totales<0.25): #Menos de 15 minutos
            print("Error: el servicio duro menos de 15 minutos.")
            exit()
        #Ve el dia de la semana
        dia=inicio.fecha.weekday()
        if(dia==5 or dia==6): #sabado 5, domingo 6
            pago=ceil(horas_totales)*tarifa.finDeSemana
        else:
            pago=ceil(horas_totales)*tarifa.semana
            
    else:  #Duro mas de 1 dia y menos de 7      
          
    #Assert postcondiciones
    
    
    
    
    
    
    
    
     
    
    
    