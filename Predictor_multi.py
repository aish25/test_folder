from sklearn import svm
import numpy as np
def reading(y,z):
    file_1 = open(y,'r')
    #print(file_1)
    file_2 = file_1.read().splitlines()
    #print(file_2)
    id = []
    sequence = []
    topology = []
    dict_top = {}
    splitting = []
    amino_list =['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
   # dict_2 = {}
    
    for line in file_2:
        #print(line)
        file_3 = line.rsplit('\n')
        for line in file_3:
            if line.startswith('>'):
                d = line.split('>')
                id.append(d)
                
            
            elif line.startswith('M'):
                sequence.append(line)
            else:
                topology.append(line)
                #print(topology)
               #print(len(topology))
        #print(file_3)
    #print(len(sequence[0]))
    #print(len(sequence[1]))
    #print(topology)
    print(id)
    dict_top ={'I':1, 'M':2, 'O':3, 'G':4}
    #rint(top_1)
    new_label = []
    for al in topology:
        splitting= list(al)
        label =[]
        #print(splitting)
        for val in splitting:
            #print(val)
            for key,value in dict_top.items():
                #print(key)
                #print(value)
                if val == key:
                    label.append(value)
        new_label.extend(label)
    #print(new_label)
    #print()
    y = np.array(label)
    #print(y)
    #print(y)
    zero_array = np.zeros(shape=(20,20),dtype=int)
    np.fill_diagonal(zero_array,1)
    #print(zero_array)
    zero_1 = zero_array.tolist()
    #print(zero_1)
    
    dict_con = {}
    for zero_array, acid in zip(zero_1,amino_list):
        dict_con[acid]=zero_array
    #print(dict_con)
    window_size = 3
    pad =int(window_size//2)
   #print(pad)
   # str_seq =','.join(sequence)
    #print(str_seq)
    pad_list = []
    for seq in sequence:
        #print(seq)
        seq_list = []
        new_sequence =(pad*'0'+seq+pad*'0')
        seq_list.append(new_sequence)
        pad_list.extend(seq_list)
    #print(pad_list)
    list_of_window = []
    for element in pad_list:
        #print(element)
        for value in range(0,len(element)):
            #print(value)
             if (value+window_size)<=len(element):
                triple = element[value:value+(window_size)]
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
    #print(x.shape)
    
    file_a = open(z,'r')
    file_2a = file_a.read().splitlines()
    ida = []
    sequencea = []
    topologya = []
    dict_topa = {}
    new_labela = []
    splittinga = []
    amino_lista =['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
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
               
               
        
    #print(len(sequencea[0]))
    #print(len(sequencea[1]))    
    dict_topa ={'I':1, 'M':2, 'O':3, 'G':4}
    
    for al in topologya:
        splittinga= list(al)
        labela = []
        for val in splittinga:
           
            for key,value in dict_topa.items():
               
               
                if val == key:
                    labela.append(value)
        new_labela.extend(labela)
    #print(new_labela)     
   
    y_test = np.array(labela)
   
    zero_arraya = np.zeros(shape=(20,20),dtype=int)
    np.fill_diagonal(zero_arraya,1)
    zero_1a = zero_arraya.tolist()
   
    dict_cona = {}
    for zero_arraya, acid in zip(zero_1a,amino_lista):
        dict_cona[acid]=zero_arraya
   
    window_sizea = 3
    pada=int(window_sizea//2)
   
   # str_seqa =','.join(sequencea)
   
    pada_list = []
    for seqa in sequencea:
        #print(seq)
        seqa_list = []
        new_sequencea =(pada*'0'+seqa+pada*'0')
        seqa_list.append(new_sequencea)
        pada_list.extend(seqa_list)
   # print(pada_list)    
    
   
    list_of_windowa = []
    for element in pada_list:
        #print(element)
        for value in range(0,len(element)):
            #print(value)
             if (value+window_sizea)<=len(element):
                triplea = element[value:value+(window_sizea)]
                list_of_windowa.append(triplea)
            # print(list_of_windowa)
          
    dict_cona.update({'0':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})
    
    #print(dict_cona)
   
    read_windowa = []
    for w in list_of_windowa:
        nw_lista = []
        for alphabet in w:
            for key,value in dict_cona.items():
                if alphabet == key:
                    nw_lista.extend(value)
        read_windowa.append(nw_lista)
   
    x_test= np.array(read_windowa)
    #print(x_test.shape)
    #print(x_test)
  

    
    #classify = svm.SVC()
    #classify.fit(x,y)
    #print(classify.predict(x_test)) # convert the final prediction to topology
    print(x.shape)
    print(y.shape) 
    file_a.close()
    file_1.close()
if __name__ =="__main__":
    reading("seq-data_t.txt","seq-data_t.txt")
    
    


