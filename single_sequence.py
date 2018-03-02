from sklearn import svm
import numpy as np
def reading(y,z):
    file_1 = open(y,'r')
    file_2 = file_1.read().splitlines()
    id = []
    sequence = []
    topology = []
    dict_top = {}
    label = []
    splitting = []
    amino_list =['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
    dict_2 = {}
    for line in file_2:
        file_3 = line.rsplit('\n')
        for line in file_3:
            if line.startswith('>'):
                d = line.split('>')
                id.append(d)
               #print(id)
            elif line.startswith('M'):
                sequence.append(line)
               #print(sequence)
            else:
                topology.append(line)
               #print(topology)
               #print(len(topology))
        #print(file_3)
        
    dict_top ={'I':1, 'M':2, 'O':3}
    #rint(top_1)
    for al in topology:
        splitting= list(al)
       #print(splitting)
        for val in splitting:
           #print(val)
            for key,value in dict_top.items():
               #print(key)
               #print(value)
                if val == key:
                    label.append(value)
   #print(label)
    y = np.array(label)
   #print(y)
    zero_array = np.zeros(shape=(20,20),dtype=int)
    np.fill_diagonal(zero_array,1)
    zero_1 = zero_array.tolist()
   #print(zero_1)
    dict_con = {}
    for zero_array, acid in zip(zero_1,amino_list):
        dict_con[acid]=zero_array
   #print(dict_con)
    window_size = 3
    pad =int(window_size//2)
   #print(pad)
    str_seq =','.join(sequence)
   #print(str_seq)
    new_sequence =(pad*'0'+str_seq+pad*'0')
    #ew_sequence = ('0'+sequence+'0')
   #print(new_sequence)
    list_of_window = []
    for value in range(0,len(new_sequence)):
       if (value+window_size)<=len(new_sequence):
           triple = new_sequence[value:value+(window_size)]
           list_of_window.append(triple)
          #print(list_of_window)
    dict_con.update({'0':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})
   #print(dict_con)
    read_window = []
    for w in list_of_window:
        nw_list = []
        for alphabet in w:
            for key,value in dict_con.items():
                if alphabet == key:
                    nw_list.extend(value)
            read_window.append(nw_list)
   #print(read_window)
    x= np.array(read_window)
   #print(x)
  

    file_a = open(z,'r')
    file_2a = file_a.read().splitlines()
    ida = []
    sequencea = []
    topologya = []
    dict_topa = {}
    labela = []
    splittinga = []
    amino_lista =['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
    dict_2a = {}
    for line in file_2a:
        file_3a = line.rsplit('\n')
        for line in file_3a:
            if line.startswith('>'):
                d = line.split('>')
                ida.append(d)
               
            elif line.startswith('M'):
                sequencea.append(line)
               
            else:
                topologya.append(line)
               
               
        
        
    dict_topa ={'I':1, 'M':2, 'O':3}
    
    for al in topologya:
        splittinga= list(al)
       
        for val in splittinga:
           
            for key,value in dict_topa.items():
               
               
                if val == key:
                    labela.append(value)
   
    y_test = np.array(labela)
   
    zero_arraya = np.zeros(shape=(20,20),dtype=int)
    np.fill_diagonal(zero_arraya,1)
    zero_1a = zero_arraya.tolist()
   
    dict_cona = {}
    for zero_arraya, acid in zip(zero_1a,amino_lista):
        dict_cona[acid]=zero_arraya
   
    window_sizea = 3
    pada=int(window_sizea//2)
   
    str_seqa =','.join(sequencea)
   
    new_sequencea =(pada*'0'+str_seqa+pada*'0')
    
   
    list_of_windowa = []
    for value in range(0,len(new_sequencea)):
       if (value+window_sizea)<=len(new_sequencea):
           triplea = new_sequencea[value:value+(window_sizea)]
           list_of_windowa.append(triplea)
          
    dict_cona.update({'0':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})
   
    read_windowa = []
    for w in list_of_windowa:
        nw_lista = []
        for alphabet in w:
            for key,value in dict_cona.items():
                if alphabet == key:
                    nw_lista.extend(value)
            read_windowa.append(nw_lista)
   
    x_test= np.array(read_windowa)
    classify = svm.SVC()
    classify.fit(x,y)
    classify.predict(x_test)
    file_a.close()
    file_1.close()
if __name__ =="__main__":
    reading("seq-data.txt","test.txt")
    
    


