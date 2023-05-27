# CST 311 Programming Assignment #3 Starter code

Contains starter code for CST311 Programming Assignment #3 and consists of two files [client.py](client.py) and [server.py](server.py).

## Usage

Both scripts requirement minimum of python 3.4[^1] to execute.
To use first call `python server.py` in one terminal window followed by `python client.py` in another.

```shell
$ python server.py
INFO:__main__:The server is ready to receive on port 12000
```

```shell
$ python client.py
Input lowercase sentence:
```

### Example Execution

```shell
$ python server.py
INFO:__main__:The server is ready to receive on port 12000
INFO:__main__:Connected to client at ('127.0.0.1', 52569)
INFO:__main__:Recieved query test.txt "Hello"
```

```shell
$ python client.py
Input lowercase sentence:Hello
From Server:
HELLO
```

### Files included:
- [client.py](client.py)
- [server.py](server.py)

[^1]: Note, this is untested but likely a bare minimum.  Probably works down to 2.7, but might have some behavior issues.
