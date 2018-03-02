import numpy as np
def reading(y):
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
    x = np.array(read_window)
    print(x) 
                
        
   
    
    
   #print(label) 
   
  
    
    
   #print(dict_top)
    file_1.close()
if __name__ =="__main__":
    reading("seq-data.txt")    
    
    
