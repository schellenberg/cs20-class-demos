import microbit

happy_ish = "00000:" \
            "09090:" \
            "00000:" \
            "90000:" \
            "09990"
face = microbit.Image(happy_ish)

microbit.display.show(face)