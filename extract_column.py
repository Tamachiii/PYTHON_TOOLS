#!/usr/bin/env python3

import argparse

def extract_column_from_file(input_file, column_number):
    """
    Extract a specified column from a text file containing a table.

    :param input_file: Path to the text file.
    :param column_number: Column number to extract (0-based).
    :return: List of values from the specified column.
    """
    with open(input_file, 'r') as file:
        lines = file.readlines()
        
        # Try to detect delimiter (assuming tab or space)
        delimiter = '\t' if '\t' in lines[0] else None

        # Extract the desired column from each line
        column_values = [line.split(delimiter)[column_number].strip() for line in lines if line.strip()]

    return column_values


def save_to_file(data, output_file):
    """
    Save a list of data in a file.

    :param data: The data to save.
    :param output_file: Path to the output text file.
    """
    with open(output_file, 'w') as file:
        for item in data:
            file.write(item + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract a specific column from a tab-delimited file.")
    
    parser.add_argument('-i', '--input', type=str, required=True, help="Path to the input file.")
    parser.add_argument('-c', '--column', type=int, required=True, help="Column number to extract (starting from 0).")
    parser.add_argument('-o', '--output', type=str, help="Path to the ouput file to save data.")

    args = parser.parse_args()

    try:
        results = extract_column_from_file(args.input, args.column)
        for value in results:
            print(value)
        if args.output:
            save_to_file(results, args.output)
            print(f'[+] Results saved to {args.output}')
    except IndexError:
        print("[!] Error: Invalid column number specified")
    except Exception as e:
        print(f"[!] {e}")
