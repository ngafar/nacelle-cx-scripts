from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

def get_collection_prods(shopify_domain, shopify_token, collection_handle):
    headers = {
        'X-Shopify-Storefront-Access-Token': shopify_token,
        'Content-Type': 'application/json'    
    }    

    transport = AIOHTTPTransport(
        url=f'https://{shopify_domain}.myshopify.com/api/2021-07/graphql.json', 
        headers=headers)

    client = Client(transport=transport, fetch_schema_from_transport=True)

    query = gql(
        """
        query GetAllProdsInCollection($collectionHandle: String!) { 
            collection(handle: $collectionHandle) {
                products(first:250) {
                    edges {
                        node {
                            handle
                        }
                    }
                }
            }
        }        
        """
    )
    
    params = {"collectionHandle": collection_handle}

    result = client.execute(query, variable_values=params)

    prods = []
    
    for edge in result['collection']['products']['edges']:
        prods.append(edge['node']['handle'])

    return prods 
