# Start with an empty array

array = [] 


# Function to sort for the biggest element in the array

def max_array(array):
  
  # Setting the first element as a point of comparison
  
  max = array[0]
  
  # The sorting algorithm
  
  for i in range(0,len(array)):
    if array[i] > max:
      max = array[i]
    
  return max
  
  
# User input to fill the array

choice = "y"

while True:
  
  
  
  if choice == "y":
    user_input = int(input("Enter a number to app to the array: "))
    array.append(user_input)
    choice = input("Do you wish to continue y/n : ")
    
  else:
    break


# Initiating the function  

print(max_array(array))
