## issue-01-encode

Тестирование функции encode из файла morse.py с помощью `doctest`


Само тестирование реализовано в файле `test_encode.py`

Для запуска тестирования необходимо воспользоваться командой:
```commandline
python -m doctest -v -o NORMALIZE_WHITESPACE test_encode.py
```

Для выгрузки результатов в файл result необходимо воспользоваться командой:
```commandline
python -m doctest -v -o NORMALIZE_WHITESPACE test_encode.py > result
```

Результаты тестов уже записаны в файл `result`