chat_messages = []

def display_chat():
    if chat_messages:
        print("\nЧат:")
        for message in chat_messages:
            print(message)
        print()


while True:
    username = input("Введите ваше имя: ")
    print("Выберите действие:")
    print("1. Посмотреть текущий текст чата")
    print("2. Отправить сообщение")
    print("3. Завершить программу")
    choice = input("Ваш выбор (1/2): ")

    if choice == '1':
        display_chat()
    elif choice == '2':
        message = input("Введите ваше сообщение: ")
        chat_messages.append(f"{username}: {message}")
    elif choice == '3':
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")