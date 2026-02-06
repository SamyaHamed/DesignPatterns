from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, video_title: str):
        pass



class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class YouTubeChannel(Subject):
    def __init__(self, name: str):
        self.name = name
        self.subscribers = []
        self.latest_video = None

    def attach(self, observer: Observer):
        self.subscribers.append(observer)

    def detach(self, observer: Observer):
        self.subscribers.remove(observer)

    def upload_video(self, title: str):
        self.latest_video = title
        print(f"\n{self.name} uploaded a new video: {title}")
        self.notify()

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update(self.latest_video)


class Subscriber(Observer):
    def __init__(self, username: str):
        self.username = username

    def update(self, video_title: str):
        print(f" {self.username} got notified about: {video_title}")



channel = YouTubeChannel("CodeWithSamya")

user1 = Subscriber("Ahmad")
user2 = Subscriber("Lina")
user3 = Subscriber("Omar")

channel.attach(user1)
channel.attach(user2)
channel.attach(user3)

channel.upload_video("Observer Pattern Explained")

channel.detach(user2)

channel.upload_video("Design Patterns in Python")
