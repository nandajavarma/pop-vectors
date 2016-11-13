# from __future__ import print_function
from random_vector_gen import RandomGenerator
from sparse_vec import SparseVector
import re
import sys
from collections import defaultdict
#
#  *
#  * @author Behrang QasemiZadeh <zadeh at phil.hhu.de>
#  


class PoPScript:
    print("init pop script")
    wordVectorMap = {}
    sumUniversalVector = float(0)
    left = 3
    right = 3
    dimension = 666
    randomIndexInfo = {}
    rg = RandomGenerator(dimension)
    print("init done")

    #
    #      * Get index vector info
    #      *
    #      * @param word
    #      * @return
    #      
    def getIndexVectorInfo(self, word):
        """ generated source for method getIndexVectorInfo """
        if word in self.randomIndexInfo:
            return self.randomIndexInfo[word]
        else:
            popIndex = self.rg.get_random_pop_index()
            self.randomIndexInfo[word] = popIndex
            return popIndex

    def train(self, file):
        print('training data from ' + str(file))
        try:
            with open(file, 'r') as f:
                for line in f:
                    #sys.stdout.write(line)
                    tokens = re.split('\W+', line)
                    j = 0
                    while j < len(tokens):
                        target_word = tokens[j]
                        context_vector = None
                        if target_word in self.wordVectorMap:
                            context_vector = self.wordVectorMap[target_word]
                        #    context_vector.incFrequency()
                        else:
                            context_vector = SparseVector(self.dimension)
                         #   context_vector.incFrequency()
                        k = max(0, j - self.left)
                        while k < j:
                            context_word = tokens[k]
                            self.addIndexVector(context_word, context_vector)
                            k += 1
                        k = j + 1
                        while k < min(j + self.right, len(tokens)):
                            context_word = tokens[k]
                            self.addIndexVector(context_word, context_vector)
                            k += 1
                        j += 1
                        self.wordVectorMap[target_word] = context_vector
        except IOError as e:
            print e.__str__()

    def addIndexVector(self, index_word, context_vector):
        indexInfo = self.getIndexVectorInfo(index_word)
        coordinate = indexInfo[0]
        value = indexInfo[1]
        context_vector.inc_value(coordinate, value)

    def serializeRawVectors(self, filename):
        file = open(filename, "w")
        for word in self.wordVectorMap:
            vec = self.wordVectorMap[word]
            stringVec = vec.__str__;
            file.write(word + " " + stringVec + '\n')
        file.close()

    def serialize_and_ppmi_weighting_vectors(self, filename):
        sum_vector = SparseVector(self.dimension)
        for word in self.wordVectorMap:
            vec = self.wordVectorMap[word]
            sum_vector.addVector(vec)
        file = open(filename, "w")
        for word in self.wordVectorMap:
            vec = self.wordVectorMap[word]
            ppmiVec = vec.getPPMIDouble(sum_vector)
            file.write(word + " " + ppmiVec.__str__+'\n')
        file.close()


def main():
    import time
    start_time = time.time()
    popscript = PoPScript()
    print("Context size is " + str(popscript.left) + "+" + str(popscript.right))
    popscript.train("data/text8.txt")
    popscript.serializeRawVectors('output/simple-pop-vec')
    popscript.serialize_and_ppmi_weighting_vectors('pop-ppmi-vec')
    end_time = time.time()
    print("Elapsed time was %g seconds" % (end_time - start_time))




if __name__ == '__main__':
    main()
