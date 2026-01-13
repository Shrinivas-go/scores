import sys

score = []

if len(sys.argv) == 4:
    for i in range(1,4):
      score.append(int(sys.argv[i]))

    sum = score[0] + score[1] + score[2]
    average = sum / len(score)

    print(f"Sum: {sum}")
    print(f"Average: {average}")
    print(f"Minimum: {min(score)}")
    print(f"Maximum: {max(score)}")
