class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ''
        while n!=0:
            binary = str(n%2) + binary
            n = n//2
        while len(binary)!=32:
            binary = '0' + binary
        d = 0
        for i in range(len(binary)):
            d += int(binary[i])*(2**i)
        return d