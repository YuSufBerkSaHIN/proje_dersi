# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.
#  Örnek olarak:
# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# output: [1,'a','cat',2,3,'dog',4,5]
list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
list2 = []
def flatten(l):
    for sublist in l:
        if type(sublist) == list:
            flatten(sublist)
        else:
            list2.append(sublist)
    return list2

print(flatten(list1))

# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

# input: [[1, 2], [3, 4], [5, 6, 7]]

# output: [[[7, 6, 5], [4, 3], [2, 1]]
input = [[1, 2], [3, 4], [5, 6, 7]]
input.reverse()
for i in range(len(input)):
    (input[i])=(input[i])[::-1]

print(input)