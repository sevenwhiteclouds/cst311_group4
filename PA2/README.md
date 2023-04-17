# Programming Assignment #2
## CST 311, Introduction to Computer Networks

READ INSTRUCTIONS CAREFULLY BEFORE YOU START THE ASSIGNMENT.

Assignment must be submitted electronically to [Canvas](https://csumb.instructure.com/) by 11:59 p.m. on the due date.
Late assignments will not be accepted.

Use the Teams on the Programming Assignment Teams document (also on Canvas under General Information → Team Information).
Select your Team leader and divide up work per the Programming Process instructions (also on Canvas under General Information → Team Information.)

Follow the steps below to develop and write the client part of a client server application. 
The naming convention of the file should be PA2_A_Server_Team<your team #>.py, PA2_A_Client_Team<your team #>py, and PA2_A_Proxy_Team<your team #>py. 
Put your names in the program as well. 

Your client program must work with the server program given to you below. 
Your program must have sufficient comments to clearly explain how your code works.

This assignment is worth 150 points. The grading objectives for the assignment are given below.

## Web Server and Proxy Server

### Part 1: Web Server

In this part, you will learn the basics of socket programming for TCP connections in Python: how to create a socket, bind it to a specific address and port, as well as send and receive a HTTP packet. 
You will also learn some basics of HTTP header format. 
You will develop a web server that handles one HTTP request at a time. 
Your web server should accept and parse the HTTP request, get the requested file from the server’s file system, create an HTTP response message consisting of the requested file preceded by header lines, and then send the response directly to the client. 
If the requested file is not present in the server, the server should send an HTTP “404 Not Found” message back to the client.

#### Code
In Appendix A, you will find the skeleton code for the Web server. 
You are to complete the skeleton code, using the socket library. 
The places where you need to fill in code are marked with `#Fill in start` and `#Fill in end`. 
Each place may require one or more lines of code.  
Choose the port number that the web server will be listening on; use a port number >1024, so that the root does not have to start the web server.   
Use the domain name www.cst311.test for your web server; you will use this domain name in a future lab.

#### Running the Server 
1. Set up Environment.   
- In Mininet, set up a three switch, three host network.  Host h1 will be the web client.  Host h2 will be the Web Server; its fully qualified domain name will be www.cst311.test.  Host h3 will be the Proxy Server in part 3.  
- Run the labs in the `$HOME/CST311` directory.  Enter the web server's domain name entry in the /etc/hosts file.  
2. Put an HTML file (e.g., HelloWorld.html) in the same directory that the server is in (`$HOME/CST311`). 
  Run the server program.  
  From host h1, run the simple http client, wget, that should already be loaded on your VM.  
  Run the three below tests.  
  In the tests, provide the corresponding URL.  
  For example: http://10.10.10.25:6789/(yourfilename).  
  (`yourfilename`) is the name of the file you placed in the server directory.  
  Note the use of the port number after the colon. 
  You need to replace this port number with whatever port you have used in the server code.  
  In the above example, we have used the port number 6789.  
  1. Test 1:  Omit the filename in the URL request.  The web server should respond with the index.html file.  (Note If you omit the port number, wget will assume port 80 and you will get the web page from the server only if your server is listening at port 80.) 
  2. Test 2:  Add (yourfilename) to the url request. The browser should then display the contents of the html file that you created. 
  3. Test 3: Then try to get a file that is not present at the server. You should get a “404 Not Found” message.


### Part 2: Web Client

For Part 2, instead of using wget, write your own HTTP client to test your server. 
Your client will connect to the server using a TCP connection, send an HTTP request to the server, and display the server response as an output. 
You can assume that the HTTP request sent is a GET method. 

#### Running the Client:
The client should take command line arguments specifying the server host name, the port at which the server is listening, and the path at which the requested object is stored at the server.  
The following is an input command format to run the client. 
```bash
python3 webclient.py [server_name] [server_port] [/path/file_name]
```

Use the socket function `gethostbyname()` in your client script to convert the server name to its IP address.


### Part 3: Proxy Server

In Part 3, you will learn how web proxy servers work and one of their basic functionalities – caching.  
Your task is to develop a small web proxy server which is able to cache web pages.  
It is a very simple proxy server which only understands simple GET-requests, but is able to handle all kinds of objects - not just HTML pages, but also images. 
Generally, when the client makes a request, the request is sent to the web server. 
The web server then processes the request and sends back a response message to the requesting client. 
To  improve the performance, we create a proxy server between the client and the web server.  
Now, both the request message sent by the client and the response message delivered by the web server pass through the proxy server. 
In other words, the client requests the objects via the proxy server. 
The proxy server will forward the client’s request to the web server. 
The web server will then generate a response message and deliver it to the proxy server, which in turn sends it to the client. 


#### Code 
In Appendix B, you will find the skeleton code for the client. 
You are to complete the skeleton code. 
The places where you need to fill in code are marked with `#Fill in start` and `#Fill in end`. Each place may require one or more lines of code.

#### Running the Proxy Server
For this part of the lab, you will again use the wget command for the browser. 
First configure the wget environment variables and initialization file using the information in [note 2](#2).
Make sure the web server from Part 1 is running.
Start the proxy server program on host h3 using your command prompt.
Then from host h1, request a web page with wget.  Direct the requests to the proxy server using your IP address and port number. 
For e.g. http://localhost:8888/www.google. 
You will replace the port number used here “8888” with the port number you have used in your server code at which your proxy server is listening. 
For your information, you can also directly configure a web browser to use a proxy. 
See [Note 3](#3). 



### What to Hand in

- [ ] You will hand in the complete web server, web client, proxy server and HTTP/2 web server Python scripts. 
- [ ] Minutes of the 3 team meetings. 
- [ ] Screenshots of server and client-side output for Part 1.  
- [ ] Screenshots of the client side output for Part 2
- [ ] Screenshots of the server side and client side output for Part 3.
- [ ] One submission per Team.

- [ ] Minutes of the 3 meetings.
- [ ] Screenshots of server and client side output in one pdf file.
- [ ] Fill in columns B and C with RTTs and lost packets as indicated in the file - Output Checker. 
- Your outputs in your screenshots must match the outputs calculated in the Output Checker.

### Grading Objectives
- [ ] (35 points) Successfully running the web server in Part 1.  You must run this program in the Mininet VM. The screenshots for the running code must come from executing your code on the mininet VM.
- [ ] (25 points) Successfully running the web client in Part 2.
- [ ] (25 points) Successfully running the proxy server as described in Part 3.
- [ ] (10 points) Documentation.
- [ ] (10 points) Submission files are in order. (Look at the “What to hand in” section.)
- [ ] ***(45 points) Teamwork grade***
  - Each team member will grade each other teammate out of 10 points during [peer evaluation](https://forms.gle/vtt31GjK9Rrerews5). 
  I will average all team members’ grades and scale it to get your teamwork grade out of 50 points. 
  
## Notes

<a id="1">[1]</a>
Parts 1-3 are based on the Web Server and Proxy Web Server labs included as student resources in Computer Networking: A Top-Down Approach, Kurose and Ross, 8th edition.


<a id="2">[2]</a>
[How to use wget to download file via proxy – The Geek Diary](https://www.thegeekdiary.com/how-to-use-wget-to-download-file-via-proxy/)

<a id="3">[3]</a>
Configuring your Browser.  
For your information, you can also directly configure a web browser to use your proxy.
This depends on your browser. 
In Microsoft Edge, you can set the proxy in Tools > Internet Options > Connections tab > LAN Settings. 
In Chrome (and derived browsers such as Mozilla), you can set the proxy in Tools > Options > Advanced tab > Network tab > Connection Settings. 
In both cases you need to give address of the proxy and the port number that you gave when you ran the proxy server

