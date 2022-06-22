## ANTARXXVII-Leg1

This repository contains short code to automate data qc for dataset `Invertebrates from the ANTARXXVII Leg1 expedition to the Bransfield Strait, Antarctica - data`


## Dataset decription

The data was manually cleaned. The code used in this repository is mainly to check whether the url in multimedia file resolved. The only issue was the extension of the multimedia file differ between the actual file and what was entered into the data sheet. 

There were a couple of url which extension is not jpg but png which were eventually corrected manually.

The clean version of dataset can be found at: 

- https://ipt.biodiversity.aq/resource?r=antarxxvii-leg1

- https://github.com/biodiversity-aq/data-publication/tree/main/datasets/antarxxvii-leg1

Please note that the dataset is licensed under CC BY 4.0.


## Repo structure

```
.
├── README.md         : description of this repository
├── data              : interim and processed data
│   ├── interim
│   └── processed
├── main.py	      : short script to check media url
└── venv
```

## Getting started

Create a virtual environment in `Python 3.8`. Install dependencies with pip:

```
pip install -r requirements.txt
```

Run the code `main.py`.

