# Wi-Fi Management Program

This Python script enables convenient management of Wi-Fi connections on Windows systems through key bindings. It allows users to connect to and disconnect from Wi-Fi networks using predefined keys. If initial key configurations fail, the program supports dynamic redefinition of these keys.

## Features

- **Connect and Disconnect:** Easily manage Wi-Fi connections using specified SSID and password.
- **Customizable Keys:** Define keys for disconnecting and connecting Wi-Fi, with validation against a predefined list.
- **Configuration File:** Stores Wi-Fi credentials and key mappings in `wifi_config.json`.
- **Dynamic Key Redefinition:** Prompted if initial keys are invalid.
- **Hide Program Option:** Utilize the insert button to hide the program window.

## Dependencies

- **keyboard:** For capturing key events.
- **colorama:** For terminal text colorization.
- **fade:** For ASCII art animation in the console.

## Usage

1. **Initialization:**
   - Launch the program and choose whether to load existing configurations from `wifi_config.json`.
   - If no configuration exists or if you opt not to load, enter Wi-Fi SSID, password, and select keys for disconnecting and connecting.

2. **Key Validations:**
   - Keys must be selected from a predefined list of valid keys.
   - If keys are deemed invalid, the program prompts for reselection.

3. **Operation:**
   - Use the configured keys to connect or disconnect from Wi-Fi networks.
   - Press `Insert` to toggle visibility of the program window.

## Getting Started

1. Clone the repository and ensure dependencies are installed (`keyboard`, `colorama`, `fade`).
2. Run the script on a Windows machine with Python installed.
3. Follow the on-screen prompts to configure Wi-Fi settings and key mappings.

## Notes

- Ensure the program is run with appropriate privileges for executing Wi-Fi commands (`netsh`).
- Modify `valid_keys` in the script to add or remove supported key bindings as needed.

