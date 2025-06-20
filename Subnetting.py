import customtkinter as ct
ct.set_appearance_mode("dark")
#
#
#To compile again
#pyinstaller -F --paths=C:\Users\conra\PycharmProjects\pythonProject\venv\Lib\site-packages --noconsole  Subnetting.py
def ipv4():
    def cal(ip, mask):
        ip = ip.split(".")
        cidr = int(mask.split("/")[1])

        if len(ip) == 4 and 255 >= int(ip[0]) >= 0 and int(ip[1]) <= 255 and int(ip[1]) >= 0 and int(ip[2]) <= 255 and int(ip[2]) >= 0 and int(ip[3]) <= 255 and int(ip[3]) >= 0:
            for index, bit in enumerate(ip):
                ip[index] = format(int(bit), '08b')

            ip = ip[0] + ip[1] + ip[2] + ip[3]
            mask = ("1" * cidr) + ("0" * (32 - cidr))
            ho = ("0" * cidr) + ("1" * (32 - cidr))

            net = ip[:cidr] + '0' * (32 - cidr)
            netdec = str(int(net[0:8], 2)) + '.' + str(int(net[8:16], 2)) + '.' + str(int(net[16:24], 2)) + '.' + str(int(net[24:32], 2))
            minhost = str(int(net[0:8], 2)) + '.' + str(int(net[8:16], 2)) + '.' + str(int(net[16:24], 2)) + '.' + str(int(net[24:32], 2) + 1)

            broad = ip[:cidr] + '1' * (32 - cidr)
            broaddec = str(int(broad[0:8], 2)) + '.' + str(int(broad[8:16], 2)) + '.' + str(int(broad[16:24], 2)) + '.' + str(int(broad[24:32], 2))
            maxhost = str(int(broad[0:8], 2)) + '.' + str(int(broad[8:16], 2)) + '.' + str(int(broad[16:24], 2)) + '.' + str(int(broad[24:32], 2) - 1)

            text1 = "Network Address: " + netdec
            text2 = "Host Range: " + minhost + " - " + maxhost
            text3 = "Broadcast Address: " + broaddec
            text4 = "Number of Hosts: " + str(int(ho, 2)-1)
            netadd.configure(text=text1)
            netrange.configure(text=text2)
            hosts.configure(text=text4)
            broadadd.configure(text=text3)

        else:
            warn = ct.CTk()
            warn.title("Error")

            v4off = v4.geometry().find("+")
            offset = v4.geometry()[v4off+1:].split("+")

            v4pos = v4.geometry().find("+")
            posi = v4.geometry()[:v4pos].split("x")

            pos = "150x100+" + str(round(int(offset[0]) + int(posi[0])/3.2)) + "+" + str(round(int(offset[1]) + int(posi[1])/5))
            warn.geometry(pos)
            warn.attributes('-topmost', True)

            warning = ct.CTkLabel(warn, text="Error: IP is Invalid", font=("Ariel", 18))
            warning.pack()


            def quit():
                warn.destroy()
                warn.quit()

            butclose = ct.CTkButton(warn, text="OK", command=quit)
            butclose.pack(pady=12, padx=10)

            warn.mainloop()

    global text1,text2,text3,text4

    v4 = ct.CTk()
    v4.title("V4")
    v4.geometry(app.geometry())
    v4.minsize(400,400)

    title = ct.CTkLabel(v4, text="IPv4 Subnet Calculator", font=("Ariel", 20, "bold"), anchor="center")
    title.pack(pady=12, padx=10)

    ip = ct.CTkEntry(v4, placeholder_text="IP Address")
    ip.pack(pady=12, padx=10)

    mask_var = ct.StringVar(value="Subnet Mask")
    l32 = []
    for m in range(1, 33):
        l32.append("/" + str(m))
    mask = ct.CTkOptionMenu(v4, values=l32, variable=mask_var)
    mask.pack(pady=12, padx=10)

    calc = ct.CTkButton(v4, text="Calculate", command= lambda: cal(ip.get(), mask.get()))
    calc.pack(pady=12, padx=10)

    netadd = ct.CTkLabel(v4, text=text1)
    netadd.pack(pady=12, padx=10)
    netrange = ct.CTkLabel(v4, text=text2)
    netrange.pack(pady=12, padx=10)
    hosts = ct.CTkLabel(v4, text=text4)
    hosts.pack(pady=12, padx=10)
    broadadd = ct.CTkLabel(v4, text=text3)
    broadadd.pack(pady=12, padx=10)


    v4.mainloop()
def ipv6():
    def cal(ip, mask):
        if ip.count("::") < 2:
            ipb = ip.split(":")

            for a in range(len(ipb)):
                if '' in ipb:
                    ipb[ipb.index('')] = '0'
            print("Line 106" , ipb)
            for b in range(8 - len(ipb)):
                ipb.insert(ipb.index('0'),'0')
            print("Line 109", ipb)


            for check in ipb:
                if int(str(check),16) > int('ffff',16):
                    warn = ct.CTk()
                    warn.title("Error")

                    v4off = v6.geometry().find("+")
                    offset = v6.geometry()[v4off + 1:].split("+")

                    v4pos = v6.geometry().find("+")
                    posi = v6.geometry()[:v4pos].split("x")

                    pos = "250x100+" + str(round(int(offset[0]) + int(posi[0]) / 3.2)) + "+" + str(
                        round(int(offset[1]) + int(posi[1]) / 5))
                    warn.geometry(pos)
                    warn.attributes('-topmost', True)

                    warning = ct.CTkLabel(warn, text="Error: Hextet value greater than FFFF", font=("Ariel", 16))
                    warning.pack()

                    warn.mainloop()

            for i, a in enumerate(ipb):
                ipb[i] = format(int(a, 16), '016b')
            print("Line 135", ipb)



        else:
            warn = ct.CTk()
            warn.title("Error")

            v4off = v6.geometry().find("+")
            offset = v6.geometry()[v4off + 1:].split("+")

            v4pos = v6.geometry().find("+")
            posi = v6.geometry()[:v4pos].split("x")

            pos = "250x100+" + str(round(int(offset[0]) + int(posi[0]) / 3.2)) + "+" + str(
                round(int(offset[1]) + int(posi[1]) / 5))
            warn.geometry(pos)
            warn.attributes('-topmost', True)

            warning = ct.CTkLabel(warn, text="Error: Exceeded amount of valid ::", font=("Ariel", 16))
            warning.pack()

            warn.mainloop()
    v6 = ct.CTk()
    v6.title("V6")
    v6.geometry(app.geometry())
    v6.minsize(400, 400)

    title = ct.CTkLabel(v6, text="IPv6 Subnet Calculator", font=("Ariel", 20, "bold"), anchor="center")
    title.pack(pady=12, padx=10)

    ip = ct.CTkEntry(v6, placeholder_text="IP Address", width=300)
    ip.pack(pady=12, padx=10)

    mask_var = ct.StringVar(value="Subnet Mask")
    l128 = []
    for m in range(1, 129):
        l128.append("/" + str(m))
    mask = ct.CTkOptionMenu(v6, values=l128, variable=mask_var)
    mask.pack(pady=12, padx=10)

    calc = ct.CTkButton(v6, text="Calculate", command=lambda: cal(ip.get(), mask.get()))
    calc.pack(pady=12, padx=10)

    text4 = "Network Prefix: "
    text5 = "IP Range: "
    text6 = "Total Addresses: "

    netprefix = ct.CTkLabel(v6, text=text4)
    netprefix.pack(pady=12, padx=10)
    netrange = ct.CTkLabel(v6, text=text5)
    netrange.pack(pady=12, padx=10)
    broadadd = ct.CTkLabel(v6, text=text6)
    broadadd.pack(pady=12, padx=10)


    v6.mainloop()


#Main launcher for the calculators
app = ct.CTk()
app.title("Subnetting")

width = 300
height = 100
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width/2)
y = (screen_height/2)
app.geometry("%dx%d+%d+%d" % (width, height, x, y))

text1 = "Network Address: "
text2 = "Host Range:"
text3 = "Broadcast Address:"
text4 = "Number of Hosts:"

butframe = ct.CTkFrame(app)
butframe.columnconfigure(0, weight=1)
butframe.columnconfigure(1, weight=1)

header = ct.CTkLabel(app,text="What IP Version?", font=("Ariel", 20, 'bold'), anchor='center')
but1 = ct.CTkButton(butframe, text="IPv4", command=ipv4)
but2 = ct.CTkButton(butframe, text="IPv6", command=ipv6)

header.pack(padx=10, pady=15)
but1.grid(row=1, column=0)
but2.grid(row=1, column=1)

butframe.pack(fill="both")

app.mainloop()

