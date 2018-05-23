from pyfsm import Generator


def main():
    generator = Generator()
    generator.loadConfig(filepath="./pyfsm/json/Hero.json")
    Hero = generator.generate()
    Hero.attack(target=Hero)

if __name__ == '__main__':
    main()
