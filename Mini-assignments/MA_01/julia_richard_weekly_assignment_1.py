# 1.

width = input("Enter the width of a room in meters: ")
length = input("Enter the length of the room in meters: ")
height = input("Enter the height of the room in meters: ")
area = (int(width)*int(length))
volume = (int(area)*int(height))

# 2.

print (f"Area in m2 = {area} m2")
print (f"Volume in m3 =  {volume} m3")

print (f"Area in mm2 = {area*100000} mm2")
print (f"Volume in mm3 =  {volume*1000000000} mm3")

# 3.

a = width
b = length
c = height

if a>b and a>c:
    print ("The width of the room is larger than both its length and height.")

if b>a and b>c:
    print ("The length of the room is larger than both its width and height.")

elif c>a and c>b:
    print ("The height of the room is larger than both its width and length.")