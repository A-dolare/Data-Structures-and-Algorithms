def buildPrefix(mat):

    n = len(mat)

    pref = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):

            curr = 1 if mat[i][j] == '*' else 0

            top = pref[i-1][j] if i > 0 else 0

            left = pref[i][j-1] if j > 0 else 0

            diag = pref[i-1][j-1] if i > 0 and j > 0 else 0

            pref[i][j] = top + left - diag + curr

    return pref


def query(pref, x1, y1, x2, y2):

    total = pref[x2][y2]

    top = pref[x1-1][y2] if x1 > 0 else 0

    left = pref[x2][y1-1] if y1 > 0 else 0

    diag = pref[x1-1][y1-1] if x1 > 0 and y1 > 0 else 0

    return total - top - left + diag


def main():

    n, q = map(int, input().split())

    mat = []

    for _ in range(n):
        mat.append(list(input()))

    pref = buildPrefix(mat)

    for _ in range(q):

        x1, y1, x2, y2 = map(int, input().split())

        # convert to 0-index
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        print(query(pref, x1, y1, x2, y2))


main()