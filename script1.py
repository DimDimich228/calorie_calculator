# -*- coding: utf-8 -*-
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("КАЛЬКУЛЯТОР КАЛОРИЙ И БЖУ")
    print("Шацкого Дмитрий Андреевича • Простая версия")
    print()

def get_integer_input(prompt, min_val, max_val, unit_name, example=""):
    while True:
        if example:
            print(f"{prompt} (например {example}): ", end="")
        else:
            print(f"{prompt}: ", end="")

        try:
            value = int(input())
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Пожалуйста, введите {unit_name} от {min_val} до {max_val}!")
        except ValueError:
            print("Пожалуйста, введите целое число!")

def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 1)

def get_bmi_status(bmi):
    if bmi < 18.5:
        return "Недостаточный вес"
    elif 18.5 <= bmi < 25:
        return "Нормальный вес"
    elif 25 <= bmi < 30:
        return "Избыточный вес"
    else:
        return "Ожирение"

def main():
    clear_screen()
    print_header()
    print("Добро пожаловать! Заполните информацию о себе:")
    print()

    # Симуляция загрузки (без прогресс-бара)
    print("Инициализация системы...")
    time.sleep(1)
    print()

    print("--- ВВОД ДАННЫХ ---")
    age = get_integer_input("Сколько вам лет", 1, 120, "возраст", "25")
    weight = get_integer_input("Какой у вас вес (кг)", 20, 300, "вес", "70")
    height = get_integer_input("Какой у вас рост (см)", 50, 250, "рост", "175")

    print("\n--- УКАЖИТЕ ВАШ ПОЛ ---")
    print("1 — Мужчина")
    print("2 — Женщина")

    while True:
        try:
            gender = int(input("Ваш выбор (1-2): "))
            if gender in [1, 2]:
                break
            else:
                print("Пожалуйста, введите 1 или 2!")
        except ValueError:
            print("Пожалуйста, введите число 1 или 2!")

    # Расчёт BMR
    print("\nРасчёт основного обмена веществ...")
    time.sleep(0.5)

    if gender == 1:
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

    # Уровень активности
    print("\n--- УРОВЕНЬ ФИЗИЧЕСКОЙ АКТИВНОСТИ ---")
    activity_data = {
        1: {"name": "минимальный", "coef": 1.2},
        2: {"name": "низкий", "coef": 1.375},
        3: {"name": "средний", "coef": 1.55},
        4: {"name": "высокий", "coef": 1.725},
        5: {"name": "экстремальный", "coef": 1.9}
    }

    for key, value in activity_data.items():
        print(f"{key} — {value['name']} ({value['desc'] if 'desc' in value else ''})")

    while True:
        try:
            activity_level = int(input("Выберите уровень активности (1-5): "))
            if 1 <= activity_level <= 5:
                break
            else:
                print("Пожалуйста, введите число от 1 до 5!")
        except ValueError:
            print("Пожалуйста, введите число от 1 до 5!")

    # Цель
    print("\n--- ВАША ЦЕЛЬ ---")
    goal_data = {
        1: {"name": "Похудение", "coef": 0.85},
        2: {"name": "Поддержание", "coef": 1.0},
        3: {"name": "Набор массы", "coef": 1.15}
    }

    for key, value in goal_data.items():
        print(f"{key} — {value['name']}")

    while True:
        try:
            goal = int(input("Выберите вашу цель (1-3): "))
            if 1 <= goal <= 3:
                break
            else:
                print("Пожалуйста, введите число от 1 до 3!")
        except ValueError:
            print("Пожалуйста, введите число от 1 до 3!")

    # Расчёты
    print("\nВыполняем расчёты...")
    time.sleep(1)

    daily_calories = bmr * activity_data[activity_level]["coef"]
    goal_calories = daily_calories * goal_data[goal]["coef"]

    if goal == 1:  # Похудение
        protein_ratio, fat_ratio, carb_ratio = 0.30, 0.25, 0.45
    elif goal == 2:  # Поддержание
        protein_ratio, fat_ratio, carb_ratio = 0.25, 0.30, 0.45
    else:  # Набор массы
        protein_ratio, fat_ratio, carb_ratio = 0.30, 0.25, 0.45

    proteins = goal_calories * protein_ratio / 4
    fats = goal_calories * fat_ratio / 9
    carbs = goal_calories * carb_ratio / 4

    bmi = calculate_bmi(weight, height)
    bmi_status = get_bmi_status(bmi)

    # Вывод результатов
    clear_screen()
    print_header()
    print("--- ВАШИ РЕЗУЛЬТАТЫ ---\n")

    print("ОСНОВНАЯ ИНФОРМАЦИЯ:")
    print(f"Пол: {'Мужчина' if gender == 1 else 'Женщина'}")
    print(f"Возраст: {age} лет")
    print(f"Вес: {weight} кг")
    print(f"Рост: {height} см")
    print(f"Активность: {activity_data[activity_level]['name']}")
    print(f"Цель: {goal_data[goal]['name']}\n")

    print("РАСЧЁТ КАЛОРИЙ:")
    print(f"Основной обмен (BMR): {round(bmr)} ккал/день")
    print(f"С учётом активности: {round(daily_calories)} ккал/день")
    print(f"Для цели '{goal_data[goal]['name']}': {round(goal_calories)} ккал/день\n")

    print("РЕКОМЕНДАЦИИ ПО БЖУ:")
    print(f"Белки: {round(proteins)} г/день ({protein_ratio * 100:.0f}% от калорий)")
    print(f"Жиры: {round(fats)} г/день ({fat_ratio * 100:.0f}% от калорий)")
    print(f"Углеводы: {round(carbs)} г/день ({carb_ratio * 100:.0f}% от калорий)\n")

    print("ИНДЕКС МАССЫ ТЕЛА (ИМТ):")
    print(f"Ваш ИМТ: {bmi} — {bmi_status}\n")

    print("РЕКОМЕНДАЦИИ:")
    if goal == 1:
        recommendations = [
            "Создайте дефицит в 300-500 ккал от рассчитанной нормы",
            "Увеличьте потребление белка до 1.6-2.2 г на кг веса",
            "Пейте 30-40 мл воды на кг веса ежедневно",
            "Сочетайте силовые и кардио тренировки",
            "Взвешивайтесь раз в неделю в одно время"
        ]
    elif goal == 2:
        recommendations = [
            "Придерживайтесь рассчитанной калорийности",
            "Следите за балансом БЖУ в ежедневном рационе",
            "Занимайтесь спортом 3-4 раза в неделю",
            "Контролируйте вес 1-2 раза в месяц",
            "Разнообразьте рацион питания"
        ]
    else:
        recommendations = [
            "Создайте профицит в 300-500 ккал от нормы",
            "Употребляйте 1.6-2.2 г белка на кг веса",
            "Увеличьте потребление сложных углеводов",
            "Тренируйтесь 4-5 раз в неделю",
            "Отдыхайте 7-9 часов в сутки"
        ]

    for rec in recommendations:
        print("- " + rec)

    print()
    save_choice = input("Сохранить результаты в файл? (да/нет): ").lower()

    if save_choice in ['да', 'yes', 'y', 'д']:
        filename = f"calorie_results_{time.strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("РЕЗУЛЬТАТЫ РАСЧЁТА КАЛОРИЙ И БЖУ\n\n")
                f.write(f"Дата расчёта: {time.strftime('%d.%m.%Y %H:%M')}\n")
                f.write(f"Пол: {'Мужчина' if gender == 1 else 'Женщина'}\n")
                f.write(f"Возраст: {age} лет\n")
                f.write(f"Вес: {weight} кг\n")
                f.write(f"Рост: {height} см\n")
                f.write(f"Активность: {activity_data[activity_level]['name']}\n")
                f.write(f"Цель: {goal_data[goal]['name']}\n\n")
                f.write(f"Основной обмен (BMR): {round(bmr)} ккал/день\n")
                f.write(f"С учётом активности: {round(daily_calories)} ккал/день\n")
                f.write(f"Для цели: {round(goal_calories)} ккал/день\n\n")
                f.write(f"Белки: {round(proteins)} г/день\n")
                f.write(f"Жиры: {round(fats)} г/день\n")
                f.write(f"Углеводы: {round(carbs)} г/день\n\n")
                f.write(f"ИМТ: {bmi} - {bmi_status}")

            print(f"Результаты сохранены в файл: {filename}")
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")

    print("\nРасчёт завершён! Для нового расчёта перезапустите программу.")
    input("Нажмите Enter для выхода...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограмма завершена пользователем.")
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")
        input("Нажмите Enter для выхода...")
