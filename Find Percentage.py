if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    toto = 0

    for a in student_marks[query_name]:
        toto = toto + a

    x = float(toto / 3)
    y = '{0:.2f}'.format(x)
    print(y)

