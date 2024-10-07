import json
import csv
import subprocess

# Функция для получения списка контактов
def get_contacts():
    try:
        # Используем termux-contact-list для получения контактов
        result = subprocess.run(['termux-contact-list'], capture_output=True, text=True)
        if result.returncode == 0:
            contacts = json.loads(result.stdout)
            return contacts
        else:
            print("Ошибка при выполнении termux-contact-list")
            return []
    except Exception as e:
        print(f"Ошибка: {e}")
        return []

# Функция для сохранения контактов в CSV файл
def save_to_csv(contacts, filename='contacts.csv'):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['name', 'number']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for contact in contacts:
                writer.writerow(contact)
        print(f"Контакты успешно сохранены в {filename}")
    except Exception as e:
        print(f"Ошибка при записи в CSV: {e}")

# Функция для чтения контактов из CSV файла и добавления их обратно в телефонную книгу
def add_contacts_from_csv(filename='contacts.csv'):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                name = row['name']
                number = row['number']
                # Добавляем контакт с помощью termux-contact-add
                subprocess.run(['termux-contact-add', '-n', name, '-p', number])
            print(f"Контакты из {filename} успешно добавлены в телефонную книгу")
    except Exception as e:
        print(f"Ошибка при чтении из CSV: {e}")

# Основная функция
def main():
    # Получаем список контактов
    contacts = get_contacts()
    
    # Сохраняем контакты в CSV файл
    save_to_csv(contacts)
    
    # Чтение контактов из CSV и добавление их обратно в телефонную книгу
    add_contacts_from_csv()

if __name__ == "__main__":
    main()
