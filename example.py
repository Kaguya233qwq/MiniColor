from mini_color import color, Color, Style

text_1 = color.green('我只是一个输出')
text_2 = color.red(
    '我只是一个输出',
    back=Color.BLACK
)
text_3 = color.random_color(
    '我只是一个输出',
    back=Color.random(),
    style=Style.HighLight
)

if __name__ == '__main__':
    print(text_1)
    print(text_2)
    print(text_3)
