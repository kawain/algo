# https://pydp.info/GoF_dp/behavior/13_Chain_Of_Responsibility/index.html

events = ["timer", "key", "mouse", "key", "mouse", "terminate"]


def main():
    print("Handler Chain #1")
    handler1 = TimerHandler(KeyHandler(MouseHandler(NullHandler())))
    i = 0
    while True:
        event = events[i]
        if event == "terminate":
            break
        handler1.handle(event)
        print("---")  # => 処理の切れ目用
        i += 1


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, event):
        if self.__successor is not None:
            self.__successor.handle(event)


class MouseHandler(NullHandler):
    def handle(self, event):
        print("(MouseHandler)")
        if event == "mouse":
            print("Click: {}".format(event))
        else:
            super().handle(event)


class KeyHandler(NullHandler):
    def handle(self, event):
        print("(KeyHandler)")
        if event == "key":
            print("Press: {}".format(event))
        else:
            super().handle(event)


class TimerHandler(NullHandler):
    def handle(self, event):
        print("(TimerHandler)")
        if event == "timer":
            print("Timeout: {}".format(event))
        else:
            super().handle(event)


if __name__ == "__main__":
    main()
