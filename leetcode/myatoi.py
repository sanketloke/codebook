class Solution(object):

    def to_digit(self, d):
        j = len(d) - 1
        t = 0
        for i in d:
            if i == '':
                break
            t += pow(10, j) * int(i)
            j -= 1
        return t

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

    def remove_prefix_zeros(self, str):
        q = 0
        for i in str:
            if i > '0':
                return str[q:]
            q += 1
        return '0'

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        f = 0
        e = 0
        space_check = 0
        start = -1
        end = -1
        for i in enumerate(str):
            if i[1].isdigit():
                if start == -1:
                    start = i[0]
                f = 1
            if f == 1 and not i[1].isdigit():
                if i[1].isalpha() and end == -1:
                    end = i[0] - 1
                    continue
                elif not i[1].isdigit():
                    space_check = 1
                    if end == -1:
                        end = i[0] - 1
                else:
                    e = 1
        if f == 0:
            e = 1
        if e == 1:
            return 0
        if end == -1:
            end = len(str) - 1
        for i in range(0, start - 1):
            if not str[i] == ' ':
                return 0
        d = str[start:end + 1].replace('\n', '')
        sign_f = 1
        if start - 1 >= 0 and str[start - 1] == '+':
            sign_f = 1
        elif start - 1 >= 0 and str[start - 1] == '-':
            sign_f = 0
        elif start - 1 >= 0 and str[start - 1] == ' ':
            sign_f = 1
        elif start - 1 >= 0:
            return 0
        if sign_f == 0:
            if self.str_compare_max(d, 0) > 0:
                return -1 * pow(2, 31)
            else:
                return -1 * self.to_digit(d)
        else:
            if self.str_compare_max(d, 1) > 0:
                return pow(2, 31) - 1
            else:
                return self.to_digit(d)

t = input()
sol = Solution()
for i in range(0, t):
    s = raw_input()
    print sol.myAtoi(s)
