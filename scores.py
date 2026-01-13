import sys
score =[]
if len(sys.argv) == 4:
  script_name = sys.argv[0]
  score[0] = sys.argv[1]
  score[1] = sys.argv[2]
  score[2] = sys.argv[3]
  sum = score[0] + score[1] + score[2]
  average = sum / len(score)
  print(f"Sum: {sum}")
  print(f"Average: {average}")
