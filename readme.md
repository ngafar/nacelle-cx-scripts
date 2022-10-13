# nacelle-orphan-tool

A tool for sifting out instances where the Nacelle dashboard has the correct data, but the API returns incorrect data. 

More specifically, instances where querying by `handles` returns an incorrect/older data. However, querying by `nacelleEntryIds` returns the expected response. This discrepancy — where `nacelleEntryIds` returns the right data, but `handles` does not — is a tell tale sign of an "orphaned" entry. 

Orphaned entries are usually the result of a handle change. 

## Installation

After cloning this repo, install dependencies:

```
pip install -r requirements.txt
```

Next, ensure you have a `data/` dir, with a `spaces.csv` file. This CSV file should only have two columns: the first containing a Space ID, and the second column, being the space's storefront token. Additionally, this CSV file should not contain column headers. 

## Usage

When running `main.py`, the program expects either a "p" or a "c." This argument determines if product or collection data is pulled. 

For example:

```python
python main.py p # Looks for orphaned products
python main.py c # Looks for orphaned collections
```