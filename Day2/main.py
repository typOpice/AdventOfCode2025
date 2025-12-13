def main():
    f = open("input.txt", "r")

    lines = f.readlines()
    f.close()

    l = list(map(lambda x: x.strip(","), lines))
    RawlistOfIDs = list(map(lambda x: x.split("-"), l)).pop(0)


def checkForDoubles():
    pass


if __name__ == "__main__":
    main()
