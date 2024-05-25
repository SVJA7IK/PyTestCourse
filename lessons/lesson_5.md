### Pytest #5: Обработка исключений + Группировка тестов

Конспект по [видео](https://www.youtube.com/watch?v=oIO7TFHpWyo&list=PLeLN0qH0-mCVdHgdjlnKTl4jKuJgCK-4b&index=6)

Для группировки тесты можно объединять в классы. Название класса должно начинаться со слова Test. Например: `TestCalculator`.

Запуск определённого класса с тестами - `pytest tests/test_main.py::TestCalculator`