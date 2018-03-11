

from sklearn import svm
import numpy as np
from sklearn.externals import joblib
import model as ref
def reading(y):
    file_1 = open(y,'r')
    file_2 = file_1.read().splitlines()
    
    sequence = []
    ids =[]
    amino_list =['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
    i=0
    for line in file_2:
        if line.startswith('>'):
             d = line.split('>')
             ids.append(d)
             sequence.append(file_2[i+1])
             
             i=i+1
        else:
             i=i+1
         
    for index in range(len(sequence)):
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
        
        for seq in [sequence[index]]:
            #seq_list = []
            new_sequence =(pad*'0'+seq+pad*'0')
            #seq_list.append(new_sequence)
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
        model = ref.read("seq-data.txt")
        model =joblib.load('filename.pkl') 
        c = model.predict(x_test)
        top_predict = []
        for i in c:
            if (i == 1):
                d = 'I'
                top_predict.extend(d)
            elif (i == 2):
                a = 'M'
                top_predict.extend(a)
            elif (i == 3):
                b =  'O'
                top_predict.extend(b)
            elif (i == 4):
                c = 'G'
                top_predict.extend(c)
    for i in range(len(ids)):               
      for j in range(len(sequence)):  
          if i==j:             
            print(ids[i])
            print(sequence[j])
    print(top_predict)
        
            
    
        #file_1.close()
if __name__ =="__main__":
    reading("testing.txt")
    
    
