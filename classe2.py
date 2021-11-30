class CSVFile():
  def __init__(self,file,name): #isinstance(name,str)
    if isinstance(name,str):
      self.name = name
    else:
      raise Exception('Il nome del file deve essere una stringa.')
    self.file = file
    
  def __str__(self):
    return ('Questo è il file {} e si chiama {}.'.format(self.file,self.name))
  
  def contarighe(self):
  numero = 0
  for i in self.file:
    numero += 1
  return numero
  
  def get_data(self, start = None, end = None):  # questa è definita sul modello di 
                       # shampoo_sales.cvs, su questo mi restituisce i valori.
              
    try:
      f = open(self.file)
      a = []
      if start != None and end != None:
        for i in range(start,end):
          f[i] = f[i].split(',')
          if f[i][0] != 'Date':
            j = f[i][1]     # queste 3 righe sono 
            j = j[:-1]   # per togliere \n 
            f[i][1] = j
            a.append(f[i])
      elif start == None:
        for i in range(0,end):
          f[i] = f[i].split(',')
          if f[i][0] != 'Date':
            j = f[i][1]     # queste 3 righe sono 
            j = j[:-1]   # per togliere \n 
            f[i][1] = j
            a.append(f[i])
      elif end == None:
        for i in range(start,len(f)):  # ATTENTA QUI DEVI RISOLVERE
          f[i] = f[i].split(',')
          if f[i][0] != 'Date':
            j = f[i][1]     # queste 3 righe sono 
            j = j[:-1]   # per togliere \n 
            f[i][1] = j
            a.append(f[i])
      else:
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
    self.fattura = self.fai_2()

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

  def fai_2(self):  # converte gli elementi di tutte colonne tranne la prima in floating point, ovvero in numeri
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

#print(shampoo.fai()[1][1]*shampoo.fai()[5][1])
print(shampoo.fattura)

def contarighe(file):
  numero = 0
  for i in f:
    numero += 1
  return numero
