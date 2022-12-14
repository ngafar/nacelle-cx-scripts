from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

def get_collection_prods(space_id, token, collection_handle):
    headers = {
        'x-nacelle-space-token': token,
        'Content-Type': 'application/json'    
    }    
    
    transport = AIOHTTPTransport(
        url=f'https://storefront.api.nacelle.com/graphql/v1/spaces/{space_id}', 
        headers=headers)

    client = Client(transport=transport, fetch_schema_from_transport=True)

    query = gql(
        """
        query GetAllProdsInCollection($collectionHandle: String!) {
            allProductCollections(filter: {handles: [$collectionHandle]}) {
                edges {
                    node {
                        products {
                            content {
                                handle
                            }
                        }
                    }
                }
            }
        }
        """
    )

    params = {"collectionHandle": collection_handle}

    result = client.execute(query, variable_values=params)

    products = []

    for edge in result['allProductCollections']['edges']:
        for product in edge['node']['products']:
            products.append(product['content']['handle'])

    return products
