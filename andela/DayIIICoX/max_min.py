def find_max_min (numbers):
  
  for items in numbers:
    
    if min(numbers) != max(numbers):
      
      return [min(numbers), max(numbers)]
      
    else:
      
      return [len(numbers)]