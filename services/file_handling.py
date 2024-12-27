import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end_signs = ',.!:;?'
    counter = 0
    if len(text) < start + size:
        size = len(text) - start
        text = text[start:start + size]
    else:
        if text[start + size] == '.' and text[start + size - 1] in end_signs:
            text = text[start:start + size - 2]
            size -= 2
        else:
            text = text[start:start + size]
        for i in range(size - 1, 0, -1):
            if text[i] in end_signs:
                break
            counter = size - i
    page_text = text[:size - counter]
    page_size = size - counter
    return page_text, page_size


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as tf:
        content = tf.read()
        start = 0
        page_num = 1
        while start < len(content):
            page_text, page_size = _get_part_text(content,start,PAGE_SIZE)
            start += page_size
            book[page_num] = page_text.strip()
            page_num += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[1], os.path.normpath(BOOK_PATH)))