import random

def insertion_sort(grades):
    # Проходим по всем элементам списка, начиная со второго
    for i in range(1, len(grades)):
        key = grades[i]  # Текущая оценка для вставки
        j = i - 1
        
        # Перемещаем элементы grades[0..i-1], которые больше key,
        # на одну позицию вперед от их текущей позиции
        while j >= 0 and key < grades[j]:
            grades[j + 1] = grades[j]
            j -= 1
        
        # Вставляем текущую оценку на её правильное место
        grades[j + 1] = key

# Пример использования
grades = [1, 2, 3, 4, 5]
print("Исходные оценки:", grades)

# Перемешиваем оценки
random.shuffle(grades)
print("Перемешанные оценки:", grades)

# Сортируем оценки
insertion_sort(grades)
print("Отсортированные оценки:", grades)
