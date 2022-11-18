## issue-05-what_is_year_now

Тестирование функции decode из файла `what_is_year_now.py` с помощью `pytest`


Само тестирование реализовано в файле `test_what_is_year_now.py`

Для запуска тестирования необходимо воспользоваться командой:
```commandline
python -m pytest -v test_what_is_year_now.py
```

Для записи результатов тестирования в файл `result` необходимо воспользоваться командой:
```commandline
python -m pytest -v test_what_is_year_now.py > result
```

Для проверки покрытия тестами  необходимо воспользоваться командой:
```commandline
python -m pytest -q test_what_is_year_now.py --cov
```

Для получения отчета по покрытию тестами в html-формате необходимо воспользоваться командой:
```commandline
python -m pytest -q test_what_is_year_now.py --cov . --cov-report html
```

Результаты тестов записаны в файл `result`