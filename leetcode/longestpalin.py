class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m=len(s)-1
        pm,qm=0,0
        l=1
        if len(s)==1:
        	return s
        if len(s)==2 and s[0]==s[1]:
        	return s
        elif len(s)==2:
        	return s[0]
        for i in range(len(s)):
        	p=i
        	q=i
        	while p>=0 and q<=m and s[p]==s[q]:
        		p-=1
        		q+=1
        	if q-(p+1)>l:
        		pm=p
        		qm=q
        		l=q-(p+1)
        	
        for i in range(0,len(s)):
        	p=i
        	q=i+1
        	while p>=0 and q<=m and s[p]==s[q]:
        		p-=1
        		q+=1
        	if q-(p+1)>l:
        		pm=p
        		qm=q
        		l=q-(p+1)
        if pm==qm:
        	return s[pm]
       	return s[pm+1:qm]

t = input()
sol = Solution()
for i in range(0, t):
    s = raw_input()
    print sol.longestPalindrome(s)