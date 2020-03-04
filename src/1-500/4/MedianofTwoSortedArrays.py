class Solution:
        
    def mediansingle(self, onelist):
        l = len(onelist)
        index = l//2
        median = onelist[index] if (l%2) \
                    else (onelist[index] + onelist[index-1])/2
        return median
    
    def medianodd(self):
        indexa = self.indexx
        indexb = (self.la+self.lb+1)//2-indexa
        print(f"{self.lbound}\t{indexa}\t{self.hbound}\t{self.la}\t{indexb}")
        if (indexa and indexa != self.la):
            if (self.lista[indexa-1] <= self.listb[indexb]) \
                and (self.listb[indexb-1] <= self.lista[indexa]):
                return max(self.lista[indexa-1], self.listb[indexb-1])
            else:
                if (self.lista[indexa-1] > self.listb[indexb]):
                    self.hbound = indexa
                    self.indexx = (indexa+self.lbound+1)//2
                    return self.medianodd()
                else:
                    self.lbound = indexa
                    self.indexx = (indexa+self.hbound+1)//2
                    return self.medianodd()
        elif (indexa == self.la):
            if (self.lista[indexa-1] <= self.listb[indexb]):
                return max(self.lista[indexa-1], self.listb[indexb-1])
        else:
            if (self.listb[indexb-1] <= self.lista[indexa]):
                return self.listb[indexb-1]
            else:
                self.lbound = indexa
                self.indexx = (indexa+self.hbound+1)//2
                return self.medianodd()
        
    def medianeven(self):
        indexa = self.indexx
        indexb = (self.la+self.lb)//2-indexa
        print(f"{self.lbound}\t{indexa}\t{self.hbound}\t{self.la}\t{indexb}")
        if (indexa and indexa != self.la):
            if (self.lista[indexa-1] <= self.listb[indexb]) \
                and (self.listb[indexb-1] <= self.lista[indexa]):
                return (max(self.lista[indexa-1], self.listb[indexb-1])+\
                        min(self.lista[indexa], self.listb[indexb]))/2
            else:
                if (self.lista[indexa-1] > self.listb[indexb]):
                    self.hbound = indexa
                    self.indexx = (indexa+self.lbound+1)//2
                    return self.medianeven()
                else:
                    self.lbound = indexa
                    self.indexx = (indexa+self.hbound+1)//2
                    return self.medianeven()
        elif (indexa == self.la):
            if (not indexb and self.lista[indexa-1] <= self.listb[indexb]):
                return (self.lista[indexa-1]+self.listb[indexb])/2
            elif (self.lista[indexa-1] <= self.listb[indexb]):
                 return (max(self.lista[indexa-1], self.listb[indexb-1])+\
                        self.listb[indexb])/2
            else:
                self.hbound = indexa
                self.indexx = (indexa+self.lbound+1)//2
                return self.medianeven()
        else:
            if (indexb == self.lb and self.listb[indexb-1] <= self.lista[indexa]):
                return (self.lista[indexa]+self.listb[indexb-1])/2
            elif (self.listb[indexb-1] <= self.lista[indexa]):
                return (min(self.lista[indexa], self.listb[indexb])+\
                       self.listb[indexb-1])/2
            else:
                self.lbound = indexa
                self.indexx = (indexa+self.hbound+1)//2
                return self.medianeven()
            
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.lista, self.listb = (nums1, nums2) if (len(nums1) <= len(nums2)) \
                                else (nums2, nums1)
        self.la, self.lb = len(self.lista), len(self.listb)
        self.indexx = 0
        self.lbound, self.hbound = 0, self.la
        if not self.lista:
            indexb = self.lb//2
            median = self.mediansingle(self.listb)
            return median
        else:
            if ((self.la+self.lb)%2):
                return self.medianodd()
            else:
                return self.medianeven()
        
