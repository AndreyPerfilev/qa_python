# QA_PYTHO N

Создана фикстура **create_book_one**.<br>
Создает объект collector класса BooksCollector и добавляет в коллекцию "Книга 1".

Тесты,которые удалось реализовать:

**1) test_add_new_book_add_two_books**<br>
Тест проверяет добавление двух разных книг в коллекцию.

**2) test_add_new_book_add_two_same_books**<br>
Тест проверяет, что при добавление двух одинаковых книг, добавится только одна

**3) test_set_book_rating_set_rating_two**<br>
Тест проверяет  что у книги установится рейтинг 2

**4) test_get_book_rating_set_two_books**<br>
Тест проверяет, что метод возращает рейтинг книги по названию

**5) test_get_books_with_specific_rating_rating_seven**<br>
Тест проверяет, что метод отбирает по указоному рейтингу   фильмы из  коллекции и добавляет их в список 

**6) test_get_books_rating**<br>
Тест проверяет, что метод возращает словарь с названием фильма и рейтингом фильма

**7) test_add_book_in_favorites**<br>
Тест проверяет, что метод добавляет книгу в список "favorites" избранное

**8) test_delete_book_from_favorites_one_book_from_two_book_del**<br>
Тест проверяет, что добавленная книга в "favorites" избранное удалена.

**9) test_get_list_of_favorites_books**<br>
Тест проверяет, что метод, возвращает список "favorites" избранное