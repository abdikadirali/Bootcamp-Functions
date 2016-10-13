def words(word):
 
 temp = word.split()
 temp_dict={}
 temp2 =[]
 for i in temp:
   try:
     int(i)
     
   except ValueError:
     temp2.append(i)
   
   else:
     temp2.append(int(i))
 
 for i in temp2:
   temp_dict[i] = temp2.count(i)
     
 return temp_dict