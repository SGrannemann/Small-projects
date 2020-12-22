import pandas as pd
import csv

# drop wrong semicolon at the end of csv files


def remove_header_and_footnote(file):
    first_column = file.split('_')[1]
    with open(f'{file}.csv', encoding='latin-1') as file_to_clean:
        line = [single_line for single_line in file_to_clean.readlines() if single_line.startswith(';')]
        fieldnames_for_csv = ';'.join(line[0].split(';'))
        
        file_to_clean.seek(0,0)
        lines_to_keep = [line for line in file_to_clean.readlines() if line.startswith('"')]
    with open(f'{file}_removedheader.csv', 'w', encoding='latin-1') as file_to_clean:

        file_to_clean.write(first_column + fieldnames_for_csv + '\n')
        for line in lines_to_keep:
            file_to_clean.write(line + '\n')


def clean_csv_from_gbeBund(file):
    
    
    


    with open(f'{file}_removedheader.csv', encoding='latin-1') as file_to_process:
        


        csv_file = csv.DictReader(file_to_process, delimiter=';')
        
        cleaned_lines = [{key:val.strip().replace(',', '.') for key, val in line.items() if key != ''} for line in csv_file]
        
        
    with open(f'{file}_cleaned.csv', 'w', encoding='latin-1') as file_to_write:
        csv_file = csv.DictWriter(file_to_write, fieldnames=cleaned_lines[0].keys(), delimiter=',')
        csv_file.writeheader()
        for line in cleaned_lines:
           csv_file.writerow(line)




remove_header_and_footnote('Depression_Region_Alter')
clean_csv_from_gbeBund('Depression_Region_Alter')

df = pd.read_csv('Depression_Region_Alter_cleaned.csv', encoding='latin-1')

print(df.head())