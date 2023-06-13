# nbdt_lib


# Installation

For installation you can run the following code in the command line/terminal:
```python
git clone https://github.com/Wanderer-of-the-abyss/nbdt_lib.git
pip install ./nbdt_lib

```

# Load Datasets

Currently the library has 4 datasets ready to use:

`arxiv`: Has nearly 4k papers

`bioarxiv`: Has 29k papers from Bioarxiv

`plos_one`: Has 17k papers from PLOS_ONE

`medline`: Has 100k papers from the top 200 journals in the neuroscience field

```python
from nbdt.datasets import load_dataset
load_dataset(dataset_name, destination_path)  # load_dataset('arxiv', 'arxiv.csv')

```


