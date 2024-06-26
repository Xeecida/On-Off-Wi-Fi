import keyboard
import os
import json
from datetime import datetime
from colorama import init, Fore, Style
import fade
import ctypes


init(autoreset=True)
CONFIG_FILE = "wifi_config.json"

def logging_print(text, level="DEBUG"):
    current_time = datetime.now().strftime("%H:%M:%S")
    colors = {
        "DEBUG": Fore.GREEN,
        "INFO": Fore.BLUE,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED
    }
    print(f"{colors.get(level, Fore.WHITE)}[{level}]{Fore.MAGENTA}[{current_time}]: {Style.RESET_ALL}{text}")

def show_window():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)

def hide_window():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def toggle_window():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if ctypes.windll.user32.IsWindowVisible(hwnd):
        hide_window()
    else:
        show_window()

def disconnect_wifi():
    logging_print("Disconnecting Wi-Fi", "INFO")
    os.system('netsh wlan disconnect')

def connect_wifi(ssid, password):
    logging_print(f"Connecting to Wi-Fi: {ssid}", "INFO")
    connect_command = f'netsh wlan connect name="{ssid}"'
    os.system(connect_command)
    profile_info = f"""
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>{ssid}</name>
        <SSIDConfig>
            <SSID>
                <name>{ssid}</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>auto</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>{password}</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>
    """
    profile_filename = f"{ssid}.xml"
    with open(profile_filename, 'w') as file:
        file.write(profile_info)
    os.system(f'netsh wlan add profile filename="{profile_filename}"')

def get_key_press(prompt):
    logging_print(prompt, "INFO")
    key_event = keyboard.read_event()
    while key_event.event_type != keyboard.KEY_DOWN:
        key_event = keyboard.read_event()
    logging_print(f"Selected key: {key_event.name}", "INFO")
    return key_event.name

def save_config(ssid, password, disconnect_key, connect_key):
    config_data = {
        "ssid": ssid,
        "password": password,
        "disconnect_key": disconnect_key,
        "connect_key": connect_key
    }
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config_data, file)
    logging_print("Settings have been saved successfully", "INFO")

def load_config():
    try:
        with open(CONFIG_FILE, 'r') as file:
            config_data = json.load(file)
        logging_print("Settings have been loaded successfully", "INFO")
        return config_data
    except FileNotFoundError:
        logging_print("No config file found, initializing new configuration", "INFO")
        return None
    except json.decoder.JSONDecodeError:
        logging_print("Invalid JSON format in config file, initializing new configuration", "ERROR")
        return None
valid_keys = {
    'esc', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
    'print_screen', 'scroll_lock', 'pause_break', 'tilde', '1', '2', '3', '4', '5', '6',
    '7', '8', '9', '0', 'minus', 'equals', 'backspace', 'insert', 'home', 'page_up',
    'tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'open_bracket', 'close_bracket',
    'backslash', 'delete', 'end', 'page_down', 'caps_lock', 'a', 's', 'd', 'f', 'g', 'h', 
    'j', 'k', 'l', 'semicolon', 'quote', 'enter', 'shift', 'z', 'x', 'c', 'v', 'b', 'n', 
    'm', 'comma', 'dot', 'slash', 'ctrl', 'win', 'alt', 'space', 'alt_gr', 'menu', 'up', 
    'left', 'down', 'right'
}

def main():
    while True:
        choice = input(f"{Fore.YELLOW}Do you want to read values from the {Fore.CYAN}{CONFIG_FILE}{Fore.WHITE}{Fore.YELLOW}? y/n: {Fore.WHITE}")
        if choice.lower() in ["y", "yes"]:
            config = load_config()
            if config:
                ssid, password, disconnect_key, connect_key = (
                    config["ssid"],
                    config["password"],
                    config["disconnect_key"],
                    config["connect_key"],
                )
            else:
                ssid = input(f"{Fore.YELLOW}Enter Wi-Fi SSID: {Fore.WHITE}")
                password = input(f"{Fore.YELLOW}Enter Wi-Fi Password: {Fore.WHITE}")
                disconnect_key = get_key_press(f"{Fore.YELLOW}Press the key to use for disconnecting Wi-Fi: {Fore.WHITE}")
                connect_key = get_key_press(f"{Fore.YELLOW}Press the key to use for connecting Wi-Fi: {Fore.WHITE}")
                save_config(ssid, password, disconnect_key, connect_key)
            break  # Exit the loop if user chooses 'y' or 'yes'
        elif choice.lower() in ["n", "not", "no"]:
            ssid = input(f"{Fore.YELLOW}Enter Wi-Fi SSID: {Fore.WHITE}")
            password = input(f"{Fore.YELLOW}Enter Wi-Fi Password: {Fore.WHITE}")
            disconnect_key = get_key_press(f"{Fore.YELLOW}Press the key to use for disconnecting Wi-Fi: {Fore.WHITE}")
            connect_key = get_key_press(f"{Fore.YELLOW}Press the key to use for connecting Wi-Fi: {Fore.WHITE}")
            save_config(ssid, password, disconnect_key, connect_key)
            break  # Exit the loop if user chooses 'n', 'not', or 'no'
        else:
            logging_print("Warning: Please select y/n", "ERROR")

    for key, func, desc in [
        (disconnect_key, lambda _: disconnect_wifi(), "disconnecting Wi-Fi"),
        (connect_key, lambda _: connect_wifi(ssid, password), "connecting Wi-Fi"),
    ]:
        if key not in valid_keys:
            logging_print(f"Invalid {desc} key: {key}", "ERROR")
            while True:
                try:
                    keyboard.on_press_key(key, func)
                    save_config(ssid, password, disconnect_key, connect_key)
                    break
                except Exception as e:
                    logging_print(f"Error using {desc} key: {e}", "ERROR")
                    key = get_key_press(f"Press the key to use for {desc}: ")

    keyboard.on_press_key("insert", lambda _: toggle_window())
    keyboard.wait()



raw_nuker_logo = '''
                                ███▄    █   ██████     ███▄    █  █    ██  ██ ▄█▀▓█████ 
                                ██ ▀█   █ ▒██    ▒     ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ 
                                ▓██  ▀█ ██▒░ ▓██▄      ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   
                                ▓██▒  ▐▌██▒  ▒   ██▒   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ 
                                ▒██░   ▓██░▒██████▒▒   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒
                                ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░
                                ░ ░░   ░ ▒░░ ░▒  ░ ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░
                                ░   ░ ░ ░  ░  ░        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░   
                                        ░       ░              ░    ░     ░  ░      ░  ░
'''
ch = f'''
{Fore.RED}
                    ╔════════════════════════════════════════════════════════════════════════════╗
                    ║                                                                            ║
                    ║  This program allows you to manage Wi-Fi connections using predefined      ║
                    ║  keys for disconnecting and connecting. If keys are invalid, you can       ║
                    ║  redefine them. Wi-Fi credentials and keys are stored in a configuration   ║
                    ║  file ('wifi_config.json'). The program also supports dynamic key          ║
                    ║  redefinition if initial keys fail to work.                                ║
                    ║                                                                            ║
                    ║  Features:                                                                 ║
                    ║  - Connect to a Wi-Fi network using specified SSID and password.           ║
                    ║  - Disconnect from Wi-Fi using a predefined key.                           ║
                    ║  - Customize keys for disconnecting and connecting Wi-Fi.                  ║
                    ║  - Do not set the insert button becuse it's a button to hide the program   ║
                    ║                                                                            ║
                    ║  Key Validations:                                                          ║
                    ║  - Keys must be selected from a predefined list of valid keys.             ║
                    ║  - If keys are invalid, the program prompts for a new selection.           ║
                    ║                                                                            ║
                    ║  Dependencies:                                                             ║
                    ║  - keyboard module for key event handling.                                 ║
                    ║  - colorama module for colored output.                                     ║
                    ║  - fade module for ASCII art animation.                                    ║
                    ║                                                                            ║
                    ╚════════════════════════════════════════════════════════════════════════════╝
{Fore.RESET}
'''


if __name__ == "__main__":
    try:
        os.system('cls')
        faded_text = fade.water(raw_nuker_logo)
        print(faded_text)
        print(fade.fire(ch))
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Program terminated by user.{Fore.WHITE}")
    except Exception as e:
        print(f"Error: {e}")
