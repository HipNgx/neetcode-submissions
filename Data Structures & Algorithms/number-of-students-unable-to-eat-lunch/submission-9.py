class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while sandwiches :
            if sandwiches[0] not in students :
                break
            if students[0] == sandwiches[0] :
                students.remove(students[0])
                sandwiches.remove(sandwiches[0])
            else :
                n = students[0]
                students.append(n)
                students.remove(students[0])
        return len(students)