class tarifa(object):
    semana=0
    finDeSemana=0
    
    def __init__(self,tarifaSemana,tarifaFinDeSemana):
        
        assert(tarifaSemana>0)
        assert(tarifaFinDeSemana>0)
        
        self.semana=tarifaSemana
        self.finDeSemana=tarifaFinDeSemana