level = 0
score = 0

def on_button_pressed_ab():
    global level, score
    basic.show_string("reset?")
    while True:
        if input.button_is_pressed(Button.A):
            level = 0
            score = 0
            break
        elif input.button_is_pressed(Button.B):
            basic.show_string("canceled")
            basic.clear_screen()
            break
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_forever():
    pass
basic.forever(on_forever)
