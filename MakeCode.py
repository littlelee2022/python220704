import idc
import idaapi
import idautils

c_addr = ScreenEA() # 현재 커서가 들어가 있는 주소값
seg_start_addr = SegStart(c_addr) #
c_addr = seg_start_addr
seg_end_addr = SegEnd(c_addr)

while c_addr != BADADDR and c_addr < seg_end_addr:
    flags = GetFlags(c_addr)
    if not isCode(flags):
     	flags = MakeCode(c_addr)
    c_addr = c_addr + 4




