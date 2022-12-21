# FILENAME binsearch.py in the main.py
# First Last: Jerusha Theobald
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 


def binary_search(item_list,item):
  
	first = 0
	last = len(item_list)-1
	found = False
  
	while( first<=last and not found):
		mid = (first + last)//2
    
		if item_list[mid] == item :
			found = True
      
		else:
			if item < item_list[mid]:
				last = mid - 1
        
			else:
				first = mid + 1	
        
	return found
	
print(binary_search([20, 40, 60, 80, 100], 20))
print(binary_search([30, 50, 70, 90, 110, 130], 40))
