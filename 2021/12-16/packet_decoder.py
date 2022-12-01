import sys

def convert_to_binary(hex_string):
    binary = ""
    for c in hex_string:
        if c == '0':
            binary += '0000'
        if c == '1':
            binary += '0001'
        if c == '2':
            binary += '0010'
        if c == '3':
            binary += '0011'
        if c == '4':
            binary += '0100'
        if c == '5':
            binary += '0101'
        if c == '6':
            binary += '0110'
        if c == '7':
            binary += '0111'
        if c == '8':
            binary += '1000'
        if c == '9':
            binary += '1001'
        if c == 'A':
            binary += '1010'
        if c == 'B':
            binary += '1011'
        if c == 'C':
            binary += '1100'
        if c == 'D':
            binary += '1101'
        if c == 'E':
            binary += '1110'
        if c == 'F':
            binary += '1111'
    return binary

# This doesn't work
def parse_packets(binary_string):
    packets = []
    index = 0
    current_string = binary_string
    while index < len(current_string):
        beginning_index = index
        version = int(binary_string[index:index+3], 2)
        packet_type = int(binary_string[index+3:index+6], 2)
        index += 6
        if packet_type == 4:
            found_zero_prefix = False
            groups = []
            while not found_zero_prefix:
                group = binary_string[index:index+5]
                if group[0] == '0':
                    found_zero_prefix = True
                index += 5
                groups.append(group[1:])
            packets.append({'version': version, 'packet_type': packet_type, 'groups': groups})
        else:
            length_type_id = binary_string[index]
            index += 1
            length = int(binary_string[index:index+11], 2)
            index += 11
            print(length_type_id, length)
            if length_type_id == '0':
                packets.append({'version': version, 'packet_type': packet_type, 'subpacket_string': binary_string[index:index+length]})
                index += length
            else:
                packets.append({'version': version, 'packet_type': packet_type, 'subpacket_string': binary_string[index:index+(length*11)]})
                index += length*11
        steps_to_go = (index - beginning_index) % 4
        index += steps_to_go
    return packets

def parse_packet(current_packet, packet_versions, num_packets_expecteds = None, packet_length_left = None):
    version = int(current_packet[0:3], 2)
    print(current_packet)
    print(version, len(current_packet), num_packets_expecteds, packet_length_left)
    packet_versions.append(version)
    packet_type = int(current_packet[3:6], 2)
    print("Version: " + str(version) + ", Type: " + str(packet_type))
    if packet_type == 4:
        index = 6
        found_zero_prefix = False
        while not found_zero_prefix:
            group = current_packet[index:index+5]
            if group[0] == '0':
                found_zero_prefix = True
            print(group)
            index += 5
        #steps_to_go = (index - 6) % 4
        #index += steps_to_go
        if packet_length_left:
            if packet_length_left == index:
                return
            if list(dict.fromkeys(list(current_packet[index:packet_length_left]))) == ['0']:
                return
            #parse_packet(current_packet[index:], packet_versions, packet_length_left = packet_length_left - index)
        elif num_packets_expecteds:
            if sum(num_packets_expecteds) == 1:
                return
            num_packets_expecteds[-1] -= 1
            if num_packets_expecteds[-1] == 0:
                num_packets_expecteds.pop()
            #parse_packet(current_packet[index:], packet_versions,  num_packets_expecteds = num_packets_expecteds)
        parse_packet(current_packet[index:], packet_versions, packet_length_left = packet_length_left - index, num_packets_expecteds = num_packets_expecteds)
    else:
        length_type_id = current_packet[6]
        print("Length type id: " + str(length_type_id))
        if length_type_id == '0':
            length = int(current_packet[7:22], 2)
            num_packets_expecteds[-1] -= 1
            parse_packet(current_packet[22:], packet_versions, packet_length_left = length, num_packets_expecteds = num_packets_expecteds)
        else:
            num = int(current_packet[7:18], 2)
            new_num_packets_expecteds = []
            if num_packets_expecteds:
                new_num_packets_expecteds = num_packets_expecteds + [num]
            else:
                new_num_packets_expecteds = [num]
            parse_packet(current_packet[18:], packet_versions, num_packets_expecteds = new_num_packets_expecteds, packet_length_left = packet_length_left - 18)



def part_1(hex_string):
    binary_string = convert_to_binary(hex_string)
    #packets = parse_packets(binary_string)
    packet_versions = []
    parse_packet(binary_string, packet_versions, num_packets_expecteds=[1], packet_length_left = len(binary_string))
    print(packet_versions)
    version_sum = 0
    for packet_version in packet_versions:
        version_sum += packet_version
    return version_sum

f = open(sys.argv[1], 'r')
transmission = f.read().strip()

print("Part 1: " + str(part_1(transmission)))
