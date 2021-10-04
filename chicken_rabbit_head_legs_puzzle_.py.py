Qus. Write a python program to solve a classic ancient Chinese puzzle.
If there are 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
 
solution : 
 
heads = int(input("Enter number of heads: "))
legs = int(input("Enter the number of legs : "))

for chickens in range(0, heads+1, 1):
    rabbits = heads - chickens
    if(chickens*2 + rabbits*4 == legs):
        print("Chikens: ", chickens, " , ", "rabbits : ", rabbits)
        quit()
print("No Solution")


 
 
 
 
