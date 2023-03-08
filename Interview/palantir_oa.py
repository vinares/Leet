
from collections import defaultdict
class Solution:
    def tasksToRun(self, taskDefinitionsInput, changedFiles):
        files_tasks_map, deps = self.parseTasks(taskDefinitionsInput)
        ans, t_order = set(), self.ts(deps)
        for file in changedFiles:
            for f in files_tasks_map.keys():
                if self.matchGlob(f, file):
                    for task in files_tasks_map[f]:
                        ans.add(task)
        res = []
        for task in t_order:
            if task in ans:
                res.append(task)
        return res
        
    def matchGlob(self, glob, filepath):
        if not glob and not filepath: return True
        if not glob: return False
        if not filepath: return glob == '*'
        if glob[0] == '*': 
            if self.matchGlob(glob[1:], filepath):
                return True
            if filepath[0] == '/':
                return False
            return self.matchGlob(glob, filepath[1:])
        if glob[0] == filepath[0]:
            return self.matchGlob(glob[1:], filepath[1:])
        
    
    def ts(self, deps):
        ts = []
        degree = defaultdict(int)
        for key, dep in deps.items():
            if key not in degree:
                degree[key] = 0
            for x in dep:
                degree[x] += 1
        while deps:
            source = [x[0] for x in degree.items() if x[1]==0]
            for s in source:
                for node in deps[s]:
                    degree[node] -= 1
                deps.pop(s)
                degree.pop(s)
            ts.extend(source)
        return ts

    def parseTasks(self, taskDefinitionsInput):
        files_tasks_map = defaultdict(list)
        aj = defaultdict(list)
        n = len(taskDefinitionsInput)
        for i in range(0, n, 4):
            name = taskDefinitionsInput[i].split()[1]
            files = taskDefinitionsInput[i+1].split()[1:]
            deps = taskDefinitionsInput[i+2].split()[1:]
            for file in files:
                files_tasks_map[file].append(name)
            for dep in deps:
                aj[dep].append(name)
            if name not in aj:
                aj[name] = []
        return files_tasks_map, aj

taskDefinitionsInput = [
    "task: d",
    "files: images/dogs/*.jpg images/*/*.png",
    "deps: cj cp",
    "",
    "task: cj",
    "files: images/dogs/*.jpg",
    "deps:",
    "",
    "task: cp",
    "files: images/*/*.png",
    "deps:",
    "",
]

changedFiles = [
    "images/dogs/dalmatian.jpg",
    "images/dogs/retriever.jpg",
]
print(Solution().tasksToRun(taskDefinitionsInput, changedFiles))
