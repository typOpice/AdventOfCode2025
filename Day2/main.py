def main():
    f = open("input.txt", "r")

    lines = f.readlines()
    f.close()

    l = list(map(lambda x: x.strip(","), lines))
    RawlistOfIDs = list(map(lambda x: x.split("-"), l)).pop(0)

    listOfIDs = []
    for i in range(0, len(RawlistOfIDs) - 2, 2):
        t = []
        t.append(RawlistOfIDs[i])
        t.append(RawlistOfIDs[i + 1])
        listOfIDs.append(t)

    print(listOfIDs)


def checkForDoubles():
    pass


if __name__ == "__main__":
    main()
