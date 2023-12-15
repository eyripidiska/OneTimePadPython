import random
import binascii


def encrypt(message, one_time_pad):
    # Computes the subset of the one time pad to be used for encryption
    subset_one_time_pad = one_time_pad[:len(message)]
    
    # XORs (bitwise exclusive OR) each byte of the message with the corresponding byte of the one-time pad
    encrypted_bytes = bytes([(m_byte ^ otp_byte) for m_byte, otp_byte in zip(message, subset_one_time_pad)])
    
    return encrypted_bytes


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

    print("Unknown Message:", ascii_string)
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




#print("One-Time Pad Encryption")
message1_case_smaller = "Small"
message1_case_equal = "Equals"
message1_case_bigger = "Big Message"

# key = 0100111000101010100100101101111001000001000001011001011000011010100011000001100100100011
# m1 =  0100001001101001011001110010000001001101011001010111001101110011011000010110011101100101
# c1 =  0000110001000011111101011111111000001100011000001110010101101001111011010111111001000110
# c2 =  000111010100111111110001101011000010010001110001
message1 = message1_case_bigger
message2 = "Secret"

# Generate a one-time pad key by the longest message
one_time_pad_bytes = bytes([random.randint(0, 255) for _ in range(max(len(message1), len(message2)))])  

print("Message 1:", message1)
print("Binary Representation Message 1: ")
message1_to_bytes = bytes(message1, 'ascii') 
print_bytes(message1_to_bytes)

message2_to_bytes = bytes(message2, 'ascii')

# Encrypt the messages using the one-time pad
print("Binary Representation Cipher 1: ")
c1 = encrypt(message1_to_bytes, one_time_pad_bytes)
print_bytes(c1)

print("Binary Representation Cipher 2: ")
c2 = encrypt(message2_to_bytes, one_time_pad_bytes)
print_bytes(c2)

print("Binary Representation Key: ")
key = get_key(message1_to_bytes, c1, max(len(message1), len(message2)))

message2 = decrypt(c2, key)

message2_to_bytes = bytes(message2, 'ascii')

print("\n")
