class Book():
    def __init__(self, name, author, isbn):
        self.name = name
        self.author = author
        self.unique_number = isbn
        self.__is_available = True

    def __str__(self):
        return f"{self.name} - {self.author}, {self.unique_number}"

    def borrow(self):
        self.__is_available = False

    def return_b(self):
        self.__is_available = True

    def check_availability(self):
        return self.__is_available

class LibraryMember():
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f'{self.name}, {self.member_id}'

    def borrow_book(self, book):
        book.borrow()
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_b()

    def get_borrowed_books(self):
        return self.borrowed_books

class Library():
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.unique_number] = book

    def add_member(self, member):
        self.members[member.member_id] = member

    def give_book(self, isbn, member_id):
        if isbn not in self.books:
            print("Такая Книга не Найдена")
            return
        if member_id not in self.members:
            print("Такой Читатель не Найден")
            return
        book = self.books[isbn]
        member = self.members[member_id]
        if book.check_availability() == False:
            print("Книга Недоступна!")
            return
        book.borrow()
        member.borrow_book(book)
        print("Книга Успешно Выдана!")

    def receive_book(self, isbn, member_id):
        if isbn not in self.books:
            print("Такая Книга не Найдена")
            return
        if member_id not in self.members:
            print("Такой Читатель не Найден")
            return
        book = self.books[isbn]
        member = self.members[member_id]
        if book.check_availability():
            print("Книга уже Возвращена")
            return
        if book not in member.borrowed_books:
            print("Читатель не Брал эту Книгу")
            return
        book.return_b()
        member.return_book(book)
        print("Книга Успешно Возвращена!")

class LibraryApp():
    def __init__(self):
        self.library = Library()

    def run(self):
        while True:
            response = input("Введите Латинскую X для Выхода или Другую Букву для Продолжения: ")
            if response.upper() == 'X':
                break
            
            print("\n=== Система Управления Библиотекой ===\n")
            print("Функционал Приложения:")
            print("1 - Добавить Книгу")
            print("2 - Добавить Читателя")
            print("3 - Выдать Книгу")
            print("4 - Вернуть Книгу")
            print("5 - Вывести Информацию о Книгах Читателя")
            print("6 - Вывести Информацию о Книге")
            print("7 - Вывести все Существующие Книги")
            
            action = input("Выберите Действие: ")
            if action in ['1', '2', '3', '4', '5', '6', '7']:
                if action == '1':
                    name = input("Введите Название Книги: ")
                    author = input("Введите Автора Книги: ")
                    unique_number = input("Введите Уникальный Номер для Книги: ")
                    try:
                        book = Book(name, author, unique_number)
                        self.library.add_book(book)
                        print(f"Книга {name} Успешно Добавлена!")
                    except Exception as e:
                        print(f"Ошибка при Добавлении Книги: {e}")
                if action == '2':
                    name = input("Введите Имя Читателя: ")
                    member_id = input("Введите Уникальный ID Читателя: ")
                    try:
                        member = LibraryMember(name, member_id)
                        self.library.add_member(member)
                        print(f"Читатель {name} Успешно Добавлен!")
                    except Exception as e:
                        print(f"Ошибка при Добавлении Читателя: {e}")
                if action == '3':
                    try:
                        unique_number = input("Введите Уникальный Номер Книги: ")
                        member_id = input("Введите Уникальный ID Читателя: ")
                        self.library.give_book(unique_number, member_id)
                    except Exception as e:
                        print(f"Произошла Ошибка {e}")
                if action == '4':
                    try:
                        unique_number = input("Введите Уникальный Номер Книги: ")
                        member_id = input("Введите Уникальный ID Читателя: ")
                        self.library.receive_book(unique_number, member_id)
                    except Exception as e:
                        print(f"Произошла Ошибка {e}")
                if action == '5':
                    member_id = input("Введите Уникальный ID Читателя: ")
                    try:
                        if member_id in self.library.members:
                            member = self.library.members[member_id]
                            borrowed_books = member.get_borrowed_books()
                            if borrowed_books:
                                print(f"Книги, Взятые Читателем {member.name} ({member_id}):")
                                for book in borrowed_books:
                                    print(f"- {book}")
                            else:
                                print(f"У Читателя {member.name} ({member_id}) нет Взятых Книг")
                        else:
                            print(f"Читатель с ID {member_id} не Найден")
                    except Exception as e:
                        print(f"Произошла Ошибка {e}")
                if action == '6':
                    unique_number = input("Введите Уникальный Номер Книги: ")
                    if len(unique_number) == 0:
                        print("Введён Пустой Уникальный Номер")
                    elif unique_number in self.library.books:
                        try:
                            book = self.library.books[unique_number]
                            print("Информация о Книге: ", book)
                        except Exception as e:
                            print(f"Произошла Ошибка {e}")
                    else:
                        print(f"Уникального Номера {unique_number} не Существует")
                if action == '7':
                    if self.library.books:
                        for book in self.library.books.values():
                            print(f"Название Книги: {book}")
                    else:
                        print("На Данный Момент Книги Отсутствуют")
            else:
                print("Неверное Действие, Попробуйте ещё")

library_system = LibraryApp()
library_system.run()
