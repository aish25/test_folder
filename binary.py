from sklearn import svm
import numpy as np
#import Predict as pr



def reading(y):
    file_1 = open(y,'r')
    file_2 = file_1.read().splitlines()
    ids = []
    sequence = []
    topology = []
    #dict_top = {}
    #splitting = []
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

  
    zero_array = np.zeros(shape=(20,20),dtype=int)
    np.fill_diagonal(zero_array,1)
    zero_1 = zero_array.tolist()
    
    
    dict_con = {}
    for zero_array, acid in zip(zero_1,amino_list):
        dict_con[acid]=zero_array
    for window_size in range(3,50):
        pad =int(window_size//2)
        pad_list = []
        for seq in sequence:
            seq_list = []
            new_sequence =(pad*'0'+seq+pad*'0')
            seq_list.append(new_sequence)
            pad_list.extend(seq_list)
        list_of_window = []
        for element in pad_list:
            for value in range(0,len(element)):
                if (value+window_size)<=len(element):
                    triple = element[value:value+(window_size)]
                    list_of_window.append(triple)
        #print(list_of_window)      
    dict_con.update({'0':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})
    
    read_window = []
    for w in list_of_window:
        nw_list = []
        for alphabet in w:
            for key,value in dict_con.items():
                if alphabet == key:
                    nw_list.extend(value)
        read_window.append(nw_list)
    #print(read_window)
    #x= np.array(read_window)
    x_test = np.array(read_window)
    print(x_test.shape)
    return(x_test)
    
    #file_1.close()
if __name__ =="__main__":
    reading("test.txt")
    
    
