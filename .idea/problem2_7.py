def problem2_7():
    s1 = float(input("Enter length of side one: "))
    s2 = float(input("Enter length of side two: "))
    s3 = float(input("Enter length of side three: "))
    s=(s1+s2+s3)/2
    area=(s*(s-s1)*(s-s2)*(s-s3))**(1/2)
    print("Area of a triangle with sides",s1,s2,s3,"is",area)

problem2_7()