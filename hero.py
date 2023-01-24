class SuperHero:
    people = 'people'
    
    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        
    def aziz(self):
        return f"name: {self.name}"
    
    def said(self):
        return f"hill: {self.health_points * 2}"

    def sid(self):
        return f"nick: {self.nickname}, superpower: {self.superpower}, health_points: {self.health_points}"

    
    def len(self):
        return len(self.catchphrase)




class Hero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = False
        self.fly = False
    def hp(self):
        self.fly = True
        return f" квадрат: {self.health_points ** 2}"
    def fl(self):
        return f"catchphrase: {self.catchphrase}"



class Villain(SuperHero):
    people = "monster"
    
    def gen_x(self):
        pass

    def crit(self, damage1, damage2):
        return f" урон: {damage1 ** damage2}"


hero = Hero("Aziz", "Said", "msms", 100,  "fly in the True phrase")
print(hero.hp())
print(hero.fl())
 
hro = Villain("Aziz", "Said", "msms", 100,  "fly in the True phrase")
print(hro.gen_x())
print(hro.crit(10,10))