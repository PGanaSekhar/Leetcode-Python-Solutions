class Solution:
    def sam(self,n):
        l=["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        t = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        if n==0:
            return ""
        elif n<20:
            return l[n]+" "
        elif n<100:
            return t[n//10]+" "+self.sam(n%10)
        else:
            return l[n//100]+" Hundred "+self.sam(n%100)

    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        r=""
        th = ["", "Thousand ", "Million ", "Billion "]
        i=0
        while num!=0:
            if num%1000 !=0:
                r=self.sam(num%1000)+th[i]+r
            print(num)
            num=num//1000
            i+=1
        return r.rstrip()
