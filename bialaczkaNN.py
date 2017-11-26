import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
# Input Array
# Output Array
training_path = '/Users/jakubsanecki/Desktop/bialaczka/Bialaczki_dane/'
# Defining CSVs
bazofilowa = genfromtxt(training_path + 'training_bazofilowa.csv', delimiter=';')
bialaczka_komorek_wielkojadrzastych = genfromtxt(training_path + 'training_bialaczka_komorek_wielkojadrzastych.csv', delimiter=';')
chloniak_limfatyczny = genfromtxt(training_path + 'training_chloniak_limfatyczny.csv', delimiter=';')
cytolukemia = genfromtxt(training_path + 'training_cytolukemia.csv', delimiter=';')
differentiation_in_part = genfromtxt(training_path + 'training_differentiation_in_part.csv', delimiter=';')
differentiation = genfromtxt(training_path + 'training_differentiation.csv', delimiter=';')
eozyrofilowa = genfromtxt(training_path + 'training_eozyrofilowa.csv', delimiter=';')
granula_mononuclear = genfromtxt(training_path + 'training_granula_mononuclear.csv', delimiter=';')
granulocylosis = genfromtxt(training_path + 'training_granulocylosis.csv', delimiter=';')
granulocyte = genfromtxt(training_path + 'training_granulocyte.csv', delimiter=';')
l2type = genfromtxt(training_path + 'training_l2type.csv', delimiter=';')
ltype = genfromtxt(training_path + 'training_ltype.csv', delimiter=';')
lymphocytic = genfromtxt(training_path + 'training_lymphocytic.csv', delimiter=';')
mielomonocytarna = genfromtxt(training_path + 'training_mielomonocytarna.csv', delimiter=';')
mlemonoblastyczna = genfromtxt(training_path + 'training_mlemonoblastyczna.csv', delimiter=';')
monoblastyczna = genfromtxt(training_path + 'training_monoblastyczna.csv', delimiter=';')
monocytarna = genfromtxt(training_path + 'training_monocytarna.csv', delimiter=';')
plazmocytowa = genfromtxt(training_path + 'training_plazmocytowa.csv', delimiter=';')
subacute_granulocyte = genfromtxt(training_path + 'training_subacute_granulocyte.csv', delimiter=';')
wielokapilarnokomorkowa = genfromtxt(training_path + 'training_wielokapilarnokomorkowa.csv', delimiter=';')

# Creating array with all training data
all_training_data = []
all_training_data.append(bazofilowa) #0
all_training_data.append(bialaczka_komorek_wielkojadrzastych) #1
all_training_data.append(chloniak_limfatyczny) #2
all_training_data.append(cytolukemia) #3
all_training_data.append(differentiation_in_part) #4
all_training_data.append(differentiation) #5
all_training_data.append(eozyrofilowa) #6
all_training_data.append(granula_mononuclear) #7
all_training_data.append(granulocylosis) #8
all_training_data.append(granulocyte) #9
all_training_data.append(l2type) #10
all_training_data.append(ltype) #11
all_training_data.append(lymphocytic) #12
all_training_data.append(mielomonocytarna) #13
all_training_data.append(mlemonoblastyczna) #14
all_training_data.append(monoblastyczna) #15
all_training_data.append(monocytarna) #16
all_training_data.append(plazmocytowa) #17
all_training_data.append(subacute_granulocyte) #18
all_training_data.append(wielokapilarnokomorkowa) #19

# first cell - type of lukemia
# second cell - single row from type
# third cell - one value from row
# print(all_training_data[1][2][3])

#Create output array
output_array = []
for x in bazofilowa:
    output_array.append(0)
for x in bialaczka_komorek_wielkojadrzastych:
    output_array.append(1)
for x in chloniak_limfatyczny:
    output_array.append(2)
for x in cytolukemia:
    output_array.append(3)
for x in differentiation_in_part:
    output_array.append(4)
for x in differentiation:
    output_array.append(5)
for x in eozyrofilowa:
    output_array.append(6)
for x in granula_mononuclear:
    output_array.append(7)
for x in granulocylosis:
    output_array.append(8)
for x in granulocyte:
    output_array.append(9)
for x in l2type:
    output_array.append(10)
for x in ltype:
    output_array.append(11)
for x in lymphocytic:
    output_array.append(12)
for x in mielomonocytarna:
    output_array.append(13)
for x in mlemonoblastyczna:
    output_array.append(14)
for x in monoblastyczna:
    output_array.append(15)
for x in monocytarna:
    output_array.append(16)
for x in plazmocytowa:
    output_array.append(17)
for x in subacute_granulocyte:
    output_array.append(18)
for x in wielokapilarnokomorkowa:
    output_array.append(19)
print(output_array)
print(len(output_array))


# lines = open(training_path + 'training_bazofilowa.csv', "r").readlines()
# print(lines)
# Sigmoid Function


# Sigmoid Function Derivative
