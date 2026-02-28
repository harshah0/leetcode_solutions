class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        shoot = points[0][1]
        arrow=1
        for st,en in points[1:]:
            if(st<=shoot):
                continue
            else:
                arrow+=1
                shoot=en
        return arrow

        