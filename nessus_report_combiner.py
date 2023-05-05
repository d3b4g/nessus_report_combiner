#!/usr/bin/env python3

import os
import shutil
import sys
import argparse
import xml.etree.ElementTree as etree

def parse_arguments():
    parser = argparse.ArgumentParser(description="Combine .nessus files into a single report.")
    parser.add_argument("-i", "--input", help="Input directory containing .nessus files", default=".")
    parser.add_argument("-o", "--output", help="Output directory for combined report", default="nss_report")
    args = parser.parse_args()
    return args.input, args.output

def combine_nessus_files(input_directory, output_directory):
    first = True
    report_filename = "report.nessus"

    for filename in os.listdir(input_directory):
        if filename.endswith(".nessus"):
            filepath = os.path.join(input_directory, filename)
            print(f":: Parsing {filepath}")
            if first:
                main_tree = etree.parse(filepath)
                report = main_tree.find("Report")
                first = False
            else:
                tree = etree.parse(filepath)
                for element in tree.findall(".//ReportHost"):
                    report.append(element)
            print(":: => done.")
    
    if os.path.exists(output_directory):
        shutil.rmtree(output_directory)
    
    os.makedirs(output_directory, exist_ok=True)
    main_tree.write(os.path.join(output_directory, report_filename), encoding="utf-8", xml_declaration=True)

def main():
    input_directory, output_directory = parse_arguments()
    combine_nessus_files(input_directory, output_directory)

if __name__ == "__main__":
    main()
