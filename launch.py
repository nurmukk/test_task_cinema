from cinema import CinemaTicketSystem

def main():
    cinema_system = CinemaTicketSystem()

    print("""
Здравствуйте, у вас есть следующие доступные функции:
""")

    while True:
        print("""
1. Добавить новый фильм;
2. Показать все доступные фильмы;
3. Добавить нового пользователя;
4. Купить билет;
5. Отменить покупку билета;
6. Выход
        """)

        choice = input("Выберите действие: ")

        if choice == '1':
            movie_name = input("Введите название фильма: ")
            cinema_system.add_movie(movie_name)
        elif choice == '2':
            cinema_system.show_all_movies()
        elif choice == '3':
            user_name = input("Введите имя пользователя: ")
            cinema_system.add_user(user_name)
        elif choice == '4':
            user_id = int(input("Введите ID пользователя: "))
            movie_id = int(input("Введите ID фильма: "))
            cinema_system.buy_ticket(user_id, movie_id)
        elif choice == '5':
            ticket_id = int(input("Введите ID билета: "))
            cinema_system.cancel_ticket(ticket_id)
        elif choice == '6':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
