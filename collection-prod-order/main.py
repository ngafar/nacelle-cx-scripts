import os
import shopify
import nacelle
from dotenv import load_dotenv

load_dotenv() 

SHOPIFY_DOMAIN = os.getenv("SHOPIFY_DOMAIN")
SHOPIFY_TOKEN = os.getenv("SHOPIFY_TOKEN")
NACELLE_SPACE_ID = os.getenv("NACELLE_SPACE_ID")
NACELLE_TOKEN = os.getenv("NACELLE_TOKEN")

collection_handle = 'shorts'

shopify_prod_list = shopify.get_collection_prods(SHOPIFY_DOMAIN, SHOPIFY_TOKEN, collection_handle)
nacelle_prod_list = nacelle.get_collection_prods(NACELLE_SPACE_ID, NACELLE_TOKEN, collection_handle)

match = shopify_prod_list == nacelle_prod_list
print(match)