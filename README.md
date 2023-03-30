This is a GUI application for producing glitch art with Audacity.

To run:

1. Ensure Python 3 is installed - https://www.python.org/downloads/
2. Ensure Audacity is installed - https://www.audacityteam.org/download/
3. Follow the instructions to enable mod-script-pipe in Audacity - https://manual.audacityteam.org/man/scripting.html
4. With Audacity open, from the command line, navigate to the agk directory and run: python3 agk.py
5. Have fun. Let me know if it doesn't work

To install:

1. Do steps 1-3 above
2. Ensure Pyinstaller is installed - https://pyinstaller.org/en/stable/installation.html
3. On Mac, run "pyinstaller agk.py && mv dist/agk /Applications/agk.app" and drag agk.ico to the application icon in the upper left corner of Get Info
4. On Windows, run "pyinstaller --icon=agk.ico agk.py"
5. Drag the app (Mac) or .exe (Windows) to your dock and run it