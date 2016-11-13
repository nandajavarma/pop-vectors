#!/usr/bin/env python

from __future__ import print_function
import random
import array
# 
#  * To change this license header, choose License Headers in Project Properties.
#  * To change this template file, choose Tools | Templates
#  * and open the template in the editor.
#  
# 
#  *
#  * @author Behrang QasemiZadeh <zadeh at phil.hhu.de>
#  * PoP random vector generator: note that using random vectors with more than
#  * <b>one</b> non-zero elements is also possible. However, if using random index
#  * vectors with more than one-zero elements is not desirable due to the imposed
#  * computational complexity.
#

class RandomGenerator(object):
    """ generated source for class RandomGenerator """
    reducedDimension = int()

    def __init__(self, reducedDimension):
        """ generated source for method __init__
        :rtype: object
        """
        self.reducedDimension = reducedDimension
       

    # 
    #      * Get the next element of index vectors that will be non-zero randomly
    #      *
    #      * @return
    #      
    #def getNextRandomIndexElement(self):
     #   """ generated source for method getNextRandomIndexElement """
      #  l = int(self.randomElement.nextInt(self.reducedDimension))
      #  return l

    # 
    #      * Get atomic Positive-Only-Random Vector packed in 32bits
    #      *
    #      * @return
    #      
    #def getPositiveOnlyRandomVector(self):
     #   """ generated source for method getPositiveOnlyRandomVector """
      #  val = int(floor(1.0 / pow(self.randomValuePositive.nextDouble(), 0.7)))
       # index = int(self.getNextRandomIndexElement())
       # l = ((index) << 16) | (val & 0xffff)
       # return l

    def get_random_pop_index(self):
       index = random.randint(0,self.reducedDimension)
       val =  int(1 // pow(random.uniform(0,1), 0.7))
       index_value= array.array('i',[index,val])
       return index_value
        # return [None] * 

    # 
    #      * Get dimensionality from packed data
    #      * @param packedData
    #      * @return 
    #      
   # def getDim(self, packedData):
    #    """ generated source for method getDim """
     #   return packedData >> 16

    # 
    #      * Get value from packed data
    #      * @param packedData
    #      * @return 
    #      
    #def getValue(self, packedData):
     #   """ generated source for method getValue """
      #  return packedData & 0xFFFF

   



