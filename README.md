

# ScaleCounterCLI.py

This is a command-line interface (CLI) for the Scale Counter program. It allows you to count scales from an image or a directory of images.

## Installation
1. Clone the repository
2. Install the required packages
```bash
pip install -r requirements.txt
```

## Usage

You can use the Scale Counter CLI by providing command line arguments. Here are the available options:

- `-f`, `--file`: Path to a single image file to count scales from.
- `-d`, `--directory`: Path to a directory to count scales from. Note: The directory should only contain images.
- `-o`, `--output`: Path to a directory where the results will be output.
- `-s`, `--split_count_select`: Add this argument to perform split count select on an image file.

### Notes:
* Please note that you must provide either a file or a directory, but not both. If you provide both, the program will use the file and ignore the directory. 
* If you do not provide a file or a directory, the program will prompt you to provide a source path.
* `-o` is optional. If you do not provide an output directory, the program will output the results to a directory beginning with "results_display_" followed by file name or directory name.
* `-s` is optional. If you provide this argument, the program will perform split count select on the image file. If you do not provide this argument, the program will perform normal scale counting on the image file. Currently not working.
* `-d` is a little finnicky, please add it as the last argument if using.
## Example


Here is an example(s) of how to use the Scale Counter CLI:

```bash
python ScaleCounterCLI.py -f /path/to/image.jpg -o /path/to/output
```
```bash
python ScaleCounterCLI.py -o /path/to/output -d /path/to/images 
```



This will count the scales in the image located at `/path/to/image.jpg` and output the results to the directory at `/path/to/output`.

## Error Handling
If neither a file nor a directory is provided, the program will not proceed and will instead prompt you to provide a source path.

## Requirements
This program requires Python and the argparse library.


python version: 3.8.10

