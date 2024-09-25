import ctypes
from mapper import Mapper
import random

class RandomMapper(Mapper):

    def mapping_fn(self, *args, rand=random.randint, **kwargs): 
        '''
        mapper_fn
        Random Map
        '''
        FLAG = ctypes.c_int32(-1) 
        ctypes.memset(self.map, FLAG, 4 * self.n_elements)
        n_set = 0
        FLAG = int.from_bytes(FLAG, signed=True)
        # Not a good implementation, 
        while n_set < self.n_elements:
            idx = rand(0, self.n_elements - 1)
            if self[idx] == FLAG: 
                self[idx] = n_set
                n_set += 1
