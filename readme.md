# nacelle-cx-scripts

This is a collection of scripts to audit the Nacelle API. Each script is housed in its own directory, and aims to test a very specific part of the API. 

## Installation 

Regardless of which script you're running, you should start by cloning the entire repository. 

Once cloned, install the required libraries/packages:

```
pip install -r requirements.txt
```

## Scripts

Each script has its own specific instruction to get setup, be sure to read the readme in each directory.

### collection-prod-order

Checks to see if the the order of products in a Nacelle collection matches the order of the products in Shopify.

### orphan-data

