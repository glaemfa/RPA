a = 123
b = 15.556
print(a, "and", b, sep='@', end='\n\n')

print("a:{0} b:{1}". format(a,b))
print(f"a{a} b:{b}")

print(f"a:{a:05d} b:{b:2f}")
print("a:%05d b:%.2f" % (a,b))

print("2개의 숫자를 입력하세요.")
num1 = int(input())
num2 = int(input())
num3 = num1 + num2
print(num3)

num4 = num1 //3
print("num1 //3 ",num4)