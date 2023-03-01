from CVector import CVector
from ctypes import Structure, wintypes
from math import sin, cos

class CMatrix(Structure):
    _fields_ = [
        ("vRight", CVector),
        ("vFront", CVector),
        ("vUp", CVector),
        ("vPos", CVector),
    ]

    def Normalize(self, normalize_position = False):
        self.vRight = self.vRight.Normalize()
        self.vFront = self.vFront.Normalize()
        self.vUp = self.vUp.Normalize()

        if(normalize_position):
            self.vPos = self.vPos.Normalize()

    def Invert(self):
        self.vOldRight = self.vRight
        self.vOldFront = self.vFront
        self.vOldUp = self.vUp

        self.vRight = CVector (self.vOldRight.fX, self.vOldFront.fX, self.vOldUp.fX)
        self.vFront = CVector (self.vOldRight.fY, self.vOldFront.fY, self.vOldUp.fY)
        self.vUp    = CVector (self.vOldRight.fZ, self.vOldFront.fZ, self.vOldUp.fZ)
        self.vPos  = self.vPos * CVector (-1.0, -1.0, -1.0)

    def Rotate(self, param, theta):
        # param = CVector
        # float theta
        self.sin_t = sin(theta)
        self.cos_t = cos(theta)
        
        mRotateMult = CMatrix(CVector(0,0,0), CVector(0,0,0), CVector(0,0,0), CVector(0,0,0))

		# rotate X
        mRotateMult.vRight.fX = self.cos_t + (1.0 - self.cos_t) * param.fX * param.fX
        mRotateMult.vRight.fY = (1.0 - self.cos_t) * param.fX * param.fY - self.sin_t * param.fZ
        mRotateMult.vRight.fZ = (1.0 - self.cos_t) * param.fX * param.fZ + self.sin_t * param.fY
		
        # rotate Y
        mRotateMult.vFront.fX = (1.0 - self.cos_t) * param.fY * param.fX + self.sin_t * param.fZ
        mRotateMult.vFront.fY = self.cos_t + (1.0 - self.cos_t) * param.fY * param.fY
        mRotateMult.vFront.fZ = (1.0 - self.cos_t) * param.fY * param.fZ - self.sin_t * param.fX

		# rotate Z
        mRotateMult.vUp.fX = (1.0 - self.cos_t) * param.fZ * param.fX - self.sin_t * param.fY
        mRotateMult.vUp.fY = (1.0 - self.cos_t) * param.fZ * param.fY + self.sin_t * param.fX
        mRotateMult.vUp.fZ = self.cos_t + (1.0 - self.cos_t) * param.fZ * param.fZ

		# multiply matrix
        mRotateMult = mRotateMult * self

		# set vectors
        mRotateMult.vPos = self.vPos
        return mRotateMult


    # operators
    def __add__(self, cm):
        return CMatrix(
            self.vRight + cm.vRight,
            self.vFront + cm.vFront,
            self.vUp + cm.vUp,
            self.vPos + cm.vPos
        )
    
    def __sub__(self, cm):
        return CMatrix(
            self.vRight - cm.vRight,
            self.vFront - cm.vFront,
            self.vUp - cm.vUp,
            self.vPos - cm.vPos
        )
    
    def __mul__(self, cm):
        return CMatrix(
            self.vRight * cm.vRight,
            self.vFront * cm.vFront,
            self.vUp * cm.vUp,
            self.vPos * cm.vPos
        )
