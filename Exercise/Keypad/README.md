## Keypad Component

A configurable keypad written using tkinter. 
Keypad behaves like a tkinter component.

To create a 2x2 keypad use:
```python
keys = ['1','2','3','4']

keypad = Keypad(parent, keynames=keys, columns=2)
```

to bind key presses to an event handler use (for example):
```python
def key_handler(event):
    key = event.widget['text']
    print(key, "pressed")

keypad.bind("<Button-1>", key_handler)
```




