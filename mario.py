#Mario more comfortable
num = int(input("Please enter a number: "))

condition = False
while not condition:
    if num > 1 and num <= 8:
        print("Height: ", num)
        for i in range(num + 1):
            pyramid = (((num - i) * " " + ("#" * i) + " " + ("#" * i)))
            print(pyramid)
            condition = True
    else:
        print("Height: ", num)
        num = int(input("Please enter a valid number between 1 and 8: "))


    
        
