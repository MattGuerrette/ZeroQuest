

class Enemy:

    def __init__(self, sprite, health):
        self.sprite = sprite
        self.health = health; #health is actually the fraction

    def check_dead(self):
        if self.health.is_zero:
            return True
        else:
            return False

class EnemyGroup:

    def __init__(self, enemies):
        self.enemies = enemies

