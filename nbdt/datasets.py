import urllib.request

def load_dataset(dataset_name, destination_path=None):
    # Mapping of dataset names to dataset URLs
    dataset_mapping = {
        'arxiv': 'https://huggingface.co/datasets/PenguinMan/ARXIV/resolve/main/arxiv2.csv',
        'bioarxiv': 'https://huggingface.co/datasets/PenguinMan/ARXIV/resolve/main/bioarxiv%20(1).csv',
        'plos-one': 'https://huggingface.co/datasets/PenguinMan/ARXIV/resolve/main/PLOS_ONE2.csv'
        # Add more dataset mappings as needed
    }

    if dataset_name in dataset_mapping:
        dataset_url = dataset_mapping[dataset_name]
        
        if destination_path is None:
            # If destination_path is not specified, it will store the dataset in a variable
            response = urllib.request.urlopen(dataset_url)
            dataset_content = response.read().decode('utf-8')
            print('Dataset downloaded successfully.') # print confirmation
            return dataset_content
        else:
            urllib.request.urlretrieve(dataset_url, destination_path)
            print('Dataset downloaded successfully.')
    else:
        print(f'Dataset "{dataset_name}" is not available.')
