def Area_of_Tri(base,height):
    Area = 1/2*(base*height)
    print("Area of triangle is ",Area)

if __name__ == "__main__":
    a = int(input("Enter base dimension "))
    b = int(input("Enter Height Dimension "))
    Area_of_Tri(a,b)
