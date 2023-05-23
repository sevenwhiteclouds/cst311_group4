# Programming Assignment #2
## CST 311, Introduction to Computer Networks

READ INSTRUCTIONS CAREFULLY BEFORE YOU START THE ASSIGNMENT.

Assignment must be submitted electronically to [Canvas](https://csumb.instructure.com/) by 11:59 p.m. on the due date.
Late assignments will not be accepted.

Use the Teams on the Programming Assignment Teams document (also on Canvas under General Information → Team Information).
Select your Team leader and divide up work per the Programming Process instructions (also on Canvas under General Information → Team Information.)

Follow the steps below to develop and write the client part of a client server application. 
The naming convention of the file should be PA2_A_Server_Team<your team #>.py and PA2_A_Client_Team<your team #>py. 
Put your names in the program as well. 

Your client program must work with the server program given to you below. 
Your program must have sufficient comments to clearly explain how your code works.

This assignment is worth 150 points. The grading objectives for the assignment are given below.


## UDP Pinger

In this assignment, you will learn the basics of socket programming for UDP in Python. 
You will learn how to send and receive datagram packets using UDP sockets and also, how to set a proper socket timeout.
Throughout the assignment, you will gain familiarity with a Ping application and its usefulness in computing statistics such as packet loss rate.

You will first study a simple Internet ping server written in Python, and implement a corresponding client. 
The functionality provided by these programs is similar to the functionality provided by standard ping programs available in modern operating systems. 
However, these programs use a simpler protocol, UDP, rather than the standard Internet Control Message Protocol (ICMP) to communicate with each other. 
The ping protocol allows a client machine to send a packet of data to a remote machine, and have the remote machine return the data back to the client unchanged (an action referred to as echoing). 
Among other uses, the ping protocol allows hosts to determine round-trip times to other machines.

You are given the complete code for the Ping server below. Your task is to write the Ping client.

### Server starter Code

The server code found in the [src](src) folder fully implements a ping server. 
You can use the server code given below as starter code for the assignment. 
You need to run this code before running your client program.  
Further, you may need to update it to print out messages received from the client.

In this server code, 30% of the client’s packets are simulated to be lost. 
You should study this code carefully, as it will help you write your ping client.


#### Code discussion

The server sits in an infinite loop listening for incoming UDP packets. When a packet comes in and if a randomized integer is greater than or equal to 4, the server simply capitalizes the encapsulated data and sends it back to the client.
Packet Loss
UDP provides applications with an unreliable transport service. Messages may get lost in the network due to router queue overflows, faulty hardware or some other reasons. Because packet loss is rare or even non-existent in typical campus networks, the server in this assignment injects artificial loss to simulate the effects of network packet loss. The server creates a variable randomized integer which determines whether a particular incoming packet is lost or not.
Client Code
The client should send 10 pings to the server. See the Message Format below for each ping to be sent to the Server. Also print the message that is sent to the server.

Because UDP is an unreliable protocol, a packet sent from the client to the server may be lost in the network, or vice versa. 
For this reason, the client cannot wait indefinitely for a reply to a ping message. 
You should get the client to wait up to one second for a reply; if no reply is received within one second, your client program should assume that the packet was lost during transmission across the network. 
You will need to look up the Python documentation to find out how to set the timeout value on a datagram socket. 
If the packet is lost, print “Request timed out”.

The program must calculate the round-trip time for each packet and print it out individually. 
Have the client print out the information similar to the output from doing a normal ping command – see sample output below. 
Your client software will need to determine and print out the minimum, maximum, and average RTTs at the end of all pings from the client along with printing out the number of packets lost and the packet loss rate (in percentage). 
Then compute and print the estimated RTT, the DevRTT and the Timeout interval based on the RTT results.

#### Sample output of ping to Google.com

Here is a sample output from a ping of Google 4 times:

```shell
Pinging google.com [216.58.195.78] with 32 bytes of data:
Reply from 216.58.195.78: bytes=32 time=13ms TTL=54
Reply from 216.58.195.78: bytes=32 time=14ms TTL=54
Reply from 216.58.195.78: bytes=32 time=16ms TTL=54
Reply from 216.58.195.78: bytes=32 time=13ms TTL=54 Ping
statistics for 216.58.195.78:
Packets: Sent = 4, Received = 4, Lost = 0 (0% loss), Approximate
round trip times in milli-seconds:
Minimum = 13ms, Maximum = 16ms, Average = 14ms
```

#### Expected output of your program

```shell
mininet@mininet-vm:~/cst311/PA2$ python udp_pinger_client.py
Ping 1: sample_rtt = 0.105 ms, estimated_rtt = 0.105 ms, dev_rtt = 0.052
Ping 2: Request timed out
Ping 3: Request timed out
Ping 4: sample_rtt = 0.174 ms, estimated_rtt = 0.114 ms, dev_rtt = 0.054
Ping 5: sample_rtt = 0.096 ms, estimated_rtt = 0.111 ms, dev_rtt = 0.045
Ping 6: Request timed out
Ping 7: sample_rtt = 0.266 ms, estimated_rtt = 0.131 ms, dev_rtt = 0.067
Ping 8: Request timed out
Ping 9: sample_rtt = 0.207 ms, estimated_rtt = 0.140 ms, dev_rtt = 0.067
Ping 10: Request timed out
Summary values:
min_rtt  = 0.096 ms
max_rtt  = 0.266 ms
avg_rtt = 0.170 ms
Packet loss: 50.00%
Timeout Interval: 0.409 ms
```

### What to Hand in

You will hand in the complete client and server code to Canvas.
- [ ] Minutes of the 3 meetings.
- [ ] Screenshots of server and client side output in one pdf file.
- [ ] Copy of [output checker](https://docs.google.com/spreadsheets/d/1WxK9ww-oc5uNbU_b-58MholQ6KzyLp-6HvXW-z9mbIo/edit?usp=sharing)
  - [ ] Fill in columns B and C with RTTs and lost packets as indicated in the file - Output Checker. 
    - Your outputs in your screenshots must match the outputs calculated in the Output Checker.
- [ ] Source code
  - [ ] Server
  - [ ] Client

### Grading Objectives
- [ ] (30 points) You must complete this program in the Mininet VM. 
  - The screenshots for the running code and the results in the Output checker file must come from executing your code on the mininet VM.
- [ ] (10 points) Ping messages must be sent using UDP.
- [ ] (8 x 5 points) Calculate and print the following on the client side in milliseconds:
  - [ ] Round trip time (RTT) - If the server doesn’t respond, print “Request timed out”.
  - [ ] Minimum RTT
  - [ ] Maximum RTT
  - [ ] Average RTT (Leave out lost packets from average calculation)
  - [ ] Estimated RTT. Consider alpha = 0.125. (Look at slides at the end for formulae.)
  - [ ] Deviation RTT. Consider beta = 0.25. (Look at slides at the end for formulae.)
  - [ ] Timeout Interval (Look at slides at the end for formulae.)
  - [ ] Packet loss percentage
- [ ] (10 points) You must write the client code to do the assignment with the calculations in #3 above without the use of a list (or array). Find an efficient and effective use of storage and program speed.
- [ ] (5 points) Programs must be well documented.
- [ ] (5 points) Submission files are in order. (Look at the “What to hand in” section.)
- [ ] ***(50 points) Teamwork grade***
  - Each team member will grade each other teammate out of 10 points during [peer evaluation](https://forms.gle/vtt31GjK9Rrerews5). 
  I will average all team members’ grades and scale it to get your teamwork grade out of 50 points. 
  

During development, you should run the Server.py on your machine, and test your client by sending packets to localhost (or, 127.0.0.1). After you have fully debugged your code, you should see how your application communicates across the network with the ping server and ping client running on different machines.


