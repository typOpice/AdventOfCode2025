def main():
    print("Hello, Fuzz 🐾")
    w = WrapNum()
    p = Parser("input.txt", w)


class WrapNum:
    def __init__(self, RANGE: int = 99, InitPointer: int = 50):
        self.RANGE = RANGE + 1
        self.CountOfZero = 0
        self.NewSecurityProtocolCountOfZero = 0
        self.pointer = InitPointer

    def GoLeft(self, steps: int):
        for i in range(steps):
            self.pointer -= 1
            if self.pointer < 0:
                self.pointer += 100

            if self.pointer == 0 and i != steps - 1:
                self.NewSecurityProtocolCountOfZero += 1
        # print(self.pointer)

    def GoRight(self, steps: int):
        for i in range(steps):
            self.pointer += 1
            if self.pointer >= self.RANGE:
                self.pointer -= 100

            if self.pointer == 0 and i != steps - 1:
                self.NewSecurityProtocolCountOfZero += 1
        # print(self.pointer)

    def checkZero(self):
        if self.pointer == 0:
            self.CountOfZero += 1
        # print(self.CountOfZero)

    @property
    def GetCountZero(self):
        return self.CountOfZero

    @property
    def GetNewSecurityProtocolCountOfZero(self):
        return self.NewSecurityProtocolCountOfZero


class Parser:
    def __init__(self, input_string: str, WrapNum: WrapNum):
        self.f = open(input_string, "r")
        self.w = WrapNum
        self.getDialMovement()

        self.f.close()

    def getDialMovement(self):
        for line in self.f:
            line = line.strip()
            if line.startswith("L"):
                steps = int(line[1:])
                self.w.GoLeft(steps)
            elif line.startswith("R"):
                steps = int(line[1:])
                self.w.GoRight(steps)
            self.w.checkZero()
        print(f"Part one {self.w.CountOfZero}")
        print(f"Part two {self.w.GetNewSecurityProtocolCountOfZero}")
        print(f"sum: {self.w.CountOfZero + self.w.GetNewSecurityProtocolCountOfZero}")


if __name__ == "__main__":
    main()
