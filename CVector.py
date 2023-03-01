from math import sqrt

class CVector(ctypes.Structure):
    _fields_ = [
        ("fX", ctypes.c_float),
        ("fY", ctypes.c_float),
        ("fZ", ctypes.c_float)
    ]

    def __init__(self, fX, fY, fZ):
        super(CVector, self).__init__(fX, fY, fZ)

    def Normalize(self):
        self.t = sqrt(self.fX * self.fX  + self.fY * self.fY + self.fZ * self.fZ)
        if(self.t > 0.0001):
            self.fX2 = self.fX / self.t
            self.fY2 = self.fY / self.t
            self.fZ2 = self.fZ / self.t

            CVector.fX = ctypes.c_float(self.fX2)
            CVector.fY = ctypes.c_float(self.fY2)
            CVector.fZ = ctypes.c_float(self.fZ2)

            # for internal use
            self.fX = self.fX2
            self.fY = self.fY2
            self.fZ = self.fZ2
        
        else:
            self.t = 0

        return self.t
    
    def Length(self):
        return sqrt((self.fX * self.fX)  + (self.fY * self.fY) + (self.fZ * self.fZ))
    
    def DotProduct(self, param):
        # param = CVector(fX, fY, fZ)

        return self.fX*param.fX + self.fY*param.fY + self.fZ*param.fZ;

    def CrossProduct(self, param):
        # param = CVector(fX, fY, fZ)

        self._fX = self.fX
        self._fY = self.fY
        self._fZ = self.fZ

        # for internal use
        self.fX = self._fY * param.fZ - param.fY * self._fZ
        self.fY = self._fZ * param.fX - param.fZ * self._fX
        self.fZ = self._fX * param.fY - param.fX * self._fY

        CVector.fX = ctypes.c_float(self.fX)
        CVector.fY = ctypes.c_float(self.fY)
        CVector.fZ = ctypes.c_float(self.fZ)
