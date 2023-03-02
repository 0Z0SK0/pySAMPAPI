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

    def ReadBit(self):
        if(self.data[self.readOffset >> 3] & (0x80 >> (self.readOffset & 7))):
            self.readOffset=self.readOffset+c_int(1)
            return c_bool(True)

        else:
            self.readOffset=self.readOffset+c_int(1)
            return c_bool(False)

    def Read(self, numberOfBytes = c_int()):
        if((self.readOffset & 7) == 0):
            if(self.readOffset + (numberOfBytes << 3) > self.numberOfBitsUsed):
                return False
            
            self.ret = self.data + (self.readOffset >> 3)
            self.readOffset = self.readOffset + (numberOfBytes << 3)

            return self.ret
        else:
            return self.ReadBits(numberOfBytes*8)
        
    def ResetReadPointer(self):
        self.readOffset = c_int(0)

    def ResetWritePointer(self):
        self.numberOfBitsUsed = c_int(0)

    def Write0(self):
        # self.AddBitsAndReallocate(c_int(1))
        if((self.numberOfBitsUsed & 7) == 0):
            self.data[self.numberOfBitsUsed >> 3] = c_char_p(0);

        self.numberOfBitsUsed = self.numberOfBitsUsed + c_int(1)

    def Write1(self):
        # self.AddBitsAndReallocate(c_int(1))
        self.numberOfBitsMod8 = self.numberOfBitsUsed & 7
        if(self.numberOfBitsMod8 == 0):
            self.data[self.numberOfBitsUsed >> 3] = 0x80
        
        else:
            self.data[self.numberOfBitsUsed >> 3] |= 0x80 >> (self.numberOfBitsMod8)

        self.numberOfBitsUsed = self.numberOfBitsUsed + c_int(1)

    def AlignWriteToByteBoundary(self):
        if(self.numberOfBitsUsed):
            self.numberOfBitsUsed = self.numberOfBitsUsed + 8 - (((self.numberOfBitsUsed - 1) & 7) + 1)

    def AlignReadToByteBoundary(self):
        if(self.readOffset):
            self.readOffset = self.readOffset + 8 - (((self.readOffset - 1) & 7) + 1)

    def WriteBits(self, input = c_char_p(), numberOfBitsToWrite = c_int(), rightAlignedBits = c_bool()):
        if(numberOfBitsToWrite <= 0):
            return
        
        # self.AddBitsAndReallocate(numberOfBitsToWrite)
        self.offset = c_int(0)
        self.dataByte = c_char()
        self.numberOfBitsUsedMod8 = self.numberOfBitsUsed & 7

        while(numberOfBitsToWrite > 0):
            self.dataByte = (input + self.offset)

            if(numberOfBitsToWrite < 8 and rightAlignedBits):
                self.dataByte = self.dataByte << 8 - numberOfBitsToWrite
            
            if(self.numberOfBitsUsedMod8 == 0):
                self.data = self.data + (self.numberOfBitsUsed >> 3) + self.dataByte

            else:
                self.data = self.data + (self.numberOfBitsUsed >> 3) | self.dataByte >> (self.numberOfBitsUsedMod8)

                if(8 - (self.numberOfBitsUsedMod8) < 8 and 8 - (self.numberOfBitsUsedMod8) < numberOfBitsToWrite):
                    self.data = self.data + (self.numberOfBitsUsed >> 3) + c_int(1) + self.dataByte << (8 - self.numberOfBitsUsedMod8)

            if(numberOfBitsToWrite >= 8):
                self.numberOfBitsUsed = self.numberOfBitsUsed + c_int(8)
            else:
                self.numberOfBitsUsed = self.numberOfBitsUsed + numberOfBitsToWrite

            numberOfBitsToWrite = numberOfBitsToWrite - c_int(8)

            self.offset = self.offset + c_int(1)

    def SetData(self, input = c_char_p()):
        self.data = input
        self.copyData = c_bool(False)

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
                            bitStream.readOffset=bitStream.readOffset + c_int(1)

                        else:
                            # write 2
                            self.data[self.numberOfBitsUsed >> 3] = c_char_p(0)
                            bitStream.readOffset=bitStream.readOffset + c_int(1)

                    else:
                        # existing bytes
                        if(bitStream.data[bitStream.readOffset >> 3] & (0x80 >> (bitStream.readOffset % 8))):
                            self.data[self.numberOfBitsUsed >> 3] |= 0x80 >> (self.numberOfBitsMod8) # Set the bit to 1
                            bitStream.readOffset=bitStream.readOffset + c_int(1)

                    numberOfBits = numberOfBits-1
                    self.numberOfBitsUsed = self.numberOfBitsUsed + c_int(1)

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

    def WriteAlignedBytes(self, input = c_char_p(), numberOfBytesToWrite = c_int()):
        self.AlignWriteToByteBoundary()
        self.Write(input, numberOfBytesToWrite)

    def ReadAlignedBytes(self, numberOfBytesToRead = c_int()):
        if(numberOfBytesToRead <= 0):
            return False
        
        self.AlignReadToByteBoundary()

        if(self.readOffset + (numberOfBytesToRead << 3) > self.numberOfBitsUsed):
            return False
        
        self.ret = self.data + (self.readOffset >> 3)
        self.readOffset = self.readOffset + (numberOfBytesToRead << 3)

        return self.ret
