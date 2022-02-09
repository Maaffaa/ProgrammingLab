<<<<<<< HEAD
class ExamException(Exception):
    pass

class MovingAverage():
    
    def __init__(self, window):
        
        # Controllo che la lunghezza della finestra si di tipo intero
        if not isinstance(window, int):
            raise ExamException('Invalid type for window, only int supported. Got "{}"'.format(type(window)))

        # Controllo che la lunghezza della finestra non sia uguale a zero o negativa.
        # nota bene che una finestra di lunghezza uno e' accettata!
        if window < 1:
            raise ExamException('Negative or zero window value provided')
        
        # Salvo la lunghezza della finestra internamente
        self.window = window
    
    def compute(self, data):

        # Controllo che i valori siano in una lista
        if not isinstance(data, list):
            raise ExamException('Invalid type for data, only list supported. Got "{}"'.format(type(data)))

        # Controllo che la lista sia abbastanza lunga
        if len(data) < self.window:
            raise ExamException('Not enough data to compute a moving average of "{}" steps'.format(self.window))
        
        # Controllo che i valori della lista siano di tipo floato o numerico.
        # Questo controllo non era veramente richiesto, e puo' alle volte
        # risultare lento perchè aggiungo un ciclo su tutti gli elementi della lista.
        # Tuttavia dava punti extra nella valutazione, per premiare chi ci ha pensato
        # e si e' posto il problema a prescindere dalle performance (che non sono
        # argomento di quetso corso).
        
        for item in data:
            if not (isinstance(item, int) or  isinstance(item, float)):
                raise ExamException('Got non-numeric item in the list data: "{}"'.format(item))
        
        # Ok, ora calcolo la media mobile ciclando su tutti gli elmenti della lista. Per la natura
        # del problema, non posso essere del tutto pythonico ed usar eper esempio il costrutto 
        # "for item in list", ma devo usare un' indice di supporto.
        
        averages = []
        for i in range(len(data)+1):
            
            # Se non ho ho abbastanza valori su cui applicarla, 
            # continuo andando al prossimo giro
            if i < self.window:
                continue
            else:
                # Forma contratta che usa la "sum" built-in. Si poteva implementare
                # questa parte in molti altri modi, piu' o meno contratti.
                averages.append(sum(data[i-self.window:i])/self.window)
                
        return averages
=======

class MovingAverage():
    def __init__(self, numero):
        if isinstance(numero, int):
            self.num = numero
        else:
            raise ExamException('Il numero deve essere un numero intero positivo e deve essere espresso in cifre.')
    
    def compute(self,serie):
        if isinstance(serie, list):
            if len(serie) >= self.num:
                risultato = []
                for i in range(0,len(serie)-(self.num-1)):
                    risultato.append(media(serie[i:i+self.num]))
                return risultato
            else:
                raise ExamException("La lista deve essere più lunga del numero inserito nell'oggetto MovingAverage.")
        else:
            raise ExamException('Per la funzione "compute" bisogna inserire una lista.')

media = lambda serie: sum(serie)/len(serie)    
mob = MovingAverage(2)
print(mob.compute([2,4,8,16]))
print(mob.compute([2]))
print(mob.compute((5,6,8)))
print(mob.compute([8.56,4.23,5]))
>>>>>>> origin/main
