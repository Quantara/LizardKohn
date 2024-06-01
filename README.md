

# ScaleCounterCLI.py

Scale Counter CLI is a command line interface tool that counts scales from a given source path and outputs the results to a specified directory. It also provides an option to perform split count select on an image file.

## Installation
This tool requires Python version 3.8 - 3.8.10 to run. If you don't have Python installed, you can download it from Python's official website.

1. To install Scale Counter CLI, clone the repository to your local machine: 
```bash
git clone https://github.com/Quantara/LizardKohn.git
```
*Note that you must have Git installed on your machine to clone the repository. Alternatively, you can click on the "Code" button on the repository page and copy the URL to clone the repository using Git. You can also click on the "Download ZIP" button to download the repository as a zip file and extract it to your local machine.*

*To install Git, run the following command:*
```bash
winget install --id Git.Git -e --source winget
```

2. Navigate to the Scale Counter CLI directory:
```bash
cd LizardKohn
```

3. Install the required packages by running the following command:
```bash
pip install -r requirements.txt
```

## Usage
To use Scale Counter CLI, you need to provide a source path from where the scales will be counted. The results will be output to a specified directory. You can also add an argument to perform split count select on an image file.

Here is the general usage:
    
```bash
python ScaleCounterCLI.py -s <source_path> -o <output_path> -scs
```

You can use the Scale Counter CLI by providing command line arguments. Here are the available options:

- `-s`, `--source`: Path to a single image file or directory of image files to count scales from. This argument is required.
- `-o`, `--output`: Path to a directory to output the results. This argument is optional.
- `-scs`, `--split_count_select`: Add this argument to perform split count select on an image file. This argument is optional.

### Notes:
* Please note that you must provide either a file or a directory.
* Do not include backslash "\" at the end of a directory if followed by `-o` or `-scs` arguments. Good `-s /path/to/images`, bad `-s /path/to/images\` 
* If using a directory with a backslash at the end followed by optional arguments, please use double backslashes. Good `-s /path/to/images\\`, bad `-s /path/to/images\`. 

## Examples

Here is an example(s) of how to use the Scale Counter CLI:

```bash
python ScaleCounterCLI.py -f /path/to/image.jpg -o /path/to/output
```
```bash
python ScaleCounterCLI.py -o /path/to/output -d /path/to/images 
```

## Error Handling
If neither a file nor a directory is provided, the program will not proceed and will instead prompt you to provide a source path.

## Requirements
This program requires Python and the argparse library.

## Support
If you encounter any issues while using Scale Counter CLI, please open an issue on the [GitHub Repository](https://github.com/Quantara/LizardKohn).

## License
This project is licensed under the MIT License - see the LICENSE file for details.

