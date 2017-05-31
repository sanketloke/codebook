class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        j = abs(x)
        i = 0
        v = 0
        while j >= 10:
            v = v * 10 + j % 10
            j = int(j / 10)
            i += 1
        v = v * 10 + j % 10
        return v == x

t = input()
sol = Solution()
for i in range(0, t):
    s = raw_input()
    print sol.isPalindrome(int(abs(s)))
