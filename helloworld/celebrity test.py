def eliminate_non_celebrities(matrix, n):
    print(matrix)
    """Take an n x n matrix that has m[i][j] = True iff i knows j and return person who is maybe a celebrity."""
    possible_celebrity = 0
    n = len(matrix)
    print(n)
    for p in range(n):
        print(p)
        print('#',possible_celebrity)
        if (matrix[possible_celebrity][p] or not matrix[p][possible_celebrity]):
            print(matrix[possible_celebrity][p])
            print(not matrix[p][possible_celebrity])
            possible_celebrity = p
            print(possible_celebrity)
    print(n)
    return possible_celebrity

def check_if_celebrity(possible_celebrity, matrix, n):
    """Take an n x n matrix that has m[i][j] = True iff i knows j and return True if possible_celeb is a celebrity."""
    for i in range(n):
        if matrix[possible_celebrity][i] is True:
            return False
    for i in range(n):
        if matrix[i][possible_celebrity] is False:
            if i != possible_celebrity:
                return False
    return True

def user_input():
    n = int(input('Number of people: '))
# create n x n matrix initialized to False that has m[i][j] = True iff i knows j
    m = []
    for i in range(n):
        print(i)
        m.append([False]*n)
    print(m)

    for i in range(n):
        people = input(f'Enter list of people known to {i}: ').split()
        print(people)
        for p in people:
            p = int(p)
            m[i][p] = True
    print(m)
    possible_celebrity = eliminate_non_celebrities(m, n)

    if check_if_celebrity(possible_celebrity, m, n):
        print(f'{possible_celebrity} is the celebrity.')
    else:
        print('There is no celebrity.')
if __name__ == "__main__":
    user_input()