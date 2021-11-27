class CSVFile():
  def __init__(self,file,name):
    self.name = name
    self.file = file
  
  def __str__(self):
    return ('Questo è il file {} e si chiama {}.'.format(self.file,self.name))
  
  def get_data(self):  # questa è definita sul modello di 
                       # shampoo_sales.cvs, su questo mi restituisce i valori.
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

shampoo = CSVFile('shampoo_sales.csv', 'shampoo')
(str(shampoo))
print(shampoo.get_data())
print(str(shampoo))
