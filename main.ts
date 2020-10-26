let level = 0
let score = 0
input.onButtonPressed(Button.AB, function () {
    basic.showString("reset?")
    while (true) {
        if (input.buttonIsPressed(Button.A)) {
            level = 0
            score = 0
            break;
        } else if (input.buttonIsPressed(Button.B)) {
            basic.showString("canceled")
            basic.clearScreen()
            break;
        }
    }
})
basic.forever(function () {
	
})
