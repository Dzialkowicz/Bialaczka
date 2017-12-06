import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
import scipy.stats as stats
from sklearn.feature_selection import VarianceThreshold
# Input Array
# Output Array
training_path = '/Users/jakubsanecki/Desktop/bialaczka/Bialaczki_dane/'
# Defining CSVs
bazofilowa = np.genfromtxt(training_path + 'training_bazofilowa.csv', delimiter=';') #0 18
bialaczka_komorek_wielkojadrzastych = np.genfromtxt(training_path + 'training_bialaczka_komorek_wielkojadrzastych.csv', delimiter=';') #1 11
chloniak_limfatyczny = np.genfromtxt(training_path + 'training_chloniak_limfatyczny.csv', delimiter=';') #2 13
cytolukemia = np.genfromtxt(training_path + 'training_cytolukemia.csv', delimiter=';') #3 21
differentiation_in_part = np.genfromtxt(training_path + 'training_differentiation_in_part.csv', delimiter=';') #4 13
differentiation = np.genfromtxt(training_path + 'training_differentiation.csv', delimiter=';') #5 22
eozyrofilowa = np.genfromtxt(training_path + 'training_eozyrofilowa.csv', delimiter=';') #6 16
granula_mononuclear = np.genfromtxt(training_path + 'training_granula_mononuclear.csv', delimiter=';') #7 12
granulocylosis = np.genfromtxt(training_path + 'training_granulocylosis.csv', delimiter=';') #8 17
granulocyte = np.genfromtxt(training_path + 'training_granulocyte.csv', delimiter=';') #9 19
l2type = np.genfromtxt(training_path + 'training_l2type.csv', delimiter=';') #10 14
ltype = np.genfromtxt(training_path + 'training_ltype.csv', delimiter=';') #11 19
lymphocytic = np.genfromtxt(training_path + 'training_lymphocytic.csv', delimiter=';') #12 16
mielomonocytarna = np.genfromtxt(training_path + 'training_mielomonocytarna.csv', delimiter=';') #13 12
mlemonoblastyczna = np.genfromtxt(training_path + 'training_mlemonoblastyczna.csv', delimiter=';') #14 17
monoblastyczna = np.genfromtxt(training_path + 'training_monoblastyczna.csv', delimiter=';') #15 15
monocytarna = np.genfromtxt(training_path + 'training_monocytarna.csv', delimiter=';') #16 21
plazmocytowa = np.genfromtxt(training_path + 'training_plazmocytowa.csv', delimiter=';') #17 12
subacute_granulocyte = np.genfromtxt(training_path + 'training_subacute_granulocyte.csv', delimiter=';') #18 11
wielokapilarnokomorkowa = np.genfromtxt(training_path + 'training_wielokapilarnokomorkowa.csv', delimiter=';') #19 11

#data output
data_output = np.genfromtxt(training_path + 'data_output.csv', delimiter=';')
# Creating array with all training data
all_training_data = np.concatenate((bazofilowa, bialaczka_komorek_wielkojadrzastych,
                    chloniak_limfatyczny, cytolukemia, differentiation_in_part, differentiation, eozyrofilowa, granula_mononuclear,
                    granulocylosis, granulocyte, l2type, ltype, lymphocytic, mielomonocytarna, mlemonoblastyczna, monoblastyczna,
                    monocytarna, plazmocytowa, subacute_granulocyte, wielokapilarnokomorkowa))
#print(len(all_training_data))

# first cell - type of lukemia
# second cell - single row from type
# third cell - one value from row
#print(all_training_data)

#Getting feature for Kolomogorow
all_training_data_T = all_training_data.T
#for i in range(20):
print(all_training_data_T[0])
kolomog = stats.kstest(all_training_data_T[0], 'norm')
print(kolomog)
#1. cecha = 0.70586087510080098
#2. 0.63055865981823633
#3. 0.69146246127401312
#4. 0.54973822483011292
#5  0.69146246127401312
#6

output_transposed = data_output.T # transposed output array
output_arr = np.expand_dims(output_transposed, axis = 1) #adding additional dimension so te arrays can be caluclated


#print(output_transposed.shape)
#print(all_training_data.shape)

#How data looks on an image
#plt.matshow(np.hstack((all_training_data, output_arr)), fignum = 1, cmap = plt.cm.gray)
#plt.show()

# Nonlinear Sigmoid Function - needed for training the weights
# Sigmoid Function Derivative - if passed true
def nonlin(x, deriv = False):
    if deriv == True:
        return x*(1-x)
    return 1/(1+np.exp(-x))




#Showing that sigmoid function actually works
#Xaxis = np.arange(-10, 10, 0.5)
#plt.plot(Xaxis, nonlin(Xaxis))
#plt.show()

# Random seed for initial weights values (most primitive method but efficient)
np.random.seed(1)
#Initializing weights
syn0 = 2*np.random.random((20,1)) - 1

# Iterating 10 000 times
for x in range(10000):

    # forward propagation
    first_layer = all_training_data
    # multiplying inputs with given weights
    output_layer = nonlin(np.dot(first_layer, syn0))

    # how big error we have?
    output_layer_error = output_arr - output_layer

    #back propagation
    #multiply how much we missed by slope of the sigmoid derivative -
    output_layer_delta = output_layer_error * nonlin(output_layer, True)

    #updating weights
    syn0 += np.dot(first_layer.T, output_layer_delta)

#print("Output: ")
#print(output_layer)
