import pymem

class CSamp():
    process = None

    def GetBaseAddress(self):
        self.pm = pymem.Pymem('gta_sa.exe')
        self.modules = list(self.pm.list_modules())
        for self.module in self.modules:
            if(self.module.name == "samp.dll"):
                return self.module.lpBaseOfDll