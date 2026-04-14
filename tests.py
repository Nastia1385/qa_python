import pytest


class TestBooksCollector:

    # 1. Тесты для add_new_book с использованием фикстуры и параметризации
    @pytest.mark.parametrize("name", [
        "Гарри Поттер",
        "a" * 40,
    ])
    def test_add_new_book_valid_name(self, empty_collector, name):
        empty_collector.add_new_book(name)
        assert name in empty_collector.books_genre

    def test_add_new_book_duplicate_not_added(self, collector_with_books):
        initial_count = len(collector_with_books.books_genre)
        collector_with_books.add_new_book("Гарри Поттер")
        assert len(collector_with_books.books_genre) == initial_count

    # 2. Тест для set_book_genre
    @pytest.mark.parametrize("genre", ["Фантастика", "Комедии", "Мультфильмы"])
    def test_set_book_genre_valid_genre(self, collector_with_books, genre):
        collector_with_books.set_book_genre("Властелин колец", genre)
        assert collector_with_books.books_genre["Властелин колец"] == genre

    # 3. Тесты для get_book_genre
    def test_get_book_genre_existing_book(self, collector_with_books):
        assert collector_with_books.get_book_genre("Гарри Поттер") == "Фантастика"

    def test_get_book_genre_nonexistent_book(self, collector_with_books):
        assert collector_with_books.get_book_genre("Нет такой книги") is None

    # 4. Тесты для get_books_with_specific_genre
    @pytest.mark.parametrize("target_genre, expected_books", [
        ("Фантастика", ["Гарри Поттер"]),
        ("Детективы", ["Шерлок Холмс"]),
        ("Ужасы", ["Кошмар на улице Вязов"]),
        ("Комедии", []),
        ("Мультфильмы", [])
    ])
    def test_get_books_with_specific_genre(self, collector_with_books, target_genre, expected_books):
        result = collector_with_books.get_books_with_specific_genre(target_genre)
        assert result == expected_books

    # 5. Тест для get_books_genre
    def test_get_books_genre_returns_correct_dict(self, collector_with_books):
        expected = {
            "Гарри Поттер": "Фантастика",
            "Шерлок Холмс": "Детективы",
            "Кошмар на улице Вязов": "Ужасы",
            "Властелин колец": ""
        }
        books_genre = collector_with_books.get_books_genre()
        assert books_genre == expected

    # 6. Тесты для get_books_for_children
    @pytest.mark.parametrize("expected_children_books", [
        ["Гарри Поттер"],  # Фантастика без рейтинга
    ])
    def test_get_books_for_children_with_rated_books(self, collector_with_books, expected_children_books):
        result = collector_with_books.get_books_for_children()
        assert "Шерлок Холмс" not in result  # Детективы с рейтингом
        assert "Ночной дозор" not in result  # Ужасы с рейтингом
        assert result == expected_children_books

        # 7. Тесты для add_book_in_favorites

    def test_add_book_in_favorites_success(self, collector_with_books):
        collector_with_books.add_book_in_favorites("Властелин колец")
        assert "Властелин колец" in collector_with_books.favorites

    def test_add_book_in_favorites_book_not_in_books_genre(self, empty_collector):
        empty_collector.add_book_in_favorites("Нет в библиотеке")
        assert "Нет в библиотеке" not in empty_collector.favorites

    # 8. Тесты для delete_book_from_favorites
    def test_delete_book_from_favorites_success(self, collector_with_favorites):
        collector_with_favorites.delete_book_from_favorites("Гарри Поттер")
        assert "Гарри Поттер" not in collector_with_favorites.favorites

    # 9. Тесты для get_list_of_favorites_books
    def test_get_list_of_favorites_books_with_favorites(self, collector_with_favorites):
        result = collector_with_favorites.get_list_of_favorites_books()
        assert result == ["Гарри Поттер", "Шерлок Холмс"]

    def test_get_list_of_favorites_books_after_deletion(self, collector_with_favorites):
        collector_with_favorites.delete_book_from_favorites("Гарри Поттер")
        assert collector_with_favorites.get_list_of_favorites_books() == ["Шерлок Холмс"]
