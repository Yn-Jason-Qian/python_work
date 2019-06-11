class Settings():
    """ 存储设置 """

    def __init__(self):
        self.width = 1200
        self.height = 600
        self.bg_color = (230, 230, 230)

        # 飞船的移动速度因子
        self.ship_speed_factor_x = 1.5
        self.ship_speed_factor_y = 1.5

        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 1
        
        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
