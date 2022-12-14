# Collection Order Audit

This is a simple script that looks at the order in which products appear within a Shopify collection, and compares it to the order in which the Nacelle API returns the products. Both Shopify, and Nacelle should have a collection's product in the same order. 

## Setup

Once you've clone the repository that houses this directory, start by installing the required packages:

```
pip install -r requirements.txt
```

Next, rename `.env.sample` to `.env`, and update the values. Please note, when adding the `SHOPIFY_DOMAIN`, you only need the the unique ID. For example, if your domain is *my-store.myshopify.com*, you only need to enter *my-store*. 