class Book:
    def __init__(self, name, author, prize) -> None:
        self.name = name
        self.author = author
        self.prize = prize

    def get_prize(self) -> int:
        return self.prize

    def set_prize(self, prize) -> None:
        self.prize = prize


def main():
    book = Book("Cracking the coding interview", "Gayle Laakmann McDowell" , 29.87)
    print(f"Book Name :{book.name}\nAuthor: {book.author}")


main()
