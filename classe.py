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


#shampoo = NumericalCSVFile('shampoo_sales.csv', 'shampoo')
#(str(shampoo))
#print(shampoo.get_data())
#print(str(shampoo))

#print(shampoo.converti_in_numeri()[1][1]*shampoo.converti_in_numeri()[5][1])
#print(shampoo.fattura)

#print(shampoo.converti_in_numeri())

def lista_completa(series):
    lista = []
    for element in series:
        lista.append(element)
    for item in lista:
        item[0] = item[0].split('-')
    return lista

A = [['1949-01', 112], ['1949-02', 118], ['1949-03', 132], ['1949-04', 132], ['1949-05', 132], ['1949-06', 132], ['1949-07', 132], ['1949-08', 132], ['1949-09', 132], ['1949-10', 132], ['1949-11', 132], ['1949-12', 132], ['1950-01', 115], ['1950-02', 126], ['1950-03', 141], ['1950-04', 141], ['1950-05', 141], ['1950-06', 141], ['1950-07', 141], ['1950-08', 141], ['1950-09', 141], ['1950-10', 141], ['1950-11', 141], ['1950-12', 141], ['1951-01', 145], ['1951-02', 150], ['1951-03', 178], ['1951-04', 178], ['1951-05', 178], ['1951-06', 178], ['1951-07', 178], ['1951-08', 178], ['1951-09', 178], ['1951-10', 178], ['1951-11', 178], ['1951-12', 178]]
b = A
print(A)
print(lista_completa(A))
print(A)
print(b)

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
