import sys

score = []

if len(sys.argv) == 4:
    for i in range(1,4):
      score.append(int(sys.argv[i]))

    total = score[0] + score[1] + score[2]
    average = total / len(score)

    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Minimum: {min(average)}")
    print(f"Maximum: {max(average)}")
