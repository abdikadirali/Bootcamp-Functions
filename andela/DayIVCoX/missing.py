def find_missing(first, second):
  
    len_first = len(first)
    len_second = len(second)
    
    if len_first == len_second:
        return 0
    else:
        for i in second:
            if i not in first:
                return i