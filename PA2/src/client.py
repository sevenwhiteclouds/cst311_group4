import socket
import time

# globals, server ip, port, dec place, socket timeout
SERVER = "10.0.0.1"
PORT = 12000
REQUESTS = 10
BUFFER_SIZE = 1024
PRECISION = 3
socket.setdefaulttimeout(1)

if __name__ == "__main__":
    print("Pinging server [" + SERVER + "] on port ["
          + str(PORT) + "] " + str(REQUESTS) + " times:")

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    min_rtt = max_rtt = est_rtt = avg_rtt = requests_ok = dev_rtt = 0.0

    for i in range(REQUESTS):
        timer_start = time.time()
        udp_socket.sendto("echo".encode(), (SERVER, PORT))

        try:
            udp_socket.recvfrom(BUFFER_SIZE)
        except socket.timeout:
            print("Ping " + str(i + 1) + ": Request timed out")
        else:
            requests_ok += 1
            sample_rtt = time.time() - timer_start

            if avg_rtt == 0.0:
                dev_rtt = sample_rtt / 2
                min_rtt = max_rtt = est_rtt = sample_rtt
            elif sample_rtt > max_rtt:
                max_rtt = sample_rtt
            elif sample_rtt < min_rtt:
                min_rtt = sample_rtt

            est_rtt = (1 - 0.125) * est_rtt + 0.125 * sample_rtt

            if i == 0:
                dev_rtt = (1 - 0) * dev_rtt + 0 * abs(sample_rtt - est_rtt)
            else:
                dev_rtt = 0.75 * dev_rtt + 0.25 * abs(sample_rtt - est_rtt)

            print("Ping " + str(i + 1)
                  + ": sample_rtt = " + str(round(sample_rtt, PRECISION))
                  + " ms, estimated_rtt = " + str(round(est_rtt, PRECISION))
                  + " ms, dev_rtt = " + str(round(dev_rtt, PRECISION)))

            avg_rtt += sample_rtt

    print("Summary values:\nmin_rtt = " + str(round(min_rtt, PRECISION))
          + " ms\nmax_rtt = " + str(round(max_rtt, PRECISION))
          + " ms\navg_rtt = " + str(round(avg_rtt / requests_ok, PRECISION))
          + " ms\nPacket loss: " + str(round(100 - (requests_ok / REQUESTS) * 100, PRECISION)) + "%\n"
          + "Timeout Interval: " + str(round(4 * dev_rtt + est_rtt, PRECISION)) + " ms")

    udp_socket.close()
