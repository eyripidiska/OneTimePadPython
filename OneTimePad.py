
def get_key(message, cipher, length):
   
    # XORs (bitwise exclusive OR) each byte of the message with the corresponding byte of cipher to get the key
    key = bytes([(m_byte ^ cipher_byte) for m_byte, cipher_byte in zip(message, cipher)])
    
    # Prints the binary representation of each key byte
    for b in key:
        binary_representation = bin(b)[2:].zfill(8)
        print(binary_representation, end=" ")
    
    # Calculate the remaining length remaining for the key
    remain_length = length - len(message)
 
    # Prints with "********" for every bytes that remaining 
    for _ in range(remain_length):
        print("********", end=" ")
    print("\n--------------------------------------------------------------------------------------------------")

    return key


def decrypt(cipher, key):
    length = min(len(cipher), len(key))
    
    subset_cipher = cipher[:length]
    
    decrypted_bytes = bytes([(key_byte ^ cipher_byte) for key_byte, cipher_byte in zip(key, subset_cipher)])
    
    ascii_string = decrypted_bytes.decode('ascii')
    
    remain_length = len(cipher) - len(ascii_string)

    message_to_bytes = bytes(ascii_string, 'ascii')

    ascii_string += '*' * remain_length

    print("Unknown Message Value:", ascii_string)
    print("Binary Representation Unknown Message: ")
    for b in message_to_bytes:
        binary_representation = bin(b)[2:].zfill(8)
        print(binary_representation, end=" ")
    # Calculate the remaining length remaining for the key
    remain_length = len(cipher) - len(key)
 
    # Prints with "********" for every bytes that remaining 
    for _ in range(remain_length):
        print("********", end=" ")

    return ascii_string


def print_bytes(bytes_to_print):
    for b in bytes_to_print:
        binary_representation = bin(b)[2:].zfill(8)
        print(binary_representation, end=" ")
    print("\n--------------------------------------------------------------------------------------------------")

def bits_to_bytes(bits):
    # Ensure the length of bits is a multiple of 8 by adding leading zeros if needed
    while len(bits) % 8 != 0:
        bits = '0' + bits

    # Convert the binary string to an integer
    decimal_value = int(bits, 2)

    # Calculate the number of bytes required
    num_bytes = (len(bits) + 7) // 8

    # Convert the integer to bytes
    byte_representation = decimal_value.to_bytes(num_bytes, byteorder='big')

    return byte_representation



# key = 0100111000101010100100101101111001000001000001011001011000011010100011000001100100100011

dict_case_smaller = {
  "message": "Small",
  "cipher": "0001110101000111111100111011001000101101"
}

dict_case_equal = {
  "message": "Equals",
  "cipher": "000010110101101111100111101111110010110101110110"
}

dict_case_bigger = {
  "message": "Big Message",
  "cipher": "0000110001000011111101011111111000001100011000001110010101101001111011010111111001000110"
}

selected_dict = dict_case_bigger

m1 = selected_dict["message"]
cipher1 =  selected_dict["cipher"]
cipher2 =  "000111010100111111110001101011000010010001110001"

c1 = bits_to_bytes(cipher1)
c2 = bits_to_bytes(cipher2)

print("Message 1 Value:",m1)
print("Binary Representation Message 1: ")
message1_to_bytes = bytes(m1, 'ascii') 
print_bytes(message1_to_bytes)

print("Binary Representation Cipher 1: ")
print_bytes(c1)

print("Binary Representation Cipher 2: ")
print_bytes(c2)

print("Binary Representation Key: ")
key = get_key(message1_to_bytes, c1, max(len(c1), len(c2)))

message2 = decrypt(c2, key)

message2_to_bytes = bytes(message2, 'ascii')

print("\n")
