# Bootcamp Repository 
 
## Folder Structure
- **homework/** → All homework contributions will be submitted here. 
- **project/** → All project contributions will be submitted here. 
- **class_materials/** → Local storage for class materials. Never pushed to 
GitHub. 
 
## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.) 
- Include all required files for grading. 
 
## Project Folder Rules
- Keep project files organized and clearly named.

## Data Storage
- **data/raw/**: Raw data files saved as CSV format with timestamps
- **data/processed/**: Processed data files saved as Parquet format with timestamps  
- **Environment Variables**: DATA_DIR_RAW and DATA_DIR_PROCESSED control folder paths
- **Format Selection**: CSV for raw data (human readable), Parquet for processed (efficient storage)
- **Validation**: Shape and dtype checks ensure data integrity during save/load cycles
- **Utilities**: write_df and read_df functions auto-detect format by file extension

## Data Cleaning Strategy
- **fill_missing_median()**: Fills missing values in numeric columns with median values
- **drop_missing()**: Removes columns with missing value ratio above specified threshold
- **normalize_data()**: Scales numeric columns to 0-1 range using min-max normalization
- **Modular Design**: Each function operates independently and returns copies of data
- **Data Integrity**: Functions validate column existence and data types before processing
- **Processing Pipeline**: Applied sequentially for systematic data cleaning workflow
