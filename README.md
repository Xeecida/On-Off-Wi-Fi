# Wi-Fi Management Program

This Python script enables convenient management of Wi-Fi connections on Windows systems through key bindings. It allows users to connect to and disconnect from Wi-Fi networks using predefined keys. If initial key configurations fail, the program supports dynamic redefinition of these keys.

## Features

### English
- **Connect and Disconnect:** Easily manage Wi-Fi connections using specified SSID and password.
- **Customizable Keys:** Define keys for disconnecting and connecting Wi-Fi, with validation against a predefined list.
- **Configuration File:** Stores Wi-Fi credentials and key mappings in `wifi_config.json`.
- **Dynamic Key Redefinition:** Prompted if initial keys are invalid.
- **Hide Program Option:** Utilize the insert button to hide the program window.

### ภาษาไทย
- **เชื่อมต่อและตัดการเชื่อมต่อ:** จัดการเชื่อมต่อ Wi-Fi ได้ง่ายดายโดยใช้ SSID และรหัสผ่านที่ระบุ
- **กำหนดคีย์ไบน์ดที่กำหนดเอง:** กำหนดคีย์สำหรับการตัดการเชื่อมต่อและเชื่อมต่อ Wi-Fi พร้อมการตรวจสอบจากรายการคีย์ที่กำหนดไว้ล่วงหน้า
- **ไฟล์กำหนดค่า:** เก็บข้อมูลรหัสผ่าน Wi-Fi และการจับคู่คีย์ใน `wifi_config.json`
- **การกำหนดค่าคีย์ไบน์ดแบบไดนามิก:** แจ้งให้กำหนดค่าใหม่หากคีย์เริ่มต้นไม่ถูกต้อง
- **ตัวเลือกซ่อนโปรแกรม:** ใช้ปุ่ม Insert เพื่อซ่อนหน้าต่างโปรแกรม

## Dependencies

- **keyboard:** For capturing key events.
- **colorama:** For terminal text colorization.
- **fade:** For ASCII art animation in the console.

## Usage

### English
1. **Initialization:**
   - Launch the program and choose whether to load existing configurations from `wifi_config.json`.
   - If no configuration exists or if you opt not to load, enter Wi-Fi SSID, password, and select keys for disconnecting and connecting.

2. **Key Validations:**
   - Keys must be selected from a predefined list of valid keys.
   - If keys are deemed invalid, the program prompts for reselection.

3. **Operation:**
   - Use the configured keys to connect or disconnect from Wi-Fi networks.
   - Press `Insert` to toggle visibility of the program window.

### ภาษาไทย
1. **การเริ่มต้นใช้งาน:**
   - เปิดโปรแกรมและเลือกที่จะโหลดการกำหนดค่าที่มีอยู่จาก `wifi_config.json`
   - หากไม่มีการกำหนดค่าหรือไม่ต้องการโหลด ให้ป้อน SSID และรหัสผ่านของ Wi-Fi และเลือกคีย์สำหรับการตัดการเชื่อมต่อและเชื่อมต่อ

2. **การตรวจสอบคีย์ไบน์ด:**
   - คีย์จะต้องถูกเลือกจากรายการคีย์ที่กำหนดไว้ล่วงหน้า
   - หากคีย์ถูกต้องไม่ได้รับการตรวจสอบ โปรแกรมจะแจ้งให้ทำการเลือกคีย์ใหม่

3. **การดำเนินการ:**
   - ใช้คีย์ที่กำหนดเพื่อเชื่อมต่อหรือตัดการเชื่อมต่อจากเครือข่าย Wi-Fi
   - กด `Insert` เพื่อสลับการมองเห็นของหน้าต่างโปรแกรม

## Getting Started

1. Clone the repository and ensure dependencies are installed (`keyboard`, `colorama`, `fade`).
2. Run the script on a Windows machine with Python installed.
3. Follow the on-screen prompts to configure Wi-Fi settings and key mappings.

## Notes

- Ensure the program is run with appropriate privileges for executing Wi-Fi commands (`netsh`).
- Modify `valid_keys` in the script to add or remove supported key bindings as needed.

[Releases](https://github.com/Xeecida/On-Off-Wi-Fi/releases/tag/Control_Wi-Fi)
