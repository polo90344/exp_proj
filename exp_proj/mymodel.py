import win32api as kernel32
import win32con as con
from ctypes import *



#进制转换函数
def anyto10(str, any=16):
    t = '0123456789ABCDEF'
    lstr = len(str)
    ustr = str.upper()
    ret = 0
    i = 0
    while lstr:
        ret = ret * any + t.find(ustr[i])
        i += 1
        lstr -= 1
    return ret

#获取窗体进程号
def getWindowPid(hwnd):
    pass

#内存操作
def readMemoryIntType(pid, lpBaseAddress):
    hProcess = kernel32.OpenProcess(con.PROCESS_ALL_ACCESS, 0, pid)
    lpBuffer = c_int(0)
    bytesRead = c_ulong(0)
    ret = windll.kernel32.ReadProcessMemory(hProcess, lpBaseAddress, byref(lpBuffer), 4, byref(bytesRead))
    windll.api.CloseHandl(hProcess)
    if ret == 0:
        return -1
    return lpBuffer.value

def readGameIntType(pid, base, offset1=None, offset2=None, offset3=None, offset4=None):
    if not offset1:
        return readMemoryIntType(pid, anyto10(base))
    data = readMemoryIntType(pid, anyto10(base))
    if not offset2:
        return readMemoryIntType(pid, data + anyto10(offset1))
    data = readMemoryIntType(pid, data + anyto10(offset1))
    if not offset3:
        return readMemoryIntType(pid, data + anyto10(offset2))
    data = readMemoryIntType(pid, data + anyto10(offset2))
    if not offset4:
        return readMemoryIntType(pid, data + anyto10(offset3))
    data = readMemoryIntType(pid, data + anyto10(offset3))
    return readMemoryIntType(pid, data + anyto10(offset4))

def writeMemoryIntType(pid, address, value):
    hProcess = kernel32.OpenProcess(con.PROCESS_ALL_ACCESS, 0, pid)
    value = c_int(value)
    ret = windll.kernel32.WriteProcessMemory(hProcess, address, byref(value), 4, 0)
    windll.api.CloseHandle(hProcess)
    if ret == 0:
        return False
    return True
    




if __name__ == "__main__":
    a = input("Enter a Hex Number to Convert:")
    r = anyto10(a)
    print("Decimal Value is:", r)