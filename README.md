# WiGLE .log file cleaner 📡

Takes raw .log files from your device, fixes the format, and gets them ready for upload to WiGLE.

## How it works

Looks for .log files in the ./logs folder.

Cleans them up (removes line numbers, adds the correct WiGLE preheader).

Saves the cleaned files into ./processed_logs.

## How to use

Put your .log files in the logs/ folder.

Run:

`python3 log-cleaner.py`

Grab your cleaned files from `processed_logs/` and upload them to WiGLE!

## Notes

Script auto-creates the `processed_logs/ folder` if it doesn’t exist.

Make sure you have Python 3 installed.

## License

MIT License
