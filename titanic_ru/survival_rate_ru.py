"""2. Какой части пассажиров удалось выжить?
Посчитайте долю выживших пассажиров. Ответ приведите в процентах
(число в интервале от 0 до 100, знак процента не нужен), округлив до двух знаков."""


def calculate_survival_rate(df, dev):
    if dev:
        print("╔═══════════════════════════════════════════╗")
        print("╠══════════════ Survival rate ══════════════╣")
        print("╚═══════════════════════════════════════════╝")

        print('Unique values: ', df['Выживший'].unique())

    # Берём среднее значение колонки "Выживший" (1 — выжил, 0 — нет)
    survival_rate = df['Выживший'].mean() * 100

    # Округляем до двух знаков после запятой
    survival_rate_rounded = round(survival_rate, 2)

    # Выводим результат
    print(f"2. Доля выживших пассажиров: {survival_rate_rounded}")
