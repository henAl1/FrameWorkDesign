from AbstractApplication.AbstractApplication import AbstractApplication


class AndroidApplication(AbstractApplication):
    def __init__(self):
        super().__init__()

    def each_should_implement(self):
        print('my version')
if __name__ == "__main__":
    A = AndroidApplication()
    print(A.foo())
    A.each_should_implement()