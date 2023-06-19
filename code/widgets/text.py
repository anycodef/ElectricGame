from pygame.font import SysFont
from pygame.draw import rect


def text_to_words_img_list(text: str, t_color, b_color, s_text, n_font):
    content = text
    font = SysFont(n_font, s_text)
    list_img_word_of_text = [font.render(word, False, t_color, b_color) for word in content.split(" ")]
    return list_img_word_of_text


def generate_list_pos_of_all_img_words_return_height_card(x_card, y_card, width_card, list_img_words, padding,
                                                          space_between_lines_words, space_between_words):
    list_list_img_pos = []

    x = x_card + padding
    y = y_card + padding

    height_word = None
    height_card = 2 * padding

    for img_w in list_img_words:
        if not height_word:
            height_word = img_w.get_height()
            height_card += height_word

        if x + img_w.get_width() > x_card + width_card - padding:
            x = x_card + padding
            y += height_word + space_between_lines_words
            height_card += height_word + space_between_lines_words

        list_list_img_pos.append([img_w, [x, y]])

        x += img_w.get_width() + space_between_words

    return list_list_img_pos, height_card


class CardText:
    def __init__(self, screen, x_card, y_card, width_card, c_card, text: str, s_text, t_color, b_color=None,
                 n_font='arial'):

        # main surface
        self.screen = screen

        # style card
        self.width_card = width_card
        self.color_card = c_card
        self.radius = 10

        # calculate of space
        self.padding = 10
        self.space_between_lines_words = 5
        self.space_between_words = 3

        self.x_card = x_card
        self.y_card = y_card

        # list words image for put in card
        self.list_img_word = text_to_words_img_list(text, t_color, b_color, s_text, n_font)
        self.list_of_list_img_word_with_position, self.height_card = generate_list_pos_of_all_img_words_return_height_card(
            self.x_card, self.y_card, self.width_card, self.list_img_word, self.padding,
            self.space_between_lines_words, self.space_between_words)

    def set_pos(self, speed_y):

        if speed_y:
            self.y_card += speed_y

            for index in range(self.list_of_list_img_word_with_position.__len__()):
                self.list_of_list_img_word_with_position[index][1][1] += speed_y

    def show(self):

        # show card
        rect(self.screen, self.color_card, (self.x_card, self.y_card, self.width_card, self.height_card),
             border_radius=self.radius)

        # show all words
        for img_w, pos in self.list_of_list_img_word_with_position:
            if -img_w.get_height() < pos[1] < self.screen.get_height():
                self.screen.blit(img_w, pos)



"""
    def __init__(self, screen, width_card, c_card, text: str, s_text, t_color, b_color=None, n_font='arial'):

        # main surface
        self.screen = screen

        # style card
        self.width_card = width_card
        self.color_card = c_card
        self.radius = 10

        # calculate of space
        self.padding = 10
        self.space_between_lines_words = 10
        self.space_between_words = 4

        self.x_card_current = 10
        self.y_card_current = 10

        # list words image for put in card
        self.list_img_word = text_to_words_img_list(text, t_color, b_color, s_text, n_font)
        self.list_of_list_img_word_with_position, self.height_card = generate_list_pos_of_all_img_words_return_height_card(self.x_card_current, self.y_card_current, self.width_card, self.list_img_word, self.padding, self.space_between_lines_words, self.space_between_words)

    def show(self):

        # show card
        rect(self.screen, self.color_card, (self.x_card_current, self.y_card_current, self.width_card, self.height_card), border_radius=self.radius)

        # show all words
        for img_w, pos in self.list_of_list_img_word_with_position:
            self.screen.blit(img_w, pos)
"""