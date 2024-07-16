def custom_fizzbuzz(x, y):
    for i in range(1, 101):
        if i % x == 0 and i % y == 0:
            print("FooBar")
        elif i % x == 0:
            print("Foo")
        elif i % y == 0:
            print("Bar")
        else:
            print(i)

if __name__ == "__main__":
    x = int(input("Enter the value for x: "))
    y = int(input("Enter the value for y: "))
    custom_fizzbuzz(x, y)