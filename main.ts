input.onButtonPressed(Button.A, function () {
    猴子.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function () {
    猴子.change(LedSpriteProperty.X, 1)
})
let 猴子: game.LedSprite = null
game.setScore(0)
猴子 = game.createSprite(2, 4)
let 香蕉 = game.createSprite(0, 0)
let 香蕉掉下數量 = 0
basic.forever(function () {
    香蕉.set(LedSpriteProperty.X, randint(0, 0))
    香蕉.set(LedSpriteProperty.Y, 0)
    for (let index = 0; index < 4; index++) {
        basic.pause(500 - game.score() * 10)
        香蕉.change(LedSpriteProperty.Y, 1)
    }
    basic.pause(50)
    香蕉掉下數量 += 1
})
basic.forever(function () {
    if (香蕉.isTouching(猴子)) {
        香蕉.set(LedSpriteProperty.Y, 0)
        game.addScore(1)
    }
    if (香蕉掉下數量 - game.score() == 5) {
        game.gameOver()
    }
})
