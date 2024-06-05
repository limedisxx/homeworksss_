import hashlib
import time
from typing import List

class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

    def __repr__(self):
        return f"User({self.nickname}, {self.password}, {self.age})"

class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Video({self.title}, {self.duration}, {self.time_now}, {self.adult_mode})"

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login: str, password: str):
        for user in self.users:
            if user.nickname == login and user.password == password:
                self.current_user = user
                break
        else:
            print("Неверный логин или пароль")

    def register(self, nickname: str, password: str, age: int):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f"Пользователь {nickname} успешно зарегистрирован")

    def log_out(self):
        self.current_user = None

    def add(self,  * videos: Video):
        for video in videos:
            if not any(vid.title == video.title for vid in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word: str) -> List[str]:
        result = [vid.title for vid in self.videos if search_word.lower() in vid.title.lower()]
        return result

    def watch_video(self, title: str):
        if self.current_user is None:
            print("Войдите в аккаунт чтобы смотреть видео")
        else:
            for video in self.videos:
                if video.title == title:
                    if video.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        print(f"Начало воспроизведения видео '{title}'")
                        time.sleep(1)
                        while video.time_now < video.duration:
                            video.time_now += 1
                            print(f"Прошло {video.time_now} секунд")
                        print("Конец видео")
                        break
            else:
                print("Видео не найдено")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')
