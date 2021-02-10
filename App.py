import ctypes
import keyboard
from infi.systray import SysTrayIcon

user32 = ctypes.WinDLL('user32')
user32.GetKeyState.restype = ctypes.c_short

def capslock_state():
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_CAPITAL = 0x14
    
    if ((hllDll.GetKeyState(VK_CAPITAL)) & 0xffff) != 0:
        return 1 # Caps-lock is ON
    else:
        return 0 # Caps-lock is off

def bye(sti): print('Bye, then.')

def switch_icon(sti):
    if sti._icon == "resources/off.ico":
        sti.update(icon="resources/on.ico", hover_text="Caps-lock is on")
    elif sti._icon == "resources/on.ico":
        sti.update(icon="resources/off.ico", hover_text="Caps-lock is off")
    else:
        print(f"Got unknown value of `{sti._icon}` for sti._icon")

sti = SysTrayIcon("resources/off.ico", "Caps-lock is off", (), on_quit=bye, default_menu_index=1)

if capslock_state() == 1:
    sti.update(icon="resources/on.ico", hover_text="Caps-lock is on")
    
keyboard.on_press_key(key='caps lock',callback= lambda _: switch_icon(sti))

sti.start()

