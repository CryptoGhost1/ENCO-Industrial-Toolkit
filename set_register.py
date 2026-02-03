import sys
import time
from pymodbus.client import ModbusTcpClient

if len(sys.argv) < 4:
    print("Usage: python set_register.py <IP> <REGISTER> <VALUE>")
    sys.exit(1)

target_ip = sys.argv[1]
reg_addr  = int(sys.argv[2])
reg_val   = int(sys.argv[3])

client = ModbusTcpClient(target_ip, port=502, timeout=5)

try:
    if client.connect():
        write_res = client.write_register(reg_addr, reg_val, slave=1)
        
        if not write_res.isError():
            print("[+] WRITE_OK")
            time.sleep(1.5)
            
            try:
                read_res = client.read_holding_registers(100, 10, slave=1)
                if not read_res.isError():
                    matrix = [read_res.registers[0]/10.0] + read_res.registers[1:]
                    print(f"[+] OT_MATRIX: {matrix}")
                else:
                    print("[!] READ_BUSY")
            except:
                print("[+] SESSION_TERMINATED")
        else:
            print("[-] WRITE_FAIL")
        
        client.close()
    else:
        print(f"[-] CONNECT_FAIL: {target_ip}")

except Exception as e:
    print(f"[-] SCRIPT_ERR: {e}")
