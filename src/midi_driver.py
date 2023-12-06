import mido

# List available MIDI input ports (find your MIDI keyboard)
input_ports = mido.get_input_names()
print(input_ports)

if not input_ports:
    print("No MIDI input ports found. Make sure your MIDI keyboard is connected.")
else:
    # Open the first available MIDI input port
    with mido.open_input(input_ports[0]) as port:
        print(f"Listening to MIDI input from {input_ports[0]}...")
        
        try:
            # Infinite loop to continuously receive MIDI messages
            for message in port:
                print(f"Received MIDI message: {message}")
        
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt, Exiting...")