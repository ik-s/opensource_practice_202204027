# get two integer parameters
# return sum
def plus(x, y):
    return x+y

def minus(x, y):
    return x-y

def multiplycation(x, y):
    return x*y

def division(x, y):
    return x/y

# input two number
def InputNumber():
    global x, y
    print("First Number")
    x = int(input())
    print("Second Number")
    y = int(input())

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:
        print("0: exit, 1: plus, 2: minus, 3: multiplycation, 4: division")
        check = int(input())
        if check >= 1 or check <= 4:
            InputNumber()
	    if check == 1:
	       	print("answer : ", plus(x,y))
            elif check == 2:
		print("answer : ", minus(x,y))
	    elif check == 3:
	       	print("answer : ", multiplycation(x,y))
	    elif check == 4:
	       	print("answer : ", division(x,y))
        elif check > 4:
            print("Unsupported")
        else:
            print("Thank you")

if __name__ == "__main__":
    main()
