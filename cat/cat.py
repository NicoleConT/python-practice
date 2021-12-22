from random import randint
import threading


global hour

action_dict = {
    'play': '我在玩耍',
    'walk': '我在散步',
    'feed': '我在吃饭',
    'seedoctor': '我在看医生',
    'letalone': '我醒着但很无聊',
    'sleep': '我在睡觉'
}


class Cat(object):
    hunger = 0
    happiness = 0
    health = 0
    current_action = 0

    def __init__(self, status=None):
        if not status:
            self.hunger = randint(0, 100)
            self.happiness = randint(0, 100)
            self.health = randint(0, 100)
            self.current_action = 'sleep'
        print('我的名字叫Tommy，一只可爱的猫咪...')
        print('你可以和我一起散布，玩耍，你也需要给我好吃的东西，带我去看病，也可以让我发呆...')
        print('Commands:')
        print('1.walk:散步')
        print('2.play:玩耍')
        print('3.feed:喂我')
        print('4.seedoctor:看医生')
        print('5.letalone:让我独自一人')
        print('6.status:查看我的状态')
        print('7.bye:不想看到我')

    def pass_tick(self):
        if self.hunger > 80 or self.hunger < 20:
            self.health -= 2
        if self.happiness < 20:
            self.health -= 1

    def let_alone(self):
        self.hunger += 2
        --self.happiness
        self.pass_tick()

    def sleep(self):
        ++self.hunger
        self.pass_tick()

    def walk(self):
        self.hunger += 3
        ++self.health
        self.pass_tick()

    def play(self):
        self.hunger += 3
        ++self.happiness
        self.pass_tick()

    def feed(self):
        self.hunger -= 3
        self.pass_tick()

    def see_doctor(self):
        self.health += 4

    def break_sleep(self):
        print('确定要打断猫猫的睡眠吗?(键入confirm确认打断，其他输入取消打断)')
        confirm_str = input().strip()
        if confirm_str == 'confirm':
            self.happiness -= 4

    def show_status(self):
        print(f'我当前的状态：{self.current_action}')
        # 输出幸福值
        happy_stars_num = self.happiness / 2
        happy_stars_str = ''
        for i in range(happy_stars_num):
            happy_stars_str += '*'
        happy_stars_str.rjust(50, '-')
        print(f'Happiness: Sad {happy_stars_str} Happy ({self.happiness})')
        # 输出饥饿值
        hungry_stars_num = self.hunger / 2
        hungry_stars_str = ''
        for i in range(hungry_stars_num):
            hungry_stars_str += '*'
        hungry_stars_str.rjust(50, '-')
        print(f'Hunger: Full {hungry_stars_str} Hungry ({self.hunger})')
        # 输出健康值
        health_stars_num = self.health / 2
        health_stars_str = ''
        for i in range(health_stars_num):
            health_stars_str += '*'
        health_stars_str.rjust(50, '-')
        print(f'Health: Sick {health_stars_str} Healthy ({self.health})')

    def bye(self):
        print('记得来找我！Bye....')
        # save 保存状态到文件
        pass


def handle_opt(option, cat):
    if option == 'walk':
        cat.current_action = 'walk'
        cat.walk()
    elif option == 'play':
        cat.current_action = 'play'
        cat.play()
    elif option == 'feed':
        cat.current_action = 'feed'
        cat.feed()
    elif option == 'seedoctor':
        cat.current_action = 'seedoctor'
        cat.see_doctor()
    elif option == 'letalone':
        cat.current_action = 'letalone'
        cat.let_alone()
    elif option == 'status':
        cat.show_status()
    elif option == 'bye':
        cat.bye()


def main():
    pass
