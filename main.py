class solution:
    def simple_reverse(self,string):
        s=""
        i=len(string)-1
        while(i>=0):
            s+=string[i]
            i-=1
        return s
a1=solution()
print(a1.simple_reverse((input())))