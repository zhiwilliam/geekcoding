class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings: return []

        all = []
        for x,y,z in buildings:
            all += [(x, -z),( y, z)]

        all.sort( ) #key = lambda x: ( x[0], abs(x[1])))

        ret = []
        heights = [0]
        pre_x = 0
        pre_y = 0
        for x,y  in all:
            if y < 0 : # left edge 
                heights.append(-y)
            else:
                heights.remove(y)

            current_height = max(heights) 

            # print('pre:({},{}), x,y = {},{}, heights:{}, currentHight:{}'.format(
            #     pre_x, pre_y, x, y, heights,current_height) )

            if  pre_y != current_height  : 
                ret.append([x, current_height])
                pre_y = current_height
                pre_x = x 

        return ret     


