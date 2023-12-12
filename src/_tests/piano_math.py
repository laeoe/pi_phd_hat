
def key_2freq(key):
    a = 440.0 # Base tone a4 = 440Hz
    return a * 2.0 **((key - 57) / 12)