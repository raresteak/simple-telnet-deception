#!/usr/bin/env python3
# purpose: Mimics a simple telnet daemon login prompts and records output
# starts a tcp listener on port and address with variables defined below
# author: Raresteak
# date: 6 October 2021
# version: 2
import datetime
import socket

HOST = '127.0.0.1'
PORT = 8023
FILE = "stn-results.json"
fh = open(FILE, "a")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            timeNow = datetime.datetime.now()
            conn.send(b'Login: ')
            username = ""
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                else:
                    try:
                        username = data.decode("utf-8").rstrip()
                    except UnicodeDecodeError:
                        username = "cancelledInput"
                    conn.send(b'Password: ')
                    password = ""
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        else:
                            try:
                                password = data.decode("utf-8").rstrip()
                            except UnicodeDecodeError:
                                password = "cancelledInput"
                            conn.sendall(b'\b \b')
                            break
                    break
            output = str("{ \"time\": \""
                         + timeNow.strftime('%d-%Y-%mT%H:%M:%S')
                         + "\", \"src.ip\": \"" + addr[0]
                         + "\", \"username\": \"" + username
                         + "\", \"password\": \"" + password + "\" }")
            print(output)
            fh.write(output + "\n")
