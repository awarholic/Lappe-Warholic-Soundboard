"""
C struct definitions credit

Author: LucasG (https://github.com/lucasg)
Source: http://stackoverflow.com/questions/13564851/generate-keyboard-events
"""
# imports time varibles 
import time
# imports key type varibles 
import ctypes



# Import the SendInput object
SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):#sets up the ablity to input @@@@@@@@@@@
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", PUL)
    ]

class HardwareInput(ctypes.Structure):#sets up the ablity to input @@@@@@@@@@@
    _fields_ = [
        ("uMsg", ctypes.c_ulong),
        ("wParamL", ctypes.c_short),
        ("wParamH", ctypes.c_ushort)
    ]

class MouseInput(ctypes.Structure):# helps user use tehr mouse 
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time",ctypes.c_ulong),
        ("dwExtraInfo", PUL)
    ]

class Input_I(ctypes.Union):# helps alow the user to use ther mosue 
    _fields_ = [
        ("ki", KeyBdInput),
        ("mi", MouseInput),
        ("hi", HardwareInput)
    ]

class Input(ctypes.Structure):#sets up the ablity to input @@@@@@@@@@@
    _fields_ = [
        ("type", ctypes.c_ulong),
        ("ii", Input_I)
    ]

class Keyboard:
    """
    Class Keyboard
    :author: Paradoxis <luke@paradoxis.nl>
    :description:

    Keyboard methods to trigger fake key events
    
    """

    # Keyboard key constants
    # More information: https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
    VK_BACKSPACE = 0x08 #Assines the backspace  key
    VK_ENTER = 0x0D #Assines the enter key
    VK_CTRL = 0x11#Assines the control key
    VK_ALT = 0x12#Assines the alt  key
    VK_0 = 0x30#Assines the key
    VK_1 = 0x31#Assines the  1  key
    VK_2 = 0x32#Assines the  2 key
    VK_3 = 0x33#Assines the 3 key
    VK_4 = 0x34#Assines the 4 key
    VK_5 = 0x35#Assines the 5 key
    VK_6 = 0x36#Assines the 6 key
    VK_7 = 0x37#Assines the 7 key
    VK_8 = 0x38#Assines the 8 key
    VK_9 = 0x39#Assines the 9 key
    VK_A = 0x41#Assines the Akey
    VK_B = 0x42#Assines the b key
    VK_C = 0x43#Assines the ckey
    VK_D = 0x44#Assines the d key
    VK_E = 0x45#Assines the f key
    VK_F = 0x46#Assines the g key
    VK_G = 0x47#Assines the g key
    VK_H = 0x48#Assines the h key
    VK_I = 0x49#Assines the i key
    VK_J = 0x4A#Assines the j key
    VK_K = 0x4B#Assines the k key
    VK_L = 0x4C#Assines the  l key
    VK_M = 0x4D#Assines the m key
    VK_N = 0x4E#Assines the n key
    VK_O = 0x4F#Assines the o key
    VK_P = 0x50#Assines the p key
    VK_Q = 0x51#Assines the q key
    VK_R = 0x52#Assines the  r key
    VK_S = 0x53#Assines the s key
    VK_T = 0x54#Assines the t key
    VK_U = 0x55#Assines the u key
    VK_V = 0x56#Assines the v key
    VK_W = 0x57#Assines the w key
    VK_X = 0x58#Assines the x key
    VK_Y = 0x59#Assines the y key
    VK_Z = 0x5A#Assines the z key
    VK_VOLUME_MUTE = 0xAD #this contols muting the volume
    VK_VOLUME_DOWN = 0xAE# this control teh volume down button
    VK_VOLUME_UP = 0xAF# this assines the volume up button
    VK_MEDIA_NEXT_TRACK = 0xB0 #not used
    VK_MEDIA_PREV_TRACK = 0xB1#not used
    VK_MEDIA_PLAY_PAUSE = 0xB3#not used 
    VK_MEDIA_STOP = 0xB2#not used 
    VK_LBUTTON = 0x01#this assines the left click
    VK_RBUTTON = 0x02#this assines the right click
    VK_CANCEL = 0x03#you get the piont it establishes the whole keyboard
    VK_MBUTTON = 0x04
    VK_XBUTTON1 = 0x05
    VK_XBUTTON2 = 0x06
    VK_BACK = 0x08
    VK_TAB = 0x09
    VK_CLEAR = 0x0C
    VK_RETURN = 0x0D
    VK_SHIFT = 0x10
    VK_CONTROL = 0x11
    VK_MENU = 0x12
    VK_PAUSE = 0x13
    VK_CAPITAL = 0x14
    VK_KANA = 0x15
    VK_HANGUEL = 0x15
    VK_HANGUL = 0x15
    VK_JUNJA = 0x17
    VK_FINAL = 0x18
    VK_HANJA = 0x19
    VK_KANJI = 0x19
    VK_ESCAPE = 0x1B
    VK_CONVERT = 0x1C
    VK_NONCONVERT = 0x1D
    VK_ACCEPT = 0x1E
    VK_MODECHANGE = 0x1F
    VK_SPACE = 0x20
    VK_PRIOR = 0x21
    VK_NEXT = 0x22
    VK_END = 0x23
    VK_HOME = 0x24
    VK_LEFT = 0x25
    VK_UP = 0x26
    VK_RIGHT = 0x27
    VK_DOWN = 0x28
    VK_SELECT = 0x29
    VK_PRINT = 0x2A
    VK_EXECUTE = 0x2B
    VK_SNAPSHOT = 0x2C
    VK_INSERT = 0x2D
    VK_DELETE = 0x2E
    VK_HELP = 0x2F
    VK_LWIN = 0x5B
    VK_RWIN = 0x5C
    VK_APPS = 0x5D
    VK_SLEEP = 0x5F
    VK_NUMPAD0 = 0x60
    VK_NUMPAD1 = 0x61
    VK_NUMPAD2 = 0x62
    VK_NUMPAD3 = 0x63
    VK_NUMPAD4 = 0x64
    VK_NUMPAD5 = 0x65
    VK_NUMPAD6 = 0x66
    VK_NUMPAD7 = 0x67
    VK_NUMPAD8 = 0x68
    VK_NUMPAD9 = 0x69
    VK_MULTIPLY = 0x6A
    VK_ADD = 0x6B
    VK_SEPARATOR = 0x6C
    VK_SUBTRACT = 0x6D
    VK_DECIMAL = 0x6E
    VK_DIVIDE = 0x6F
    VK_F1 = 0x70
    VK_F2 = 0x71
    VK_F3 = 0x72
    VK_F4 = 0x73
    VK_F5 = 0x74
    VK_F6 = 0x75
    VK_F7 = 0x76
    VK_F8 = 0x77
    VK_F9 = 0x78
    VK_F10 = 0x79
    VK_F11 = 0x7A
    VK_F12 = 0x7B
    VK_F13 = 0x7C
    VK_F14 = 0x7D
    VK_F15 = 0x7E
    VK_F16 = 0x7F
    VK_F17 = 0x80
    VK_F18 = 0x81
    VK_F19 = 0x82
    VK_F20 = 0x83
    VK_F21 = 0x84
    VK_F22 = 0x85
    VK_F23 = 0x86
    VK_F24 = 0x87
    VK_NUMLOCK = 0x90
    VK_SCROLL = 0x91
    VK_LSHIFT = 0xA0
    VK_RSHIFT = 0xA1
    VK_LCONTROL = 0xA2
    VK_RCONTROL = 0xA3
    VK_LMENU = 0xA4
    VK_RMENU = 0xA5
    VK_BROWSER_BACK = 0xA6
    VK_BROWSER_FORWARD = 0xA7
    VK_BROWSER_REFRESH = 0xA8
    VK_BROWSER_STOP = 0xA9
    VK_BROWSER_SEARCH = 0xAA
    VK_BROWSER_FAVORITES = 0xAB
    VK_BROWSER_HOME = 0xAC
    VK_LAUNCH_MAIL = 0xB4
    VK_LAUNCH_MEDIA_SELECT = 0xB5
    VK_LAUNCH_APP1 = 0xB6
    VK_LAUNCH_APP2 = 0xB7
    VK_OEM_1 = 0xBA
    VK_OEM_PLUS = 0xBB
    VK_OEM_COMMA = 0xBC
    VK_OEM_MINUS = 0xBD
    VK_OEM_PERIOD = 0xBE
    VK_OEM_2 = 0xBF
    VK_OEM_3 = 0xC0
    VK_OEM_4 = 0xDB
    VK_OEM_5 = 0xDC
    VK_OEM_6 = 0xDD
    VK_OEM_7 = 0xDE
    VK_OEM_8 = 0xDF
    VK_OEM_102 = 0xE2
    VK_PROCESSKEY = 0xE5
    VK_PACKET = 0xE7
    VK_ATTN = 0xF6
    VK_CRSEL = 0xF7
    VK_EXSEL = 0xF8
    VK_EREOF = 0xF9
    VK_PLAY = 0xFA
    VK_ZOOM = 0xFB
    VK_NONAME = 0xFC
    VK_PA1 = 0xFD
    VK_OEM_CLEAR = 0xFE

    def keyDown(keyCode):# this sets up the down key 
        """
        Key down wrapper
        :param keyCode: int
        :return: void
        """
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(keyCode, 0x48, 0, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def keyUp( keyCode):#writes teh code to make the volume up key work as untended 
        """
        Key up wrapper
        :param keyCode: int
        :return: void
        """
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(keyCode, 0x48, 0x0002, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def key( keyCode, length = 0):# this is the template that we used to make the keys pior
        """
        Type a key
        :param keyCode: int
        :param length: int
        :return:
        """
        Keyboard.keyDown(keyCode)
        time.sleep(length)
        Keyboard.keyUp(keyCode)