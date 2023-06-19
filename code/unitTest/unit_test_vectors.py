

if __name__ == '__main__':
    list_ = [4, 2, 3, 1, 4, 3]

    print(list_, list_.index(0))
    list_.reverse()
    print(list_, list_.__len__() - list_.index(0) - 1)

