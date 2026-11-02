# TermuxBird

A small Python utility for Termux that lets you trigger a photo capture from the interactive Python console by typing a custom command.

## Features

- Captures a photo using the Termux:API camera command.
- Starts the capture in the background, so the console returns immediately.
- Saves photos in `~/.local/cam/`.
- Supports a custom trigger command (you can replace `termuxbird` with your own word).

## Requirements

- Android with Termux installed.
- Python 3 in Termux.
- The Termux:API app installed from the same source as your Termux app.
- The Termux:API package installed inside Termux.
- Camera permission granted to Termux / Termux:API when Android asks.

## Installation

Open Termux and run:

```bash
pkg update
pkg install python termux-api
```

Install the Termux:API Android app from the same source you used for Termux, then grant camera permission.

Download or clone this repository, open its folder, and run:

```bash
python cam.py
```

At the Python console prompt, type:

```text
termuxbird
```

The photo capture is started in the background. Photos are saved under:

```text
~/.local/cam/
```

## Set your own private trigger command

You can change `termuxbird` to any word you prefer, for example `mycamera`.

1. Open `cam.py` in a text editor.
2. Search for every occurrence of `termuxbird`.
3. Replace **all** occurrences with your chosen command, using the same spelling everywhere. For example, replace each `termuxbird` with `mycamera`.
4. Save `cam.py` and run it again:

   ```bash
   python cam.py
   ```

5. Type your new command at the Python console prompt:

   ```text
   mycamera
   ```

**Important:** Replace every occurrence, not just one. Use a simple lowercase word without spaces. This command is a convenience trigger, not a password or security feature.

## Exit and console shortcuts

- `exit` or `quit` — close the console.
- `clear` — clear the terminal screen.
- Your chosen camera trigger — start a photo capture.

## Notes and troubleshooting

- If typing the trigger does nothing, check that the Termux:API Android app and the `termux-api` package are installed.
- Make sure camera permission is granted.
- The script uses camera ID `0`.
- The script starts capture asynchronously. If the camera service is unavailable or the command is missing, the script may return without displaying a detailed error.
- This project does not include a graphical interface.

## License

This project is released under the MIT License. See [LICENSE](LICENSE).
