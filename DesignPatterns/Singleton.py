class SingletonProduct:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == "__main__":
    singleton1 = SingletonProduct()
    singleton2 = SingletonProduct()

    print(singleton1 == singleton2)

