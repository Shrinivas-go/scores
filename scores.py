import sys

score = []

if len(sys.argv) == 4:
    score.append(int(sys.argv[1]))
    score.append(int(sys.argv[2]))
    score.append(int(sys.argv[3]))

    total = score[0] + score[1] + score[2]
    average = total / len(score)

    print(f"Sum: {total}")
    print(f"Average: {average}")
