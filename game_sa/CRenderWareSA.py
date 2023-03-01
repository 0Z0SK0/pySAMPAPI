from ctypes import Structure, wintypes, c_char, c_void_p, c_int, c_uint, c_float, c_short, c_char_p, CFUNCTYPE
import ctypes

RW_STRUCT_ALIGN = c_int(~(0)>>1)
RW_TEXTURE_NAME_LENGTH = 32
RW_MAX_TEXTURE_COORDS = 8

class RwV2d(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float)
    ]   

class RwV3d(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float)
    ]   

class RwPlane(Structure):
    _fields_ = [
        ("normal", RwV3d),
        ("lenght", c_float)
    ]   

class RwBBox(Structure):
    _fields_ = [
        ("max", RwV3d),
        ("min", RwV3d)
    ]   

class RwSphere(Structure):
    _fields_ = [
        ("position", RwV3d),
        ("radius", c_float)
    ] 

class RwMatrix(Structure):
    _fields_ = [
        ("right", RwV3d),
        ("flags", c_uint),
        ("up", RwV3d),
        ("pad1", c_uint),
        ("at", RwV3d),
        ("pad2", c_uint),
        ("pos", RwV3d),
        ("pad3", c_uint)
    ] 

class RwPrimitiveType(Structure):
    _fields_ = [
        ("PRIMITIVE_NULL", c_int),
        ("PRIMITIVE_LINE_SEGMENT", c_int),
        ("PRIMITIVE_LINE_SEGMENT_CONNECTED", c_int),
        ("PRIMITIVE_TRIANGLE", c_int),
        ("PRIMITIVE_TRIANGLE_STRIP", c_int),
        ("PRIMITIVE_TRIANGLE_FAN", c_int),
        ("PRIMITIVE_POINT", c_int),
        ("PRIMITIVE_LAST", c_int)
    ] 

class RwCameraType(Structure):
    _fields_ = [
        ("RW_CAMERA_NULL", c_int),
        ("RW_CAMERA_PERSPECTIVE", c_int),
        ("RW_CAMERA_ORTHOGRAPHIC", c_int),
        ("RW_CAMERA_LAST", c_int)
    ] 
        
class RpAtomicFlags(Structure):
	_fields_ = [
        ("ATOMIC_COLLISION", c_int),
        ("ATOMIC_VISIBLE", c_int),
        ("ATOMIC_LAST", c_int)
    ]

class RwRasterLockFlags(Structure):
    _fields_ = [
        ("RASTER_LOCK_WRITE", c_int),
        ("RASTER_LOCK_READ", c_int),
        ("RASTER_LOCK_LAST", c_int)
    ]

class RwTransformOrder(Structure):
    _fields_ = [
        ("TRANSFORM_INITIAL", c_int),
        ("TRANSFORM_BEFORE", c_int),
        ("TRANSFORM_AFTER", c_int),
        ("TRANSFORM_LAST", c_int)
    ]

class RpLightType(Structure):
    _fields_ = [
        ("LIGHT_TYPE_NULL", c_int),
        ("LIGHT_TYPE_DIRECTIONAL", c_int),
        ("LIGHT_TYPE_AMBIENT", c_int),
        ("LIGHT_TYPE_POINT", c_int),
        ("LIGHT_TYPE_SPOT_1", c_int),
        ("LIGHT_TYPE_SPOT_2", c_int),
        ("LIGHT_TYPE_LAST", c_int)
    ]

class RpLightFlags(Structure):
    _fields_ = [
        ("LIGHT_ILLUMINATES_ATOMICS", c_int),
        ("LIGHT_ILLUMINATES_GEOMETRY", c_int),
        ("LIGHT_FLAGS_LAST", c_int)
    ]

class RwObject(Structure):
    _fields_ = [
        ("type", c_char),
        ("subtype", c_char),
        ("flags", c_char),
        ("privateFlags", c_char),
        ("parent", c_void_p),
    ]

class RwVertex(Structure):
    _fields_ = [
        ("position", RwV3d),
        ("normal", RwV3d),
        ("color", c_uint),
        ("u", c_float),
        ("v", c_float),
    ]

class RwListEntry(Structure):
    _fields_ = [
        ("next", c_void_p),
        ("prev", c_void_p)
    ]

class RwList(Structure):
    _fields_ = [
        ("root", RwListEntry)
    ]

class RwFrame(Structure):
    _fields_ = [
        ("object", RwObject),
        ("pad1", c_void_p),
        ("pad2", c_void_p),
        ("modelling", RwMatrix),
        ("ltm", RwMatrix),
        ("objects", RwList),

        ("child", c_void_p),
        ("next", c_void_p),
        ("root", c_void_p),

        ("pluginData", c_char),
        ("szName", c_char),
    ]

class RwTexDictionary(Structure):
    _fields_ = [
        ("object", RwObject),
        ("textures", RwList),
        ("globalTXDs", RwListEntry)
    ]
     
class RwRaster(Structure):
    _fields_ = [
        ("parent", c_void_p),
        ("pixels", c_char),
        ("palette", c_char),
        ("width", c_int),
        ("height", c_int),
        ("depth", c_int),
        ("stride", c_int),
        ("u", c_short),
        ("v", c_short),
        ("type", c_char),
        ("flags", c_char),
        ("privateFlags", c_char),
        ("format", c_char),
        ("origPixels", c_char),
        ("origWidth", c_int),
        ("origHeight", c_int),
        ("origDepth", c_int)
    ]

class RwTexture(Structure):
    _fields_ = [
        ("raster", RwRaster),
        ("txd", RwTexDictionary),
        ("TXDList", RwListEntry),
        ("name", c_char),
        ("mask", c_char),
        ("flags", c_uint),
        ("refs", c_int)
    ]
     
class RwTextureCoordinates(Structure):
    _fields_ = [
        ("u", c_float),
        ("v", c_float)
    ]
     
class RwColorFloat(Structure):
    _fields_ = [
        ("r", c_float),
        ("g", c_float),
        ("b", c_float),
        ("a", c_float)
    ]

class RwColor(Structure):
    _fields_ = [
        ("r", c_char),
        ("g", c_char),
        ("b", c_char),
        ("a", c_char)
    ]

class RwObjectFrame(Structure):
    _fields_ = [
        ("object", RwObject),
        ("lFrame", RwListEntry),
        ("callback", c_void_p)
    ]

class RwCameraFrustum(Structure):
    _fields_ = [
        ("plane", RwPlane),
        ("x", c_char),
        ("y", c_char),
        ("z", c_char),
        ("unknown1", c_char)
    ]

class RwCameraPreCallback(Structure):
    _fields_ = [
        # idk
    ]

class RwCameraPostCallback(Structure):
    _fields_ = [
        # idk
    ]

class RwCamera(Structure):
    _fields_ = [
        ("object", RwObject),
        ("type", RwCameraType),
        ("preCallback", RwCameraPreCallback),
        ("postCallback", RwCameraPostCallback),
        ("matrix", RwMatrix),
        ("bufferColor", RwRaster),
        ("bufferDepth", RwRaster),
        ("screen", RwV2d),
        ("screenInverse", RwV2d),
        ("screenOffset", RwV2d),
        ("nearplane", c_float),
        ("farplane", c_float),
        ("fog", c_float),
        ("unknown1", c_float),
        ("unknown2", c_float),
        ("frustum4D", RwCameraFrustum),
        ("viewBBox", RwBBox),
        ("frustum3D", RwV3d)
    ]

class RpInterpolation(Structure):
    _fields_ = [
        ("unknown1", c_uint),
        ("unknown2", c_uint),
        ("unknown3", c_float),
        ("unknown4", c_float),
        ("unknown5", c_float)
    ]

class RwClumpCallback(Structure):
    _fields_ = [
        # idk
    ]

class RpClump(Structure):
    _fields_ = [
        ("object", RwObject),
        ("atomics", RwList),
        ("lights", RwList),
        ("cameras", RwList),
        ("globalClumps", RwListEntry),
        ("callback", RwClumpCallback),
    ]

class RpLight(Structure):
    _fields_ = [
        ("object", RwObjectFrame),
        ("radius", c_float),
        ("color", RwColorFloat),
        ("unknown1", c_float),
        ("sectors", RwList),
        ("globalLights", RwListEntry),
        ("frame", c_short),
        ("unknown2", c_short),
    ]

class RpMaterialLighting(Structure):
    _fields_ = [
        ("ambient", c_float),
        ("specular", c_float),
        ("diffuse", c_float)
    ]

class RpMaterial(Structure):
    _fields_ = [
        ("texture", RwTexture),
        ("color", RwColor),
        ("render", c_void_p),
        ("lighting", RpMaterialLighting),
        ("refs", c_short),
        ("id", c_short)
    ]

class RpMaterials(Structure):
    _fields_ = [
        ("materials", RpMaterial),
        ("entries", c_int),
        ("unknown", c_int)
    ]

class RpTriangle(Structure):
    _fields_ = [
        ("v1", c_short),
        ("v2", c_short),
        ("v3", c_short),
        ("materialId", c_short)
    ]

class RpGeometry(Structure):
    _fields_ = [
        ("object", RwObject),
        ("flags", c_uint),
        ("unknown1", c_short),
        ("refs", c_short),

        ("triangles_size", c_int),
        ("vertices_size", c_int),
        ("unknown_size", c_int),
        ("texcoords_size", c_int),

        ("materials", RpMaterials),
        ("triangles", RpTriangle),
        ("colors", RwColor),
        ("texcoords", RwTextureCoordinates),
        ("unknown2", c_void_p),
        ("info", c_void_p),
        ("unknown3", c_void_p)
    ]

class RpAtomicCallback(Structure):
     _fields_ = [
          # idk
     ]

class RpAtomic(Structure):
    _fields_ = [
        ("object", RwObjectFrame),
        ("info", c_void_p),
        ("geometry", RpGeometry),
        ("bsphereLocal", RwSphere),
        ("bsphereWorld", RwSphere),
        ("clump", RpClump),
        ("globalClumps", RwListEntry),
        ("renderCallback", RpAtomicCallback),
        ("interpolation", RpInterpolation),
        ("frame", c_short),
        ("unknown7", c_short),
        ("sectors", RwList),
        ("render", c_void_p)
    ]

class RpAtomicContainer(Structure):
    _fields_ = [
        ("atomic", RpAtomic),
        ("szName", c_char)
    ]

class SReplaceParts(Structure):
    _fields_ = [
        ("szName", c_char_p),
        ("ucIndex", c_char),
        ("pReplacements", RpAtomicContainer),
        ("uiReplacements", c_uint)
    ]

class RwStreamTypeData(Structure):
    _fields_ = [
        ("position", c_uint),
        ("size", c_uint),
        ("ptr", c_void_p),
        ("file", c_void_p),
        ("callbackClose", CFUNCTYPE(c_int, c_void_p)),
        ("callbackRead", CFUNCTYPE(c_uint, c_void_p, c_void_p, c_uint)),
        ("callbackWrite", CFUNCTYPE(c_int, c_void_p, c_void_p, c_uint)),
        ("callbackOther", CFUNCTYPE(c_int, c_void_p, c_uint)),
        ("ptr", c_void_p)
    ]

class RwStreamType(Structure):
    _fields_ = [
        ("STREAM_TYPE_NULL", c_int),
        ("STREAM_TYPE_FILE", c_int),
        ("STREAM_TYPE_FILENAME", c_int),
        ("STREAM_TYPE_BUFFER", c_int),
        ("STREAM_TYPE_CALLBACK", c_int),
        ("STREAM_TYPE_LAST", c_int)
    ]

class RwStreamMode(Structure):
    _fields_ = [
        ("STREAM_MODE_NULL", c_int),
        ("STREAM_MODE_READ", c_int),
        ("STREAM_MODE_WRITE", c_int),
        ("STREAM_MODE_LAST", c_int)
    ]

class RwStream(Structure):
    _fields_ = [
        ("type", RwStreamType),
        ("mode", RwStreamMode),
        ("pos", c_int),
        ("data", RwStreamTypeData),
        ("id", c_int)
    ]

class CRenderWareSA():
    def RwStreamFindChunk(self, stream = RwStream(), type = c_uint(0), lengthOut = c_uint(0), versionOut = c_uint(0)):
        self.func_type = CFUNCTYPE(c_int, RwStream, c_uint, c_uint, c_uint)
        self.func = self.func_type(0x007ED2D0)
        return self.func(stream, type, lengthOut, versionOut)

    # custom functions
    def ReplacePartsCB(self, object = RwObject(), data = SReplaceParts()):
        self.Atomic = RpAtomic(object)
        self.szAtomicName = None

        # iterate through our loaded atomics
        for i in range(data.uiReplacements):
            # get the correct atomic name based on the object # in our parent frame
            if (data.ucIndex == 0):
                self.szAtomicName = f"{data.szName}_ok"
            else:
                self.szAtomicName = f"{data.szName}_dam"

            # see if we have such an atomic in our replacement atomics array
            if (data.pReplacements[i].szName[0] == self.szAtomicName[0]):
                # if so, override the geometry
                self.RpAtomicSetGeometry(self.Atomic, data.pReplacements[i].atomic.geometry, 0)

                # and copy the matrices
                self.RwFrameCopyMatrix(self.RpGetFrame(self.Atomic), self.RpGetFrame(data.pReplacements[i].atomic))

                self.object = data.pReplacements[i].atomic
                data.ucIndex = data.ucIndex+1

        return object
