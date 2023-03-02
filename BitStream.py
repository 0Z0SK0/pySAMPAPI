from ctypes import Structure, c_int, c_uint, c_char_p, c_bool, c_char, create_string_buffer, memmove

BITSTREAM_STACK_ALLOCATION_SIZE = 256

class BitStream(Structure):
    _fields_ = [
        ("numberOfBitsUsed", c_int),
        ("numberOfBitsAllocated", c_int),
        ("readOffset", c_int),
        ("data", c_char_p),
        ("copyData", c_bool),
        ("stackData", c_char)
    ]

    def __init__(self, initialBytesToAllocate = c_int(0), _data = c_char_p(), lengthInBytes = c_uint(), _copyData = c_bool()):
        self.readOffset = c_int(0)
        
        if(_data):
            self.numberOfBitsUsed = c_int(lengthInBytes << 3)
            self.copyData = _copyData
            self.numberOfBitsAllocated = c_int(lengthInBytes << 3)

            if(self.copyData):
                if(lengthInBytes > 0):
                    if(lengthInBytes < BITSTREAM_STACK_ALLOCATION_SIZE):
                        self.data = self.stackData
                        self.numberOfBitsAllocated = c_int(BITSTREAM_STACK_ALLOCATION_SIZE << 3)
                    
                    else:
                        self.data = create_string_buffer(lengthInBytes)

                    memmove(self.data, _data, lengthInBytes)
                
                else:
                    self.data = c_char_p(0)
            
            else:
                self.data = _data

        else:
            self.numberOfBitsUsed = c_int(0)

            if(initialBytesToAllocate <= BITSTREAM_STACK_ALLOCATION_SIZE):
                self.data = self.stackData
                self.numberOfBitsAllocated = c_int(BITSTREAM_STACK_ALLOCATION_SIZE * 8)
            else:
                self.data = create_string_buffer(initialBytesToAllocate)
                self.numberOfBitsAllocated = c_int(initialBytesToAllocate << 3)

            self.copyData = c_bool(True)

    def __del__(self):
        if(self.copyData and self.numberOfBitsAllocated > c_int(BITSTREAM_STACK_ALLOCATION_SIZE << 3)):
            self.data = c_char_p(0)


    def SetNumberOfBitsAllocated(self, lengthInBits = c_uint()):
        self.numberOfBitsAllocated = lengthInBits

    def Reset(self):
        self.numberOfBitsUsed = c_int(0)
        self.readOffset = c_int(0)

    def Write(self, bitStream = classmethod, numberOfBits = c_int(), input = c_char_p(), numberOfBytes = c_int()):
        if(bitStream):
            if(numberOfBits):
                # self.AddBitsAndReallocate(numberOfBits)
                self.numberOfBitsMod8 = c_int(0)
                while(numberOfBits > 0 and bitStream.readOffset <= bitStream.numberOfBitsUsed):
                    self.numberOfBitsMod8 = self.numberOfBitsUsed & 7
                    if(self.numberOfBitsMod8 == 0):
                        if(bitStream.data[bitStream.readOffset >> 3] & (0x80 >> (bitStream.readOffset % 8))):
                            # write 1
                            self.data[self.numberOfBitsUsed >> 3] = c_char_p(0x80)
                            bitStream.readOffset=bitStream.readOffset+1

                        else:
                            # write 2
                            self.data[self.numberOfBitsUsed >> 3] = c_char_p(0)
                            bitStream.readOffset=bitStream.readOffset+1

                    else:
                        # existing bytes
                        if(bitStream.data[bitStream.readOffset >> 3] & (0x80 >> (bitStream.readOffset % 8))):
                            self.data[self.numberOfBitsUsed >> 3] |= 0x80 >> (self.numberOfBitsMod8) # Set the bit to 1
                            bitStream.readOffset=bitStream.readOffset+1

                    numberOfBits = numberOfBits-1
                    self.numberOfBitsUsed = self.numberOfBitsUsed+1

            else:
                self.Write(bitStream, bitStream.GetNumberOfBitsUsed())

        else:
            if(numberOfBytes == 0):
                return
            
            if((self.numberOfBitsUsed & 7) == 0):
                # AddBitsAndReallocate( BYTES_TO_BITS(numberOfBytes) );
                # memcpy(data+BITS_TO_BYTES(numberOfBitsUsed), input, numberOfBytes);
                # numberOfBitsUsed+=BYTES_TO_BITS(numberOfBytes);
                pass
            
            else:
                # WriteBits( ( unsigned char* ) input, numberOfBytes * 8, true );
                pass
