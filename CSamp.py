import pymem
from ctypes import Structure, Union, c_byte, c_char_p, c_void_p, c_int, c_uint8, c_uint16, c_uint32, c_char, c_bool, c_float, wintypes

class stTextdraw(Structure):
    _fields_ = [
        ("szText", c_char),
        ("szString", c_char),
        ("fLetterWidth", c_float),
        ("fLetterHeight", c_float),
        ("dwLetterColor", wintypes.DWORD),
        ("byte_unk", c_uint8),
        ("byteCenter", wintypes.BYTE),
        ("byteBox", wintypes.BYTE),
        ("fBoxSizeX", c_float),
        ("fBoxSizeY", c_float),
        ("dwBoxColor", wintypes.DWORD),
        ("byteProportional", wintypes.BYTE),
        ("dwShadowColor", wintypes.DWORD),
        ("byteShadowSize", wintypes.BYTE),
        ("byteOutline", wintypes.BYTE),
        ("byteLeft", wintypes.BYTE),
        ("byteRight", wintypes.BYTE),
        ("iStyle", c_int),
        ("fX", c_float),
        ("fY", c_float),
        ("unk", c_byte),
        ("dword99B", wintypes.DWORD),
        ("dword99F", wintypes.DWORD),
        ("index", wintypes.DWORD),
        ("byte9A7", wintypes.BYTE),
        ("sModel", c_uint16),
        ("fRot", c_float),
        ("fZoom", c_float),
        ("sColor", wintypes.WORD),
        ("f9BE", wintypes.BYTE),
        ("byte9BF", wintypes.BYTE),
        ("byte9C0", wintypes.BYTE),
        ("dword9C1", wintypes.DWORD),
        ("dword9C5", wintypes.DWORD),
        ("dword9C9", wintypes.DWORD),
        ("dword9CD", wintypes.DWORD),
        ("byte9D1", wintypes.BYTE),
        ("dword9D2", wintypes.DWORD)
    ]

class stTextdrawPool(Structure):
    _fields_ = [
        ("iIsListed", c_int),
        ("iPlayerTextDraw", c_int),
        ("textdraw", stTextdraw),
        ("playerTextdraw", stTextdraw)
    ]

class stPickup(Structure):
    _fields_ = [
        ("iModelID", c_int),
        ("iType", c_int),
        ("fPosition", c_float)
    ]

class stPickupPool(Structure):
    _fields_ = [
        ("iPickupsCount", c_int),
        ("ul_GTA_PickupID", c_uint32),
        ("iPickupID", c_int),
        ("iTimePickup", c_int),
        ("unk", c_uint8),
        ("pickup", stPickup)
    ]

class stPlayerPool(Structure):
    _fields_ = [
        ("ulMaxPlayerID", c_uint32),
        ("sLocalPlayerID", c_uint16),
        ("pVTBL_txtHandler", c_void_p),
        ("strLocalPlayerName", c_char_p),
        ("pLocalPlayer", stLocalPlayer),
        ("iLocalPlayerPing", c_int),
        ("iLocalPlayerScore", c_int),
        ("pRemotePlayer", stRemotePlayer),
        ("iIsListed", c_int),
        ("dwPlayerIP", wintypes.DWORD)
    ]

class _sampKeys(Union):
    _fields_ = [
        ("sKeys", c_uint16),
        ("stSampKeys", stSAMPKeys)
    ]

class stOnFootData(Structure):
    _anonymous_ = ("u",)

    _fields_ = [
        ("sLeftRightKeys", c_uint16),
        ("sUpDownKeys", c_uint16),
        ("u", _sampKeys),
        ("fPosition", c_float),
        ("fQuaternion", c_float),
        ("byteHealth", c_uint8),
        ("byteArmor", c_uint8),
        ("byteCurrentWeapon", c_uint8),
        ("byteSpecialAction", c_uint8),
        ("fMoveSpeed", c_float),
        ("fSurfingOffsets", c_float),
        ("sSurfingVehicleID", c_uint16),
        ("sCurrentAnimationID", wintypes.SHORT),
        ("sAnimFlags", wintypes.SHORT)
    ]

class _unkUni(Union):
    _fields_ = [
        ("HydraThrustAngle", c_uint16),
        ("fTrainSpeed", c_float)
    ]

class stInCarData(Structure):
    _anonymous_ = ("u","uu",)

    _fields_ = [
        ("sVehicleID", c_uint16),
        ("sLeftRightKeys", c_uint16),
        ("sUpDownKeys", c_uint16),
        ("u", _sampKeys),
        ("fQuaternion", c_float),
        ("fPosition", c_float),
        ("fMoveSpeed", c_float),
        ("fVehicleHealth", c_float),
        ("bytePlayerHealth", c_uint8),
        ("byteArmor", c_uint8),
        ("byteCurrentWeapon", c_uint8),
        ("byteSiren", c_uint8),
        ("byteLandingGearState", c_uint8),
        ("sTrailerID", c_uint16),
        ("uu", _unkUni)
    ]

class stAimData(Structure):
    _fields_ = [
        ("byteCamMode", wintypes.BYTE),
        ("vecAimf1", c_float),
        ("vecAimPos", c_float),
        ("fAimZ", c_float),
        ("byteCamExtZoom", wintypes.BYTE),
        ("byteWeaponState", wintypes.BYTE),
        ("bUnk", wintypes.BYTE)
    ]

class stTrailerData(Structure):
    _fields_ = [
        ("sTrailerID", c_uint16),
        ("fPosition", c_float),
        ("fQuaternion", c_float),
        ("fSpeed", c_float),
        ("fSpin", c_float)
    ]

class stPassengerData(Structure):
    _anonymous_ = ("u",)

    _fields_ = [
        ("sVehicleID", c_uint16),
        ("byteSeatID", c_uint8),
        ("byteCurrentWeapon", c_uint8),
        ("byteHealth", c_uint8),
        ("byteArmor", c_uint8),
        ("sLeftRightKeys", c_uint16),
        ("sUpDownKeys", c_uint16),
        ("u", _sampKeys),
        ("fPosition", c_float)
    ]

class stDamageData(Structure):
    _fields_ = [
        ("sVehicleID_lastDamageProcessed", c_uint16),
        ("iBumperDamage", c_int),
        ("iDoorDamage", c_int),
        ("byteLightDamage", c_uint8),
        ("byteWheelDamage", c_uint8)
    ]

class stSurfData(Structure):
    _fields_ = [
        ("iIsSurfing", c_int),
        ("fSurfPosition", c_float),
        ("iUnk0", c_int),
        ("sSurfingVehicleID", c_uint16),
        ("ulSurfTick", c_uint32),
        ("pSurfingVehicle", stSAMPVehicle),
        ("iUnk1", c_int),
        ("iSurfMode", c_int)
    ]

class stUnoccupiedData(Structure):
    _fields_ = [
        ("sVehicleID", c_uint16),
        ("byteSeatID", c_uint8),
        ("fRoll", c_float),
        ("fDirection", c_float),
        ("fPosition", c_float),
        ("fMoveSpeed", c_float),
        ("fTurnSpeed", c_float),
        ("fHealth", c_float)
    ]

class stSpectatorData(Structure):
    _anonymous_ = ("u",)

    _fields_ = [
        ("sLeftRightKeys", c_uint16),
        ("sUpDownKeys", c_uint16),
        ("u", _sampKeys),
        ("fPosition", c_float)
    ]

class stStatsData(Structure):
    _fields_ = [
        ("iMoney", c_int),
        ("iAmmo", c_int)
    ]

class stHeadSync(Structure):
    _fields_ = [
        ("fHeadSync", c_float),
        ("iHeadSyncUpdateTick", c_int),
        ("iHeadSyncLookTick", c_int)
    ]

class stLocalPlayer(Structure):
    _fields_ = [
        ("pSAMP_Actor", stSAMPPed),
        ("sCurrentAnimID", c_uint16),
        ("sAnimFlags", c_uint16),
        ("ulUnk0", c_uint32),
        ("iIsActive", c_int),
        ("iIsWasted", c_int),
        ("sCurrentVehicleID", c_uint16),
        ("sLastVehicleID", c_uint16),
        ("onFootData", stOnFootData),
        ("passengerData", stPassengerData),
        ("trailerData", stTrailerData),
        ("inCarData", stInCarData),
        ("aimData", stAimData),
        ("byteTeamID", c_uint8),
        ("iSpawnSkin", c_int),
        ("byteUnk1", c_uint8),
        ("fSpawnPos", c_float),
        ("fSpawnRot", c_float),
        ("iSpawnWeapon", c_int),
        ("iSpawnAmmo", c_int),
        ("iIsActorAlive", c_int),
        ("iSpawnClassLoaded", c_int),
        ("ulSpawnSelectionTick", c_uint32),
        ("ulSpawnSelectionStart", c_uint32),
        ("iIsSpectating", c_int),
        ("byteTeamID2", c_uint8),
        ("usUnk2", c_uint16),
        ("ulSendTick", c_uint32),
        ("ulSpectateTick", c_uint32),
        ("ulAimTick", c_uint32),
        ("ulStatsUpdateTick", c_uint32),
        ("ulWeapUpdateTick", c_uint32),
        ("sAimingAtPid", c_uint16),
        ("usUnk3", c_uint16),
        ("byteCurrentWeapon", c_uint8),
        ("byteWeaponInventory", c_uint8),
        ("iWeaponAmmo", c_int),
        ("iPassengerDriveBy", c_int),
        ("byteCurrentInterior", c_uint8),
        ("iIsInRCVehicle", c_int),
        ("sTargetObjectID", c_uint16),
        ("sTargetVehicleID", c_uint16),
        ("sTargetPlayerID", c_uint16),
        ("headSyncData", stHeadSync),
        ("ulHeadSyncTick", c_uint32),
        ("byteSpace3", wintypes.BYTE),
        ("surfData", stSurfData),
        ("iClassSelectionOnDeath", c_int),
        ("iSpawnClassID", c_int),
        ("iRequestToSpawn", c_int),
        ("iIsInSpawnScreen", c_int),
        ("ulUnk4", c_uint32),
        ("byteSpectateMode", c_uint8),
        ("byteSpectateType", c_uint8),
        ("iSpectateID", c_int),
        ("iInitiatedSpectating", c_int),
        ("vehicleDamageData", stDamageData)
    ]

class stDialogInfo(Structure):
    _fields_ = [
        ("m_pD3DDevice", IDirect3DDevice9),
        ("iTextPoxX", c_int),
        ("iTextPoxY", c_int),
        ("uiDialogSizeX", c_uint32),
        ("uiDialogSizeY", c_uint32),
        ("iBtnOffsetX", c_int),
        ("iBtnOffsetY", c_int),
        ("pDialog", _CDXUTDialog),
        ("pList", _CDXUTListBox),
        ("pEditBox", _CDXUTIMEEditBox),
        ("iIsActive", c_int),
        ("iType", c_int),
        ("DialogID", c_uint32),
        ("pText", c_char_p),
        ("uiTextWidth", c_uint32),
        ("uiTextHeight", c_uint32),
        ("szCaption", c_char),
        ("bServerside", c_int)
    ]

class stSAMPPools(Structure):
    _fields_ = [
        ("pActor", stActorPool),
        ("pObject", stObjectPool),
        ("pGangzone", stGangzonePool),
        ("pText3D", stTextLabelPool),
        ("pTextdraw", stTextdrawPool),
        ("pPlayerLabels", c_void_p),
        ("pPlayer", stPlayerPool),
        ("pVehicle", stVehiclePool),
        ("pPickup", stPickupPool)
    ]

class stServerPresets(Structure):
    _fields_ = [
        ("byteCJWalk", c_uint8),
        ("m_iDeathDropMoney", c_int),
        ("fWorldBoundaries", c_float),
        ("m_bAllowWeapons", c_bool),
        ("fGravity", c_float),
        ("byteDisableInteriorEnterExits", c_uint8),
        ("ulVehicleFriendlyFire", c_uint32),
        ("m_byteHoldTime", c_bool),
        ("m_bInstagib", c_bool),
        ("m_bZoneNames", c_bool),
        ("m_byteFriendlyFire", c_bool),
        ("iClassesAvailable", c_int),
        ("fNameTagsDistance", c_float),
        ("m_bManualVehicleEngineAndLight", c_bool),
        ("byteWorldTime_Hour", c_uint8),
        ("byteWorldTime_Minute", c_uint8),
        ("byteWeather", c_uint8),
        ("byteNoNametagsBehindWalls", c_uint8),
        ("iPlayerMarkersMode", c_int),
        ("fGlobalChatRadiusLimit", c_float),
        ("byteShowNameTags", c_uint8),
        ("m_bLimitGlobalChatRadius", c_bool)
    ]

class stServerInfo(Structure):
    _fields_ = [
        ("uiIP", c_uint32),
        ("usPort", c_uint16)
    ]

class stSAMP(Structure):
    _fields_ = [
        ("pUnk0", c_void_p),
        ("pServerInfo", stServerInfo),
        ("byteSpace", c_uint8),
        ("szIP", c_char),
        ("szHostname", c_char),
        ("bNametagStatus", c_bool),
        ("ulPort", c_uint32),
        ("ulMapIcons", c_uint32),
        ("iLanMode", c_int),
        ("iGameState", c_int),
        ("ulConnectTick", c_uint32),
        ("pSettings", stServerPresets),
        ("pRakClientInterface", c_void_p),
        ("pPools", stSAMPPools)
    ]

class CSamp():
    process = None

    def GetBaseAddress(self):
        self.pm = pymem.Pymem('gta_sa.exe')
        self.modules = list(self.pm.list_modules())
        for self.module in self.modules:
            if(self.module.name == "samp.dll"):
                return self.module.lpBaseOfDll