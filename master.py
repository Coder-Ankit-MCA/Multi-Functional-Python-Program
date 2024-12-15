import matplotlib.pyplot as plt
def calculator():
    try:
        print("Choose an Operation to perform:-")
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Squareroot\n6. Exponential Calculator")
        m = int(input("Enter your choice(1-6): "))
        if m <= 0 or m>=7:
            raise ValueError("Please enter a valid number between 1-6.")
        elif m ==1:
            a = int(input("Enter the 1st number: "))
            b = int(input("Enter the 2nd number: "))
            result = a+b
            print(f"The sum of {a} and {b} is {result}.")
        elif m==2:
            a = int(input("Enter the 1st number: "))
            b = int(input("Enter the 2nd number: "))
            result = a-b
            print(f"The difference between {a} and {b} is {result}.")
        elif m==3:
            a = int(input("Enter the 1st number: "))
            b = int(input("Enter the 2nd number: "))
            result = a*b
            print(f"The product of {a} and {b} is {result}.")
        elif m ==4:
            a = int(input("Enter the 1st number: "))
            b = int(input("Enter the 2nd number: "))
            result = a/b
            print(f"The result after the  division of {a} by {b} is {result}.")
        elif m==5:
            a = int(input("Enter a number: "))
            result = a**(1/2)
            print(f"The Squareroot of {a} is {result}.")
        else:
            a = int(input("Enter the base number: "))
            b = int(input("Enter the exponent (power): "))
            result = a**b
            print(f"The product of {a} and {b} is {result}.")
    except ValueError as e:
        print("Error: ")
    except ZeroDivisionError:
        print("Error:\nYou cannot divide a number with 0.")
    except TypeError:
        print("Please enter a Valid Number.")

def converter():
    try:
        print("Choose the Conversion Type:-")
        print("1. From Decimal\n2. From Binary\n3. From Octal\n4. From Hexadecimal")
        m = int(input("Enter your choice(1-4): "))
        if m <= 0 or m>=5:
            raise ValueError("Please enter a valid number between 1-4.")
        elif m==1:
            print("From Decimal to ??")
            print("1. to Binary\n2. to Octal\n3. to Hexadecimal")
            n = int(input("Enter your choice(1-3): "))
            if n <= 0 or n>=4:
                raise ValueError("Please enter a valid number between 1-3.")
            elif n ==1:
                a = int(input("Enter the number: "))
                binary = bin(a)[2:]
                print(f"The binary representation of {a} is {binary}.")
            elif n ==2:
                a = int(input("Enter the number: "))
                octal = oct(a)[2:]
                print(f"The octal representation of {a} is {octal}.")
            else:
                a = int(input("Enter the number: "))
                hexadecimal = hex(a)[2:]
                print(f"The Hexadecimal representation of {a} is {hexadecimal}.")
        elif m==2:
            print("From Binary to ??")
            print("1. to Decimal\n2. to Octal\n3. to Hexadecimal")
            n = int(input("Enter your choice(1-3): "))
            if n <= 0 or n>=4:
                raise ValueError("Please enter a valid number between 1-3.")
            elif n ==1:
                a = input("Enter the number: ")
                decimal = int(a,2)
                print(f"The Decimal representation of the Binary number {a} is {decimal}.")
            elif n==2:
                a = input("Enter the number: ")
                decimal = int(a,2)
                octal = oct(decimal)[2:]
                print(f"The Octal representation of the Binary number {a} is {octal}.")
            else:
                a = input("Enter the number: ")
                decimal = int(a,2)
                hexa = hex(decimal)[2:]
                print(f"The Hexadecimal representation of the Binary number {a} is {hexa}.")
        elif m ==3:
            print("From Octal to ??")
            print("1. to Decimal\n2. to Binary\n3. to Hexadecimal")
            n = int(input("Enter your choice(1-3): "))
            if n <= 0 or n>=4:
                raise ValueError("Please enter a valid number between 1-3.")
            elif n ==1:
                a = input("Enter the number: ")
                decimal = int(a,8)
                print(f"The Decimal representation of the Octal number {a} is {decimal}.")
            elif n==2:
                a = input("Enter the number: ")
                decimal = int(a,8)
                binary = bin(decimal)[2:]
                print(f"The Binary representation of the Octal number {a} is {binary}.")
            else:
                a = input("Enter the number: ")
                decimal = int(a,8)
                hexa = hex(decimal)[2:]
                print(f"The Hexadecimal representation of the Octal number {a} is {hexa}.")
        else:
            print("From Hexadecimal to ??")
            print("1.to Decimal\n2. to Binary\n3. to Octal")
            n = int(input("Enter your choice(1-3): "))
            if n <= 0 or n>=4:
                raise ValueError("Please enter a valid number between 1-3.")
            elif n ==1:
                a = input("Enter the number: ")
                decimal = int(a,16)
                print(f"The Decimal representation of the Hexadecimal number {a} is {decimal}.")
            elif n==2:
                a = input("Enter the number: ")
                decimal = int(a,16)
                binary = bin(decimal)[2:]
                print(f"The Binary representation of the Hexadecimal number {a} is {binary}.")
            elif n ==3:
                a = input("Enter the number: ")
                decimal = int(a,16)
                octal = oct(decimal)[2:]
                print(f"The Octal representation of the Hexadecimal number {a} is {octal}.")
    except ValueError as e:
        print("Error:")
    except TypeError:
        print("Please enter a Valid Number.")

def check_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    sum_of_product = sum(int(digit)**num_len for digit in num_str)
    return sum_of_product == num

def is_armstrong():
    try:
        num = int(input("Enter a number: "))
        num_str = str(num)
        num_len = len(num_str)
        sum_of_product = sum(int(digit)**num_len for digit in num_str)
        if num == sum_of_product:
            print(f"The given number {num} is a Armstrong Number.")
        else:
            print(f"The given number {num} is not a Armstrong Number.")
    except TypeError as e:
        print("Error: Please enter a Valid Number",e)

def find_armstrong(start,end):
    try:
        armstrong_no= []
        for i in range(start,end+1):
            if check_armstrong(i):
                armstrong_no.append(i)
        return armstrong_no
    except ValueError:
        print("Error: ")

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def check_leap_year():
    print("This program helps to check if an Year provided by the user is a leap year or not.")
    year = int(input("Enter a Year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return print(f"The Year {year} is a Leap Year")
    else:
        return print(f"The Year {year} is not a Leap Year")

def find_leap_year(start,end):
    try:
        leap_year = []
        for i in range(start,end+1):
            if is_leap_year(i):
                leap_year.append(i)
        return leap_year
    except:
        print("Error: ")

def plot():
    try:
        print("Choose the type of Plot you want to create:-")
        print("1. Histogram\n2. Bar Graph\n3. Scatter Plot\n4. Line Plot")
        n = int(input("Enter your choice: "))
        if n<=0 or n>4:
            raise ValueError("Please enter a valid number between 1-4.")
        elif n==1:
            data = input("Enter the numbers separated by spaces: ").split()
            num_bins = int(input("Enter the no. of Bars you want to create: "))
            plt.hist(data, bins=num_bins, color='blue', edgecolor='black')
            plt.title("Histogram")
            plt.xlabel("Value")
            plt.ylabel("Frequency")
            plt.show()
        elif n==2:
            categories = input("Enter the categories (numbers allowed, separated by spaces): ").split()
            values = input("Enter the values corresponding to the categories (separated by spaces): ").split()
            val_int = [int(val) for val in values]
            plt.bar(categories, val_int, color='skyblue')
            plt.title("Bar Graph")
            plt.xlabel("Categories")
            plt.ylabel("Values")
            plt.show()
            pass
        elif n ==3:
            x_string = input("Enter the X-axis values separated by spaces: ").split()
            x_int = [int(x) for x in x_string]
            y_string = input("Enter the Y-axis values separated by spaces: ").split()
            y_int = [int(x) for x in y_string]
            plt.scatter(x_int, y_int, marker='o', color= 'blue')
            plt.title("Scatter Plot")
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")
            plt.show()            
        elif n ==4:
            x_string = input("Enter the X-axis values separated by spaces: ").split()
            x_int = [int(x) for x in x_string]
            y_string = input("Enter the Y-axis values separated by spaces: ").split()
            y_int = [int(x) for x in y_string]
            plt.plot(x_int,y_int, color='red', marker='o', linestyle='--')
            plt.title("Line Plot")
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")
            plt.show() 
    except ValueError as e:
        print("Error: ", e)

def attendance_calc():
    try:
        print("This Program helps to calculate the required no. of classes to achieve a specific % of attendance.")
        class_total = int(input("Enter the total no. of classes taken: "))
        class_attended = int(input("Enter the total no. of classes attended: "))
        if class_attended > class_total:
            raise ValueError("Total Classes Attended cannot be greater than Total Class taken.")
        goal = int(input("Enter the Attendance Percent you want to achieve (without '%' symbol): "))
        percent = (class_attended/class_total)*100
        class_required = (goal*class_total/100 - class_attended)/(1-goal/100)
        if percent >= goal:
            print(f"Your attendance is {int(percent)}%.")
        else:
            print(f"Your attendance is {int(percent)}%.\nYou need to attend more {int(class_required)} classes without missing any class for your attendance to be {goal}%.")
            
    except ValueError as e:
        print("Error: ",e)

def main():
    try:
        while True:
            print("Main Menu:")
            print("Choose the Operation:\n1. Calculator\n2. Converter\n3. Armstrong Number Checker\n4. Find Armstrong Number\n5. Leap Year Checker\n6. Find Leap Years\n7. Graph Plot\n8. Attendance Calculator\n9. Exit")
            p = int(input("Enter your choice: "))
            if p <= 0 or p > 9:
                raise ValueError("Please enter a valid number (1-9).")
            elif p == 1:
                calculator()
            elif p == 2:
                converter()
            elif p==3:
                is_armstrong()
            elif p==4:
                print("This Program helps to find all Armstrong Numbers between any two numbers given by the user.")
                start = int(input("Enter the First Number: "))
                end = int(input("Enter the Second Number: "))
                if start > end:
                    raise ValueError("The 1st no. cannot be greater than the second no.")
                result = find_armstrong(start,end)
                print(f"Armstrong Numbers between {start} and {end} is {result}")
            elif p==5:
                check_leap_year()
            elif p==6:
                print("This Program helps to find all Leap Years between any two Years given by the user.")
                start = int(input("Enter the First Year: "))
                end = int(input("Enter the Second Year: "))
                if start > end:
                    raise ValueError("The 1st Year cannot be greater than the second Year")
                result = find_leap_year(start,end)
                print(f"All Leap Years between {start} and {end} is {result}")
            elif p==7:
                plot()
            elif p==8:
                attendance_calc()
            elif p == 9:
                print("Successfully Exited the Program.")
                break
    except ValueError as a:
        print("Error:", a)
    except Exception as e:
        print("There is an Error:", e)

if __name__ == "__main__":
    main()