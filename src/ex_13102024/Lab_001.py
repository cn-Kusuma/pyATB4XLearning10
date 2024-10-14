# decorator

def add_before_ui_after_ui(func):
    def wrapper():
        print("Before running UI TC ")
        print("Start the browser")
        func()
        print("Ending running UTI TC")
        print("quit the browser")

    return wrapper()


@add_before_ui_after_ui
def test_ui():
    print("I will test the UI ")
