class CircularArray:
    def __init__(self,array):
        self.array=array
        self.root=0

    def index_rotate(self,index):
        index += len(array)
        return (self.root + index) % len(array)

    def rotate(self,shift):
        self.root=index_rotate(shift)

    def set(self, index, item):
        self.array[index_rotate(index)] = item

class Iterator:
    def __init__(self):
        self.current=-1

    def array_iterator(self,array):
        pass

    def next(self,array):
     self.current+=1
     return array[convert(self.current)]

