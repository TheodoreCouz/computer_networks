import pyshark
import matplotlib.pyplot as plt
import datetime

def network_conversation(packet):
    try:
        protocol = packet.transport_layer
        source_address = packet.ip.src
        source_port = packet[packet.transport_layer].srcport
        destination_address = packet.ip.dst
        destination_port = packet[packet.transport_layer].dstport
        return (f'{protocol} {source_address}:{source_port} --> {destination_address}:{destination_port}')
    except AttributeError as e:
        pass

# Graphs data arrays
UDP_TCP_intervals = []
Ports_data = {}
#

capture = pyshark.FileCapture('X_receivesMessage_Y.pcapng')

minTime = float("inf")
maxTime = float("-inf")

packets = {}
for i,packet in enumerate(capture):
    
    if i%1000==0 and i>0:
        print(f"{i} packets parsed...")

    protocol = packet.transport_layer
    if not (protocol in packets.keys()):
        packets[protocol] = []
    
    time = packet.sniff_time.timestamp()
    if(time < minTime): minTime = time
    if(time > maxTime): maxTime = time

    source_port         = packet[packet.transport_layer].srcport
    destination_port    = packet[packet.transport_layer].dstport 
    if not (source_port in Ports_data.keys()):      Ports_data[source_port] = 0
    if not (destination_port in Ports_data.keys()): Ports_data[destination_port] = 0

    Ports_data[source_port] += 1
    Ports_data[destination_port] += 1

    packets[protocol].append((time, packet))

# Stacked UDP/TCP bar chart
step = 0.1 # 100ms
timeWindow = maxTime - minTime
numberOfSteps = int(timeWindow/step) + 1
for i in range(numberOfSteps):
    UDP_TCP_intervals.append({
        "UDP": [],
        "TCP": []
    })

def timeToInterval(timestamp):
    global step
    return int(timestamp/step)

for protocol in packets.keys():
    packets_for_protocol = packets[protocol]

    for i,data in enumerate(packets_for_protocol):

        time, packet_ = data

        source_address      = packet_.ip.src
        source_port         = packet_[packet_.transport_layer].srcport
        destination_address = packet_.ip.dst
        destination_port    = packet_[packet_.transport_layer].dstport 
        packet_time         = packet_.sniff_time
        packet_timestamp    = packet_.sniff_timestamp
        
        indexInGraph = timeToInterval(time - minTime)
        UDP_TCP_intervals[indexInGraph][protocol].append(packet_)

x = [i*step for i in range(len(UDP_TCP_intervals))]
UDP = []
TCP = []

for g in UDP_TCP_intervals:
    UDP.append(len(g["UDP"]))
    TCP.append(len(g["TCP"]))
 
plt.bar(x, TCP, color='r', label="TCP packets")
plt.bar(x, UDP, bottom=TCP, color='b', label="UDP packets")
plt.legend()
plt.show()

# Ports graph
plt.bar(Ports_data.keys(), Ports_data.values(), color='g', label="Packet per port")
plt.legend()
plt.show()