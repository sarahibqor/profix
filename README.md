# ProFix

ProFix is a Python utility that automatically rotates the screen orientation for tablets and monitors based on predefined settings on Windows.

## Features

- Automatically changes screen orientation at regular intervals.
- Supports multiple screen orientations: default, 90 degrees, 180 degrees, and 270 degrees.

## Requirements

- Windows Operating System
- Python 3.x

## Installation

1. Clone the repository or download the `profix.py` file.
2. Ensure you have Python installed on your system.

## Usage

1. Open a command prompt or terminal.
2. Navigate to the directory where `profix.py` is located.
3. Run the script using Python:

   ```bash
   python profix.py
   ```

4. The script will automatically rotate your screen orientation every 10 seconds through the predefined orientations.

## Important Notes

- Running this script requires administrative privileges to change display settings.
- Changing screen orientation may not be supported on all devices.
- The script currently rotates the screen at fixed intervals. Adjust the intervals as needed by modifying the `time.sleep()` value in the script.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.