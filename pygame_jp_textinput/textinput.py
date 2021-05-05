import pygame
from pygame.locals import *

from .text import Text


class TextInput(Text):
    def __init__(self, font, font_color=(0, 0, 0)):
        super().__init__()
        pygame.key.start_text_input()
        self.font = font
        self.font_color = font_color
        self.text_surface = None
        self.input_text = ""
        self.set_surface(format(self))

    def set_surface(self, text: str):
        self.text_surface = self.font.render(text, True, self.font_color)

    @property
    def get_surface(self):
        return self.text_surface

    def update(self, events):
        # テキスト入力時のキーとそれに対応するイベント
        event_trigger = {
            K_BACKSPACE: self.delete_left_of_cursor,
            K_DELETE: self.delete_right_of_cursor,
            K_LEFT: self.move_cursor_left,
            K_RIGHT: self.move_cursor_right,
            K_RETURN: self.enter,
        }
        for event in events:
            # キーダウンかつ、全角入力中でない
            if event.type == KEYDOWN and not self.is_editing:
                if event.key in event_trigger.keys():
                    self.input_text = event_trigger[event.key]()
                    self.set_surface(self.input_text)
                # 入力の確定
                if event.unicode in ("\r", "") and event.key == K_RETURN:
                    event = pygame.event.Event(pygame.USEREVENT, Text=self.input_text)
                    pygame.event.post(event)
                    # テキストボックスに"|"を表示
                    self.set_surface(format(self))
                    # "|"に戻す
                    self.input_text = format(self)
            elif event.type == TEXTEDITING:
                self.input_text = self.edit(event.text, event.start)
                self.set_surface(self.input_text)
            elif event.type == TEXTINPUT:
                self.input_text = self.input(event.text)
                self.set_surface(self.input_text)
