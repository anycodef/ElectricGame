from pygame.image import load
from pygame.transform import scale
from pygame.draw import rect


class CardImg:
    def __init__(self, screen, x_card, y_card, filename, width_card, height_card):

        self.screen = screen

        self.x_card = x_card
        self.y_card = y_card

        self.width_card = width_card
        self.height_card = height_card

        self.padding = 5
        self.radius = 5
        self.color_background = "dark blue"

        # for image
        self.new_height_img = None
        self.new_width_img = None

        self.img_src = load(filename)

        if self.height_card <= self.width_card:
            self.new_height_img = self.height_card - 2 * self.padding
            self.new_width_img = self.new_height_img * self.img_src.get_width() / self.img_src.get_height()
        else:
            self.new_width_img = self.width_card - 2 * self.padding
            self.new_height_img = self.height_card * self.img_src.get_height() / self.img_src.get_width()

        self.img_src = scale(self.img_src, [self.new_width_img, self.new_height_img])

        self.pos_x_img = self.x_card + (self.width_card - self.new_width_img) / 2
        self.pos_y_img = self.y_card + (self.height_card - self.new_height_img) / 2

    def set_pos(self, speed_y):
        if speed_y:
            self.y_card += speed_y
            self.pos_y_img += speed_y

    def show(self):

        # draw on the screen
        rect(self.screen, self.color_background, (self.x_card, self.y_card, self.width_card, self.height_card), border_radius=self.radius)

        # put image on the card image
        self.screen.blit(self.img_src, (self.pos_x_img, self.pos_y_img))










