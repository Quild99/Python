#making a calculator that follows the rules of math

def Exponentiation(base, exp=2):
    return(base ** exp)

def root(base, exp=2):
    return(base ** (1/exp))

def multiplication(a, b):
    return(a * b)

def division(a, b):
    return(a / b)

def addition(a, b): 
    return(a + b)

def substraction(a, b):
    return(a - b)

def calculation(a, b, c):
    try:
        if c == "**":
            func = Exponentiation
        elif c == "*/":
            func = root
        elif c == "*":
            func = multiplication
        elif c == "/":
            func = division
        elif c == "+":
            func = addition
        elif c == "-":
            func = substraction
        return(func(float(a), float(b)))
    except:
        print("please make sure the equation is correct")
        exit


#adds a way to enter formula in one go
print("The allowed math symbols are: **, */, *, /, +, - ")
answer = str(input("Enter the equation, press enter when finished: "))
sum = []
ans = ""
for i in answer:
    if i in (" ", "**", "*/", "*", "/", "+", "-"):
        if i == " ":
            continue
        #add a way to differentiate between **, */ and *
        ans2 = i
        sum.extend([ans, ans2])
        ans = ""
    else:
        ans += i
        if len(answer) == len(sum) + 1:
            sum.extend(ans)

    
#ToDo, incorporate parenthesis
work_sum = sum[:]

order = ["**", "*/", "*", "/", "+", "-"]
counter = 0
#make this a definition that accepts a list, which will be without parenthesis
while counter < 6:
    a = order[counter]
    b = order[counter+1]
    if a in work_sum:
        loc1 = work_sum.index(a)
        var = a
    else:
        loc1 = 0
    if b in work_sum:
        loc2 = work_sum.index(b)
        var = b
    else:
        loc2 = 0
    if loc1 == loc2 == 0:
        counter += 2
        continue
    elif (loc1 < loc2 and loc1 != 0) or loc2 == 0:
        loc = loc1
    else:
        loc = loc2
    int_ans = calculation(work_sum[loc-1], work_sum[loc+1], var)
    del work_sum[loc-1:loc+2]
    work_sum.insert(loc-1, int_ans)
    print("work_sum: ", work_sum)
    counter += 2

print("The answer is: ", work_sum[0])
