class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        students=students[::-1]
        sandwiches=sandwiches[::-1]
        n=len(students)
    
        while True:
            
            if len(students)==0:
                break
            if sandwiches[-1] not in students:
                break
            
            x=students.pop()
            y=sandwiches.pop()
            
            if x==y:
                pass
            else:
                students.insert(0,x)
                sandwiches.append(y)
            
        return len(students)