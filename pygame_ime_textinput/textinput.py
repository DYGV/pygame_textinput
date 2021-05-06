from typing import List, Optional, Tuple

import pygame

from .text import Text


class TextInput(Text):
    def __init__(
        self, font: pygame.font.Font, font_color: Tuple[int, int, int] = (0, 0, 0)
    ):
        super().__init__()
        pygame.key.start_text_input()
        pygame.key.set_repeat(30)
        self.font = font
        self.font_color = font_color
        self.text_surface = None
         # テキスト入力時のキーとそれに対応するイベント
        self.event_trigger = {
            pygame.K_BACKSPACE: self.delete_left_of_cursor,
            pygame.K_DELETE: self.delete_right_of_cursor,
            pygame.K_LEFT: self.move_cursor_left,
            pygame.K_RIGHT: self.move_cursor_right,
            pygame.K_RETURN: self.enter,
        }
        self.input_text = ""
        self.set_surface(format(self))

    def set_surface(self, text: str) -> None:
        self.text_surface = self.font.render(text, True, self.font_color)

    def get_surface(self) -> Optional[pygame.Surface]:
        return self.text_surface

    def update(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            # キーダウンかつ、全角入力中でない
            if event.type == pygame.KEYDOWN and not self.is_editing:
                if event.key in self.event_trigger.keys():
                    self.input_text = self.event_trigger[event.key]()
                    self.set_surface(self.input_text)
                # 入力の確定
                if event.unicode in ("\r", "") and event.key == pygame.K_RETURN:
                    event = pygame.event.Event(pygame.USEREVENT, Text=self.input_text)
                    pygame.event.post(event)
                    # テキストボックスに"|"を表示
                    self.set_surface(format(self))
                    # "|"に戻す
                    self.input_text = format(self)
            elif event.type == pygame.TEXTEDITING:
                self.input_text = self.edit(event.text, event.start)
                self.set_surface(self.input_text)
            elif event.type == pygame.TEXTINPUT:
                self.input_text = self.input(event.text)
                self.set_surface(self.input_text)
