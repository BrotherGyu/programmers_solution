import itertools

def solution(n):
    li = [i for i in range(n)]

    # permutations() - [조합]
    print('permutations')
    print(list(itertools.permutations(li, 2)),'\n')

    # combinations() - [중복 조합]
    print('combinations')
    print(list(itertools.combinations(li, 2)),'\n')
    # 데카르트 곱
    print('product')
    a_li = [1, 2, 3]
    b_li = [4, 5]
    ab_li = [[1, 2, 3], [4, 5]]
    print(list(itertools.product(a_li, b_li)))
    print(list(itertools.product(*ab_li)),'\n')
    


if __name__ == '__main__':
    solution(3)
