from datetime import datetime, date, time, timedelta
import calendar

class tiempoDeTrabajo(object):
    fecha = date(2018,1,1) #anio, mes, dia
    tiempo = time(0,0,0) #hora, min, seg
    
    def __init__(self,anio,mes,dia,hora,min,seg):
        assert(anio>0)
        assert(1<=mes<12)
        assert(1<=dia<31)
        assert(0<=hora<23)
        assert(0<=min<60)
        assert(0<=seg<60)
        
        self.fecha = date(anio, mes, dia)
        self.tiempo = time(hora,min,seg)