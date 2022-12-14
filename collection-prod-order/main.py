import shopify
import nacelle

shopify_list = shopify.get_collection_prods()
nacelle_list = nacelle.get_collection_prods(space_id, token, collection_handle)