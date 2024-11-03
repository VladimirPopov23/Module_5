# module5hard.py
# 04.11.2024 Задание "Свой YouTube"

import time


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname: str = nickname  # имя пользователя
        self.password: int = hash(password)  # пароль в хэшированном виде
        self.age: int = age  # возраст

    def __str__(self):  # для отображения в консоли
        return self.nickname


class Video:
    time_now = 0

    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title: str = title  # заголовок видео
        self.duration: int = duration  # продолжительность видео
        self.time_now: int = time_now  # секунда остановки (изначально 0)
        self.adult_mode: bool = adult_mode  # возрастное ограничение 18+ (False по умолчанию)

    def __str__(self):  # для отображения в консоли
        return self.title


class UrTube:
    def __init__(self):
        self.users = []  # список пользователей
        self.videos = []  # список видео
        self.current_user = None  # текущий пользователь (None по умолчанию)

    def log_in(self, nickname: str, password: str):  # авторизация пользователя
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                return True
            return False

    def register(self, nickname: str, password: str, age: int):  # регистрация пользователей
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
                return False
        new_user = User(nickname, password, age)
        self.users.append(new_user)  # добавляем нового пользователя в список пользователей
        self.current_user = new_user  # текущим пользователем становится новый пользователь

    def log_out(self):  # выход из логина
        self.current_user = None

    def add(self, *videos):  # добавление видео
        for video in videos:
            if video.title not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word):  # поиск видео
        result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():  # поиск по ключевому слову
                result.append(str(video))
        return result

    def watch_video(self, video_title):  # просмотр видео
        if self.current_user is None:  # проверка авторизации
            print('Войдите в аккаунт, чтобы смотреть видео')
        elif self.current_user.age < 18 and any(
                [video.adult_mode for video in self.videos if video.title == video_title]):
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            for video in self.videos:  # запуск видео
                if video.title == video_title:
                    print('Просмотр видео:', video_title)
                    print('Время просмотра:', end=' ')
                    for sec in range(1, (video.duration) + 1):
                        print(sec, end=' ')
                        time.sleep(1)
                    print('Конец видео!')
                    break
            else:
                print('Видео с таким названием не найдено')


if __name__ == '__main__':


    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')