# Input system support in Pygame

**This is a library that supports input using IME and direct input in pygame.**  
(PygameでIMEや直接入力を支援するライブラリです)  
As far as I can tell, you can type in English, Japanese, and Chinese.
## install with pip
```
pip install git+https://github.com/DYGV/pygame_textinput.git
```

## Usage of example
```python
import sys

import pygame
from pygame_textinput.textinput import TextInput


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    text_box = TextInput(pygame.font.SysFont("yumincho", 30), (255, 0, 0))
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.USEREVENT:
                # 入力確定したテキスト
                print(event.Text)
        screen.fill((112, 225, 112))
        text_box.update(events)
        screen.blit(text_box.get_surface(), (10, 550))
        pygame.display.update()


if __name__ == "__main__":
    main()
```
__In some environments, you can't use the "yumincho" font . Please refer to [this page](https://dygv.github.io/blog/post/2021/01/pygame%E3%81%AE%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E5%85%A5%E5%8A%9B/#%E3%83%95%E3%82%A9%E3%83%B3%E3%83%88%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6).__  
  
__You can also type in Chinese if you set up your IME and specify the font.__  
  
↓ Microsoft IME(Japanese)
![実行結果_jp](https://user-images.githubusercontent.com/8480644/117116657-941ea480-adc9-11eb-97fd-90c3400f4bfa.gif)  
  
↓ Microsoft pinyin(Chinese)
![実行結果_ch](https://user-images.githubusercontent.com/8480644/117170882-5c355280-ae05-11eb-84fe-c0d2a2760744.gif)
