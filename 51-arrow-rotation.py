import microbit
import time

arrow_images = [microbit.Image.ARROW_N, microbit.Image.ARROW_E, microbit.Image.ARROW_S, microbit.Image.ARROW_W]

#William's version
# def check_pressed_toggle(toggle):
#     if microbit.button_b.was_pressed():
#         return True
#     elif microbit.button_a.was_pressed():
#         return False
#     else:
#         return toggle
# 
# toggle = True
# while True:
#     for image in arrow_images:
#         while toggle == False:
#             toggle = check_pressed_toggle(toggle)
#         microbit.display.show(image)
#         time.sleep(0.25)

#Kevin's version
# list_item = 0
# while True:
#     if microbit.button_a.was_pressed():
#         while not microbit.button_b.was_pressed():
#             microbit.display.show(arrow_images[list_item])
#             list_item += 1
#             if list_item == 4:
#                 list_item = 0
#             time.sleep(0.25)

#Eason's version
# while True:
#     for image in arrow_images:
#         if microbit.button_a.was_pressed():
#             while not microbit.button_b.was_pressed():
#                 time.sleep(0.5)
#         microbit.display.show(image)
#         time.sleep(0.25)