from ctypes import Structure, c_float
from math import sqrt, fabs, atan2, pi

class CVector(Structure):
    _fields_ = [
        ("fX", c_float),
        ("fY", c_float),
        ("fZ", c_float)
    ]

    def __init__(self, fX, fY, fZ):
        super(CVector, self).__init__(fX, fY, fZ)

    def Normalize(self):
        self.t = sqrt(self.fX * self.fX  + self.fY * self.fY + self.fZ * self.fZ)
        if(self.t > 0.0001):
            self.fX2 = self.fX / self.t
            self.fY2 = self.fY / self.t
            self.fZ2 = self.fZ / self.t

            CVector.fX = c_float(self.fX2)
            CVector.fY = c_float(self.fY2)
            CVector.fZ = c_float(self.fZ2)

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

        CVector.fX = c_float(self.fX)
        CVector.fY = c_float(self.fY)
        CVector.fZ = c_float(self.fZ)

    def GetAngleRadians(self):
        return -atan2(self.fY, -self.fX)
    
    def GetAngleDegrees(self):
        self.radtodeg = 180.0/pi
        self.ret = (atan2(self.fY, -self.fX) * self.radtodeg) + 270.0
        if (self.ret >= 360.0):
            self.ret -= 360.0

        return self.ret

    # operators
    def __add__(self, cv):
        return CVector(self.fX + cv.fX, self.fY + cv.fY, self.fZ + cv.fZ) 
    
    def __sub__(self, cv):
        return CVector(self.fX - cv.fX, self.fY - cv.fY, self.fZ - cv.fZ) 
    
    def __mul__(self, cv):
        return CVector(self.fX * cv.fX, self.fY * cv.fY, self.fZ * cv.fZ)
    
    def __truediv__(self, cv):
        return CVector(self.fX / cv.fX, self.fY / cv.fY, self.fZ / cv.fZ)
    
    def __iadd__(self, cv):
        # for internal use
        self.fX += cv.fX
        self.fY += cv.fY
        self.fZ += cv.fZ

        CVector.fX = c_float(self.fX)
        CVector.fY = c_float(self.fY)
        CVector.fZ = c_float(self.fZ)

    def __isub__(self, cv):
        # for internal use
        self.fX -= cv.fX
        self.fY -= cv.fY
        self.fZ -= cv.fZ

        CVector.fX = c_float(self.fX)
        CVector.fY = c_float(self.fY)
        CVector.fZ = c_float(self.fZ)

    def __imul__(self, cv):
        # for internal use
        self.fX *= cv.fX
        self.fY *= cv.fY
        self.fZ *= cv.fZ

        CVector.fX = c_float(self.fX)
        CVector.fY = c_float(self.fY)
        CVector.fZ = c_float(self.fZ)

    def __idiv__(self, cv):
        # for internal use
        self.fX /= cv.fX
        self.fY /= cv.fY
        self.fZ /= cv.fZ

        CVector.fX = c_float(self.fX)
        CVector.fY = c_float(self.fY)
        CVector.fZ = c_float(self.fZ)
    
    def __eq__(self, cv):
        return ((fabs( self.fX - cv.fX ) < 0.0001) and
                (fabs( self.fY - cv.fY ) < 0.0001) and
                (fabs( self.fZ - cv.fZ ) < 0.0001))
    
    def __ne__(self, cv):
        return ((fabs( self.fX - cv.fX ) >= 0.0001) and
                (fabs( self.fY - cv.fY ) >= 0.0001) and
                (fabs( self.fZ - cv.fZ ) >= 0.0001))
