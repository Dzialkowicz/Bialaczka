import numpy as np
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

# lines = open(training_path + 'training_bazofilowa.csv', "r").readlines()
# print(lines)
# Sigmoid Function


# Sigmoid Function Derivative
