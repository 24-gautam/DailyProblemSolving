class Solution:
    LessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    Tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    Thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0 : return 'Zero' 
        i , word = 0 , ''

        while num : 
            if num % 1000 != 0 : 
                word = self.convert(num % 1000) + self.Thousands[i] + " "  + word

            num //= 1000 
            i += 1 

        return word.strip()

        
    def convert(self, num) : 
        if num == 0 : return '' 
        if num < 20 : return self.LessThan20[num] + " "
        if num < 100 : return self.Tens[num//10] + " " + self.convert(num % 10)
        else : return self.LessThan20[num//100] + ' Hundred ' + self.convert(num % 100)