# Collection Order Audit

This is a simple script that looks at the order in which products appear within a Shopify collection, and compares it to the order in which the Nacelle API returns the products. Both Shopify, and Nacelle should have a collection's product in the same order. 

## Setup

Once you've clone the repository that houses this directory, start by installing the required packages:

```
pip install -r requirements.txt
```

Next, rename `.env.sample` to `.env`, and update the values. 

Please note, when adding the `SHOPIFY_DOMAIN`, you only need the the unique ID. For example, if your domain is *my-store.myshopify.com*, you only need to enter *my-store*. 

## Usage 

When running `main.py`, you have two options: 

1. Specifying the collection handle you'd like to audit.
2. Not specifying any handle.

If you're specifying a handle your command should look like this `python main.py holidays`. In this example, the *holidays* collection will be audited. If no handle is provided, the script will get a list of all collections from Nacelle, and check each of them. 

When the script is completed, a `out.csv` file will be created in this directory. The second column of the CSV will either be True or False. A True observance signifies that the order in both Shopify and Nacelle match. Ideally you want every item in column two to be True. 