import re
#filename='regex_sum_42.txt'
filename='regex_sum_367932.txt'
file=open(filename)
total=0
for line in file:
    matchedNum= [int(num) for num in re.findall('[0-9]+',line)]
    if len(matchedNum)!=0:
        total+= sum(matchedNum)

print total

print sum( [ int(num) for num in re.findall('[0-9]+',open('regex_sum_367932.txt').read()) ] )
