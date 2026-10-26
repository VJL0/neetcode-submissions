class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        dp = [False]*numCourses

        edgeList = [[] for _ in range(numCourses)]

        for start, end in prerequisites:
            edgeList[start].append(end)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if edgeList[course] == []:
                return True

            visited.add(course)
            for pre in edgeList[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            edgeList[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True