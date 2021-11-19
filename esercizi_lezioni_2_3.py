def sum_list(lista):
  s = 0
  for i in lista:
    s += i
  return s

#print(sum_list([1,2,3,4,5,6,7,8,9]))


#shampoo = open('shampoo_sales.csv','r')
#j = 0
#arr_linea = []
#for i in shampoo:
#  arr_linea.append(i.split(','))
#  arr_linea[j][1] = arr_linea[j][1][:-1]
  #print(arr_linea)
#  j += 1
#def somma_lista(lista):
#  s = 0
#  for i in lista:
#    if i[1] != 'Sales':
#      s += float(i[1])
#      print(s)
#  return s 

#print(somma_lista(arr_linea))
#shampoo.close()

shampoo = open('shampoo_sales.csv','r')

arr_linea = []
for i in shampoo:
  elements = i.split(',')
  if elements[1] != 'Sales\n':
    arr_linea.append(float(elements[1][:-1]))
print(sum(arr_linea))

shampoo.close()