# AREAPERI
length = int(input())
breadth = int(input())

if(length*breadth) == 2*(length+breadth):
    print("Eq")
    print(length*breadth)
elif (length*breadth) > 2*(length+breadth):
    print("Area")
    print(length*breadth)
else:
    print("Peri")
    print(2*(length+breadth))
