height_sum=0
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  height_sum += student_heights[n]
print(student_heights)
average_height = int(height_sum/(n+1))
print(average_height)