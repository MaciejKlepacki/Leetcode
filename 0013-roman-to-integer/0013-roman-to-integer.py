class Solution(object):
    def romanToInt(self, s):
        value = 0
        list_values = []
        for i in range(len(s)):
            if s[i] == 'I': list_values.append(1)
            elif s[i] == 'V': list_values.append(5)
            elif s[i] == 'X': list_values.append(10)
            elif s[i] == 'L': list_values.append(50)
            elif s[i] == 'C': list_values.append(100)
            elif s[i] == 'D': list_values.append(500)
            elif s[i] == 'M': list_values.append(1000)
            else: return False
        list_values.append(0)
        is_minus = False
        for i in range(len(list_values)-1):
            if (list_values[i+1] <= list_values[i] and is_minus == False): value += list_values[i]
            elif is_minus == True: is_minus = False
            else:
                value += abs(list_values[i+1] - list_values[i])
                is_minus = True;
        return value