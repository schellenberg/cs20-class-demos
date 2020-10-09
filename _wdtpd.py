import microbit
microbit.radio.config(group=132, queue=10)
microbit.radio.on()

while True:
    time.sleep(0.1)
    incoming = microbit.radio.receive_bytes()

    if incoming != "None":  #TODO: api.py will need better None handler.
        incoming = stripMakeCodeHeader(incoming)
        print(incoming)
