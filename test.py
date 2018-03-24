from Pyfsm import Generator
from Pyfsm import Controller


def main():
    machine = Generator().generatorMachine()
    control = Controller(machine)
    control.handle("Open")


if __name__ == '__main__':
    main()
