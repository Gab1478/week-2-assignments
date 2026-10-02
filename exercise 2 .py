a=10
b=20
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)






#d2
limit=50
print(limit==50)
print(limit==60)

# D3
attemps=4
max_attemps=3
is_locked=attemps>=max_attemps
print(is_locked)
print(type(is_locked))

# D4
percent=95
print(percent>=90 and percent<100)
print(percent<50 or percent>90)
print(not(percent>90))

# D5
#because it only runs when the if function is true.
value=80
limit=100
if value>limit:  
   print("OVER LIMIT")

   # D7
Value=95
limit=100
percent=(value/limit)*100
if percent >= 100:
    print("OVERLIMIT")
elif percent >= 90:
    print("WARNING")
else:
    print("OK")


# D8
#both print functions run when value is true.
value = 50
limit = 100

if value > limit:
    print("OVER LIMIT")
    print("Check finished")

    # D9
count=1
while count <=10:
     print(count)
     count=count+1


     # D10
#because in its own terms the statement is true in that 1 will always be less than 5 hence the infinite loop.
count = 1
while count <= 5:
    print(count)


    # D11
total=0
while True


# D12
number=1
while number <= 11:
    if number == 5:
        number=number + 1
        continue

print(number)
number=number + 1
    


# D13
for i in range(5):
    print(i)
for i in range(1,6):
    print(i)


    # D14
 for i in range(2,21,2):
      print(i)


       # D15
code = "A7X"
for number,character in enumerate(code,start=1):
    print("character",number,":",character)

    # D16
for i in range (3):
    number = input("Enter a number")
    print(number)
while passwors=input("Enter password:")


