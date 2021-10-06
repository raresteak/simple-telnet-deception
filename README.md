# simple-telnet-deception
A low interaction telnet honeypot/deception written in Python3, logs username and password input

## Usage
1. Update HOST, PORT, FILE variables.

2. Execute
```
python3 ./simple-telnet-deception.py
```

## Output 
Logged to a file and shown on the screen in json format.  Example:
```
{ "time": "2021-10-06T16:55:29", "src.ip": "127.0.0.1", "username": "root", "password": "password" }
{ "time": "2021-10-06T16:55:35", "src.ip": "127.0.0.1", "username": "toor", "password": "toor" }
{ "time": "2021-10-06T16:55:40", "src.ip": "127.0.0.1", "username": "user", "password": "cancelledInput" }
{ "time": "2021-10-06T16:55:44", "src.ip": "127.0.0.1", "username": "cancelledInput", "password": "cancelledInput" }
```
