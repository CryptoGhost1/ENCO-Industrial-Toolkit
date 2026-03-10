# ❄️ ENCO: FrostyTrigger
### Industrial Logic Manipulator & ICS/OT Infrastructure Auditor

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Protocol](https://img.shields.io/badge/Protocol-Modbus--TCP-orange?style=for-the-badge)
![Sector](https://img.shields.io/badge/Sector-Industrial--OT-red?style=for-the-badge)

```text
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
```

---

## 🔍 Vulnerability Overview

**FrostyTrigger** is a specialized tool designed for auditing and manipulating process logic in **Programmable Logic Controllers (PLCs)**. It focuses on the exploitation of insecure industrial protocols, specifically **Modbus TCP (Port 502)**.

The tool allows a security researcher to bypass logic guards and perform unauthorized writes to holding registers, simulating a **Logic Injection Attack** that can override safety parameters in critical infrastructure.

---

## 🚀 Execution Guide

### 1. Identify Target Infrastructure
Ensure the target PLC is reachable on the network and has port **502** open.

### 2. Run the Logic Injection
Execute the script by specifying the target IP, the register to manipulate, and the desired value:

```bash
python frosty_trigger.py <PLC_IP> <REGISTER> <VALUE>
```

**Example:**
```bash
python frosty_trigger.py 172.16.9.118 101 1
```

---

## 🛠️ Script Parameters

| Parameter | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `<IP>` | `IPv4` | Target PLC or Gateway IP address | `Required` |
| `<REGISTER>` | `Int` | Modbus Holding Register address | `Required` |
| `<VALUE>` | `Int` | New value to inject into the logic | `Required` |

---

## 📑 Known OT Matrix (Registers)

| Address | Function | Impact upon Injection |
| :--- | :--- | :--- |
| **101** | `SABOTAGE_TRIGGER` | **1** = Force Stealth Frost Mode (45°C) |
| **102** | `TEMP_SETPOINT` | Target operational temperature |
| **104** | `STRESS_TRIGGER` | **1** = Hardware Fatigue (Fast Cycling) |
| **105** | `GLITCH_TRIGGER` | **1** = Visual UI Desync (HMI Panic) |

---

## 🛡️ Industrial Remediation

* **Network Segmentation**: Place PLCs within a dedicated VLAN (Purdue Model Level 1) with strict Firewall rules.
* **Deep Packet Inspection (DPI)**: Deploy IDS/IPS solutions capable of inspecting Modbus traffic for anomalous write commands.
* **Logic Hardening**: Implement safety interlocks within the PLC code that cannot be overridden solely via communication registers.

---

> **Disclaimer**: This tool is for educational purposes and authorized industrial cybersecurity auditing only. Unauthorized access to critical infrastructure is illegal.
