


class CinemaTicketSystem:
    def __init__(self):

        self.movies = {}  
        self.users = {}  
        self.tickets = {}

        self.movie_id_counter = 0
        self.user_id_counter = 0
        self.ticket_id_counter = 0

    def add_movie(self, movie_name):
        """
        Добавляет новый фильм с заданным именем. 
        Возвращает идентификатор добавленного фильма.
        """

        self.movie_id_counter += 1
        movie_id = self.movie_id_counter
        self.movies[movie_id] = movie_name
        return movie_id

    def show_all_movies(self):
        """
        Выводит список всех доступных фильмов.
        """

        for movie_id, movie_name in self.movies.items():
            print(f"{movie_id}. {movie_name}")

    def add_user(self, user_name):
        """
        Регистрирует нового пользователя с заданным именем. 
        Возвращает идентификатор добавленного пользователя.
        """

        user_id = self.user_id_counter
        self.users[user_id] = user_name
        self.user_id_counter += 1
        return user_id

    def buy_ticket(self, user_id, movie_id):
        """
        Регистрирует покупку билета пользователем на указанный фильм. 
        Возвращает идентификатор билета.
        """


        ticket_id = self.ticket_id_counter
        self.tickets[ticket_id] = (user_id, movie_id)
        self.ticket_id_counter += 1
        return ticket_id

    def cancel_ticket(self, ticket_id):
        """
        Отменяет покупку билета по его идентификатору.
        Возвращает true, если билет был успешно отменен, и false, если билет с
        таким идентификатором не найден.
        """


        if ticket_id in self.tickets:
            del self.tickets[ticket_id]
            return True
        else:
            return False
