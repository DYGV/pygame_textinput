import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../pygame_ime_textinput"))

from text import Text


class TestText:
    """Textの単体テストをするクラス"""

    def test_input(self):
        text = Text()
        assert format(text) == "|"  # インスタンス化時はカーソルのみ
        assert text.input("HelloWorld") == "HelloWorld|"
        text.cursor_pos = 5
        assert text.input(" ") == "Hello World|"  # カーソル自体はmove_cursorメソッドで動かす

    def test_edit(self):
        text = Text()
        input_text = "こんにちは"
        for i, x in enumerate(input_text):
            assert text.edit(x, i + 1) == "[{}|]".format(x)

    def test_delete_left_of_cursor(self):
        text = Text()
        assert text.input("HelloWorld") == "HelloWorld|"
        for i in range(5):
            text.delete_left_of_cursor()
        assert format(text) == "Hello|"

    def test_delete_right_of_cursor(self):
        text = Text()
        assert text.input("HelloWorld") == "HelloWorld|"
        for i in range(5):
            text.move_cursor_left()
        for i in range(5):
            text.delete_right_of_cursor()
        assert format(text) == "Hello|"

    def test_enter(self):
        text = Text()
        text.input("HelloWorld")
        assert text.enter() == "HelloWorld"

    def test_move_cursor_left(self):
        text = Text()
        input_text = "HelloWorld"
        text.input(input_text)
        assert text.cursor_pos == len(input_text)
        for i in range(len(input_text)):
            text.move_cursor_left()
            assert text.cursor_pos == len(input_text) - i - 1

    def test_move_cursor_right(self):
        text = Text()
        input_text = "HelloWorld"
        text.input(input_text)
        assert text.cursor_pos == len(input_text)
        text.move_cursor_right()
        assert text.cursor_pos == len(input_text)  # カーソル位置は変わらないはず
        text.cursor_pos = 0
        for i in range(len(input_text)):
            text.move_cursor_right()
            assert text.cursor_pos == i + 1
