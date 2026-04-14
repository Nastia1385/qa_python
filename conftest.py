import pytest

from main import BooksCollector


@pytest.fixture
def collector_with_books():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    collector.add_new_book("Властелин колец")
    collector.add_new_book("Шерлок Холмс")
    collector.add_new_book("Кошмар на улице Вязов")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    collector.set_book_genre("Шерлок Холмс", "Детективы")
    collector.set_book_genre("Кошмар на улице Вязов", "Ужасы")
    return collector


# Фикстура для коллектора с избранными книгами
@pytest.fixture
def collector_with_favorites(collector_with_books):
    collector_with_books.add_book_in_favorites("Гарри Поттер")
    collector_with_books.add_book_in_favorites("Шерлок Холмс")
    return collector_with_books


# Фикстура для пустого коллектора (базовая)
@pytest.fixture
def empty_collector():
    return BooksCollector()
