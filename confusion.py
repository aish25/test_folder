from sklearn import svm
import numpy as np
from sklearn.externals import joblib
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import model as ref
np.set_printoptions(threshold=np.nan)
def reading(y):
    file_1 = open(y,'r')
    file_2 = file_1.read().splitlines()
    sequence = []
    topology = []
    ids =[]
    amino_list =['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
    i=0
    for line in file_2:
        if line.startswith('>'):
             d = line.split('>')
             ids.append(d)
             sequence.append(file_2[i+1])
             topology.append(file_2[i+2])
             
             i=i+1
        else:
             i=i+1
    dict_top ={'I':1, 'M':2, 'O':3, 'G':4}
    new_label = []
    for al in topology:
        splitting= list(al)
        label =[]
        for val in splitting:
            for key,value in dict_top.items():
                
                if val == key:
                    label.append(value)
        new_label.extend(label)
   
    y_test = np.array(new_label)         
    
    zero_array = np.zeros(shape=(20,20),dtype=int)
    np.fill_diagonal(zero_array,1)
    zero_1 = zero_array.tolist()
    dict_con = {}
    for zero_array, acid in zip(zero_1,amino_list):
        dict_con[acid]=zero_array
    dict_con.update({'0':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})
    window_size = 5
    pad =int(window_size//2)
    pad_list = []
        
    for seq in sequence:
            new_sequence =(pad*'0'+seq+pad*'0')
            pad_list.append(new_sequence)
    list_of_window = []
    for element in pad_list:
        for value in range(0,len(element)):
            
                if (value+window_size)<=len(element):
                    triple = element[value:value+(window_size)]
                    list_of_window.append(triple)
    read_window = []
    for w in list_of_window:
        nw_list = []
        for alphabet in w:
            for key,value in dict_con.items():
                    if alphabet == key:
                        nw_list.extend(value)
        read_window.append(nw_list)
    x_test = np.array(read_window)
    print(x_test.shape)
    print(y_test.shape)
    model = ref.read("seq-data_t.txt")
    model =joblib.load('filename.pkl')
    print(y_test)
    c = model.predict(x_test)
    y= ref.read("seq-data_t.txt")
    m = confusion_matrix(c, y_test)
    print(m)
    plt.matshow(m)
    plt.colorbar()
    plt.title("confusion matrix")
    plt.xticks(y)
    plt.yticks(y_test)
    plt.ylabel('predicted')
    plt.xlabel('true')
    plt.show()    
        #top_predict = []
        #for i in c:
         #   if (i == 1):
          #      d = 'I'
           #     top_predict.extend(d)
            #elif (i == 2):
             #   a = 'M'
              #  top_predict.extend(a)
            #elif (i == 3):
             #   b =  'O'
              #  top_predict.extend(b)
            #elif (i == 4):
             #   c = 'G'
              #  top_predict.extend(c)
    #print(top_predict)
             
    
        
if __name__ =="__main__":
    reading("data1.txt")
    
    
