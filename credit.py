credit_num = input("Please enter a valid credit card number without hyphens: ")
products_sum = []
other_numbers = []
    

rev_num = credit_num[::-1]


for i in range(0,len(rev_num)):
    if i % 2 != 0:      
        products = (int(rev_num[i]) * 2)
        string_products = str(products)#multiplys every other number by 2 then stores in list
        products_sum.append(string_products)
    elif i % 2 == 0:
        other_numbers.append(rev_num[i]) #stores even index numbers in list

   
empty_string = ""
for item in products_sum:
    empty_string = empty_string + item #stores the odd index numbers in an empty string
    
sum_digits = 0
for item in empty_string:
    sum_digits += int(item) #adds up the digits from the string 

    
sum_other_nums = 0  
for item in other_numbers: #adds up remaining numbers in credit_num
    sum_other_nums += int(item)
    

total_sum = sum_digits + sum_other_nums #this is the total sum of all the digits

if total_sum % 10 == 0:
    print("Valid number: " + credit_num)
else:
    print("Invalid number: " + credit_num)


