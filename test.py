from Pyfsm.Event import ActiveEvent


def main():
    door = ActiveEvent(
        name="door", doc={
            "new": "Door is open",
            "del": "Door is close"
        })
    door.executeEvent()


if __name__ == '__main__':
    main()
