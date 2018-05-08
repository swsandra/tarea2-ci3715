
#############
#Documento Vacio
# Sandra Vera
# Aurivan Castro
# Elvin Quero
###############

from datetime import datetime, date, time
from tarifa import tarifa
from tiempoDeTrabajo import tiempoDeTrabajo
from math import ceil

def calcularPrecio(tarifa, tiempoDeServicio):
    
    #Assert de los tipos
    
    
    
    inicio=tiempoDeServicio[0]
    fin=tiempoDeServicio[1]
    
    #Vemos la cantidad de dias
    dias_totales=((fin.fecha-inicio.fecha).days)-1#Para no contar el primer y ultimo dia, porque probablemente no se cubren completos
    #print(dias_totales)
    
    #Horas del primer dia
    horasInicio=inicio.tiempo.hour+(inicio.tiempo.minute/60) #Agrega los minutos a la hora
    
    #print(str(horasInicio) + " horas inicio")
    
    #Horas del ultimo dia
    horasFin=fin.tiempo.hour+(fin.tiempo.minute/60) #Agrega los minutos a la hora
    
    #print(str(horasFin) + " horas final")
    
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
            return pago
        else:
            pago=ceil(horas_totales)*tarifa.semana
            return pago

    else:
        horasInicio=24-horasInicio
        horasFin=0+horasFin
        horas_totales=horasFin-horasInicio
        

#tarifa = tarifa(15,20)
#inicio = tiempoDeTrabajo(2018,5,9,2,50,53)
#final = tiempoDeTrabajo(2018,5,9,3,50,54)
#tiempoDeServicio = [inicio, final]
#tiempoDeServicio[0]
#calcularPrecio(tarifa, tiempoDeServicio)