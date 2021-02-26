class Vehicle:
    def __init__(self, owner, deceleration_amount, top_speed):
        self.speed = 0
        self.owner = owner
        self.deceleration_amount = deceleration_amount
        self.top_speed = top_speed

    def get_speed(self):
        return self.speed

    def accelerate(self, increase_speed):
        self.speed += increase_speed

    def breaking(self):
        self.speed -= 10

    def get_owner(self):
        return self.owner

    def set_owner(self, new_owner):
        self.owner = new_owner

    def get_top_speed(self):
        return self.top_speed


class Car(Vehicle):
    def __init__(self, owner, deceleration_amount, top_speed):
        super().__init__(owner, deceleration_amount, top_speed)
        self.reverse_gear = False

    def accelerate(self, increase_speed):
        if self.reverse_gear is False:
            if self.speed + increase_speed <= self.top_speed:
                self.speed += increase_speed
            else:
                print("MAX SPEED. YOUR SPEED IS NOW", self.top_speed)
                self.speed = self.top_speed
        else:
            if self.speed + increase_speed <= -self.top_speed:
                self.speed += increase_speed
            else:
                print("MAX SPEED. YOUR SPEED IS NOW", -self.top_speed)
                self.speed = -self.top_speed

    def breaking(self):
        if self.reverse_gear is False:
            if self.speed - self.deceleration_amount < 0:
                self.speed = 0
                print('Stopped')
            elif self.speed >= 0:
                self.speed -= self.deceleration_amount
            else:
                print('Stopped')
        else:
            if self.speed + self.deceleration_amount > 0:
                self.speed = 0
                print('Stopped')
            elif self.speed <= 0:
                self.speed += self.deceleration_amount
            else:
                print('Stopped')

    def set_reverse_gear(self, setting):
        if self.speed == 0:
            self.reverse_gear = bool(setting)
        else:
            print("Not applicable")


class Airplane(Vehicle):
    def __init__(self, owner, deceleration_amount, top_speed):
        super().__init__(owner, deceleration_amount, top_speed)
        self.in_air = False

    def accelerate(self, increase_speed):
        if self.speed + increase_speed <= self.top_speed:
            self.speed += increase_speed
        else:
            print("MAX SPEED. YOUR SPEED IS NOW", self.top_speed)
            self.speed = self.top_speed

    def breaking(self):
        if self.speed - self.deceleration_amount < 0:
            self.speed = 0
            print('Stopped')
        elif self.speed >= 0:
            self.speed -= self.deceleration_amount
        else:
            print('Stopped')

    def set_in_air(self):
        if self.speed > 250:
            self.in_air = True
        elif self.speed < 250:
            self.in_air = False

    def get_in_air(self):
        return self.in_air
