# Pygameのテキスト(英語・日本語)入力
## インストール
```
pip install git+https://github.com/DYGV/pygame_jp_textinput.git
```

## サンプル
```python
import sys

import pygame
from pygame.locals import *
from pygame_jp_textinput.textinput import TextInput


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.update()
    # 使うフォント、フォントカラー
    font = pygame.font.SysFont("yumincho", 30)
    font_color = (255, 0, 0)
    # フォントとフォントカラーでTextBoxをインスタンス化
    text_box = TextInput(font, font_color)
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == USEREVENT:
                # 入力確定したテキスト
                print(event.Text)
        pygame.display.get_surface().fill((112, 225, 112))
        text_box.update(events)
        screen.blit(text_box.get_surface, (10, 550))
        pygame.display.update()


if __name__ == "__main__":
    main()

```