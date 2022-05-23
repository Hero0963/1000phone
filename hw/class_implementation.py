class Person(object):
    def __init__(self, gun):
        self.gun = gun

    def fire(self):
        self.gun.shoot()


class Gun(object):
    def __init__(self, bulletBox):
        self.bulletBox = bulletBox

    def shoot(self):
        if self.bulletBox.count == 0:
            print("no bullet")
        else:
            self.bulletBox.count -= 1
            print("shoot a bullet, now bulletCount= ", self.bulletBox.count)


class BulletBox(object):
    def __init__(self, count):
        self.count = count


bb = BulletBox(5)
gun = Gun(bb)
per = Person(gun)

per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
