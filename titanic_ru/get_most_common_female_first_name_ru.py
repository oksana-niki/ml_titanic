"""6. Какое самое популярное женское имя на корабле? Извлеките из полного имени
    пассажира (колонка Name) его личное имя (First Name).
    Это задание – типичный пример того, с чем сталкивается специалист по анализу данных.
    Данные очень разнородные и шумные, но из них требуется извлечь необходимую информацию.
    Попробуйте вручную разобрать несколько значений столбца Name и выработать правило
    для извлечения имен, а также разделения их на женские и мужские."""


def get_most_common_female_first_name(df, dev):
    if dev:
        print("╔═══════════════════════════════════════════╗")
        print("╠════════ Most popular female name ═════════╣")
        print("╚═══════════════════════════════════════════╝")

    df = set_first_name(df)

    # Фильтруем пассажиров с gender == female
    female_passengers = df[df['Пол'] == 'женский']

    # Считаем количество каждого имени
    name_counts = female_passengers['First Name'].value_counts()

    # Получаем самое популярное имя
    most_common_name = name_counts.idxmax()
    most_common_name_count = name_counts.max()

    # Выводим самое популярное женское имя
    if dev:
        print(female_passengers)
        print(name_counts)

    # print('Anna----------', df[df['Имя'].str.contains('Mary', case=True, na=False)].shape[0])
    # print('Anna++++++++', df[df['Имя'].str.contains('Mary', case=True, na=False)]['First Name'])
    # print('Mary----------', df[df['Имя'].str.contains('Mary', case=False, na=False)]['Name'])

    print(f"6. Самое популярное женское имя на корабле: {most_common_name} ({most_common_name_count} раз)")


def set_first_name(df):
    """Извлекает личное имя из полного имени."""
    df['First Name'] = df['Имя'].apply(extract_first_name)

    return df


def extract_first_name(name):
    """Извлекает личное имя из полного имени."""
    # Для замужних женщин, чье имя в скобках после "Mrs."
    if 'Mrs,' in name and '(' in name:
        # Разделяем строку по скобке
        parts = name.split("(")

        # Получаем имя и фамилию после скобки
        name_and_surname = parts[1].split(")")[0].strip()  # Берем все до закрывающей скобки и убираем пробелы

        # Разделяем по пробелу, первое слово - имя, второе - девичья фамилия
        name_and_surname_parts = name_and_surname.split(" ")

        return name_and_surname_parts[0]
    # Проверяем, есть ли запятая в имени
    else:
        # Разделяем строку по запятой
        parts = name.split(",")

        # Откидываем фамилию и титул
        name_and_surname = parts[1].strip()

        # Разделяем по пробелу, первое слово - титул, второе - имя
        name_and_surname_parts = name_and_surname.split(" ")

        # Личное имя будет вторым словом после титула
        return name_and_surname_parts[0]
