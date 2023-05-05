# nessus_report_combiner

![Python 3.6+](https://img.shields.io/badge/python-3.6%2B-blue)


This script combines multiple `.nessus` files into a single report. It is particularly useful for aggregating data from multiple Nessus scans.

## Requirements

- Python 3.6 or later

## Installation

Clone this repository or download the `nessus_report_combiner.py` script.
git clone https://github.com/yourusername/nessus-report-combiner.git


### Arguments

- `-i`, `--input`: The input directory containing `.nessus` files (default: current directory)
- `-o`, `--output`: The output directory for the combined report (default: `nss_report`)

### Example
python nessus_report_combiner.py -i scans -o combined_reports

This command will combine all `.nessus` files found in the `scans` directory and write the combined report to the `combined_reports` directory.

## Notes

- The script will overwrite the output directory if it already exists.
- The script expects that the input `.nessus` files are valid and well-formed. If any issues arise during parsing, the script may not function as intended.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

This command will combine all `.nessus` files found in the `scans` directory and write the combined report to the `combined_reports` directory.

## Notes

- The script will overwrite the output directory if it already exists.
- The script expects that the input `.nessus` files are valid and well-formed. If any issues arise during parsing, the script may not function as intended.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

