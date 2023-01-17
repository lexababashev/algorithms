import shutil

class NaturalSorting:
    def __init__(self, Apath: str, Bpath: str, Cpath: str):
        self.Apath = Apath
        self.Bpath = Bpath
        self.Cpath = Cpath

    def CopyFile(self, path: str):
        shutil.copy(path, self.Apath)

    def NaturalSort(self):
        while self.isSorted()!=True:
            self.divide()
            self.merge()

        Bfile = open(self.Bpath, "wb")
        Cfile = open(self.Cpath, "wb")
        Bfile.close()
        Cfile.close()

    def divide(self):
        Afile = open(self.Apath, "rb")
        Bfile = open(self.Bpath, "wb")
        Cfile = open(self.Cpath, "wb")

        flag = True
        current = Afile.read(4)
        next = Afile.read(4)
        while current:
            if flag:
                Bfile.write(current)
            else:
                Cfile.write(current)
            if current > next:
                flag = not flag
                # if flag:
                #     flag = False
                # else:
                #     flag = True
            current = next
            next = Afile.read(4)
        Afile.close()
        Bfile.close()
        Cfile.close()

    def merge(self):
        Afile = open(self.Apath, "wb")
        Bfile = open(self.Bpath, "rb")
        Cfile = open(self.Cpath, "rb")
        Bcurrent = Bfile.read(4)
        Ccurrent = Cfile.read(4)
        Bnext = Bfile.read(4)
        Cnext = Cfile.read(4)
        while Ccurrent and Bcurrent:
            if Bcurrent <= Bnext and Ccurrent <= Cnext:
                if Bcurrent <= Ccurrent:
                    Afile.write(Bcurrent)
                    Bcurrent = Bnext
                    Bnext = Bfile.read(4)
                else:
                    Afile.write(Ccurrent)
                    Ccurrent = Cnext
                    Cnext = Cfile.read(4)
            elif Bcurrent >= Bnext and Ccurrent <= Cnext:
                while Ccurrent <= Cnext:
                    if Bcurrent <= Ccurrent:
                        Afile.write(Bcurrent)
                        Bcurrent = Bnext
                        Bnext = Bfile.read(4)
                        while Ccurrent <= Cnext:
                            Afile.write(Ccurrent)
                            Ccurrent = Cnext
                            Cnext = Cfile.read(4)
                        Afile.write(Ccurrent)
                        Ccurrent = Cnext
                        Cnext = Cfile.read(4)
                        break
                    else:
                        Afile.write(Ccurrent)
                        Ccurrent = Cnext
                        Cnext = Cfile.read(4)
            elif Ccurrent >= Cnext and Bcurrent <= Bnext:
                while Bcurrent <= Bnext:
                    if Ccurrent <= Bcurrent:
                        Afile.write(Ccurrent)
                        Ccurrent = Cnext
                        Cnext = Cfile.read(4)
                        while Bcurrent <= Bnext:
                            Afile.write(Bcurrent)
                            Bcurrent = Bnext
                            Bnext = Bfile.read(4)
                        Afile.write(Bcurrent)
                        Bcurrent = Bnext
                        Bnext = Bfile.read(4)
                        break
                    else:
                        Afile.write(Bcurrent)
                        Bcurrent = Bnext
                        Bnext = Bfile.read(4)
            else:
                if Ccurrent <= Bcurrent:
                    Afile.write(Ccurrent)
                    Afile.write(Bcurrent)
                else:
                    Afile.write(Bcurrent)
                    Afile.write(Ccurrent)
                Ccurrent = Cnext
                Cnext = Cfile.read(4)
                Bcurrent = Bnext
                Bnext = Bfile.read(4)
        if not Bcurrent and Ccurrent:
            while Ccurrent:
                Afile.write(Ccurrent)
                Ccurrent = Cnext
                Cnext = Cfile.read(4)
        elif not Ccurrent and Bcurrent:
            while Bcurrent:
                Afile.write(Bcurrent)
                Bcurrent = Bnext
                Bnext = Bfile.read(4)
        Afile.close()
        Bfile.close()
        Cfile.close()

    def ShowFirstElementsOfArray(self, path: str):
        with open(path, "rb") as file:
            s = ""
            for i in range(100):
                s = s + str(int.from_bytes(file.read(4), byteorder="big")) + " "
        print(s)

    def isSorted(self):
        Afile = open(self.Apath,"rb")
        current = Afile.read(4)
        next = Afile.read(4)
        while next:
            if current > next:
                Afile.close()
                return False
            current = next
            next = Afile.read(4)
        Afile.close()
        return True