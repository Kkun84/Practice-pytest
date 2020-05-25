def send(message: str):
    ok = receive(message)

    if ok:
        return 'success'
    return 'failure'


def receive(message: str) -> bool:
    print('received: {}'.format(message))

    return True
