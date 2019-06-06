class Settings():
    """ 存储设置 """

    def __init__(self):
        self.width = 1200
        self.height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的移动速度因子
        self.ship_speed_factor_x = 1.5
        self.ship_speed_factor_y = 1.5
