import pandas as pd
import os
from datetime import datetime

def run_data_pipeline(input_folder, output_file):
    """
    Finds all Excel files in a directory, cleans them, 
    and merges them into a single master file.
    """
    all_dfs = []
    
    # 1. Recursive Search for Excel files
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(('.xlsx', '.xls')):
                path = os.path.join(root, file)
                
                # 2. Extract & Tag
                try:
                    df = pd.read_excel(path)
                    df['source_file'] = file
                    df['processed_at'] = datetime.now().strftime("%Y-%m-%d")
                    all_dfs.append(df)
                    print(f"✅ Successfully processed: {file}")
                except Exception as e:
                    print(f"❌ Error reading {file}: {e}")

    # 3. Consolidate & Export
    if all_dfs:
        master_df = pd.concat(all_dfs, ignore_index=True)
        master_df.to_excel(output_file, index=False)
        print(f"\n🚀 Pipeline Complete! Master file saved as: {output_file}")
    else:
        print("No files found to process.")

if __name__ == "__main__":
    run_data_pipeline(input_folder='./data', output_file='Master_Report.xlsx')