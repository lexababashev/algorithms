from NaturalSort import NaturalSorting
#from random import randint

# def CreateFile(path: str, numOfElements: int, maxElement: int):
#     with open(path, "wb") as file:
#         for i in range(numOfElements):
#             file.write(randint(0, maxElement).to_bytes(4, byteorder="big"))



def main():

    sorting = NaturalSorting("A.bin", "B.bin", "C.bin")
    sorting.CopyFile("10Mb.bin")

    sorting.ShowFirstElementsOfArray("A.bin")
    print("\n====================================================\n")
    sorting.NaturalSort()
    sorting.ShowFirstElementsOfArray("A.bin")

    if sorting.isSorted():
        print("array is succesfully sorted!\n")

if __name__ == "__main__":
    main()