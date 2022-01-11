
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