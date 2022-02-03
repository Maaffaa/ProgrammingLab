class CSVFile():
  def __init__(self,file,name):
    self.name = name
    self.file = file
    
  def __str__(self):
    return ('Questo è il file {} e si chiama {}.'.format(self.file,self.name))
  
  def get_data(self):  # questa è definita sul modello di 
                       # shampoo_sales.cvs, su questo mi restituisce i valori.
    try:
      f = open(self.file)
      a = []
      for i in f:
        i = i.split(',')
        if i[0] != 'Date':
          j = i[1]     # queste 3 righe sono 
          j = j[:-1]   # per togliere \n 
          i[1] = j
          a.append(i)
      f.close()
      return a
    except:
      return ('Il file non esiste.')

class NumericalCSVFile (CSVFile):
  def __init__(self, file, name):
    self.name = name
    self.file = file
    self.fattura = self.converti_in_numeri()

  def fai(self):  # converte gli elementi di tutte colonne tranne la prima in floating point, ovvero in numeri
    cestino = self.get_data()
    for i in cestino:
      for j in range (1,len(cestino[0])):
        try:              # questo cancella solo il valore che non riesce a convertire
          i[j] = float(i[j])
        except:
          print ("Errore! '{}' non posso convertirlo in un numero! L'ho cancellato.".format(i[j]))
          del(i[j])

    return cestino

  def converti_in_numeri(self):  # converte gli elementi di tutte colonne tranne la prima in floating point, ovvero in numeri
    cestino = self.get_data()
    i = 0
    while i < len(cestino):
      try:               # questo cancella tutta la riga che contiene il valore non convertibile
        for j in range (1,len(cestino[0])):
          cestino[i][j] = float(cestino[i][j])
        i += 1
      except:
        print ("Errore! '{}' non posso convertirlo in un numero! L'ho cancellato.".format(cestino[i][j]))
        del(cestino[i])
        i += 1
          

    return cestino


shampoo = NumericalCSVFile('shampoo_sales.csv', 'shampoo')
#(str(shampoo))
#print(shampoo.get_data())
#print(str(shampoo))

#print(shampoo.converti_in_numeri()[1][1]*shampoo.converti_in_numeri()[5][1])
print(shampoo.fattura)

print(shampoo.converti_in_numeri())