import re

import gender_guesser.detector as gender

"""1. Какое количество мужчин и женщин плыло на корабле?"""


def count_genders(df, dev):
    if dev:
        print("╔═══════════════════════════════════════════╗")
        print("╠══════════════ Gender Count ═══════════════╣")
        print("╚═══════════════════════════════════════════╝")

    """В этом шаге создается новый столбец Gender в DataFrame df,
    в который записываются результаты работы функции get_gender().
    Для каждого значения в столбце Name вызывается функция get_gender(name),
    и результат сохраняется в новый столбец Gender."""
    df["Gender"] = df["Name"].apply(get_gender)

    """С помощью метода value_counts() подсчитывается,
    сколько раз встречается каждое значение в столбце Gender
    Этот результат сохраняется в переменной gender_counts и выводится на экран."""
    gender_counts = df["Gender"].value_counts()

    if dev:
        print(gender_counts)
    else:
        print(
            f"1. Количество мужчин на корабле: {gender_counts.get('Male', 0)} | Количество женщин на корабле: {gender_counts.get('Female', 0)}")


def get_gender(name):
    # сокращение от "Mistress"
    if "Mrs" in name:
        return "Female"
    elif "Ms" in name:
        return "Female"
    elif "Miss" in name:
        return "Female"
    elif "Lady" in name:
        return "Female"
    # сокращение от "Madame"
    elif "Mme" in name:
        return "Female"
    # сокращение от "Mademoiselle"
    elif "Mlle" in name:
        return "Female"
    # испанский титул
    elif "Dona" in name:
        return "Female"
    # "Countess" — это титул, который используется для женщин, являющихся супругами или вдовами графа (в английской аристократии)
    elif "Countess" in name:
        return "Female"

    elif "Mr" in name:
        return "Male"
    elif "Master" in name:
        return "Male"
    elif "Sir" in name:
        return "Male"
    # сокращение от "Father" (отец) и использовался для католических священников
    elif "Fr" in name:
        return "Male"
    # сокращение от итальянского слова "Signore", что в переводе на русский означает "господин" или "мистер"
    elif "Sig" in name:
        return "Male"
    # "Colonel" — это воинское звание в армии, которое в русском языке переводится как "полковник"
    elif "Colonel" in name:
        return "Male"
    # сокращение от "Reverend", что переводится как "Преподобный"
    elif "Rev" in name:
        return "Male"
    elif "Captain" in name:
        return "Male"
    # "Major" — это военный титул, обозначающий звание майора в армии
    elif "Major" in name:
        return "Male"
    # "Don" — это испанский титул, используемый для обращения к мужчинам
    elif "Don" in name:
        return "Male"

    elif "Dr" in name:
        # Используем регулярное выражение, чтобы найти имя после "Dr"
        match = re.search(r"Dr\s+([A-Za-z]+)", name)

        if match:
            d = gender.Detector()
            first_name = match.group(1)
            g = d.get_gender(first_name)
            if g == 'female':
                return "Female"
            elif g == 'male':
                return "Male"
            elif first_name in 'Washington':
                return "Male"
            else:
                print('===========', name)
                return "Unknown"
        else:
            return "Unknown"
    else:
        return "Unknown"
