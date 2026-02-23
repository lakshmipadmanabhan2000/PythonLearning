import random
def guess():
    actualNum=random.randint(1,100) #Generate a random number b/w 1 and 100
    print(actualNum)
    attemptNo=1
    maxAttempt=10
    while(attemptNo<=maxAttempt):
        try:
            x=int((input("Enter a number: ")))
            if(x>actualNum): 
                print("High")
            elif(x< actualNum): 
                print("Low")
            elif(x==actualNum): 
                print("Congrats You won!") 
                return
            print(str(maxAttempt-attemptNo) +" attempts left")
            attemptNo+=1
        except ValueError:
            print("Exception: Enter a number")
            print(str(maxAttempt-attemptNo) +" attempts left")
            attemptNo+=1
    print("Better luck Next Time!")
guess()
        