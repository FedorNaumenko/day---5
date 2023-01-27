student_scores = input("Input a list of student scores ").split()
top_student_score = 0
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if student_scores[n] > top_student_score:
    top_student_score = int(student_scores[n])
print(student_scores)
print(top_student_score)