class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i=0
        while len(students)>0:
            if students.count(sandwiches[i])>0:
                if students[i]==sandwiches[i]:
                    students.pop(i)
                    sandwiches.pop(i)
                else:
                    a=students[i]
                    students.pop(i)
                    students.append(a)
            else:
                return len(students)
        return 0
