#!/usr/bin/env python

from __future__ import print_function
import numpy as np




class SparseVector:

    LABEL_DELIMIT = "\t\t"
    VECTOR_IND_VLU_DELIMIT = ":"
    DIM_DELIMITER = " "

    def __init__(self, dimensionality):
        # type: (object) -> object
        """

        :rtype: object
        """

        self.dense = []
        self.vector = {}
        self.dimensionality = dimensionality
    
    def initFromVectro(self, vec):
        self.vector = {}
        for i in xrange(len(vec)):
            self.vector[i] = vec[i]

    @property
    def __str__(self):
        sb = ""
        #keys = self.vector.keys()
        for key in self.vector:
            if self.vector[key]!=0:
                sb += str(key) + self.VECTOR_IND_VLU_DELIMIT + str(self.vector[key])+self.DIM_DELIMITER
        return sb.rstrip()

    def incFrequency(self):
        self.frequency += 1


    def get_frequency(self):
        return self.frequency

    def addVector(self, v):
        for i in v.vector:
            elementvalue = self.getValue(i) + v.vector[i]
            self.vector[i] = elementvalue

    @classmethod
    def fromStringSparse(cls, line, dim):
        """ generated source for method fromStringSparse 
        :type line: object
        """
        sv = SparseVector(dim)
        splitLine = line.split(cls.DIM_DELIMITER)
        i = 0
        for vecbit in splitLine:
            splitBit = vecbit.split(cls.VECTOR_IND_VLU_DELIMIT)
            index = int(splitBit[0])
            value = float(splitBit[1])
            sv.setValue(index, value)
            i += 1
        return sv

    @classmethod
    def fromStringDense(cls, line, dim):
        """ generated source for method fromStringDense """
        dense = [None] * dim
        splitLine = line.split(cls.DIM_DELIMITER)
        i = 0
        while i < dim:
            dense[i] = float(splitLine[i])
            if np.isnan(dense[i]) or np.isinf(dense[i]):
                raise Exception("There is some error in the input file at dim " + i + " in line ")
            i += 1
        return dense

    def convertToPPMIDouble(self, ssAll):
        """ generated source for method convertToPPMIDouble """
        sumAll = ssAll.getSum()
        sumThisRow = self.getSum()
        pmiVec = float()
        idx = 0
        while idx < self.dimensionality:
            pmi = np.log((self.getValue(idx) * sumAll) / (sumThisRow * ssAll.getValue(idx)))
            pmiVec = max(0, pmi)
            if np.isinf(pmiVec):
                pmiVec = 0xFFFF
            elif np.isnan(pmiVec):
                    pmiVec = 0
            self.vector[idx] = pmiVec
            idx += 1

    def getPPMIDouble(self, ssAll):
        """ generated source for method getPPMIDouble 
        :rtype: SparseVector
        """
        sum_all = ssAll.getSum()
        sumThisRow = self.getSum()

        pmi_vec = SparseVector(self.dimensionality)
        idx = 0
        while idx < self.dimensionality:
            pmi = 0.0
            enum = sumThisRow * ssAll.getValue(idx)
            if enum != 0:
                exp_pmi = np.divide(self.getValue(idx) * sum_all, enum);
                if exp_pmi != 0:
                    pmi = np.log(exp_pmi)
            # if np.isinf(pmi):
            #     pmi= 0xFFFF
            # elif np.isnan(pmi):
            #     pmi = 0
            pmi_vec.vector[idx] = max(0.0, pmi)
            idx += 1
        return pmi_vec

    def set_value(self, index, value):
        self.vector[index] = value

    def inc_value(self, index, value):
        """
        :param index: index of vector
        :param value:  assigned value to it
        :return:
        """
        if index in self.vector:
            newvalue = self.vector[index]
            self.vector[index] = newvalue + value
        else:
            self.vector[index] = value
        

    def getValue(self, index):
        """ generated source for method getValue """
        if index in self.vector:
            get = self.vector[index]
            return get
        else:
            return 0

    # def getIndices(self):
    #     """ generated source for method getIndices """
    #     return self.vector.keys()

    def getSum(self):
        """ generated source for method getSum """
        sum = 0
        for value in self.vector.values():
            sum += value
        return sum

