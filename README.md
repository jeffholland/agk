What is AGK (Audacity Glitch Kitchen)?

It is a GUI application for producing glitch art with Audacity. Audacity is a free audio editing software. Not a lot of people know that you can use it to transform any file, such as an image file, into raw data represented as audio. From there you can manipulate the audio using audio effects, then export it back into an image. This can produce some pretty weird, wacky, and wonderful results. AGK automates this process and provides an interface to make it easier for you to experiment and make art.

How to run agk:

1. Ensure Python 3 is installed - https://www.python.org/downloads/

2. Ensure Audacity is installed - https://www.audacityteam.org/download/

UPDATE 2024 - it seems like this project will not work with Audacity 3.4 or later, it only produces corrupt files. I'm currently investigating the issue, but for now, use version 3.3.3 or earlier, which can be downloaded from https://www.fosshub.com/Audacity-old.html.

3. Before you run agk for the first time, you will need to configure Audacity by doing the following:
- In Audacity, go to Preferences > Modules and make sure that mod-script-pipe is set to enabled.
- Import any .bmp file using File > Import > Raw Data. For the encoding, select U-Law. Make sure it's in 1 channel (Mono).
- Now export audio by doing File > Export > Audio (or cmd+shift+e on Mac / ctrl+shift+e on Windows). For the file type, select Other uncompressed files; for the encoding type, U-Law; and for the header, RAW (headerless). Click save to export the file. Make sure that it exported to a viewable RAW image, not a corrupted file.
- Quit and re-open Audacity.

4. With Audacity open, from the command line, navigate to the agk directory and run: python3 agk.py.

How to install agk as an app:

1. Do steps 1-3 above
2. Install Pyinstaller - https://pyinstaller.org/en/stable/installation.html
3. On Mac, run "pyinstaller agk.py && mv dist/agk /Applications/agk.app" and drag agk.ico to the application icon in the upper left corner of Get Info
4. On Windows, run "pyinstaller --icon=agk.ico agk.py"
5. Drag the app (Mac) or .exe (Windows) to your dock and run it

How to use agk:

First, find an image that you want to be the source file, and convert it to a bitmap (.bmp) file. This can be done in most image editors, such as GIMP or Microsoft Paint.

Next, select your options. AGK allows you to set the following options:
a. Folder name: the name of the folder into which your glitch edits will be spat out.
b. Counter start: the number from which AGK will start counting the first glitch edit iteration.
c. Num iterations: the number of glitch edit iterations to be spat out.
d. Import: you'll want to check this box the first time you run AGK. It will allow you to import your source image file into Audacity after you hit the Run button.
e. Fill gaps / gaps: we'll get to this later.

Now you can add effects by clicking the plus button. I suggest Echo for your first run, as the results are usually easy to see. You'll notice that the effect appears below with different options for parameters. On the left are the start parameters, and on the right are the end parameters. AGK will use the start value for the first iteration, the end value for the last iteration, and it will gradually ramp the values in between, so no matter how many iterations you chose to produce, each one will be different.

About one out of every 10 exports from AGK will produce a corrupted image file. This is what the "fill gaps" feature is for. If you find that your last batch of exports has a few corrupted files, just check the "fill gaps" box and type in the numbers associated with each gaps into the gaps text field, separated by commas. It will then attempt to re-export only those gaps. Just keep doing that until there are no more gaps.