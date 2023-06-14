import pandas as pd
import urllib.request
import io

def load_dataset(dataset_name, start_year=None, end_year=None, destination_path=None):
    # Mapping of dataset names to dataset URLs
    dataset_mapping = {
        'arxiv': 'https://huggingface.co/datasets/PenguinMan/ARXIV/resolve/main/arxiv2.csv',
        'bioarxiv': 'https://huggingface.co/datasets/PenguinMan/ARXIV/resolve/main/bioarxiv%20(1).csv',
        'plos-one': 'https://huggingface.co/datasets/PenguinMan/ARXIV/resolve/main/plos_one_new.csv',
        'medline': 'https://huggingface.co/datasets/PenguinMan/ARXIV/resolve/main/MEDLINE_Journal_Recommend2.csv'
        # Add more dataset mappings as needed
    }

    if dataset_name in dataset_mapping:
        dataset_url = dataset_mapping[dataset_name]

        response = urllib.request.urlopen(dataset_url)
        dataset_content = response.read().decode('utf-8')
        dataset_dataframe = pd.read_csv(io.StringIO(dataset_content))
        
        if dataset_name == 'arxiv' and start_year and end_year:
            dataset_dataframe = dataset_dataframe[
                (pd.to_datetime(dataset_dataframe['date']).dt.year >= start_year) &
                (pd.to_datetime(dataset_dataframe['date']).dt.year <= end_year)
            ]
        elif dataset_name == 'bioarxiv' and start_year and end_year:
            dataset_dataframe = dataset_dataframe[
                (pd.to_datetime(dataset_dataframe['update_date']).dt.year >= start_year) &
                (pd.to_datetime(dataset_dataframe['update_date']).dt.year <= end_year)
            ]
        
        print(f'Dataset "{dataset_name}" loaded and filtered based on date selection.')
        return dataset_dataframe
    else:
        print(f'Dataset "{dataset_name}" is not available.')




