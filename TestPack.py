import struct

print(struct.pack('i', 1001))

bin2 = b'\x02\x00\x00\x00\x07\x010\xe7\x03\x00\x00\x03'

bin = b'\x02\x00\x00\x00\x07\x01\x34\xe7\x03\x00\x00\x03'

# head
print(bin[0])

print(struct.pack('i', 10))

print(bin[1])

print(hex(10))

print(int('0x10', 16))