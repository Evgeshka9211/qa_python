from main import BooksCollector
import pytest

class TestBooksCollector:

    @pytest.mark.parametrize('name', ['Шрек', 'Букварь', 'Дюймовочка'])
    def test_add_new_book_add_three_books(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        # проверяем, что книга добавилась, длина словаря стала равна 1
        assert (len(collector.books_genre) == 1)

    def test_set_book_genre_set_correct_genre_to_exists_book(self):
        #создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        #добавляем в справочник новую книгу 'Шрек'
        collector.add_new_book('Шрек')
        #задаем для книги Шрек значение жанра Мультфильмы
        collector.set_book_genre('Шрек','Мультфильмы')
        #проверяем, что для книги 'Шрек' появилось значение жанра
        assert len(collector.books_genre.get('Шрек')) > 0

    def test_get_book_genre_get_correct_name_of_exists_book(self):
        #Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        #Добавляем в справочник новую книгу 'Шрек'
        collector.add_new_book('Шрек')
        #Задаем для книги Шрек значение жанра 'Мультфильмы', используя метод set_book_genre
        collector.set_book_genre('Шрек', 'Мультфильмы')
        #Получаем значение жанра для книги Шрек через метод get_book_genre
        book_genre_result = collector.get_book_genre('Шрек')
        #Проверяем что полученное значение совпадает с ранее установленным
        assert book_genre_result == 'Мультфильмы'

    def test_get_books_with_specific_genre_get_two_books_from_three(self):
        #Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        #Добавляем в справочник три книги
        collector.add_new_book('Пункт назначения')
        collector.add_new_book('Шрек')
        collector.add_new_book('Пила')

        #Задаем значения жанра для книг из справочника
        collector.set_book_genre('Пункт назначения', 'Ужасы')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        collector.set_book_genre('Пила', 'Ужасы')

        #Получаем список книг с жанром Ужасы
        horror_books = collector.get_books_with_specific_genre('Ужасы')
        #проверяем, что длина списка полученных книг с заданным жанром равна 2
        assert len(horror_books) == 2

    def test_get_books_genre_get_three_items(self):
        # Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # Добавляем в справочник три книги
        collector.add_new_book('Пункт назначения')
        collector.add_new_book('Шрек')
        collector.add_new_book('Пила')

        #Задаем значения жанра для книг из справочника
        collector.set_book_genre('Пункт назначения', 'Ужасы')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        collector.set_book_genre('Пила', 'Ужасы')
        #Получаем содержимое словаря
        book_genres = collector.get_books_genre()
        #Проверяем, что словарь содержит 3 ключа и у каждого задано значение
        assert len(book_genres) == 3 and book_genres['Пункт назначения'] and book_genres['Шрек'] and book_genres['Пила']

    def test_get_books_for_children_get_two_books_from_three(self):
        #Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # Добавляем в справочник 4 книги
        collector.add_new_book('Пункт назначения')
        collector.add_new_book('Шрек')
        collector.add_new_book('Пила')
        collector.add_new_book('Дюймовочка')

        #Задаем значения жанра для книг из справочника
        collector.set_book_genre('Пункт назначения', 'Ужасы')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.set_book_genre('Дюймовочка', 'Мультфильмы')

        #Получаем из справочника список книг для детей
        children_books = collector.get_books_for_children()
        #Проверяем, что результат попали только две книги из 4-х
        assert len(children_books) == 2 and 'Шрек' in children_books and 'Дюймовочка' in children_books

    def test_add_book_in_favorites_add_one_book_in_favorites(self):
        #Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        #Добавляем в справочник книгу
        collector.add_new_book('Шерлок Холмс')
        #Добавляем книгу из справочника в избранное
        collector.add_book_in_favorites('Шерлок Холмс')
        #Проверяем, что списке избранного появилась новая запись
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_delete_one_book_from_two(self):
        #Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        #Добавляем в справочник две книги
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Шрек')
        #Добавляем обе книги из справочника в избранное
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.add_book_in_favorites('Шрек')
        #Удаляем одну книгу из избранного
        collector.delete_book_from_favorites('Шерлок Холмс')
        #Проверяем, что списке избранного осталась одна запись
        assert len(collector.favorites) == 1

    def tets_get_list_of_favorites_books_get_two_books(self):
        # Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # Добавляем в справочник две книги
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Шрек')
        #Добавляем обе книги из справочника в избранное
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.add_book_in_favorites('Шрек')
        #Получаем список избранного методом get_list_of_favorites_books
        favorite_books = collector.get_list_of_favorites_books()
        #Проверяем, количество записей в полученном списке соответствует количеству добавленных книг
        assert len(favorite_books) == 2