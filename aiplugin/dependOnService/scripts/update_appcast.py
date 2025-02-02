import hashlib
import json
import sys
from pathlib import Path


def update_appcast(message):
    with open ("aiplugin/dependOnService/src/info.json", "r") as f:
        info = json.load(f)
    version = info["version"]
    release_file = Path(f"release/easyuseai-plugin-akl-youdao-free-translate.aiplugin")
    assert release_file.is_file(), "Release file not exist"
    with open(release_file, "rb") as f:
        c = f.read()
        file_hash = hashlib.sha256(c).hexdigest()
    version_info = {
        "version": version,
        "desc": message,
        "sha256": file_hash,
        "url": f"https://github.com/ytsteven/easyuseai-plugin-akl-youdao-free-translate/releases/download/v{version}/easyuseai-plugin-akl-youdao-free-translate_v{version}.aiplugin",
        "minVersion": "0.4.0"
    }
    appcast_file = Path("aiplugin/dependOnService/appcast.json")
    if appcast_file.is_file():
        with open(appcast_file, "r") as f:
            appcast = json.load(f)
    else:
        appcast = dict(identifier="com.akl.easyuseai-plugin-akl-youdao-free-translate", versions=[])
    appcast["versions"].insert(0, version_info)
    with open(appcast_file, "w") as f:
        json.dump(appcast, f, ensure_ascii=False, indent=2)
    print(f"v{version}")


if __name__ == "__main__":
    message = sys.argv[1]
    update_appcast(message)
