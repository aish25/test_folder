from sklearn import svm
import numpy as np
def reading(y):
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
                #topology.remove('')
                #print(topology)
               #print(len(topology))
        #print(file_3)
    #print(len(sequence[0]))
    #print(len(sequence[1]))
    #print(topology)
    #print(sequence)
    #print(id)
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
   # print(new_label)
    #print()
    y = np.array(new_label)
    print(y)
    #print(y)
    #print(y.shape)
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
    print(read_window)
    x= np.array(read_window)
    #print(x)
    print(x.shape)
    print(y.shape)
    #classify = svm.SVC()
    #classify.fit(x,y)
    #print(classify.predict(x))
    file_1.close()
if __name__ =="__main__":
    reading("data.txt")
"""
Spyder Editor

This is a temporary script file.
"""

