#!/usr/bin/python3
"""N queens problem"""

N = 4
lst = []


class Queen:
    """class represent a queen"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reserved(self):
        for i in range(N):
            if [self.x, i] not in lst:
                lst.append([self.x, i])

        for i in range(N):
            if [i, self.y] not in lst:
                lst.append([i, self.y])

        for i in range(N):
            if (
                0 <= self.x + i < N
                and 0 <= self.y + i < N
                and [self.x + i, self.y + i] not in lst
            ):
                lst.append([self.x + i, self.y + i])

        for i in range(N):
            if (
                0 <= self.x - i < N
                and 0 <= self.y - i < N
                and [self.x - i, self.y - i] not in lst
            ):
                lst.append([self.x - i, self.y - i])

        for i in range(N):
            if (
                0 <= self.x - i < N
                and 0 <= self.y + i < N
                and [self.x - i, self.y + i] not in lst
            ):
                lst.append([self.x - i, self.y + i])

        for i in range(N):
            if (
                0 <= self.x + i < N
                and 0 <= self.y - i < N
                and [self.x + i, self.y - i] not in lst
            ):
                lst.append([self.x + i, self.y - i])

        return lst

    def __str__(self):
        return f"q{self.x, self.y}"


# queens = []
# for i in range(N):
#     queens.append(i)


solutions = []


def get_solutions(xp, yp):
    # for f in range(N):
    qCount = 0
    k = 0
    queens = [i for i in range(N)]
    flag = 0
    flag2 = 0
    for i in range(xp if flag2 == 0 else 0, N):
        for j in range(yp if flag2 == 0 else 0, N):
            flag2 = 1
            if [i, j] not in lst:
                # if flag > 0:
                #     flag -= 1
                #     continue
                queens[k] = Queen(i, j)
                queens[k].reserved()
                qCount += 1
                k += 1
            if qCount == N:
                break
        if qCount == N:
            break
    # for i in range(N):
    #     print(queens[i], end="&")
    if qCount == N:
        solutions.append(queens)
    # flag += f + 1


for i in range(N):
    for j in range(N):
        lst = []
        get_solutions(i, j)


for i in range(len(solutions)):
    for j in range(len(solutions[i])):
        print(solutions[i][j], end=" & " if j != len(solutions[i]) - 1 else "\n\n")

# print(solutions)
