def handler():
    print("Initialize Handler")
    while True:
        value = (yield)
        print("Recived %s" % value)

listener = handler()
listener.__next__()
listener.send(1)
listener.send("message")
