class BinarySearch(object):

    def __init__(self,a,b):
        super(BinarySearch, self).__init__()
        self.a = a
        self.b = b

    def search(self, length):
      start, end = 0, len(l)-1
   
      while start <= end:
          mid = (start + end) / 2
          if l[mid] == length:
              return mid
          elif l[mid] < length:
              start = mid + 1
          else:
              end = mid - 1
      return -1