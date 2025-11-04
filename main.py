import random

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key):
        index = self.hash_function(key)
        if key not in self.table[index]:
            self.table[index].append(key)
            return True
        return False
    
    def remove(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            self.table[index].remove(key)
            return True
        return False
    
    def search(self, key):
        index = self.hash_function(key)
        return key in self.table[index]
    
    def remove_even(self):
        removed_count = 0
        for i in range(self.size):
            original_length = len(self.table[i])
            self.table[i] = [x for x in self.table[i] if x % 2 != 0]
            removed_count += original_length - len(self.table[i])
        return removed_count
    
    def get_all_elements(self):
        elements = []
        for chain in self.table:
            elements.extend(chain)
        return elements
    
    def display(self):
        print(f"\nГеш-таблиця (розмір {self.size}):")
        total_elements = 0
        for i, chain in enumerate(self.table):
            if chain:
                print(f"Індекс {i}: {chain}")
                total_elements += len(chain)
        print(f"Всього елементів: {total_elements}")
        return total_elements

def main():
    variant = 7
    N = variant * 5 + 50
    S = int(N * 0.75)
    
    print(f"Варіант: {variant}")
    print(f"N = {variant} * 5 + 50 = {N}")
    print(f"S = 75% від {N} = {S}")
    
    hash_table = HashTable(S)
    
    print("\nОПЕРАЦІЇ З ГЕШ-ТАБЛИЦЕЮ")
    
    while True:
        print("\nОберіть операцію:")
        print("1 - Додати елемент")
        print("2 - Видалити елемент")
        print("3 - Знайти елемент")
        print("4 - Продовжити до наступного кроку")
        
        choice = input("Ваш вибір: ")
        
        if choice == '1':
            try:
                key = int(input("Введіть число для додавання: "))
                if hash_table.insert(key):
                    print(f"Елемент {key} успішно додано")
                else:
                    print(f"Елемент {key} вже існує в таблиці")
            except ValueError:
                print("Будь ласка, введіть ціле число")
                
        elif choice == '2':
            try:
                key = int(input("Введіть число для видалення: "))
                if hash_table.remove(key):
                    print(f"Елемент {key} успішно видалено")
                else:
                    print(f"Елемент {key} не знайдено в таблиці")
            except ValueError:
                print("Будь ласка, введіть ціле число")
                
        elif choice == '3':
            try:
                key = int(input("Введіть число для пошуку: "))
                if hash_table.search(key):
                    print(f"Елемент {key} знайдено в таблиці")
                else:
                    print(f"Елемент {key} не знайдено в таблиці")
            except ValueError:
                print("Будь ласка, введіть ціле число")
                
        elif choice == '4':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
    
    print(f"\nЗАПОВНЕННЯ {N} ВИПАДКОВИМИ ЧИСЛАМИ")
    for i in range(N):
        hash_table.insert(random.randint(1, 1000))
    
    print("Таблицю заповнено випадковими числами")
    elements_before = hash_table.get_all_elements()
    print(f"Кількість елементів до видалення парних: {len(elements_before)}")
    hash_table.display()
    
    print(f"\nВИДАЛЕННЯ ПАРНИХ ЧИСЕЛ")
    removed_count = hash_table.remove_even()
    print(f"Видалено парних чисел: {removed_count}")
    
    print(f"\nРЕЗУЛЬТАТ")
    print(f"ГЕШ-ТАБЛИЦЯ БЕЗ ПАРНИХ ЧИСЕЛ")
    hash_table.display()

if __name__ == "__main__":
    main()