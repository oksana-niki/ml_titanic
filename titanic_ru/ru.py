import pandas as pd

from df_info.show_df import show_df
from titanic_ru.age_statistics_ru import calculate_age_statistics
from titanic_ru.class_1_ratio_ru import calculate_class_1_ratio
from titanic_ru.count_genders_ru import count_genders
from titanic_ru.get_most_common_female_first_name_ru import get_most_common_female_first_name
from titanic_ru.pearson_correlation_ru import calculate_pearson_correlation
from titanic_ru.survival_rate_ru import calculate_survival_rate


def ru(dev):
    """Reads a CSV file."""
    df = pd.read_csv('Титаник.csv', encoding='windows-1251', sep=';')

    if dev:
        show_df(df)

    """1. Какое количество мужчин и женщин плыло на корабле?"""
    count_genders(df, dev)

    """2. Какой части пассажиров удалось выжить?
    Посчитайте долю выживших пассажиров. Ответ приведите в процентах
    (число в интервале от 0 до 100, знак процента не нужен), округлив до двух знаков."""
    calculate_survival_rate(df, dev)

    """3. Какую долю пассажиры первого класса составляли среди всех пассажиров?
    Ответ приведите в процентах (число в интервале от
    0 до 100, знак процента не нужен), округлив до двух знаков."""
    calculate_class_1_ratio(df, dev)

    """4. Какого возраста были пассажиры? Посчитайте среднее и медиану возраста пассажиров.
    В качестве ответа приведите два числа через пробел."""
    calculate_age_statistics(df, dev)

    """5. Коррелируют ли число братьев/сестер/супругов с числом родителей/детей?
    Посчитайте корреляцию Пирсона между признаками SibSp и Parch."""
    calculate_pearson_correlation(df, dev)

    """6. Какое самое популярное женское имя на корабле? Извлеките из полного имени
    пассажира (колонка Name) его личное имя (First Name).
    Это задание – типичный пример того, с чем сталкивается специалист по анализу данных.
    Данные очень разнородные и шумные, но из них требуется извлечь необходимую информацию.
    Попробуйте вручную разобрать несколько значений столбца Name и выработать правило
    для извлечения имен, а также разделения их на женские и мужские."""
    get_most_common_female_first_name(df, dev)
