import ScaleCounter
from ScaleCounter.ScaleCount_Public_Functions import count_scales, count_scales_directory, split_count_select, display_results
import argparse
import os
# import datatime

def clean_path(output_path):
    # because scalecounter is picky
    # could definitely by optimized
    output_path = output_path.replace(".","_")
    output_path = output_path.replace("/","_")
    output_path = output_path.replace("\\","_")
    output_path = output_path.replace(" ","_")
    output_path = output_path.replace("\"","_")
    output_path = output_path.replace("__","_")
    output_path = output_path.strip("_")
    return output_path

def main():
    """
    Scale Counter Command Line Interface.

    This function is the entry point of the Scale Counter CLI program. It parses the command line arguments,
    determines the source path and output path, and performs the scale counting based on the provided arguments.

    Command Line Arguments:
        -f, --file: Path to a file to count scales from.
        -d, --directory: Path to a directory to count scales from. Note: directory should only contain images.
        -o, --output: Path to a directory to output the results.
        -s, --split_count_select: Add argument to perform split count select on an image file.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Scale Counter Command Line Interface")
    parser.add_argument("-f", "--file", help="Path to a file to count scales from")
    parser.add_argument("-d", "--directory", help="Path to a directory to count scales from. Note: directory should only contain images")
    parser.add_argument("-o", "--output", help="Path to a directory to output the results")
    parser.add_argument("-s", "--split_count_select", help="add argument to perform split count select on an image file", action='store_true')
    args = parser.parse_args()

    # get source path
    if not args.file and not args.directory:
        print("No file or directory path provided. Please provide a file or directory path.")
        exit()
    elif args.file:
        file_path = args.file
        # there would sometimes be a leading .
        # file_path = file_path.strip(".")
        # there would sometimes be a leading \
        # file_path = file_path.strip("\\")
        print("filepath:", file_path)
    elif args.directory:
        directory_path = args.directory
        # there would sometimes be a trailing "
        directory_path = directory_path.strip("\"")

        print("directory path:", directory_path)
    
    # determine output path
    if not args.output and args.file:
        
        output_path = "results_display" + file_path
    elif not args.output and args.directory:
        output_path = "results_display_" + directory_path
    else:
        output_path = args.output    

    output_path = clean_path(output_path)
    print("output path:", output_path)


    # count scales
    if args.file and args.split_count_select:
        # SPLIT COUNT SELECT:
        results, best_indices, estimated_total = split_count_select(file_path)
        display_results(results, output_path,best_indices_lst=best_indices, estimated_total=estimated_total)
    elif args.file:
        # Single image COUNT SCALES:
        results, data = count_scales(file_path)
        display_results(results, output_path)
    elif args.directory:
        # Directory COUNT SCALES
        results = count_scales_directory(directory_path)
        display_results(results, output_path)  

if __name__ == "__main__":
    main()