def add(f_num,s_num):
  return int(f_num) + int(s_num)
def subtract(f_num,s_num):
  return int(f_num) - int(s_num)
def divide(f_num,s_num):
  return int(f_num) / int(s_num)
def cube(f_num):
  return int(f_num) * int(f_num)*int(f_num)


f_num = input("Enter f_num: ")
s_num = input("Enter s_num: ")

print("Sum: " +str(add(f_num,s_num)))
print("Cube: " +str(cube(f_num)))
print("Subtract: " +str(subtract(f_num,s_num)))
print("Divde: " +str(divide(f_num,s_num)))