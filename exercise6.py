def main():
    number=int(input("Enter the number: "))
    list_num=[1,2,3,4,66,55,44,77,88,99,57]
    print("Numbers in the list taht are greater than",number)

    funct(list_num,number)
    
def funct(list_num,number):
    for num in list_num:
        if num > number:
            print(num)
        
main()