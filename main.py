
#############
# Main tarea 2
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
    
    #Vemos la cantidad de dias intermedios
    dias_intermedios=((fin.fecha-inicio.fecha).days)-1#Para no contar el primer y ultimo dia, porque probablemente no se cubren completos
    #print(dias_intermedios)
    assert(dias_intermedios>=-1)
    
    #Horas del primer dia
    horasInicio=inicio.tiempo.hour+(inicio.tiempo.minute/60) #Agrega los minutos a la hora
    
    #print(str(horasInicio) + " horas inicio")
    
    #Horas del ultimo dia
    horasFin=fin.tiempo.hour+(fin.tiempo.minute/60) #Agrega los minutos a la hora
    
    #print(str(horasFin) + " horas final")
    
    #date.isoweekday()
    if(dias_intermedios+2>7): #Fueron mas de 7 dias
        print("Error: el servicio duro mas de 7 dias.")
        exit()
    elif(dias_intermedios==-1): #Fue el mismo dia, -1 por la resta
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
        
        return pago
    
    elif(dias_intermedios==0): #Fueron dos dias (inicio y fin)
        horasInicio=24-horasInicio
        horasFin=0+horasFin
        horas_totales=horasInicio+horasFin
        if(horas_totales<0.25): #Menos de 15 minutos
            print("Error: el servicio duro menos de 15 minutos.")
            exit()
        #Vemos si fue fin de semana
        diaInicio=inicio.fecha.weekday()
        diaFin=fin.fecha.weekday()
        if(diaInicio==5): #sabado
            pago=ceil(horas_totales)*tarifa.finDeSemana
        elif(diaInicio==6): #domingo
            pago=ceil(horasInicio)*tarifa.finDeSemana
            pago=pago+ceil(horasFin)*tarifa.semana
        elif(diaFin==5): #termina un sabado
            pago=ceil(horasInicio)*tarifa.semana
            pago=pago+ceil(horasFin)*tarifa.finDeSemana
        else: #entre semana
            pago=ceil(horas_totales)*tarifa.semana
        return pago
    else: #Mas de dos dias
        horasInicio=24-horasInicio
        horasFin=0+horasFin
        diaInicio=inicio.fecha.weekday()
        diaFin=fin.fecha.weekday()
        #Si es sabado o domingo
        if (diaInicio==5):
            pago=ceil(horasInicio)*tarifa.finDeSemana
            pago=pago+(24*tarifa.finDeSemana) #dom
            pago=pago+(dias_intermedios*(24*tarifa.semana))
            pago=pago+(ceil(horasFin)*tarifa.semana)
            
        elif(diaInicio==6):
            pago=ceil(horasInicio)*tarifa.finDeSemana
            pago=pago+(dias_intermedios*(24*tarifa.semana))
            #Si el dia fin es sabado
            if(diaFin==5):
                pago=pago+(ceil(horasFin)*tarifa.finDeSemana)
            else: 
                pago=pago+(ceil(horasFin)*tarifa.semana)
        else: #empieza cualquier dia de semana        
            pago=ceil(horasInicio)*tarifa.semana
            if(diaFin==5): #termina un sabado
                pago=pago+(dias_intermedios*(24*tarifa.semana))
                pago=pago+(ceil(horasFin)*tarifa.finDeSemana)
            elif(diaFin==6): #termina un domingo 
                dias_intermedios=dias_intermedios-1 #le quita el sab
                pago=pago+(dias_intermedios*(24*tarifa.semana))
                pago=pago+(24*tarifa.finDeSemana)
                pago=pago+(ceil(horasFin)*tarifa.finDeSemana)
        return pago
    
    #Assert de la postcondicion (sobre pago)
    
    
#tarifa = tarifa(15,20)
#inicio = tiempoDeTrabajo(2018,5,9,2,50,53)
#final = tiempoDeTrabajo(2018,5,9,3,50,54)
#tiempoDeServicio = [inicio, final]
#tiempoDeServicio[0]
#calcularPrecio(tarifa, tiempoDeServicio)

