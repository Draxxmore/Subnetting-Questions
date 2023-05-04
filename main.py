#!/usr/bin/python3
"""
This python script runs exercises based on Block 4 - Networking Fundamentals
of the Cyber Warfare Operater's (CWO) course. 
"""

from random import randint
import platform
import os

__author__ = "William Scarset"
__email__ = "wscarset@gmail.com"
__status__ = "Development"


def clear_screen():
    if platform.system == 'win32':
        os.system('cls')
    else:
        os.system('clear')


def setup1():
    """
    Generates random IP address and binary list.

    Returns:
        tuple: IPv4 address (string), binary list (list)
    """
    ip_addr = [randint(1, 255) for num in range(4)]
    binary_list = [bin(x) for x in ip_addr]

    for idx, binary in enumerate(binary_list):
        binary = binary[2:]
        binary_list[idx] = binary
        bin_len = len(binary)

        if bin_len < 8:
            num_zeros = 8 - bin_len
            new_bin = "0" * num_zeros + binary
            binary_list[idx] = new_bin

    return ip_addr, binary_list


def setup2():
    """
    setup2() generates a valid hexadecimal value

    Returns:
        string: Hexadecimal value 
    """
    value_list = ['0', '1', '2', '3', '4', '5', '6',
                  '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hex_value = ''
    for item in range(4):
        hex_value += value_list[randint(0, 15)]

    return hex_value


def bin2dec():
    """
    bin2dec runs the exercise to convert a binary value to its decimal equivalent.
    """
    ip_addr, binary_list = setup1()

    while True:
        clear_screen()
        print(
            f'Convert this binary into an IP address: {" ".join(binary_list)}\n'
        )
        user_ans = input(f'Answer (Example: 127.0.0.1): ')
        ans_split = list(map(int, user_ans.split('.')))

        if ans_split != ip_addr:
            print(f'Your answer was not right, please try again!\n')
        else:
            print(f'Correct!\n')

            continue_prompt = input('Do you want to continue? (y/n): ')
            if continue_prompt.lower() == 'y':
                bin2dec()
            else:
                break


def dec2bin():
    """
    dec2bin() runs the exercise to convert a decimal value to its binary equivalent.
    """
    setup = setup1()
    ip_addr = setup[0]

    while True:
        clear_screen()
        print(
            f'Convert the following IP Address to Binary: {".".join(list(map(str, ip_addr)))}\n')

        user_ans = input('Answer (place spaces between each ip_addr): ')

        ans_split = user_ans.split(" ")
        correct = 0
        for idx, num in enumerate(ans_split):
            if int(num, base=2) != ip_addr[idx]:
                print(f'Your answer was not right, please try again!\n')
                break
            correct += 1

        if correct == 4:
            print('Correct!')

            continue_prompt = input('Do you want to continue? (y/n): ')
            if continue_prompt.lower() == 'y':
                dec2bin()
            else:
                break


def hex2dec():
    """
    hex2dec() runs the exercise to convert a hexadecimal value to its decimal equivalent.
    """
    hex_value = setup2()

    while True:
        clear_screen()
        print(
            f'Return the decimal equivalent of this hexidecimal number: {hex_value} \n')
        user_ans = input('Answer (must be a number i.e. 12345): ')

        if int(user_ans) != int(hex_value, base=16):
            print('Your answer is not right, please try again!\n')
        else:
            print('Correct!')
            continue_prompt = input('Would you like to continue? (y/n): ')

            if continue_prompt == 'y':
                hex2dec()
            else:
                break


def dec2hex():
    """
    dec2hex() runs the exercise to convert a decimal value to its hexadecimal equivalent.
    """
    result = setup1()
    ip_addr = result[0]
    hex_list = [hex(num) for num in ip_addr]

    for idx, num in enumerate(hex_list):
        num = num[2:]
        hex_list[idx] = num.upper()

        if len(num) < 2:
            num_zeroes = 2 - len(num)
            new_num = "0" * num_zeroes + num
            hex_list[idx] = new_num.upper()

    while True:
        clear_screen()
        print(
            f'Convert the following IP address to its hexadecimal equivalent: {".".join(list(map(str, ip_addr)))}\n')

        octet1 = False
        octet2 = False
        octet3 = False
        octet4 = False

        while octet1 == False:
            user_ans1 = input('Hexadecimal for first octet (i.e. AE): ')

            if user_ans1 != hex_list[0]:
                print('Your answer is not right. Please try again!\n')
            else:
                print('Correct!\n')
                octet1 = True

        while octet2 == False:
            user_ans2 = input('Hexadecimal for first octet (i.e. AE): ')

            if user_ans2 != hex_list[1]:
                print('Your answer is not right. Please try again!\n')
            else:
                print('Correct!\n')
                octet2 = True

        while octet3 == False:
            user_ans3 = input('Hexadecimal for first octet (i.e. AE): ')

            if user_ans3 != hex_list[2]:
                print('Your answer is not right. Please try again!\n')
            else:
                print('Correct!\n')
                octet3 = True

        while octet4 == False:
            user_ans4 = input('Hexadecimal for first octet (i.e. AE): ')

            if user_ans4 != hex_list[3]:
                print('Your answer is not right. Please try again!\n')
            else:
                print('Correct!\n')
                octet4 = True

        if octet1 == True and octet2 == True and octet3 == True and octet4 == True:
            print('You got them all right! Congratulations!')
            continue_prompt = input('Do you want to continue? (y/n): ')

            if continue_prompt.lower() == 'y':
                dec2hex()
            else:
                break


def submask(ip):
    """
    Creates a subnet mask based on the IPv4 Address given

    Args:
        ip (string): IPv4 Address

    Returns:
        tuple: CIDR (integer), list of IP octets represented as binary (list), combined string of binary for subnet mask (string)
    """
    octet_list = ip.split(".")

    if int(octet_list[0]) <= 127:
        cidr = 30 - randint(0, 21)
    if int(octet_list[0]) > 127 and int(octet_list[0]) <= 191:
        cidr = 30 - randint(0, 13)
    if int(octet_list[0]) > 191:
        cidr = 30 - randint(0, 5)

    bits = "1" * cidr
    while len(bits) < 32:
        bits += "0"
    bin_split = [bits[i:i+8] for i in range(0, len(bits), 8)]

    return cidr, bin_split, bits


def network_class(ip):
    """Generates class based on IP given

    Args:
        ip (string): IPv4 address (i.e. '127.0.0.1')

    Returns:
        string: 'A', 'B', or 'C'
    """
    ip_split = ip.split(".")
    if int(ip_split[0]) > 191:
        class_ans = 'C'
    if int(ip_split[0]) <= 191 and int(ip_split[0]) >= 128:
        class_ans = 'B'
    if int(ip_split[0]) < 128:
        class_ans = 'A'

    return class_ans


def network_bits_id(net_class, bits, ip):
    """Generates number of network bits and network ID based on network class.

    Args:
        net_class (string): Network class (i.e. 'A', 'B', 'C') 
        bits (string): string of 1's and 0's; representing subnet mask
        ip (string): IPv4 Address (i.e. '127.0.0.1')

    Returns:
        subnet_bits (integer): Number of subnet bits
        net_id_asn (string): Network ID
    """
    ip_split = ip.split(".")
    network_id_list = []

    if net_class == 'A':
        subnet_bits = bits.count('1') - 8
        network_id_list.append(ip_split[0])
        for num in range(3):
            network_id_list.append("0")

    if net_class == 'B':
        subnet_bits = bits.count('1') - 16
        for num in range(2):
            network_id_list.append(ip_split[num])
        for num in range(2):
            network_id_list.append("0")

    if net_class == 'C':
        subnet_bits = bits.count('1') - 24
        for num in range(3):
            network_id_list.append(ip_split[num])
        network_id_list.append("0")

    net_id_ans = ".".join(network_id_list)

    return subnet_bits, net_id_ans


def subnet_practice():
    ip_addr = ".".join(
        list(map(str, [randint(1, 253) for num in range(4)])))
    cidr, subnet_mask_list, bits = submask(ip_addr)
    subnet_mask = ".".join(
        list(map(str, [int(x, base=2) for x in subnet_mask_list])))

    answers = [False, False, False, False, False, False]

    while True:
        clear_screen()
        print('Given an IP address and Subnet Mask, identify the number of bits taken, the Network ID, the Subnet ID, and the Network Class')
        print(f'\tIP Address: {ip_addr}')
        print(f'\tSubnet Mask: {subnet_mask}\n')

        # Gathering information
        class_ans = network_class(ip_addr)
        subnet_bits, net_id_ans = network_bits_id(class_ans, bits, ip_addr)
        first_host, last_host = first_last_valid_host(ip_addr, subnet_mask)

        while answers[0] == False:
            network_class_asn = input('What is the Network class?: ')

            if network_class_asn.lower() != class_ans.lower():
                print(f'Your answer is not right. Please try again!')
            else:
                print('Correct!\n')
                answers[0] = True

        while answers[1] == False:
            bits_taken = input('What is the bits taken for the subnet?: ')

            if int(bits_taken) != subnet_bits:
                print('Your answer is not right. Please try again!')
            else:
                print('Correct!\n')
                answers[1] = True

        while answers[2] == False:
            network_id = input('What is the Network ID for this IP address?: ')

            if network_id != net_id_ans:
                print('Your answer is not right. Please try again!\n')
            else:
                print('Correct!\n')
                answers[2] = True

        while answers[3] == False:
            subnet_id = input('What is the Subnet ID for this IP address?: ')
            interation_dict = {"128": 128, "192": 64, "224": 32,
                               "240": 16, "248": 8, "252": 4, "254": 2, "255": 1}
            subnet_mask = subnet_mask.split(".")
            subnet_id_list = []
            ip_split = ip_addr.split('.')

            for idx, num in enumerate(subnet_mask):
                if int(num) == 255:
                    subnet_id_list.append(ip_split[idx])
                elif int(num) > 0:
                    subnet_id_list.append(
                        str((int(ip_split[idx]) // interation_dict[num]) * interation_dict[num]))
                else:
                    subnet_id_list.append("0")

            if ".".join(subnet_id_list) != subnet_id:
                print('Your answer is not right. Please try again!\n')
            else:
                print('Correct!\n')
                answers[3] = True

        while answers[4] == False:
            f_host_question = input(
                'What is the first valid host in the IP\'s subnet?: ')

            if f_host_question != first_host:
                print('Your answer is not right. Please try again!\n')
            else:
                print('Correct!\n')
                answers[4] = True

        while answers[5] == False:
            l_host_question = input(
                'What is the last valid host in the IP\'s subnet?: ')

            if l_host_question != last_host:
                print('Your answer is not right. Please try again!\n')
            else:
                print('Correct!\n')
                answers[5] = True

        continue_prompt = input('Do you want another question? (y/n): ')
        if continue_prompt == 'y':
            subnet_practice()
        else:
            break


def first_last_valid_host(ip, subnet):
    """first_last_valid_host() generates first and last host IPs within a subnet.

    Args:
        ip (string): IPv4 Address (i.e. '127.0.0.1')
        subnet (string): Subnet Mask (i.e. '255.255.255.0') 

    Returns:
        tuple: First Host IP, Last Host IP 
    """
    iteration_dict = {"128": 128, "192": 64, "224": 32,
                      "240": 16, "248": 8, "252": 4, "254": 2, "255": 1}
    subnet = subnet.split(".")
    ip = ip.split(".")
    first_host = []
    last_host = []

    for idx, num in enumerate(subnet):
        if num == '255':
            first_host.append(int(ip[idx]))
            last_host.append(int(ip[idx]))
        elif num > '0':
            sub_id_num = int(ip[idx]) // iteration_dict[num] * \
                iteration_dict[num]
            if idx == 3:
                first_host.append(sub_id_num)
                last_host.append((sub_id_num + iteration_dict[num]) - 2)
            else:
                first_host.append(sub_id_num)
                last_host.append((sub_id_num + iteration_dict[num]) - 1)
        else:
            if idx == 3:
                first_host.append(1)
                last_host.append(254)
            else:
                first_host.append(0)
                last_host.append(255)

    return ".".join(list(map(str, first_host))), ".".join(list(map(str, last_host)))


if __name__ == "__main__":
    print(f"""
            1. Binary to Dotted Decimal
            2. Dotted Decimal to Binary 
            3. Hexadecimal to Decimal 
            4. Dotted Decimal to Hexadecimal
            5. Subnetting Practice 
         """)
    exercise_num = input(
        "What exercise to you want to start? (Choose a number): ")

    if exercise_num == str(1):
        bin2dec()

    if exercise_num == str(2):
        dec2bin()

    if exercise_num == str(3):
        hex2dec()

    if exercise_num == str(4):
        dec2hex()

    if exercise_num == str(5):
        subnet_practice()
