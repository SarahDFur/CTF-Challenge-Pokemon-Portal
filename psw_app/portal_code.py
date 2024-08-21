import tkinter as tk
import time
import asyncio
from scapy import all
from scapy.layers.inet import ICMP, IP
from scapy.packet import Raw
from scapy.sendrecv import send

FST_PSW = "pikachu_i_choose_u"
SND_PSW = "hoopa_arise!"

class PortalCTF:
    def __init__(self):
        self.isEntering = False
        self.root = tk.Tk()
        self.root.title("Portal CTF (〃￣︶￣)人(￣︶￣〃)")
        self.root.geometry("500x500")
        self.root.configure(bg="lightblue")

        self.success_label = tk.Label(self.root)
        self.success_label.pack()

        self.stage_label_title = tk.Label(text="Stage 1", font=('Comic Sans MS', 16))
        self.stage_label_title.pack(pady=2)

        self.stage_psw_input = tk.Entry(self.root, show="*")
        self.stage_psw_input.pack()

        self.error_label = tk.Label(self.root, text="", fg="red")
        self.error_label.pack()

        self.verify_button1 = tk.Button(self.root, text="Verify", command=self.verify_stage_1_psw)
        self.verify_button1.pack()

        self.root.mainloop()
    
    def verify_stage_1_psw(self):
        self.password1 = self.stage_psw_input.get()
        if self.password1 == FST_PSW:
            self.create_stage_2()
            # self.transmit_portal_key()
        else:
            self.error_label.config(text="Incorrect password")
    
    def create_stage_2(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Portal CTF (〃￣︶￣)人(￣︶￣〃)")
        self.root.geometry("500x500")

        self.success_label = tk.Label(self.root)
        self.success_label.pack()

        self.stage_label_title = tk.Label(text="Stage 2", font=('Comic Sans MS', 16))
        self.stage_label_title.pack(pady=2)

        self.stage_psw_input = tk.Entry(self.root, show="*")
        self.stage_psw_input.pack()

        self.error_label = tk.Label(self.root, text="", fg="red")
        self.error_label.pack()

        self.verify_button1 = tk.Button(self.root, text="Verify", command=self.verify_stage_2_psw)
        self.verify_button1.pack()
        # Create a simple ICMP echo request packet
        self.root.after(2000, self.transmit_portal_key)
        # for i in range(5):
        #     packet = IP(dst="127.0.0.1") / ICMP(type='echo-request', id=1234)
        #
        #     # Send the packet
        #     send(packet)
        #     time.sleep(3)
        #     print(packet)

        self.root.mainloop()



    def verify_stage_2_psw(self):
        self.password2 = self.stage_psw_input.get()
        if self.password2 == SND_PSW:
            self.success_label.config(text="Verified")
        else:
            self.error_label.config(text="Incorrect password")

    def transmit_portal_key(self):
        # Create a simple ICMP echo request packet
        while not self.isEntering:
            time.sleep(0.5)
            packet = IP(dst="127.0.0.1") / ICMP(type='echo-request', id=1234) / Raw(load="hoopa_arise!")

            # Send the packet
            send(packet)

            print(packet)
            self.root.update()


PortalCTF()