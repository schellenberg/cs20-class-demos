import microbit

#microbit.display.show(microbit.Image.ANGRY)

dice_one  = "33333:" \
            "30003:" \
            "30903:" \
            "30003:" \
            "33333"

dice_four = "33333:" \
            "39093:" \
            "30003:" \
            "39093:" \
            "33333"

dice = microbit.Image(dice_one)
microbit.display.show(dice)