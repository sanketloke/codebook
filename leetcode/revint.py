class Solution(object):

    def str_compare_max(self, c, f):
        if f == 1:
            max_int = str(pow(2, 31) - 1)
        else:
            max_int = str(pow(2, 31))
        if len(c) < len(max_int):
            return -1
        if len(c) > len(max_int):
            return 1
        for i in range(len(c)):
            if c[i] > max_int[i]:
                return 1
            if c[i] < max_int[i]:
                return 0
            else:
                continue
        return 0

    def get_digits(self, n):
        s = ''
        j = n
        if j < 10:
            return str(j)
        while j < 10:
            j = int(j / 10)
            s += str(j)
        s += str(j)
        return s

    def to_digit(self, d):
        j = len(d) - 1
        t = 0
        for i in d:
            t += pow(10, j) * int(i)
            j -= 1
        return t

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x < 0:
            d = self.get_digits(abs(x))
            d = d[::-1]
            if self.str_compare_max(d, 0) > 0:
                return 0
            else:
                return -1 * self.to_digit(d)
        else:
            d = self.get_digits(abs(x))
            d = d[::-1]
            if self.str_compare_max(d, 1) > 0:
                return 0
            else:
                return self.to_digit(d)


t = input()
sol = Solution()
for i in range(0, t):
    s = raw_input()
    print sol.reverse(int(s))
