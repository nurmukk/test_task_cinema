# Приложите инструкцию по запуску вашей программы и запускаемый файл
#
# Автор: Нурмухан Айманов
# telegram: @nurmukk
# a.nurmuhan03@gmail.com
#
# Данный код написан в целях прохождение этапа
#
# Для запуска вывполните команду в терминал
# $ python3 filename.py 
#
# Если хотите запустить с command line интерфейсом 
# $ python3 launch.py

from cinema import CinemaTicketSystem


#Пример использования на Python:
cinemaSystem = CinemaTicketSystem()

movieId1 = cinemaSystem.add_movie("Inception")
movieId2 = cinemaSystem.add_movie("The Matrix")

cinemaSystem.show_all_movies() 
# Вывод:
# 1. Inception
# 2. The Matrix

userId1 = cinemaSystem.add_user("Alice")
userId2 = cinemaSystem.add_user("Bob")

ticketId1 = cinemaSystem.buy_ticket(userId1, movieId1)  # Alice покупает билет на Inception
ticketId2 = cinemaSystem.buy_ticket(userId2, movieId2)  # Bob покупает билет на The Matrix

print(cinemaSystem.cancel_ticket(ticketId1))  # Вернет True, билет отменен
print(cinemaSystem.cancel_ticket(999))  # Вернет False, билет с таким идентификатором не найден