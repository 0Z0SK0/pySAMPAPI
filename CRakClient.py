import pymem
from ctypes import c_byte, c_char_p, c_void_p, c_int, c_uint8, c_uint16, c_uint32, c_char, c_bool, c_float, wintypes

from BitStream import BitStream

class CRakClient():
    process = None

    def __init__(self):
        self.g_RakClient = None

    def RPC(self, rpcId = c_int(0), bitStream = BitStream(), priority = PacketPriority(), reliability = PacketReliability(), orderingChannel = c_char(0), shift = c_bool(False)):
        if(not self.g_RakClient):
           return
        
        #

        return 