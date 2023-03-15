import pyshark
import matplotlib.pyplot as plt

capture = pyshark.FileCapture('./traces/Ethernet/background_noise.pcapng')

lines = []

for i,packet in enumerate(capture):

    if i%1000==0 and i>0:
        print(f"{i} packets parsed...")

    try:
        source_address      = packet.ip.src
        source_port         = packet[packet.transport_layer].srcport
        destination_address = packet.ip.dst
        destination_port    = packet[packet.transport_layer].dstport 

        line = f"{source_address}:{source_port} {destination_address}:{destination_port}"

        if line in lines:
            continue

        lines.append(line)
    except:
        pass

with open('Data/noise.txt', 'w') as f:
    f.write("FROM TO\n")
    for line in lines:
        f.write(f"{line}\n")