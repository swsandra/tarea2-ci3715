
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

def calcularPrecio(tarifaDada, tiempoDeServicio):
    
    #Assert de los tipos
    assert isinstance(tarifaDada, tarifa)
    assert isinstance(tiempoDeServicio, tiempoDeTrabajo)
    
    
    
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
        raise Exception()
    elif(dias_intermedios==-1): #Fue el mismo dia, -1 por la resta
        horas_totales=horasFin-horasInicio
        if(horas_totales<0.25): #Menos de 15 minutos
            print("Error: el servicio duro menos de 15 minutos.")
            raise Exception()
        #Ve el dia de la semana
        dia=inicio.fecha.weekday()
        if(dia==5 or dia==6): #sabado 5, domingo 6
            pago=ceil(horas_totales)*tarifaDadaDada.finDeSemana
        else:
            pago=ceil(horas_totales)*tarifaDada.semana
        
        return pago
    
    elif(dias_intermedios==0): #Fueron dos dias (inicio y fin)
        horasInicio=24-horasInicio
        horasFin=0+horasFin
        horas_totales=horasInicio+horasFin
        if(horas_totales<0.25): #Menos de 15 minutos
            print("Error: el servicio duro menos de 15 minutos.")
            raise Exception()
        #Vemos si fue fin de semana
        diaInicio=inicio.fecha.weekday()
        diaFin=fin.fecha.weekday()
        if(diaInicio==5): #sabado
            pago=ceil(horas_totales)*tarifaDada.finDeSemana
        elif(diaInicio==6): #domingo
            pago=ceil(horasInicio)*tarifaDada.finDeSemana
            pago=pago+(ceil(horasFin)*tarifaDada.semana)
        elif(diaFin==5): #termina un sabado
            pago=ceil(horasInicio)*tarifaDada.semana
            pago=pago+(ceil(horasFin)*tarifaDada.finDeSemana)
        else: #entre semana
            pago=ceil(horas_totales)*tarifaDada.semana
        return pago
    
    else: #Mas de dos dias
        horasInicio=24-horasInicio
        horasFin=0+horasFin
        horas_totales=horasInicio+horasFin
        diaInicio=inicio.fecha.weekday()
        diaFin=fin.fecha.weekday()
        #Si es sabado o domingo
        if (diaInicio==5):
            pago=ceil(horasInicio)*tarifaDada.finDeSemana
            dias_intermedios=dias_intermedios-1 #le quita el domingo
            pago=pago+(24*tarifaDada.finDeSemana) #dom
            pago=pago+(dias_intermedios*(24*tarifaDada.semana))
            pago=pago+(ceil(horasFin)*tarifaDada.semana)
            
        elif(diaInicio==6):
            #pago=ceil(horasInicio)*tarifaDada.finDeSemana
            pago=pago+(dias_intermedios*(24*tarifaDada.semana))
            #Si el dia fin es sabado
            if(diaFin==5):
                pago=pago+(ceil(horas_totales)*tarifaDada.finDeSemana)
            else: 
                pago=pago+(ceil(horasFin)*tarifaDada.semana)
        else: #empieza cualquier dia de semana        
            #pago=ceil(horasInicio)*tarifaDada.semana
            if(diaFin==5): #termina un sabado
                pago=ceil(horasInicio)*tarifaDada.semana
                pago=pago+(dias_intermedios*(24*tarifaDada.semana))
                pago=pago+(ceil(horasFin)*tarifaDada.finDeSemana)
            elif(diaFin==6): #termina un domingo 
                pago=ceil(horasInicio)*tarifaDada.semana
                dias_intermedios=dias_intermedios-1 #le quita el sab
                pago=pago+(dias_intermedios*(24*tarifaDada.semana))
                pago=pago+(24*tarifaDada.finDeSemana)
                pago=pago+(ceil(horasFin)*tarifaDada.finDeSemana)
            #si pasa del fin de semana
            elif(diaFin<diaInicio):
                pago=ceil(horas_totales)*tarifaDada.semana
                dias_intermedios=dias_intermedios-2 #le quita el fin de sem
                pago=pago+(2*(24*tarifaDada.finDeSemana))
                pago=pago+(dias_intermedios*(24*tarifaDada.semana))
                #pago=pago+(ceil(horasFin)*tarifaDada.semana)
            else:   #si es entre semana pero no pasa el fin de semana
                pago=ceil(horas_totales)*tarifaDada.semana
                pago=pago+(dias_intermedios*(24*tarifaDada.semana))
                #pago=pago+(ceil(horasFin)*tarifaDada.semana)
        return pago
    
    #Assert de la postcondicion (sobre pago)
    
    
#tarifaDada = tarifa(15,20)
#inicio = tiempoDeTrabajo(2018,5,9,2,50,53)
#final = tiempoDeTrabajo(2018,5,9,3,50,54)
#tiempoDeServicio = [inicio, final]
#tiempoDeServicio[0]
#calcularPrecio(tarifaDada, tiempoDeServicio)

