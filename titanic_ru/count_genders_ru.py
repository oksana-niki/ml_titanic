"""1. Какое количество мужчин и женщин плыло на корабле?"""


def count_genders(df, dev):
    if dev:
        print("╔═══════════════════════════════════════════╗")
        print("╠══════════════ Gender Count ═══════════════╣")
        print("╚═══════════════════════════════════════════╝")

        """Получаем все уникальные значения колонки Пол"""
        print('Unique values: ', df['Пол'].unique())

    """С помощью метода value_counts() подсчитывается,
    сколько раз встречается каждое значение в столбце Пол
    Этот результат сохраняется в переменной gender_counts и выводится на экран."""
    gender_counts = df['Пол'].value_counts()

    if dev:
        print(gender_counts)
    else:
        print(
            f"1. Количество мужчин на корабле: {gender_counts.get('мужской', 0)} | Количество женщин на корабле: {gender_counts.get('женский', 0)}")
