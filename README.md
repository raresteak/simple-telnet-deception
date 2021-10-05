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
{ "time": "05-2021-10T10:36:59", "src.ip": "127.0.0.1", "username": "maintenance", "password": "powerdown"}
{ "time": "05-2021-10T10:37:09", "src.ip": "127.0.0.1", "username": "root", "password": "password"}
{ "time": "05-2021-10T10:37:18", "src.ip": "127.0.0.1", "username": "toor", "password": "toor"}
{ "time": "05-2021-10T10:37:26", "src.ip": "127.0.0.1", "username": "user", "password": "cancelledInput"}
```
