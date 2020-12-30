def on_button_pressed_a():
    猴子.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    猴子.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

猴子: game.LedSprite = None
game.set_score(0)
猴子 = game.create_sprite(2, 4)
香蕉 = game.create_sprite(0, 0)
香蕉掉下數量 = 0

def on_forever():
    global 香蕉掉下數量
    香蕉.set(LedSpriteProperty.X, randint(0, 0))
    香蕉.set(LedSpriteProperty.Y, 0)
    for index in range(4):
        basic.pause(500 - game.score() * 10)
        香蕉.change(LedSpriteProperty.Y, 1)
    basic.pause(50)
    香蕉掉下數量 += 1
basic.forever(on_forever)

def on_forever2():
    if 香蕉.is_touching(猴子):
        香蕉.set(LedSpriteProperty.Y, 0)
        game.add_score(1)
    if 香蕉掉下數量 - game.score() == 5:
        game.game_over()
basic.forever(on_forever2)
