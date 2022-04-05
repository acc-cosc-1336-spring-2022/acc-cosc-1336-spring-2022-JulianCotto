num = 20  # outer variable

def use_local_variable(num):
    num = 10  # inner variable
    print(num)

print(use_local_variable(num))
print(num)
