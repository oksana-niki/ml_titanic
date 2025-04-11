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
    if dev:
        print(df[["First Name", "Name"]].head())

    # Фильтруем пассажиров с gender == female
    female_passengers = df[df['Gender'] == 'Female']

    # Считаем количество каждого имени
    name_counts = female_passengers['First Name'].value_counts()

    # Получаем самое популярное имя
    most_common_name = name_counts.idxmax()
    most_common_name_count = name_counts.max()

    # Выводим самое популярное женское имя
    if dev:
        print(female_passengers)

    # print('Anna----------', df[df['Name'].str.contains('Mary', case=True, na=False)].shape[0])
    # print('Anna++++++++', df[df['Name'].str.contains('Mary', case=True, na=False)]['First Name'])
    print(f"6. Самое популярное женское имя на корабле: {most_common_name} ({most_common_name_count} раз)")


def set_first_name(df):
    """Извлекает личное имя из полного имени."""
    df['First Name'] = df['Name'].apply(extract_first_name)

    return df


def extract_first_name(name):
    """Извлекает личное имя из полного имени."""
    # Проверяем, есть ли запятая в имени
    if ',' in name:
        # Разделяем строку по запятой
        parts = name.split(",")

        # Получаем титул и имя
        title_and_name = parts[1].strip()

        # Разделяем по пробелу, первое слово - титул, второе - имя
        title_and_name_parts = title_and_name.split(" ")

        # Личное имя будет вторым словом после титула
        first_name = title_and_name_parts[1] if len(title_and_name_parts) > 1 else None
    else:
        # Если запятой нет, то предполагаем, что имя - предпоследнее слово
        parts = name.split(" ")
        first_name = parts[-2] if len(parts) > 1 else None

    return first_name
