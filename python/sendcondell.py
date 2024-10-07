import subprocess
import os

# Путь к файлу, который нужно передать
source_file = "/data/data/com.termux/files/home/scripts/python/contacts.csv"

# Данные для подключения по scp
remote_user = "attor"
remote_host = "192.168.2.1"
remote_port = "4050"
remote_path = "/home/attor/Documents/s24ultra/contacts/"

# Команда для передачи файла по scp
scp_command = [
    "scp",
    "-P", remote_port,
    source_file,
    f"{remote_user}@{remote_host}:{remote_path}"
]

# Проверяем, существует ли файл
if os.path.exists(source_file):
    try:
        # Выполняем команду scp
        result = subprocess.run(scp_command, check=True)
        print("Файл успешно передан!")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при передаче файла: {e}")
else:
    print(f"Файл {source_file} не найден.")
