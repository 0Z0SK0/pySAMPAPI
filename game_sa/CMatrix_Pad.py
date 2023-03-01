from CVector import CVector
from ctypes import Structure, wintypes

class CMatrix_Padded(Structure):
    _fields_ = [
        ("vRight", CVector),
        ("dwPadRoll", wintypes.DWORD),
        ("vFront", CVector),
        ("dwPadDirection", wintypes.DWORD),
        ("vUp", CVector),
        ("dwPadWas", wintypes.DWORD),
        ("vPos", CVector),
        ("dwPadPos", wintypes.DWORD)
    ]
