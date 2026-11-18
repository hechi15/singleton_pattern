class Singleton:
    _instance = None

    def __init__(self):
        raise RuntimeError("Singleton()으로 직접 만들 수 없습니다. get_instance()를 사용하세요.")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.counter = 0
        return cls._instance