from main import BooksCollector

import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    @pytest.fixture(scope='function')
    def create_book_one(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        return collector

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_two_same_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_set_rating_two(self, create_book_one):
        create_book_one.set_book_rating("Книга 1", 2)
        assert create_book_one.get_book_rating("Книга 1") == 2

    def test_get_book_rating_set_two_books(self, create_book_one):
        create_book_one.set_book_rating("Книга 1", 5)
        create_book_one.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert create_book_one.get_book_rating("Книга 1") == 5

    def test_get_books_with_specific_rating_rating_seven(self, create_book_one):
        create_book_one.add_new_book("Книга 2")
        create_book_one.add_new_book("Книга 3")
        create_book_one.add_new_book("Книга 4")
        create_book_one.set_book_rating("Книга 1", 7)
        create_book_one.set_book_rating("Книга 2", 7)
        create_book_one.set_book_rating("Книга 3", 7)
        collector_specific = create_book_one.get_books_with_specific_rating(7)
        assert ["Книга 1", "Книга 2", "Книга 3"] == collector_specific

    def test_get_books_rating(self, create_book_one):
        create_book_one.add_new_book("Книга 2")
        assert create_book_one.get_books_rating() == {"Книга 1": 1, "Книга 2": 1}

    def test_add_book_in_favorites(self, create_book_one):
        create_book_one.add_book_in_favorites('Книга 1')
        assert ['Книга 1'] == create_book_one.get_list_of_favorites_books()

    def test_delete_book_from_favorites_one_book_from_two_book_del(self, create_book_one):
        create_book_one.add_new_book("Книга 2")
        create_book_one.add_book_in_favorites('Книга 1')
        create_book_one.add_book_in_favorites('Книга 2')
        create_book_one.delete_book_from_favorites('Книга 1')
        assert ['Книга 1'] not in create_book_one.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, create_book_one):
        create_book_one.add_new_book("Книга 2")
        create_book_one.add_book_in_favorites('Книга 1')
        assert 'Книга 1' in create_book_one.get_list_of_favorites_books()
