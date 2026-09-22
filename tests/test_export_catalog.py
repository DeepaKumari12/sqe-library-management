import pytest

from library.library import Library, LibraryIOError
from library.book import Book


def _library_with_one_book():
    """Helper: a Library holding a single 2-copy book."""
    library = Library()
    library.add_book(Book('Clean Code', '9780132350884', 'R. Martin', total_copies=2))
    return library


def test_export_catalog_writes_expected_content(mocker):
    """mocks open() so no real file is written, and checks write() got the
    expected content.
    """
    # Arrange
    library = _library_with_one_book()
    m = mocker.mock_open()
    mocker.patch('builtins.open', m)

    # Act
    library.export_catalog('catalog.txt')

    # Assert
    m.assert_called_once_with('catalog.txt', 'w')
    handle = m()
    handle.write.assert_called_once_with('Clean Code,9780132350884,2/2\n')


def test_export_catalog_wraps_os_error(mocker):
    """mocks open() to raise OSError, and checks export_catalog() raises
    our own LibraryIOError instead of leaking the raw OSError.
    """
    # Arrange
    library = _library_with_one_book()
    mocker.patch('builtins.open', side_effect=OSError('disk full'))

    # Act / Assert
    with pytest.raises(LibraryIOError):
        library.export_catalog('catalog.txt')
