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


a = SuperHero
print(a.people)
hero = SuperHero("aziz","said","magic",1000,"stop")
print(hero.aziz())
print(hero.said())
print(hero.sid())
print(hero.len())