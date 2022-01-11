class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self, numero):
        if isinstance(numero, int):
            self.num = numero
        else:
            raise ExamException('Il numero deve essere un numero intero positivo e deve essere espresso in cifre.')
    
    def compute(serie):
        if isinstance(serie, list):
            for elem in serie:
                if type(elem) = float:
                    if len(serie) >= self.num:
                        risultato = []
                        for i in range(0,len(serie)-(self.num + 1)):
                            risultato.append(media(serie[i:i+self.num]))
                            print(risultato)
                    else:
                        raise ExamException("La lista deve essere più lunga del numero inserito nell'oggetto MovingAverage.")
                else:
                    raise ExamException('La lista deve essere composta da numeri reali.')
        else:
            raise ExamException('Per la funzione "compute" bisogna inserire una lista.')

media = lambda serie: sum(serie)/len(serie)    