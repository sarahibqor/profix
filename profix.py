import ctypes
import time
from ctypes import wintypes

# Constants for screen orientation
DMDO_DEFAULT = 0
DMDO_90 = 1
DMDO_180 = 2
DMDO_270 = 3

# Define some necessary structures and enums
class DEVMODE(ctypes.Structure):
    _fields_ = [
        ("dmDeviceName", wintypes.WCHAR * 32),
        ("dmSpecVersion", wintypes.WORD),
        ("dmDriverVersion", wintypes.WORD),
        ("dmSize", wintypes.WORD),
        ("dmDriverExtra", wintypes.WORD),
        ("dmFields", wintypes.DWORD),
        ("dmOrientation", wintypes.SHORT),
        ("dmPaperSize", wintypes.SHORT),
        ("dmPaperLength", wintypes.SHORT),
        ("dmPaperWidth", wintypes.SHORT),
        ("dmScale", wintypes.SHORT),
        ("dmCopies", wintypes.SHORT),
        ("dmDefaultSource", wintypes.SHORT),
        ("dmPrintQuality", wintypes.SHORT),
        ("dmColor", wintypes.SHORT),
        ("dmDuplex", wintypes.SHORT),
        ("dmYResolution", wintypes.SHORT),
        ("dmTTOption", wintypes.SHORT),
        ("dmCollate", wintypes.SHORT),
        ("dmFormName", wintypes.WCHAR * 32),
        ("dmLogPixels", wintypes.WORD),
        ("dmBitsPerPel", wintypes.DWORD),
        ("dmPelsWidth", wintypes.DWORD),
        ("dmPelsHeight", wintypes.DWORD),
        ("dmDisplayFlags", wintypes.DWORD),
        ("dmDisplayFrequency", wintypes.DWORD),
        ("dmICMMethod", wintypes.DWORD),
        ("dmICMIntent", wintypes.DWORD),
        ("dmMediaType", wintypes.DWORD),
        ("dmDitherType", wintypes.DWORD),
        ("dmReserved1", wintypes.DWORD),
        ("dmReserved2", wintypes.DWORD),
        ("dmPanningWidth", wintypes.DWORD),
        ("dmPanningHeight", wintypes.DWORD),
    ]

def set_screen_orientation(orientation):
    # Initialize DEVMODE structure
    devmode = DEVMODE()
    devmode.dmSize = ctypes.sizeof(DEVMODE)

    # Get current display settings
    if ctypes.windll.user32.EnumDisplaySettingsW(None, 0, ctypes.byref(devmode)) != 0:
        # Set new orientation
        devmode.dmDisplayOrientation = orientation
        if ctypes.windll.user32.ChangeDisplaySettingsW(ctypes.byref(devmode), 0) != 0:
            print("Failed to change display settings")
        else:
            print("Screen orientation changed successfully")
    else:
        print("Failed to get display settings")

def main():
    # Example settings: Rotate screen every 10 seconds
    orientations = [DMDO_DEFAULT, DMDO_90, DMDO_180, DMDO_270]
    while True:
        for orientation in orientations:
            set_screen_orientation(orientation)
            time.sleep(10)

if __name__ == "__main__":
    main()