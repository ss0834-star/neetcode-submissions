class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        result=[]
        for s in strs:
            sorted_s=tuple(sorted(s))
            if sorted_s not in dic:
                dic[sorted_s] = []
            dic[sorted_s].append(s)
        for values in dic.values():
            result.append(values)    
        return result