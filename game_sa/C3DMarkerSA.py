from ctypes import Structure, wintypes
from CMatrix_Pad import CMatrix_Padded
from CMatrix import CMatrix
from CVector import CVector

class C3DMarkerSAInterface(Structure):
    _fields_ = [
        ("m_mat", CMatrix_Padded),
        ("dwPad", wintypes.DWORD),
        ("dwPad2", wintypes.DWORD),
        #("m_pRwObject", RpClump),
        ("m_pMaterial", wintypes.DWORD),
        ("m_nType", wintypes.WORD),
        ("m_bIsUsed", wintypes.BOOL),
        ("m_nIdentifier", wintypes.DWORD),
        #("rwColour", RGBA),
        ("m_nPulsePeriod", wintypes.WORD),
        ("m_nRotateRate", wintypes.SHORT),
        ("m_nStartTime", wintypes.DWORD),
        ("m_fPulseFraction", wintypes.FLOAT),
        ("m_fStdSize", wintypes.FLOAT),
        ("m_fSize", wintypes.FLOAT),
        ("m_fBrightness", wintypes.FLOAT),
        ("m_fCameraRange", wintypes.FLOAT),

        ("m_normal", CVector),

        ("m_LastMapReadX", wintypes.WORD),
        ("m_LastMapReadY", wintypes.WORD),
        ("m_LastMapReadResultZ", wintypes.FLOAT),
        ("m_roofHeight", wintypes.FLOAT),
        ("m_lastPosition", CVector),
        ("m_OnScreenTestTime", wintypes.DWORD),
    ]

class C3DMarkerSA():
    def __init__(self, _internalInterface = C3DMarkerSAInterface()):
        self.internalInterface = _internalInterface

    def GetInterface(self):
        return self.internalInterface

    def GetMatrix(self, pMatrix = CMatrix()):
        self.mat = self.GetInterface().m_mat
        pMatrix.vPos = self.mat.vPos
        pMatrix.vFront = self.mat.vFront
        pMatrix.vRight = self.mat.vRight
        pMatrix.vUp = self.mat.vUp

    def SetMatrix(self, pMatrix = CMatrix()):
        self.mat = self.GetInterface().m_mat
        self.mat.vPos = pMatrix.vPos
        self.mat.vFront = pMatrix.vFront
        self.mat.vRight = pMatrix.vRight
        self.mat.vUp = pMatrix.vUp

    def SetPosition(self, vecPosition = CVector()):
        self.GetInterface().m_mat.vPos = vecPosition

    def GetPosition(self):
        return self.GetInterface().m_mat.vPos
    
    def GetType(self):
        return self.GetInterface().m_nType
    
    def SetType(self, dwType = wintypes.DWORD):
        self.GetInterface().m_nType = dwType

    def IsActive(self):
        return self.GetInterface().m_bIsUsed
    
    def GetIdentifier(self):
        return self.GetInterface().m_nIdentifier
    
    def GetColor(self):
        self.ulABGR = self.GetInterface().rwColour
        return ( self.ulABGR >> 24 ) | self.ulABGR | ( self.ulABGR >> 8 ) | ( self.ulABGR >> 16 )
    
    '''
    def SetColor(self, color = RGBA()):
        self.GetInterface().rwColour = ( color.A << 24 ) | ( color.B << 16 ) | ( color.G << 8 ) | color.R
    '''
    
    def SetPulsePeriod(self, wPulsePeriod = wintypes.WORD):
        self.GetInterface().m_nPulsePeriod = wPulsePeriod

    def SetRotateRate(self, RotateRate = wintypes.SHORT):
        self.GetInterface().m_nRotateRate = RotateRate

    def GetSize(self):
        return self.GetInterface().m_fSize
    
    def SetSize(self, fSize = wintypes.FLOAT):
        self.GetInterface().m_fSize = fSize

    def GetBrightness(self):
        return self.GetInterface().m_fBrightness
    
    def SetBrightness(self, fBrightness = wintypes.FLOAT):
        self.GetInterface().m_fBrightness = fBrightness

    def SetCameraRange(self, fCameraRange = wintypes.FLOAT):
        self.GetInterface().m_fCameraRange = fCameraRange

    def GetPulseFraction(self):
        return self.GetInterface().m_fPulseFraction
    
    def SetPulseFraction(self, fPulseFraction = wintypes.FLOAT):
        self.GetInterface().m_fPulseFraction = fPulseFraction

    def Disable(self):
        self.GetInterface().m_nIdentifier = 0

    def DeleteMarkerObject(self):
        if(self.GetInterface().m_pRwObject):
            # delete
            pass

    def Reset(self):
        self.internalInterface.m_lastPosition = self.internalInterface.m_mat.vPos
