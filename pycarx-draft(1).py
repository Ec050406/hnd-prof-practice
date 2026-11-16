from picarx import Picarx

car = Picarx()
while True:
    try:
        if keyboard.is_pressed('w'):
            car.forward(50)
        elif keyboard.is_pressed('s'):
            car.backward(50)
        elif keyboard.is_pressed('a'):
            car.left(50)
        elif keyboard.is_pressed('d'):
            car.right(50)
        
    finally:
        car.stop()