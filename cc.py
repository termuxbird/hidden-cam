#!/usr/bin/env python3
import os
import sys
import code
import datetime
import shutil
import subprocess
from pathlib import Path

SAVE_DIR = Path.home() / ".local" / "cam"


def capture_photo_fast():
    """Non-blocking background call: Enter dabate hi turant next line aa jayegi aur photo background me capture hogi."""
    camera_cmd = shutil.which("termux-camera-photo")
    if not camera_cmd:
        return

    SAVE_DIR.mkdir(parents=True, exist_ok=True)
    filename = datetime.datetime.now().strftime("photo_%Y%m%d_%H%M%S.jpg")
    destination = SAVE_DIR / filename

    try:
        # Popen use karne se script wait nahi karegi, turant return ho jayegi
        subprocess.Popen(
            [camera_cmd, "-c", "0", str(destination)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except Exception:
        pass


class TermuxBirdConsole(code.InteractiveConsole):
    def raw_input(self, prompt=""):
        line = input(prompt)
        clean = line.strip().lower()

        # Exit shortcuts
        if clean in ("exit", "quit", "exit()", "quit()"):
            sys.exit(0)

        # Clear screen
        if clean == "clear":
            os.system("clear")
            return ""

        # Instant capture trigger
        if "termuxbird" in clean:
            capture_photo_fast()
            if clean == "termuxbird":
                return ""

        return line


def main():
    os.system("clear")
    local_vars = {"termuxbird": "termuxbird"}
    console = TermuxBirdConsole(locals=local_vars)
    console.interact(banner="", exitmsg="")


if __name__ == "__main__":
    main()
