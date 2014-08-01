n = 5000
numbers = range(2, n)
#print numbers
results = []
exceptions = set()
for number in numbers:
    #print "number: ", number
    if number not in exceptions:
        results.append(number)
    #print "Result: ", results
    for num in numbers:
        if num%number == 0:
            exceptions.add(num)
            #print "Exception: ", exceptions
            
print len(results)
