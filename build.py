import json

package_json_file = "package.json"
with open(package_json_file, "r", encoding="utf-8") as file:
    package_data = json.load(file)


File = package_data.get("file", "")
icon = package_data.get("icon", "")
company = package_data.get("company", "")
program_name = package_data.get("program_name", "")
version = tuple(package_data.get("version", ()))
patch_version = tuple(package_data.get("patch_version", ()))
description = package_data.get("description", "")
Copyright = package_data.get("copyright", "")
title = package_data.get("title", "")

command = [
    "python", "-m", "nuitka",
    "--follow-imports",
    "--onefile",
    "--standalone",
    "--windows-icon-from-ico=" + icon,
    "--company-name=" + company,
    "--product-name=" + program_name,
    "--file-version=" + ".".join(map(str, version)),
    "--product-version=" + ".".join(map(str, patch_version)),
    "--file-description=" + description,
    "--copyright=" + Copyright,
    "--trademarks=" + title,
    "--windows-uac-admin",
    File
]


try:
    import subprocess
    subprocess.run(command, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error during compilation: {e}")