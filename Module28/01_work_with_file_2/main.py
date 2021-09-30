import os
from typing import TextIO


class File:
    """
    Контекст менеджер как open

    """

    def __init__(self, file: str, method: str) -> None:
        """

        :param file: файл для чтения/записи. Если такого нет - создается новый в режиме записи
        :param method: режим чтения или записи
        """
        self._file = file
        self._method = method
        self._open_file = None

    def __enter__(self) -> TextIO:
        """

        :return: возвращает файловы объект
        """

        if self._file in os.listdir():
            self._open_file = open(self._file, self._method)
        else:
            print('Файла нет в каталоге! Создаем новый в режиме записи')
            self._open_file = open(self._file, 'w')
        print(type(self._open_file))
        return self._open_file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return: пропускает все ошибки
        """
        self._open_file.close()
        return True


with File('text3.txt', 'r') as my_f:
    my_f.write('kek')
