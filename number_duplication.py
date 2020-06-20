#program to seperate the duplicate items and no duplicate items in the given list and to display the count
lst1 = [1,2,3,4,5,6,2,1,5,6,7,8,4,12,11,10,5,5,5,1,1,2,8]
no_duplicates=[]
duplicate_items=[]
print ("Original list is : ",lst1) 
lst1.sort()
print("After Sorting : ",lst1)
duplicate_count = []
dup_count =0
for i in range(len(lst1)):
    if(i==0):
        no_duplicates.append(lst1[i])
    else:
        if lst1[i] not in no_duplicates:
            if(dup_count!=0):
               duplicate_count.append(dup_count)
            dup_count = 0
            no_duplicates.append(lst1[i])
        else:
            dup_count+= 1
            if lst1[i] not in duplicate_items :
                duplicate_items.append(lst1[i])
                
print("no-Duplicate list and duplictes-list") 
print(no_duplicates,duplicate_items,sep='\n')
print("count of duplicates is : ")
print(tuple(zip(duplicate_items,duplicate_count)))
print("no change in the list after the program and the original sorted list is : \n",lst1)
