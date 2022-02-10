<<<<<<< HEAD
class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name # nome del file
        
        self.can_read = True # provo ad aprirlo e leggere una riga 
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
        
    def get_data(self):
        if not self.can_read: # se nell'init ho settato can_read a False vuol dire che
                              # il file non poteva essere aperto o era illeggibile
            raise ExamException('Errore, file non aperto o illeggibile.')
            return None
        else:
            data = [] # creo una lista vuota
            my_file = open(self.name,'r')
            for line in my_file:  # leggo il file riga per riga
                elements = line.split(',')  # faccio lo split di ogni linea sulla virgola
                elements[-1] = elements[-1].strip() # pulisco il carattere di newline
                                                    # dall'ultimo elemento con la funzione strip()
                if elements[0] != 'date': # questo è superfluo se poi si usa l'altra funzione
                    for i in elements:
                        if str.isdigit(i):
                            indice = elements.index(i)
                            elements[indice] = int(i) # converto in interi le stringhe che contengono interi
                    data.append(elements) # aggiungo gli elementi della riga
                    
            # ora abbiamo data che è la nostra lista con i valori
            # vogliamo alzare un'eccezione se la stessa stringa del tipo '1949-06' è presente n>1 volte in data
            s = {} # creo un dizionario vuoto
            for i in data:
                for j in i:
                    if isinstance(j,str):
                        s[j] = s.get(j,0)+1 # conto quante volte una stessa stringa è ripetuta in data
        
            for valore in s:
                if s[valore]>1:
                    # qui scremo e considero le stringhe che rappresentano le date ripetute e alzo un'eccezione
                    for indi in range(0,10): 
                        if '-0'+str(indi) in valore: 
                            raise ExamException('Il valore {} compare più di una volta.'.format(valore))
                    for indi in range(10,13):
                        if '-'+str(indi) in valore:
                            raise ExamException('Il valore {} compare più di una volta.'.format(valore))
                        
            datas = amico(data) # mi servo di una funzione di supporto da me definita  
            for luce in range(0,len(datas)): # questo serve a pulire la serie da cose varie.
                datas = amico(datas) # mi servo di una funzione di supporto da me definita  
            
            datas = funxio(datas) # anche qui mi servo di una funzione di supporto da me definita        
            my_file.close() # chiudo il file
            return datas

# QUESTE FUNZIONI SERVONO ALL'INTERNO DI get_data()
        
def funxio(datas): 
    # scopo di questa funzione è:
    # verificare che gli elementi siano effettivamente date
    # verificare che le date siano in ordine
    for pluto in datas: # es. pluto = ['1949-05',126]
        if len(pluto[0])!= 7: # elimino tutti gli elementi che non possono essere date (perchè le stringhe sono troppo corte)
            del(datas[datas.index(pluto)])
            return funxio(datas) # ritorno ricorsivamente la funzione
        mese = pluto[0][-2:] # es. mese = '05'
        anno = pluto[0][0:4] # es. anno = '1949'
        if not str.isdigit(mese) or not str.isdigit(anno): # se gli ultimi 2 elementi o i primi 4 non sono
                                                           # stringhe di cifre allora non sono date: lo elimino
            del(datas[datas.index(pluto)])
            return funxio(datas) # ritorno ricorsivamente la funzione
    for pluto in datas: # controllo che le date siano in ordine
        numero = datas.index(pluto)
        mese = pluto[0][-2:] # es. mese = '05'
        anno = pluto[0][0:4] # es. anno = '1949'
        if numero != len(datas)-1: # escludo l'ultimo elemento perchè non ha un successivo
            if anno == datas[numero+1][0][0:4]: # se gli anni di due elementi successivi sono uguali
                if mese != '12': # e il mese del primo non è dicembre
                    if int(mese)+1 > int(datas[numero+1][0][-2:]): # se i mesi non sono in ordine alzo un'eccezione
                        raise ExamException("Gli elementi non sono ordinati.(I) In particolare {} non è al posto giusto (bisogna controllare i mesi).".format(datas[numero+1]))
                elif mese == '12': # se il mese è dicembre 
                    if int(anno)+1 > int(datas[numero+1][0][0:4]): # ovv. se un mese dello stesso anno segue dicembre
                        raise ExamException('Gli elementi non sono ordinati.(II) In particolare {} non è al posto giusto oppure tale numero non corrisponde a nessuna data (bisogna controllare i mesi).'.format(datas[numero+1]))
                    elif datas[numero+1][0][-2:] != '01': 
                        raise ExamException("Gli elementi non sono ordinati.(V) In particolare {} non è al posto giusto (bisogna controllare i mesi).".format(datas[numero+1]))
       
            elif int(anno)+1 > int(datas[numero+1][0][0:4]): # se gli anni non sono ordinati alzo un'eccezione
                raise ExamException('Gli elementi non sono ordinati.(III) In particolare {} non è al posto giusto (bisogna controllare gli anni).'.format(datas[numero+1]))

    return datas
        
    
def amico(data):  
    # scopo di questa funzione è:
    # pulire la lista da elementi che non contengono interi e stringhe 
    # mettere tutti gli elementi che hanno un intero ed una stringa in ordine (ovv. nella forma [stringa, intero])
    # rendere tutti gli elementi di lunghezza 2 
    # salvare solo gli elementi contenenti una data
    for k in data:
        if len(k)>2: # se la lista ha più di 2 elementi
            if not isinstance(k[-1],int): # se l'ultimo elemento di k non è un intero
                for mes in ['-01','-02','-03','-04','-05','-06','-07','-08','-09','-10','-11','-12']:
                    if isinstance(k[-1],str) and mes in k[-1]: # se trovo la stringa di una data all'ultimo posto
                        k[-1],k[-2] = k[-2],k[-1] # la scambio con il penultimo elemento
                        return amico(data) # ritorno ricorsivamente la funzione
                k.pop() # se non trovo la stringa di una data all'ultimo posto, elimino l'ultimo elemento 
                        # perchè non è né un intero né una data, quindi è un dato superfluo e posso eliminarlo
                return amico(data) # ritorno ricorsivamente la funzione
            else: # se l'ultimo elem di k è un intero
                for mes in ['-01','-02','-03','-04','-05','-06','-07','-08','-09','-10','-11','-12']:
                    if isinstance(k[-2],str) and mes in k[-2]:  # se trovo la stringa di una data al penultimo posto
                        del(k[-3]) # elimino il terzultimo elemento perchè non è né un intero né una data, quindi inultile
                        return amico(data) # ritorno ricorsivamente la funzione
                del(k[-2]) # se non trovo la stringa di una data al penultimo posto, lo elimino
                return amico(data) # ritorno ricorsivamente la funzione
        elif len(k)<2: # se la lista ha meno di 2 elementi significa che non mi tornerà utile nella computazione
            indice = data.index(k) 
            del(data[indice]) # quindi posso eliminarla
        else:  # se la lista ha lunghezza esattamente 2
            if not isinstance(k[0],str): # se il primo elemento non è una stringa
                k[1],k[0] = k[0],k[1] # scambio i 2 elementi
                if not isinstance(k[0],str): # se di nuovo il primo elemento non è una stringa significa che k non mi interessa
                    indice = data.index(k) # indice di k in series
                    del(data[indice]) # quindi posso eliminare k
            if not isinstance(k[1],int) or k[1] == 0: # arrivo qui se il primo elemento è una stringa
                                                      # se il secondo non è un intero
                indice = data.index(k) # indice di k in series
                del(data[indice]) # posso eliminare k perchè non ha dati utili
    return data


def sostegno(series,first,last,diff):
    # scopo di questa funzione è:
    # pulire la lista da elementi che non contengono interi e stringhe 
    # mettere tutti gli elementi che hanno un intero ed una stringa in ordine (ovv. nella forma [stringa, intero])
    # rendere tutti gli elementi di lunghezza 2 
    # salvare solo gli elementi contenenti una data
    # è da considerarsi superflua se si usa una lista presa da un file tramite la funzione get_data() per CSVTimeSeriesFile
    # ma se si passa una lista qualsiasi allora serve.
    
    for k in series: # per ogni elemento della serie
        if len(k)>2: # qui faccio in modo che ogni elemento della lista sia una lista composta da 2 elementi
            if not isinstance(k[-1],int): # se l'ultimo elem non è un intero (num passeggeri)
                for year in range(0,diff+1):
                    for mes in ['-01','-02','-03','-04','-05','-06','-07','-08','-09','-10','-11','-12']:
                        if isinstance(k[-1],str) and str(int(first)+year)+mes in k[-1]: # se al penultimo posto c'è una data, 
                                                                                        # allora cambio di posto gli ultimi due
                            k[-1],k[-2] = k[-2],k[-1]
                            return sostegno(series,first,last,diff) # richiamo ricorsivamente la funzione
                k.pop() # se l'ultimo elemento di k non è il num di passeggeri e nemmeno la data, allora elimino l'elemento k
                return sostegno(series,first,last,diff) # richiamo ricorsivamente
            else: # se l'ultimo elemento di k è un intero
                for year in range(0,diff+1):
                    for mes in ['-01','-02','-03','-04','-05','-06','-07','-08','-09','-10','-11','-12']:
                        if isinstance(k[-2],str) and str(int(first)+year)+mes in k[-2]: # se il penultimo elemento di k è la data
                            del(k[-3]) # elimino il terzultimo (che sarà superfluo)
                            return sostegno(series,first,last,diff) # richiamo ricorsivamente
                
                del(k[-2]) # se il pernultimo elemento di k non è la data, allora lo elimino 
                return sostegno(series,first,last,diff) # ritorno ricorsivamente
                        
        elif len(k)<2: # se l'elemento ha lunghezza minore di 2 vuol dire che mancherà o la data o il num di passeggeri
                       # quindi k è inutile: lo elimino
            indice = series.index(k) # indice di k in series
            del(series[indice])       
        else: # se la lunghezza di k è 2 
            if not isinstance(k[0],str): # se il primo elemento non è una stringa, 
                k[1],k[0] = k[0],k[1]    # cambio di posto i due elementi
                if not isinstance(k[0],str): # se ancora non ho una stringa, elimino k perchè inutile
                    indice = series.index(k) # indice di k in series
                    del(series[indice]) 
            if not isinstance(k[1],int): # se ho una stringa ma non un intero, la lista è ancora inutile: la elimino
                indice = series.index(k) # indice di k in series
                del(series[indice]) 
    
    return series


def compute_avg_monthly_difference(series,first,last): # calcola la variazione media per un dato intervallo di anni
    
    if not isinstance(first,str) or not isinstance(last,str): # se first o last non sono passate come stringhe
        raise ExamException('Bisogna inserire una stringa come valori di first e last. I valori che hanno dato problemi sono stati {} oppure {}'.format(first,last))
    
    if str.isdigit(first)==False or str.isdigit(last)==False: # se first o last non sono numeri interi (dentro una stringa) es. '1949'
        raise ExamException('Le stringhe di first e last devono essere stringhe di numeri interi. I valori che hanno dato problemi sono stati {} oppure {}'.format(first,last))
    
    if int(last)<int(first): # queste due righe riordinano last e first se scambiati
        last, first = first, last
    
    if first == last: # se sono uguali la differenza media è nulla
        return [0,0,0,0,0,0,0,0,0,0,0,0]
    
    if not isinstance(series,list): # se la series non è una lista
        raise ExamException("Il primo input deve essere una lista di liste. L'elemento che ha dato problemi è stato {}.".format(series))
    if series == []: # o se è una lista vuota
        raise ExamException("Il primo input deve essere una lista di liste. L'elemento che ha dato problemi è stato {}.".format(series))
    for elemento in series: # o se non è composta da liste
        if not isinstance(elemento,list):
            raise ExamException("Il primo input deve essere una lista di liste. L'elemento che ha dato problemi è stato {}.".format(elemento))
        
    
    diff = int(last) - int(first) # differenza degli anni presi in considerazione
    ris = None # definisco il risultato
    
    for i in range(0,len(series)): # questo serve a pulire la serie da cose varie.
        serie = sostegno(series,first,last,diff) # mi servo di una funzione di supporto da me definita
    
    # qui aggiungo uno spazio davanti ad ogni data, in modo tale posso procedere solo se 
    # l'anno è presente (e non solo magari le ultime 2 cifre)
    # es. se l'anno 1959 compare, questo non significa che compaia anche l'anno 959, 59 o 9
    # e con queste due righe mi assicuro che compaia esattamente 1959 tra gli anni, altrimenti
    # alza una eccezione (vedi sotto)
    for elem in serie: 
        elem[0] = ' '+elem[0]
    
    i = -1
    while i < len(serie)-1:
        i += 1
        if ' '+first+'-' in serie[i][0]: # controllo che il primo anno compaia nella series
            m = -1
            while m < len(serie)-1:
                m += 1
                if ' '+last+'-' in serie[m][0]: # controllo che il secondo anno compaia nella series
                    
                    ris = [0,0,0,0,0,0,0,0,0,0,0,0] # se si arriva a questo punto significa
                                                    # che gli anni agli estremi sono presenti
                                                    # quindi ci sarà un risultato
                    dizio = dict(serie) # creo un dizionario con gli elementi della series
                                        
                    # Noto che basta fare la sottrazione tra il valore dell'ultimo anno e del primo, ignorando
                    # i valori nel mezzo poichè compaiono tutti due volte con segni opposti, quindi si elidono.
                    for j in range(1,10):
                        for s in range(1,diff+1):
                            ultimo = ' '+last+'-0'+str(j) # es. 1951-03
                            primo = ' '+first+'-0'+str(j)
                            
                            # se uno dei mesi di uno degli anni agli estremi (last, first) non compare, allora sostituisco con 
                            # i dati provenienti dall'anno precedente o successivo rispettivamente
                            if ' '+str(int(last)-s)+'-0'+str(j) in dizio:
                                dizio[ultimo] = dizio.get(ultimo,dizio[' '+str(int(last)-s)+'-0'+str(j)]) # es. 1951-03:
                            if ' '+str(int(first)+s)+'-0'+str(j) in dizio:
                                dizio[primo] = dizio.get(primo,dizio[' '+str(int(first)+s)+'-0'+str(j)])
                        
                        # aggiorno i valori del risultato calcolando la variazione media per ogni mese
                        # (posso dividere per la differenza perchè, se si è arrivati qui, diff != 0)
                        # considero il valore assoluto perchè non è detto che il numero di passeggeri sia sempre in aumento
                        ris[j-1] = dizio[' '+str(int(first)+diff)+'-0'+str(j)] - dizio[' '+str(int(first))+'-0'+str(j)]
                        ris[j-1] = abs(ris[j-1]/diff) 
                    
                    # qui analogo a quello sopra solo che per i mesi a due cifre
                    for j in range(10,13):
                        for s in range(0,diff+1):
                            ultimo = ' '+last+'-'+str(j) # es. 1951-11
                            primo = ' '+first+'-'+str(j)
                            
                            if ' '+str(int(last)-s)+'-'+str(j) in dizio:
                                dizio[ultimo] = dizio.get(ultimo,dizio[' '+str(int(last)-s)+'-'+str(j)]) # es. 1951-03:
                            if ' '+str(int(first)+s)+'-'+str(j) in dizio:
                                dizio[primo] = dizio.get(primo,dizio[' '+str(int(first)+s)+'-'+str(j)])
                                                        
                        ris[j-1] = dizio[' '+str(int(first)+diff)+'-'+str(j)] - dizio[' '+str(int(first))+'-'+str(j)]
                        ris[j-1] = abs(ris[j-1]/diff)
                        
                    break # interrompo il ciclo while perchè ho calcolavo ciò che mi interessa
    
    for elem in serie: # tolgo gli spazi che avevo aggiunto per verificare l'anno
        elem[0] = elem[0][1:]
    
    if ris == None: # ritorna None solo se non ha verificato le prime due condizioni dentro il primo while
        raise ExamException('Almeno uno dei due valori {} o {} non è contenuto nel file.'.format(first,last))
    
    return ris


#mia_file = CSVTimeSeriesFile(name='sub.csv')
#print('Nome del file: "{}"'.format(mia_file.name))
#S = (mia_file.get_data())

#print(S)
#s = (compute_avg_monthly_difference(S,'1951','1949'))
#print(s)