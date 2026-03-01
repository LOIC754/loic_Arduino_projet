import serial 
import tkinter 

arduinoData = serial.Serial('COM3', 9600)

def led_on():
    arduinoData.write(b'1')
def led_off():
    arduinoData.write(b'0')
led_controlm_window = tkinter.Tk()
led_controlm_window.title("LED Control")
led_controlm_window.geometry("300x200")
buton= tkinter.Button
btn1 = button(led_controlm_window, text="LED ON", command=led_on)
btn1.pack(pady=20)
btn2 = button(led_controlm_window, text="LED OFF", command=led_off)
btn2.pack(pady=20)
btn1.grid(row=0, column=1, padx=10, pady=10)
btn2.grid(row=1, column=1, padx=10, pady=10)
led_controlm_window.mainloop()
input("Press Enter to exit")