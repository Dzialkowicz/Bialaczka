import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
# Input Array
# Output Array
training_path = '/Users/jakubsanecki/Desktop/bialaczka/Bialaczki_dane/'
# Defining CSVs
bazofilowa = np.genfromtxt(training_path + 'training_bazofilowa.csv', delimiter=';') #0
bialaczka_komorek_wielkojadrzastych = np.genfromtxt(training_path + 'training_bialaczka_komorek_wielkojadrzastych.csv', delimiter=';') #1
chloniak_limfatyczny = np.genfromtxt(training_path + 'training_chloniak_limfatyczny.csv', delimiter=';') #2
cytolukemia = np.genfromtxt(training_path + 'training_cytolukemia.csv', delimiter=';') #3
differentiation_in_part = np.genfromtxt(training_path + 'training_differentiation_in_part.csv', delimiter=';') #4
differentiation = np.genfromtxt(training_path + 'training_differentiation.csv', delimiter=';') #5
eozyrofilowa = np.genfromtxt(training_path + 'training_eozyrofilowa.csv', delimiter=';') #6
granula_mononuclear = np.genfromtxt(training_path + 'training_granula_mononuclear.csv', delimiter=';') #7
granulocylosis = np.genfromtxt(training_path + 'training_granulocylosis.csv', delimiter=';') #8
granulocyte = np.genfromtxt(training_path + 'training_granulocyte.csv', delimiter=';') #9
l2type = np.genfromtxt(training_path + 'training_l2type.csv', delimiter=';') #10
ltype = np.genfromtxt(training_path + 'training_ltype.csv', delimiter=';') #11
lymphocytic = np.genfromtxt(training_path + 'training_lymphocytic.csv', delimiter=';') #12
mielomonocytarna = np.genfromtxt(training_path + 'training_mielomonocytarna.csv', delimiter=';') #13
mlemonoblastyczna = np.genfromtxt(training_path + 'training_mlemonoblastyczna.csv', delimiter=';') #14
monoblastyczna = np.genfromtxt(training_path + 'training_monoblastyczna.csv', delimiter=';') #15
monocytarna = np.genfromtxt(training_path + 'training_monocytarna.csv', delimiter=';') #16
plazmocytowa = np.genfromtxt(training_path + 'training_plazmocytowa.csv', delimiter=';') #17
subacute_granulocyte = np.genfromtxt(training_path + 'training_subacute_granulocyte.csv', delimiter=';') #18
wielokapilarnokomorkowa = np.genfromtxt(training_path + 'training_wielokapilarnokomorkowa.csv', delimiter=';') #19

# Creating array with all training data
#print(len(bazofilowa))
all_training_data = np.concatenate((bazofilowa, bialaczka_komorek_wielkojadrzastych,
                    chloniak_limfatyczny, cytolukemia, differentiation_in_part, differentiation, eozyrofilowa, granula_mononuclear,
                    granulocylosis, granulocyte, l2type, ltype, lymphocytic, mielomonocytarna, mlemonoblastyczna, monoblastyczna,
                    monocytarna, plazmocytowa, subacute_granulocyte, wielokapilarnokomorkowa))
#print(len(all_training_data))


# Creating array with all training data
# all_training_data = np.array([])
# all_training_data.np.append(bazofilowa) #0
# all_training_data.append(bialaczka_komorek_wielkojadrzastych) #1
# all_training_data.append(chloniak_limfatyczny) #2
# all_training_data.append(cytolukemia) #3
# all_training_data.append(differentiation_in_part) #4
# all_training_data.append(differentiation) #5
# all_training_data.append(eozyrofilowa) #6
# all_training_data.append(granula_mononuclear) #7
# all_training_data.append(granulocylosis) #8
# all_training_data.append(granulocyte) #9
# all_training_data.append(l2type) #10
# all_training_data.append(ltype) #11
# all_training_data.append(lymphocytic) #12
# all_training_data.append(mielomonocytarna) #13
# all_training_data.append(mlemonoblastyczna) #14
# all_training_data.append(monoblastyczna) #15
# all_training_data.append(monocytarna) #16
# all_training_data.append(plazmocytowa) #17
# all_training_data.append(subacute_granulocyte) #18
# all_training_data.append(wielokapilarnokomorkowa) #19



# first cell - type of lukemia
# second cell - single row from type
# third cell - one value from row
print(all_training_data)

#Create output array
output_array = np.array([])
for x in bazofilowa:
    output_array.np.append(0)
for x in bialaczka_komorek_wielkojadrzastych:
    output_array.np.append(1)
for x in chloniak_limfatyczny:
    output_array.np.append(2)
for x in cytolukemia:
    output_array.np.append(3)
for x in differentiation_in_part:
    output_array.np.append(4)
for x in differentiation:
    output_array.np.append(5)
for x in eozyrofilowa:
    output_array.np.append(6)
for x in granula_mononuclear:
    output_array.np.append(7)
for x in granulocylosis:
    output_array.np.append(8)
for x in granulocyte:
    output_array.np.append(9)
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
# print(output_array)
# print(len(output_array))

output_transposed = output_array.T # transposed output array

plt.matshow(np.hstack((all_training_data, output_transposed)), fignum-10, cmap-plt.cm.gray)
plt.show()
# lines = open(training_path + 'training_bazofilowa.csv', "r").readlines()
# print(lines)
# Sigmoid Function


# Sigmoid Function Derivative
