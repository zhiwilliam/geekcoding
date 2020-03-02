class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # excpetion handle 
        if len(points) <= 2:
            return len(points)

        lines = {}
        points.sort()

        for p0 in range(len(points)-1):
            x0, y0  = points[p0]
            for p1 in range(p0+1, len(points)):
                # x1,y1 in points[p0 + 1:]:
                x1, y1  = points[p1] # [0],p[1]
                if x1 == x0:
                    x = x1
                    y = 0 
                    dx = 0
                    dy = 1  
                elif y1 == y0:
                    y = y1 
                    x = 0 
                    dx = 1
                    dy = 0 
                else:
                    x,y = x0 , y0
                    gcd = math.gcd( y1 -y0, x1 - x0)
                    dx = (x1 - x0)//gcd
                    dy = (y1 - y0)//gcd 
                    
                if ( x,y,dx, dy ) in lines:
                    lines[(x,y,dx,dy )].add(p0)
                    lines[(x,y,dx,dy )].add(p1)
                else:
                    lines[(x,y,dx, dy)] = set([p0, p1])
                # x0, y0 = x1, y1 
        #print( lines)

        return max([ len(x) for x in lines.values()] )

'''
[[0,0],[94911151,94911150],[94911152,94911151]]
'''
