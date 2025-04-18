import pandas as pd

"""4. Какого возраста были пассажиры? Посчитайте среднее и медиану возраста пассажиров.
    В качестве ответа приведите два числа через пробел."""

"""
1. Среднее (average) — это сумма всех значений возраста, делённая на количество пассажиров.
2. Медиана — это среднее значение возраста, когда все возраста отсортированы по
возрастанию (если количество элементов нечётное, то это просто центральное значение;
если чётное, то медиана — это среднее двух центральных значений).
"""


def calculate_age_statistics(df, dev):
    if dev:
        print("╔═══════════════════════════════════════════╗")
        print("╠══════════════ Age statistics ═════════════╣")
        print("╚═══════════════════════════════════════════╝")

        print(df['Возраст'].unique())

    # Преобразуем возраст в числовой формат
    df['Возраст'] = pd.to_numeric(df['Возраст'], errors='coerce')

    # Исключаем нулевые значения, если они есть
    df_filtered = df[df['Возраст'] > 0]

    # Рассчитываем среднее и медиану возраста пассажиров
    average_age = df_filtered['Возраст'].mean()
    median_age = df_filtered['Возраст'].median()

    # Выводим оба значения, округленных до двух знаков после запятой
    print(f"4. Среднее возраста пассажиров: {average_age} | Медиана возраста пассажиров: {median_age}")
