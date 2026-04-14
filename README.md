Список тестов.

1. def test_add_new_book_valid_name - проверяет возможность добавления книги с валидной длинной названия в список.

2. def test_add_new_book_duplicate_not_added - проверяет, что в список нельзя добавить две одинаковые книги.

3. def test_set_book_genre_valid_genre - проверяет, что у книги установлен правильный жанр из имеющегося списка.

4. def test_get_book_genre_existing_book - проверяет вывод жанра по наименованию книги из словаря.

5. def test_get_book_genre_nonexistent_book- вместо жанра выводит None, если книги нет в словаре.

6. def test_get_books_with_specific_genre - проверка вывода списка книг по жанрам.

7. def test_get_books_for_children_with_rated_books - проверка, что для детей возвращаются книги без возрастного рейтинга.

8. def test_add_book_in_favorites_success - добавление книги из общего списка в избранное.

9. def test_add_book_in_favorites_book_not_in_books_genre - проверяет, что невозможно добавить книгу в избранное, если она отсутствует в библиотеке.

10. def test_delete_book_from_favorites_success - проверяет удаление книги из избранного списка.

11. def test_get_list_of_favorites_books_with_favorites - проверяет получение списка избранных книг.

12. def test_get_list_of_favorites_books_after_deletion- проверка списка избранных книг, после удаление из него одной из книг.
