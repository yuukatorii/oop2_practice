import modules.SayHello as App
def run():
    app = App.SayHello("Git")
    app = App.SayHello("Github")
    app.say()
if __name__ == '__main__':
    run()