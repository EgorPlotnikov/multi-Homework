Итак, сегодняшняя работа на параллелизм и асинхронность.

# Задание 1. IO-bound. Проверяем ссылки на страницах Википедии.

После создания нового репозитория, подключаем его к PyCharm.
Далее создаём файл IO-bound.py для решения первого задания.
Копируем данным нам код, в котором берётся 100 случайных ссылок из Википедии. Все ссылки с каждого рандомного сайта википедии записываются в файл. После, мы синхронно, в один поток, оправшиваем каждую ссылку.

Замерим время синхронного, однопоточного исполнения файла. 
Время составило примерно 1 332 000 миллисекунд или 22 минуты.

Теперь перепишем код, используя TreadPoolExecutor. Для замера времени исполнения используем cProfile.
Многопоточное исполнение программы ускорило весь процесс.

1) С 5 воркерами время составило примерно 455 000 миллисекунд или 7 минут.
2) С 10 воркерами время составило примерно 327000 миллисекунд или 5 минут.
3) С 100 воркерами время составило примерно  миллисекунд или  минут.

Таким образом, хочется подвести итоги первого задания. Многопоточное исполнение программ, действительно, ускоряет процесс. Лишь при 5 воркерах процесс ускорился в 3 раза! Но стоит отметить, что при таком использовании процессор нагружается немного сильнее по сравнению с однопоточным исполнением.

# Задание 2. CPU-bound. Генерируем монетки

Я создал новый файл CPU-bound.py, в который поместил указанный код.
Время однопроцессного поиска десяти монеток составило примерно 1000 секунд.

Теперь перепишем наш код используя многопроцессное исполнение.
Запустив свеженаписанный код, программа действительно стала работать немного быстрей, примерно 800 секунд.
