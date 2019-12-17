class TelephoneBook():
    def __init__(self):
        self.book = dict()

    def add(self, number, name):
        self.book[number] = name

    def find(self, number):
        if number not in self.book.keys():
            return "not found"
        return self.book[number]

    def delete(self, number):
        if number in self.book.keys():
            self.book.pop(number)


def main():
    myBook = TelephoneBook()
    num_ops = int(input())
    for i in range(num_ops):
        op = list(input().split())
        if op[0] == 'add':
            myBook.add(int(op[1]), op[2])
        elif op[0] == 'find':
            print(myBook.find(int(op[1])))
        elif op[0] == 'del':
            myBook.delete(int(op[1]))

if __name__ == "__main__":
    main()