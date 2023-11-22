class Solution:
    def findOrder(self, numCourses: int, prerequisites: list) -> list:
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ajacent_list = [[] for _ in range(numCourses)]
        inDegree = [0 for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            ajacent_list[prerequisite].append(course)
            inDegree[course] += 1
        inZero = []

        for i in range(numCourses):
            if inDegree[i] == 0:
                inZero.append(i)

        for start in inZero:
            for course in ajacent_list[start]:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    inZero.append(course)
        return inZero if len(inZero) == numCourses else []

print(Solution().findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))