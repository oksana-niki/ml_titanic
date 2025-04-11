"""5. Коррелируют ли число братьев/сестер/супругов с числом родителей/детей?
    Посчитайте корреляцию Пирсона между признаками SibSp и Parch."""

"""
Корреляция Пирсона будет выражена числом от -1 до 1:

- Значение 1 означает идеальную положительную корреляцию.
- Значение -1 означает идеальную отрицательную корреляцию.
- Значение 0 означает отсутствие линейной корреляции.
"""


def calculate_pearson_correlation(df, dev):
    if dev:
        print("╔═══════════════════════════════════════════╗")
        print("╠═══════════ Pearson correlation ═══════════╣")
        print("╚═══════════════════════════════════════════╝")

    # Добавляет столбец с фамилией
    df = set_surname(df)
    if dev:
        print(df[["Name", "Surname"]].head())

    # Классифицирует пассажиров как SibSp или Parch по возрастной разнице
    df = classify_relatives_by_age(df)
    if dev:
        print(df[["Name", "Surname", "SibSp", "Parch"]].head())

    # Рассчитываем корреляцию Пирсона между SibSp и Parch
    correlation = df["SibSp"].corr(df["Parch"])
    print(f"5. Корреляция Пирсона между количеством братьев/сестер/супругов и количеством родителей/детей: {correlation:.2f}")

def set_surname(df):
    """Добавляет столбец с фамилией"""
    df["Surname"] = df["Name"].apply(extract_surname)
    return df


def extract_surname(name):
    """Извлекает фамилию пассажира (до запятой)"""
    return name.split(",")[0].strip()


def classify_relatives_by_age(df):
    """Классифицирует пассажиров как SibSp или Parch по возрастной разнице"""

    # Считаем количество родственников
    sib_sp = []
    parch = []

    # Для каждого пассажира находим его однофамильцев
    for index, row in df.iterrows():
        surname = row['Surname']
        passenger_age = row['Age']

        # Находим всех пассажиров с такой же фамилией
        family_members = df[df['Surname'] == surname]

        sib_count = 0
        parch_count = 0

        for _, member in family_members.iterrows():
            if member['Name'] != row['Name']:  # Пропускаем самого себя
                age_diff = abs(passenger_age - member['Age'])

                if age_diff <= 16:
                    sib_count += 1  # SibSp: братья/сестры/супруги
                elif age_diff > 16:
                    parch_count += 1  # Parch: родители/дети

        sib_sp.append(sib_count)
        parch.append(parch_count)

    df["SibSp"] = sib_sp
    df["Parch"] = parch
    return df
