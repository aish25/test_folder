from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import numpy as np
#import binary as te
def read(y):
    
    #print(test)
    file_1 = open(y,'r')
    file_2 = file_1.read().splitlines()
    ids = []
    sequence = []
    topology = []
    dict_top = {}
    splitting = []
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
   
    y = np.array(new_label)
    
    
    #print(y.shape)
    zero_array = np.zeros(shape=(20,20),dtype=int)
    np.fill_diagonal(zero_array,1)
    zero_1 = zero_array.tolist()
    
    
    dict_con = {}
    for zero_array, acid in zip(zero_1,amino_list):
        dict_con[acid]=zero_array
    scores = 0
   
    #print (dict_con)
   
    for window_size in range(3,51,2):
        print(window_size)
        pad =int(window_size//2)
        
        pad_list = []
        #seq_list = []
        for seq in sequence:
            new_sequence =(pad*'0'+seq+pad*'0')
            pad_list.append(new_sequence)
        #pad_list.extend(seq_list)
        #print(pad_list)    
        list_of_window = []
        for element in pad_list:
            for value in range(0,len(element)):
                if (value+window_size)<=len(element):
                    triple = element[value:value+(window_size)]
                    list_of_window.append(triple)
                 
             
        dict_con.update({'0':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})
        #print(list_of_window)
        read_window = []
        for w in list_of_window:
              #print(w)  
              nw_list = []
              for alphabet in w:
                  for key,value in dict_con.items():
                      if alphabet == key:
                           nw_list.extend(value)
              read_window.append(nw_list)
              #print(read_window)    
        x= np.array(read_window)
        #print(x.shape)
        #print(y.shape)
        SVM = svm.SVC()
        scores = cross_val_score(SVM,x,y)
        max_score = max(scores)
        print("scores:",window_size, max_score)
        parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],'C': [1, 10, 100, 1000]},{'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]
        search = GridSearchCV(SVM,parameters)
        search.fit(x,y)
        #print(sorted(search.cv_results_.keys()))
        print("The best parameters found:")
        print(search.best_params_)
    #print(read_window)
    
    #test = te.reading("test.txt")
    #print(test)
    
    #print(test.shape)
    #print(x.shape)
    #print(y.shape)
    
    #classify.fit(x,y)
    #c = classify.predict(test)
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
           # top_predict.extend(c)
    #print(top_predict)
    #print(c)
    #print(x,y)
    
       
         
    #file_1.close()
if __name__ =="__main__":
    read("seq-data.txt")
    
