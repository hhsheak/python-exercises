import math
no = int(input("Input number:")) #Gets user input

count = 0
isPerfectSquare = False
while count < no:
    if count ** 2 == no:
        print(f"It is a perfect square. Its square root is {count}.")
        isPerfectSquare = True
        break
    count += 1
    
if isPerfectSquare == False:
    def getUpperLimit(num): #Finds the upper limit (Which is the square root of the first perfect square after the number inputted)
        count = 0
        squared = 1
        while count ** 2 < num:
            squared = count ** 2
            count += 1
        return count
        
    
    def getTrial (lowerLimit, upperLimit): #Finds the number between the lower limit and upper limit
        number_to_try = lowerLimit + ((upperLimit - lowerLimit) / 2)
        return number_to_try 
    
    
    def guessAndCheck(no, number_to_try): #Multiplies the number to be tried and return the difference between the number inputted
        squaring = number_to_try ** 2
        difference = no - squaring
        return difference
    
    difference = 0
    
    upperLimit = getUpperLimit(no)    
    lowerLimit = upperLimit - 1 #The lower limit is the square root of the perfect square right before the number inputted
    number_to_try = getTrial(lowerLimit, upperLimit)
    difference = guessAndCheck(no, number_to_try)
    
    while abs(difference) > 0.000001:
        if difference < 0: #If difference is negative, the number tried is more than the square root and thus, it will become the new upper limit, with the square root falling between this new upper limit and the previous lower limit
            upperLimit = number_to_try 
            number_to_try = getTrial(lowerLimit, upperLimit)
            difference = guessAndCheck(no, number_to_try)
        if difference > 0: #If difference is positive, the number tried is less than the square root and thus, it will become the new lower limit, with the square root falling between this new lower limit and the previous upper limit
            lowerLimit = number_to_try 
            number_to_try = getTrial(lowerLimit, upperLimit)
            difference = guessAndCheck(no, number_to_try)
    
    result = f"{number_to_try:.6f}" #Rounds the six decimal places
    print(f"The square root of {no} is {result}.")    

    