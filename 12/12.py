class Solution:
    def intToRoman(self, num: int) -> str:
        s = ""

        if int(num/1000):
            s+= "M" * int(num/1000)
            num = num % 1000
        
        if int(num/900):
            s+= "CM"
            num = num % 900

        if int(num/500):
            s+= "D" * int(num/500)
            num = num % 500

        if int(num/400):
            s+= "CD" 
            num = num % 400

        if int(num/100):
            s+= "C" * int(num/100)
            num = num % 100

        if int(num/90):
            s+= "XC" 
            num = num % 90
        

        if int(num/50):
            s+= "L" * int(num/50)
            num = num % 50

        if int(num/40):
            s+= "XL" 
            num = num % 40

        if int(num/10):
            s+= "X" * int(num/10)
            num = num % 10
        
        if int(num/9):
            s+= "IX" 
            num = num % 9

        if int(num/5):
            s+= "V" * int(num/5)
            num = num % 5

        if int(num/4):
            s+= "IV"
            num = num % 4

        if int(num/3):
            s+= "III"
            num = num % 3

        if int(num/1):
            s+= "I" * int(num/1)
            num = num % 1

        return s





