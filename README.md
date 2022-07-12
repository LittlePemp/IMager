# IMager bot
## О чем речь?
IMager - пакет, позволяющий собрать картинку из картинок, тематично скачанных с сайта [Fonwall](fonwall.com), или собственноручно загруженных.

IMager bot - телеграм бот, реализующий интерфейс пользователя для пакета IMager.

## Каков в действии
|   |   |
|---|---|
|<img src="https://downloader.disk.yandex.ru/preview/2d4a9782abeb07572815ced6f1da2b586a770622aa5e6fce5d524804b6cd334b/62ce1a88/ku_u4IexMttnBzOJ19yoMVjB7ldIQEXtUu6due9OMS-c_5AwZFljUsoP2KvvmA3TvBrwKkzYHLBQSd7KfWAQeQ%3D%3D?uid=0&filename=5.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964" width="100%">|<img src="https://downloader.disk.yandex.ru/preview/808ede7f44daac32b4757a66fa119e2b72b01788bdaf3b4e2ed35f9534cc958d/62ce1aac/JBwRimG7zatDeoOQZEniFljB7ldIQEXtUu6due9OMS_Lvvo0P2PVI2mSuhCkK_xpGdaHvS8iNxq0hTSLcS2atg%3D%3D?uid=0&filename=6.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964" width="100%">|

![result_chat](https://downloader.disk.yandex.ru/preview/09d35ef798534bff9bd8ee7c0fe3ae8f47feaaaa920c1175b538b993ec0cbbd9/62ce1b0b/eMteB1EgLOmCnc6dPXXlkmOKYAIwIKVOkaqDDe-QUywSs891zREiDw58SctLn3q5IK-tEE_8NN21X8bUXAzSbA%3D%3D?uid=0&filename=3.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964)

## Поэтапно
### Общее
При старте бота `/start` он здоровается и предлагает на выбор общие команды:
1. /Начать
2. /Поддержать
3. /Помощь

![](https://downloader.disk.yandex.ru/preview/8aaca73d4e2f7e7ec73b2164f957a6768db395a185a0078c9f78307d1b841133/62ce1b3f/VyjjruFdx5YwRO-8Befuvcv9q-9fTrBnExqmdM1MfaLrDEI9mDvQvHvSnXj4OOFAJnLT772s2rkN5nC3xBAKtw%3D%3D?uid=0&filename=7.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964)

##### 1. Начать
Команда `/Начать` инициализирует FSM.

##### 2. Поддержать
Команда `/Поддержать` выводит информацию для поддержки разработчка (Кнопка для красоты).

##### 3. Помощь
Команда `/Помощь` выводит сообщение `/start` (со скриншота выше).

##### (+) 4. В начало
В дальнейших состояниях появится кнопка `В начало`, переводящая в общее меню. 

---
#### /Начать - Выбрать тему
Входим в FSM

![](https://downloader.disk.yandex.ru/preview/937551f455863b3c7d1177fe9e36e820fd3a4ca5cf349fb6a6e7e36474c49446/62ce1b68/4vRNhDfT8uaL_IEmTJlm34IINfzBHo08P-KvEJZ6CKG5i-Kk6CjeXArdZym1eWD5M9qUW44N5HDbuvt7y7SsdQ%3D%3D?uid=0&filename=8.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964)

На выбор предоставляется набор тем для заполнения. Данный набор регулируется разработчкиом.

#### Выбрать степень шума
![](https://downloader.disk.yandex.ru/preview/682ddb631856ab409bd30ca61c610c87522af981f21468466e3085e59206b8c0/62ce1be2/3RN4UWh8xZD8gCTlqpUmmfrvnNftrqLWdLs7cUe8cP3iGws06i2C7TC8l5jrtvrxRDEzvkAjPiqbZzoV6ulncw%3D%3D?uid=0&filename=9.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964)

После выбранной темы предлагается выбрать [степень шума](#1-степень-шума).

---
#### Выбрать размер изображения
![](https://downloader.disk.yandex.ru/preview/46efb9e6f2f51ad306f599644e4c2d25786ae80e9e45d0a8604486de376fc95a/62ce1d15/N2nt-3-RSLFFL1YIKPe22I8Dcj9fdKD-tzVB1fxhm7dgwNe2mCObGJe2wUkF-SHyD9XDGXgtBDvhWZ0elTgNjw%3D%3D?uid=0&filename=15.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964)

После выбранной степени шума предлагается выбрать [размер изображения](#2-размер-изображения).

#### Загрузка картинки, ожидание и результат

![](https://downloader.disk.yandex.ru/preview/c2f38ab07d289e67ec019da8c38adf2912ba24aeb149d022ba29d5093759a5fe/62ce1d4e/aSsYIesUkt3TJlF_NwFs7QW3k1IvT6CkWbzCFbmVDSbPxcN6n26T_OIveohkniFboNcCjCcdo-hCB9t5Dwr5eA%3D%3D?uid=0&filename=13.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964)

После выбранного размера картинки предлагается загрузить картинку.<br>
Результат присылается файлом в формате *.png.

## Технологии
* Python 3.9+
* Pillow
* Poetry
* Sqlite3
* git
* linux
* VSCode/Sublime Text 3

## Дополнительныая информация об исполнении
### Наложение оригинала
На каждую собранную картинку сверху накладывается оригинал.<br>
Это позволяет сгладить "неровности" вставленных картинок и подогнать к оригиналу.

Оригинал конвертируется в RGBA с установленным альфа-каналом 120/256, что дает такой результат...

Данные:
|Тема|Степень шума|Размер|Картинка|
|---|:---:|---|---|
|Котики|Средняя|Большое|Случайная|

| Без наложения | С наложением |
|:---:|:---:|
|<img src="https://downloader.disk.yandex.ru/preview/f263f8c7727efeb6b768f859d2cee94346d16de67f2cabeab759fee2289ee933/62ce1e7e/ejO60w5I6znwfJZiq4ueNY1bdxR4zs2Vx3Fq2ZeBOz7Pi9XlA28Cu6VBCSxxtq4PkxNoQQa-bC2kU6caNYYfJQ%3D%3D?uid=0&filename=5.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=1920x964" width="100%">|<img src="https://downloader.disk.yandex.ru/preview/6457ad8afc9c8eeb351add6c8d961d700d557c348ac6e6b6568149929ae608f1/62ce1e49/2li48zJtiPQKD9hRroxPJxCt13IprY8ex6qm6UhN1ey-esfy9MdvsEA9Sx_muJeGGFq_gldEWpUM8KxV44Hf4A%3D%3D?uid=0&filename=4.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=1920x964" width="100%">|

### Нагрузка на оперативную память
Для ускоренной работы приложения и сборки в оперативной памяти хранится информация:
* rgb + имя каждой картинки из используемых тем.
* Объекты каждой прочитанной в картинки изиспользуемых тем.
Даже с учетом обычного [набора данных](#наборы-картинок) программа занимает ±200Мб ОЗУ.

## Установка
1. Клонировать репозиторий

```git clone git@github.com:LittlePemp/IMager.git```

2. Установить зависимости<br>
Для работы с менеджером пакетов Poetry можно воспользоваться [шпаргалками](https://habr.com/ru/post/593529/)

3. Настраиваем под запуск бота<br>
Приложение работает с помощью управляющего скрипта и [командами](#3-команды-приложения) к нему.

## Приложение
### [0] Тестовые данные
#### Наборы картинок:
*Высота картинок в среднем 750px
1. Котики (2 282 картинки)
2. Аниме (733 картинки)
3. Дота (1 209 картинок)
#### Степени шума:
1. Нет (0)
2. Среднее (от 0 до 12 )
3. Сильно (от 12 др 30)
#### Размеры собранного изображения:
1. 25 картинок
2. 50 картинок
3. 100 картинок
### [1] Степень шума.
Степень шума - важный параметр, используемы для сборки картинки.

О важности наличия шума в аудиотреках, изображениях и тд. можно много говорить: советую ознакомиться с данной статьей ["Эстетика шума в аналоговой музыке"](https://habr.com/ru/post/403927/). В ней поднимаются достаточно интересные вопросы.

Что на практике?

Рассмотрим важность шума на практике.<br>
Каждое поле RGB хранит по 256 значений (8 бит) для обычных картинок. Чтобы покрыть каждое возможное значение цвета потребуется 256^3 (2^24) картинок.<br>
Во-первых, практически невозможно найти, например, (0, 0, 255) адекватную картинку, если не просто синий квадрат, от чего не смысла.<br>
Во-вторых, иметь и обрабатывать такое количество изображений $-$ безумство.

Поэтому на картинку, соответствующей определенному цвету, претендуют остальные цвета, находящиеся рядом.

Из этого следуют некоторые решения:<br>
1. Если определенному набору $RGB(r, g, b)$ соответствует несколько близжайших по среднему цвету картинок {$A_1(r_1, g_1, b_1)$, $A_2(r_2, g_2, b_2)$, $A_3(r_3, g_3, b_3)$ ...} с расстояниями {$ρ_{1}, ρ_{2}, ρ_{3} ...$}, где<br>(1) $ρ_{1} <= ρ_{2} <= ρ_{3} <= ...$ соответственно, а <br>$ρ_{i} = \sqrt{(r_{i} - r)^2 + (g_{i} - g)^2 + (b_i - b)^2}$. Чтобы найти новую, но достаточно близкую картинку, посчитаем новые значения $ρ_{i}^{*} = |ρ_{i} - randint(rand1, rand2)|$, где $0 <=rand1, rand2$ - значение разброса. После чего утверждать, что условие (1) выполняется для $ρ_{i}$ нельзя
2. Либо напрямую изменить каждое поле и также иcкать ближайшее:<br>$RGB^*(r ± randint(rand3),$<br>    $g ± randint(rand3),$<br>    $b ± randint(rand3))$<br> где $rand3 \simeq \sqrt[3]{(rand2)}$.

Из этого следует следующий эффект:

**1. Отсутствие шума. Плохой расклад.**

Данные:
|Тема|Степень шума|Размер|Картинка|
|---|:---:|---|---|
|Дота|Нет|Большое|Градиент|

<details><summary>Оригинал</summary><br>
<img src = "https://downloader.disk.yandex.ru/preview/eac7554c84bd9c2597164a1d59b6300be26e94a792f8797548efeb703882cba1/62ce18f2/emJjdxILAJ4vz3qyzsOtQHx9aSVpcUVwNpbEfZtCjQoFDx6fWAo2VQG55IDnT6WG6ojwzvOrOuu6eKYLynYlPQ%3D%3D?uid=0&filename=1.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=1920x964"></details>

<details><summary>Результат</summary><br>
<img src = "https://downloader.disk.yandex.ru/preview/053e9cb9576dbf51ad710c85cba08ea99af25b9236171ecc554d7661ebeaf047/62ce1ef4/pMxRKNXxFwCXO-qghtA3SzUYnt7TZ_-CTxIHmArDOnxookjBTYeGl3aX8Bcu9wMdZu38eocK8VwFGqBAQlIevQ%3D%3D?uid=0&filename=1.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964"></details>

<details><summary>Увеличение</summary><br>
<img src = "https://downloader.disk.yandex.ru/preview/4f051e49063f8c2dd53d073d3bbd3665a1af6f1467b09df56cbf06f78892e665/62ce1f4c/reZoNrAf13orNhkFphdxUYTmOZrvPw9JOaehh4-3GfXMq3RiVhF7M_Ftr7soDJdVZ4NX1ktZzku0gx0L988aDw%3D%3D?uid=0&filename=10.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964"></details>

Заметно, что при таком раскладе происходит по теории выше. Одна картинка охватывает некоторый диапазон цветов.

**2. Сильный шум. Хорошый расклад**

Данные:
|Тема|Степень шума|Размер|Картинка|
|---|:---:|---|---|
|Дота|Сильно|Большое|Градиент|

<details><summary>Оригинал</summary><br>
<img src = "https://downloader.disk.yandex.ru/preview/eac7554c84bd9c2597164a1d59b6300be26e94a792f8797548efeb703882cba1/62ce18f2/emJjdxILAJ4vz3qyzsOtQHx9aSVpcUVwNpbEfZtCjQoFDx6fWAo2VQG55IDnT6WG6ojwzvOrOuu6eKYLynYlPQ%3D%3D?uid=0&filename=1.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=1920x964"></details>

<details><summary>Результат</summary><br>
<img src = "https://downloader.disk.yandex.ru/preview/aa86abff17abb6302bc55c205dd3c7a43741dbce9125c53ca9ab3304727f558d/62ce1fa2/AOmgItN9GWfsX4s5no42nRcnMFbvgF2YkCPb8r7zzAB3HMkT_eROpMuyQiR8CWPrcy9HV-KMs8i0AbOzKzPcdQ%3D%3D?uid=0&filename=2.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964"></details>

<details><summary>Увеличение</summary><br>
<img src = "https://downloader.disk.yandex.ru/preview/c76693b52dab450dccd72a65b6891ebcfe3c152e131ed306c91802fc01abcd77/62ce1fc8/saiKC1YKgGh7_3lHeFKoD1ZDZDkamflnNvaQbAo_FhIoo-4rFg_cEgCRcsAE1_hooZq-erRa3dsWV5w59GmuAg%3D%3D?uid=0&filename=11.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964"></details>

В данном случае это выглядит намного органичнее.

**3. Отсутствие шума. Хороший расклад.**

Стоит отметить, что при уже пестрой картинке наличие шума будет излишним.

Данные:
|Тема|Степень шума|Размер|Картинка|
|---|:---:|---|---|
|Дота|Сильно|Большое|Пестрая|

<details><summary>Оригинал</summary><br>
<img src = "https://sun9-4.userapi.com/impg/V_rjxVpoi9PPSPIsYhWDF9wub9rA9gqbfWt_5Q/ehN-DuDsRmY.jpg?size=1280x590&quality=96&sign=12bd88416bd6bf5427a52445f33cb7b2&type=album"></details>

<details><summary>Результат</summary><br>
<img src = "https://downloader.disk.yandex.ru/preview/837cc18110fa4c8ab06d254eb627cb23f32a32ad6985744a357a5627829ccbd7/62ce2093/5WBNjo5yKJhCXd4wP17aZU9EudBnFE0LTRZ3M-Z-I1g1jRL1gIrxUgFuSqiL0anLIXn_gu8GzzufswintWHnbw%3D%3D?uid=0&filename=4.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964"></details>

<details><summary>Увеличение</summary><br>
<img src = "https://downloader.disk.yandex.ru/preview/52d12c201227ed35b978ed9104f8b059f26266360c9cc75a0e9670c8568b4ce2/62ce20bd/fgneCgxqVdcI7j7Kuao1S_5mkOpocGJVBAK_se0noqcSZabIxdIIF1IzuZkA-MMiSZZQOtPWVZJ7N8S-toyUoQ%3D%3D?uid=0&filename=12.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964"></details>

Как видно, данная картинка отлично смотрится при отсутствии шума. С сильным шумом тут будет просто хаос.

### [2] Размер изображения.
"Размеры изображения" (далее - размер изображения, разрешение) устанавливаются разработчиком и в совокупе с размером вставляемой картинкой ограничиваются библиотекой python `Pillow`.

Размер изображения представляет собой количество вставленных картинок по наибольшей стороне. Т.е. из картинки с разрешением 250х500px с настройками:<br>{Размер изображения: 50,<br>Ширина вставляемой картинки (которая тоже устанавливается разработчиком): 50px}<br>создастся новая картинка размером 25х50 картинок с разрешением 1250х2500px!!

Следуя из вышеперечисленного понятно, что в собранной картинке из картинки с мелкими элементами, они пропадут.<br>
Тогда почти всегда логично исользовать большое разрешение.

Однако маленькое разрешение имеет место быть.

Данные:
|Тема|Степень шума|Размер|Картинка|
|---|:---:|---|---|
|Дота|Среднее|Маленькое|Маленькая, с большими элементами|

<details><summary>Оригинал</summary><br>
<img src = "https://downloader.disk.yandex.ru/preview/7bca012444235d3971d93a274bc3ddf84200e12a0a8d04a498f8fedd4f621b84/62ce20fe/DrNQ6nADKVR7GgAwv72IqxRcJaHxMqSh0MmXjqTllYShyTheB62iko89VxOd9CrHWjqsqe61HYHz8qc4FOamRg%3D%3D?uid=0&filename=3.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=1920x964"></details>

<details><summary>Результат</summary><br>
<img src = "https://downloader.disk.yandex.ru/preview/09d35ef798534bff9bd8ee7c0fe3ae8f47feaaaa920c1175b538b993ec0cbbd9/62ce1b0b/eMteB1EgLOmCnc6dPXXlkmOKYAIwIKVOkaqDDe-QUywSs891zREiDw58SctLn3q5IK-tEE_8NN21X8bUXAzSbA%3D%3D?uid=0&filename=3.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964"></details>

### [3] Команды приложения.

**ВАЖНО!!! ВСЕ КОМАНДЫ ДОЛЖЫ ЗАПУСКАТЬСЯ ИЗ ДИРЕКТОРИИ С ФАЙЛОМ "manage.py"**

Получить список команд можно запустив скрипт.

```python manage.py```

Вывод:<br>
```>> ...Commands: ['download_topic', 'show_db_distribution', 'start', 'test_engine', 'update_db', 'update_db_single']```

#### **Команда @download_topic**
Команда позволяет скачать картинки с сайта [Fonwall](fonwall.com).

```python manage.py download_topic```

a. Далее вводим набор картинок, например: "Коты".<br>
b. Предлагается выбрать к какому набору докачать новые картинки или создать новую.<br>
с. После выбора начнется парсинг. Для останоовки парсинга нажать комбинацию (Ctrl + C), либо дождаться окончания парсинга.<br>
d. После парсинга начнется скачивание новых изображений, которое можно также остановить комбинациекй клавиш (Ctrl + C).<br>

#### **Команда @update_dp**
Команда позволяет обновить полностью бд на основе директорий.

```python manage.py update_db```

#### **Команда @update_dp_single**
Команда позволяет обновить или добавить одну определенную таблицу в бд на основе директории с картинками.

```python manage.py update_db_single```

#### **Команда @show_db_distribution**
Команда позволяет посмотреть распределение картинок на 3D RGB палитре.

```python manage.py show_db_distribution```

Например:
| Коты | Дота |
|:---:|:---:|
|<img src="https://downloader.disk.yandex.ru/preview/225a0ddc3ade8f66762439223436dc47f0c70dbff14c8c3d6cf9345dcb34af99/62ce213c/fgneCgxqVdcI7j7Kuao1S-cfokv_6Ww1n7u2wVnzkNREzn5f-_WqPGzI9WHrUqR1AvALtPuVGq0gaDJ_5ejbaw%3D%3D?uid=0&filename=koty.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964" width="100%">|<img src="https://downloader.disk.yandex.ru/preview/bae00ba770500fbf19d583307ce320830aef6891a7c12d14a8bee4ab290d5b14/62ce2152/llT07mye62KbGsJkC5Vwb-cfokv_6Ww1n7u2wVnzkNS0qonvXrZ2uAL0PdjFeitJDv2n7mKoR1SQ0y9uOK_jbQ%3D%3D?uid=0&filename=dota.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x964" width="100%">|

#### **Команда @test_engine**
Программа собирает картинку без учета телеграм бота. На вывод получите абсольтный путь к итоговой картинке.

```python manage.py test_engine```

a. В начале выбираем набор картинок для заполнения<br>
b. Далее вводим абсолютный путь до картинки

#### **Команда @start**
Команда запускает функционирующего бота.

```python manage.py start```

### [4] Дерево приложения
```
IMager
├───content
│   ├───results
│   │   ├───<Собранные картинки>
│   ├───TEMP
│   │   ├───<Промежуточные файлы для сборки>
│   ├───topics
│   │   └───<Темы изображений>
│   └───users_images
│       └───<Загруэенные tg-пользователями картинки>
├───IMager_bot
│   ├───commands
│   │   └───<Команды прилжения>
│   ├───IMager
│   │   ├───exceptions
|   |   |   └───<Некоторые кастомные исключения>
|   |   └──<Скрипты приложения>
│   ├───settings
│   │   └───<Конфиги и еще кастомные исключения>
│   ├───tg_bot
│   │   ├───handlers
│   │   │   └───<Хендлеры бота>
│   │   ├───keyboards
│   │   │   └───<Клавиатуры бота>
│   │   └───<Основные файлы бота>
│   └───manage.py
└───<Прочие служебные файлы>
```