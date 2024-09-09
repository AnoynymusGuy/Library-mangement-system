class Library: 
    books = []

    def __init__(self, boooklist):
        self.books = boooklist
    def display(self):
        for l in self.books:
            print(l)

booklist = ["Unbound", "Hari Puttar", "Sherby Homless", "Monk who bought a ferrari"]

library = Library(booklist)

while True:
    print("\n---- Library Menu ----\n")
    print("1. Display available books")
    print("2. Get ou..Borrow a book")
    print("3. Buy a book :)")
    print("4. Return a book")
    print("5. Leave(me alone)")
    choice = input("Enter the option [1\ 2\ 3\ 4]: ")

    if choice == "1":
        library.display()
    elif choice == "4":
        break
    else:
        print("You chose the wrong option you idi...-_-")
