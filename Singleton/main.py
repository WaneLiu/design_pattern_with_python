from threading import Lock, Thread

class Singleton():
    __instance = None
    __lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls.__lock:
            if cls.__instance is None:
                print('create a single instance')
                cls.__instance = super().__new__(cls)
            return cls.__instance

def test_single(*args):
    print(args[0])
    return Singleton()


if __name__ == "__main__":
    t1 = Thread(target=test_single, args=('FOO',))
    t2 = Thread(target=test_single, args=('BAR',))
    t1.start()
    t2.start()

    # if id(s1) == id(s2):
    #     print("Singleton works")
    # else:
    #     print("Singleton failed")