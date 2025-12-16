from tabnanny import check


def main():
    f = open("input.txt", "r")

    lines = f.readlines()
    f.close()

    l = list(map(lambda x: x.split(","), lines)).pop(0)
    # print(l)
    listOfIDs = list(map(lambda x: list(map(int, x.split("-"))), l))
    print(listOfIDs)

    # def checkForDoubles():
    #     for i in range(len(listOfIDs)):
    #         print(i)

    # checkForDoubles()


if __name__ == "__main__":
    main()
