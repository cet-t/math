import ctypes
__dll = ctypes.cdll.LoadLibrary('./mathdll.dll')


def pi() -> float:
    return __dll.pi()
