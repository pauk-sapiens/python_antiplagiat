class CodePattern:

    def __init__(self, file):
        self.__code = {}
        self.__amount = 0
        with open(file, 'r', encoding='utf-8') as f:
            words = f.read().split()
            for word in words:
                if word not in self.__code.keys():
                    self.__code[word] = 1
                else:
                    self.__code[word] += 1
                self.__amount += 1

    def get_amount(self):
        return self.__amount

    def get_code(self):
        return self.__code


class PairedFile:

    def __init__(self, file: str):
        self.__pairs = []
        with open(file) as f:
            for line in f:
                self.__pairs.append(line.split())

    def get_pairs(self):
        return self.__pairs


print("Введите имя файла с парами файлов")
path = input()
print("Введите имя выходного файла")
out = input()
paths = PairedFile(path)
with open(out, 'w') as out:
    print("Выполнение...")
    for pair in paths.get_pairs():
        plagiates = 0
        code1 = CodePattern(pair[0])
        code2 = CodePattern(pair[1])
        for word in code1.get_code().keys():
            if word in code2.get_code().keys():
                plagiates += min(code1.get_code()[word], code2.get_code()[word])
        plagiates /= max(code1.get_amount(), code2.get_amount())
        out.write(str(round(plagiates, 3)) + "\n")
print("Done")


