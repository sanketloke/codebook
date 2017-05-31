class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        j = 0
        R = [[] for _ in range(numRows)]
        i = 0
        if numRows == 1:
            return s
        while i < len(s):
            if j == 0:
                R[0].append(s[i])
                j += 1
                i += 1
            elif j == numRows-1:
                R[numRows-1].append(s[i])
                j += 1
                i += 1
            elif j == numRows:
                j = 0
                i += (numRows-2)
            else:
                a = i
                b = i + 2*(numRows - 2 - j)+1 + 1
                if a < len(s):
                    R[j].append(s[a])
                if b < len(s):
                    R[j].append(s[b])
                j += 1
                i += 1
        return ''.join([''.join(i) for i in R])

t = input()
sol = Solution()
for i in range(0, t):
    s, numRows = raw_input().split()
    print sol.convert(s, int(numRows))
