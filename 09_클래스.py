# 선언
class Dog:
    def __init__(self, name):  # 생성자
        self.name = name

    sound = "멍멍"    # public
    _breed = "푸들"   # protected
    __age = "9"   # private


    def info(self):
        print('breed : ' + self._breed + ' age : ' + self.__age)
    def bark(self):  # 메서드
        print(self.name + "가 " + self.sound)


myDog = Dog("초코");  # 인스턴스 생성
myDog2 = Dog("두부")
myDog.info()
myDog2.info()
myDog.sound = "왈왈";
myDog.bark()  # 초코가 왈왈
myDog2.bark()  # 두부가 멍멍


# 상속
class Pokemon:
    def __init__(self, name):  # 생성자
        self.name = name

    def attack(self):  # 메서드
        print(self.name + "가 공격한다.")

    def move(self):  # 메서드
        print(self.name + "가 이동한다.")


class Pikachu(Pokemon):
    def __init__(self, name, skill):
        super().__init__(name)
        self.skill = skill

    def attack(self):
        print(self.name + "가 " + self.skill + "로 공격한다.")


class Pizeon(Pokemon):
    def __init__(self, name, skill):
        super().__init__(name)
        self.skill = skill

    def attack(self):
        print(self.name + "가 " + self.skill + "로 공격한다.")

    def fly(self):
        print(self.name + "가 날아간다")


pokemon1 = Pikachu("피카츄", "백만볼트")
pokemon2 = Pizeon("피죤", "날개공격")

pokemon1.attack();
pokemon1.move();
pokemon2.attack();
pokemon2.move();
pokemon2.fly();
