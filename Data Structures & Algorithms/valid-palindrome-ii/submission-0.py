class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                rstr,lstr=s[l:r],s[l+1:r+1]
                return (lstr==lstr[::-1]or rstr==rstr[::-1])
                    
            l+=1
            r-=1
        return True          
        