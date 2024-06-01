import argparse
import os
import sys
sys.path.append(".ScaleCounter")
from ScaleCount_Public_Functions import count_scales, count_scales_directory, split_count_select, display_results

def clean_path(output_path):
    # because scalecounter is picky
    # could definitely by optimized
    output_path = output_path.replace(".","_")
    output_path = output_path.replace("/","_")
    output_path = output_path.replace("\\","_")
    output_path = output_path.replace(" ","_")
    output_path = output_path.replace("\"","_")
    while output_path.find("__") != -1:
        output_path = output_path.replace("__","_")
    output_path = output_path.strip("_")
    return output_path

def parse_argument_path(argument_path):
    path = argument_path
    path = path.strip(".")
    path = path.strip("\"")
    path = path.strip("\\")

    return path

def determine_source_path(source_argument)->str:
    if not source_argument:
        print("No file or directory path provided. Please provide a file or directory path.")
        exit()
    else:
        return parse_argument_path(source_argument)

def determine_output_path(output_argument, source_path)->str:
    if output_argument:
        output_path =  clean_path(output_argument)
    else:
        output_path =  clean_path("results_display_" + parse_argument_path(source_path))
    
    output_path = uniquify(output_path)

    return output_path

def folders_in(directory_path) -> bool:
    for name in os.listdir(directory_path):
        if os.path.isdir(os.path.join(directory_path, name)):
            return True
    return False


def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extension
        counter += 1

    return path

def count_scales_and_display_results(split_count_select_argument, source_path, output_path):
    source_path_is_file = os.path.isfile(source_path)
    if source_path_is_file and split_count_select_argument:
        # SPLIT COUNT SELECT:
        results, best_indices, estimated_total = split_count_select(source_path)
        display_results(results, output_path,best_indices_lst=best_indices, estimated_total=estimated_total)
    elif source_path_is_file:
        # Single image COUNT SCALES:
        results, data = count_scales(source_path)
        display_results(results, output_path)
    else:
        # Directory COUNT SCALES
        results = count_scales_directory(source_path)
        display_results(results, output_path)

def handle_invalid_source(source_path, split_count_select_argument):
    is_dir = os.path.isdir(source_path) 
    if is_dir and folders_in(source_path):
        print("Error: Folder found in directory. Directory can only contain image files.")
        exit(1)
    elif "\"" in source_path:
        print("Error: Source path cannot have a backslash at the end if followed by optional arguments.")
        exit(1)
    elif is_dir and split_count_select_argument:
        print("Warning: Split count select argument supplied but source path is a directory.\nWill not be performing split count select")

def scale_counter_cli():
    """
    Scale Counter Command Line Interface.

    This function is the entry point of the Scale Counter CLI program. It parses the command line arguments,
    determines the source path and output path, and performs the scale counting based on the provided arguments.

    Command Line Arguments:
        -s, --source: Path to count scales from.
        -o, --output: Path to a directory to output the results.
        -sc, --split_count_select: Add argument to perform split count select on an image file.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Scale Counter Command Line Interface")
    parser.add_argument("-s", "--source", help="Path to a file or directory to count scales from", required=True)
    parser.add_argument("-o", "--output", help="Path to a directory to output the results", required=False)
    parser.add_argument("-scs", "--split_count_select", help="add argument to perform split count select on an image file", action='store_true', required=False)
    args = parser.parse_args()

    source_path = determine_source_path(args.source)
    print("source path:", source_path)

    handle_invalid_source(source_path, args.split_count_select)

    output_path = determine_output_path(args.output, source_path)
    print("output path:", output_path)

    count_scales_and_display_results(args.split_count_select, source_path, output_path)

if __name__ == "__main__":
    scale_counter_cli()