import importlib.metadata
import platform

import PyInstaller.__main__

VERSION = importlib.metadata.version("aau_spritegen")
OS = None
if platform.system() == "Windows":
    OS = f"win{platform.release()}"
elif platform.system() == "Linux":
    import distro

    OS = f"{distro.id()}{distro.version()}"
else:
    raise NotImplementedError("This OS is not supported yet")


PyInstaller.__main__.run(
    [
        "src/aau_spritegen/main.py",
        f"--name=aau_spritegen_{VERSION}_{OS}",
        "--noconfirm",
        "--clean",
        "--onefile",
        "--noupx",
    ]
)
