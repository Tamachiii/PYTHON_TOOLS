#!/usr/bin/env python3

import argparse

def extract_column_from_file(file_path, column_number):
    """
    Extract a specified column from a text file containing a table.

    :param file_path: Path to the text file.
    :param column_number: Column number to extract (0-based).
    :return: List of values from the specified column.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        # Try to detect delimiter (assuming tab or space)
        delimiter = '\t' if '\t' in lines[0] else None

        # Extract the desired column from each line
        column_values = [line.split(delimiter)[column_number].strip() for line in lines if line.strip()]

    return column_values

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract a specific column from a tab-delimited file.")
    
    parser.add_argument('--input', type=str, required=True, help="Path to the input file.")
    parser.add_argument('--column', type=int, required=True, help="Column number to extract (starting from 0).")

    args = parser.parse_args()

    try:
        results = extract_column_from_file(args.input, args.column)
        for value in results:
            print(value)
    except IndexError:
        print("Error: Invalid column number specified")
