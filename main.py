from pathlib import Path
'''import csv

data_folder = Path(__file__).parent / "raw_data"

for file in data_folder.iterdir():
    if file.suffix == ".csv":
        with open(file, "r") as file:
            reader = csv.reader(file)

            row_count = 0
            for row in reader:
                row_count +=1

            print(f"{file.name} has {row_count} rows.")'''

import pandas as pd
data_folder = Path(__file__).parent / "raw_data"
all_data = []
summary_stats = []

for file_path in data_folder.iterdir():
    if file_path.suffix == ".csv":
        
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip().str.lower()
        
        original_rows = len(df)
        print(original_rows)

        df = df.drop_duplicates()
        print(df)

        new_rows = len(df)
        duplicates_removed = original_rows - new_rows
        
        summary_stats.append({
            "filename": file_path.name,
            "original_rows": original_rows,
            "clean_rows": new_rows,
            "duplicates_removed": duplicates_removed
        })

        all_data.append(df)

merged_df = pd.concat(all_data, ignore_index=True)

print(f"Total rows after merging: {len(merged_df)}")


summary_df = pd.DataFrame(summary_stats)

output_path = Path(__file__).parent / "clean_report.xlsx"

with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    merged_df.to_excel(writer, sheet_name = "Clean_Data", index=False)
    summary_df.to_excel(writer, sheet_name="Summary", index=False)

print(f"Report saved successfuly to {output_path.name}!")












