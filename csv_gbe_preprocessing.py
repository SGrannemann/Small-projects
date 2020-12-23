"""This module contains functions that can process CSV files from gbe-bund.de
(Gesundheitsberichterstattung des Bundes).
CSV files from this source use ';' as delimiters and use ',' for number separation
this can be converted using the functions in this module.
The provided functions can also remove the header and footnote from the csv.
Use them in the following order:
remove_header_and_footnote_gbeBund
reformat_csv_gbeBund

See example dir in this repository for examples of file before and after processing.
See documentation of the functions for more details.

"""
import csv
from pathlib import Path
import pandas as pd



def remove_header_and_footnote_gbe(filename, outputpath):
    """Removes the header and footnote from a GBE CSV file.
    Uses the filename in addition to information from the CSV file to provide a correct
    header line in the CSV.
    Creates a new file whose filename is the old file + _removedheader .

    Parameters
    ----------
    :param filename: path of the file to process
    :type filename: Path
    :param filename: path to directory for output
    :type filename: Path

    """
    # files are namend according to Illness_RowName_ColumnName
    # e.g. Depression_Alter_Geschlecht is a table where each row corresponds to an age cohort
    # and there are 3 columns: All sexes, male, female
    # thus, we can get the name of the very first column (age cohorts in the example) via the filename

    first_column = str(filename).split('_')[1]

    with open(f'{filename}', encoding='latin-1') as file_to_clean:
        # the column names are placed in a line that starts with ';', the delimiter is ';' too.
        fieldnames_for_csv = [line for line in file_to_clean.readlines() if line.startswith(';')][0]

        # rewind the file
        file_to_clean.seek(0,0)
        # the actual table data lines all start with quotation marks
        # we can dismiss the rest of the lines (header and footnote)
        lines_to_keep = [line for line in file_to_clean.readlines() if line.startswith('"')]
    
    newfilename = outputpath / Path(filename.stem + '_removedheader.csv')
    with open(f'{newfilename}', 'w', encoding='latin-1') as file_to_clean:
        # to get our table header right, we use the information from the filename and from the CSV
        file_to_clean.write(first_column + fieldnames_for_csv + '\n')
        for line in lines_to_keep:
            file_to_clean.write(line + '\n')

    return newfilename

def reformat_csv_gbe(filename, outputpath):
    """Takes a CSV processed by remove_header_and_footnote_gbe() and changes the delimiter to ','
    and the ',' in numbers to '.' .
    Tidies up unnecessary spacing in the leftmost column too and removes trailing ;
    Creates a new file with _cleaned as suffix.

    Parameters
    ----------
    :param filename: path of the original file (not the one with removed header)
    :type filename: Path
    :param outputath: path for directory of output
    :type filename: Path
    """

    with open(f'{filename}', encoding='latin-1') as file_to_process:
        csv_file = csv.DictReader(file_to_process, delimiter=';')
        # replace ',' with '.' : convert to english writing style for numbers
        # remove unnecessary whitespace and the trailing ; too.
        cleaned_lines = [{key:val.strip().replace(',', '.') for key, val in line.items() if key != ''} for line in csv_file]

    newfilename = outputpath / Path(filename.stem + '_cleaned.csv')
    with open(f'{newfilename}', 'w', encoding='latin-1') as file_to_write:

        csv_file = csv.DictWriter(file_to_write, fieldnames=cleaned_lines[0].keys())
        csv_file.writeheader()
        for line in cleaned_lines:
            csv_file.writerow(line)
    return newfilename

if __name__ == '__main__':
    #test code
    path_to_data = Path.cwd() / Path('data')
    path_for_output = Path.cwd() / Path('processed data')
    for data_file in path_to_data.glob('*.csv'):

        processed_file = remove_header_and_footnote_gbe(data_file, path_for_output)
        cleaned_file = reformat_csv_gbe(processed_file, path_for_output)

        df = pd.read_csv(cleaned_file, encoding='latin-1')

        print(df.head())
