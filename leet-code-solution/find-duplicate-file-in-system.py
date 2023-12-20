class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        D = defaultdict(list)
        
        for path in paths:
            directory, *files = path.split()
            
            for file in files:
                filename, content = file.split('(')
                D[content].append(directory + '/' + filename)
                
        return [val for val in D.values() if len(val) > 1]

            #files = path.split()
            #directory = files[0]
                #D[content[:-1]].append(directory + '/' + filename)
        #return [D[content] for content in D if len(D[content]) > 1]

############################################
        #ans = []
        #for i in range(len(paths)):
        #    if int("abcd") in paths[i][i["("]:i[")"]]:
        #        dic[paths[i][i["("]:i[")"]]] += 1
        #         print(dic)
        #    else:
        #        dic[paths[i][i["("]:i[")"]]] = 1

        #    max_dup = max(dic[paths[i][i["("]:i[")"]]], default = 0)
        #    print(max)
        #return ans