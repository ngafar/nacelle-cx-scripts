from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

def get_all_products(space_id, token, end_cursor=''):
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
        query GetAllProducts($endCursor: String!) { 
            allProducts(filter: {first: 100, after: $endCursor}) {
                pageInfo {
                    hasNextPage
                    endCursor
                }
                edges {
                    node {
                        nacelleEntryId
                        content {
                            handle
                        }
                    }
                }
            }
        }        
        """
    )


    params = {"endCursor": end_cursor}

    result = client.execute(query, variable_values=params)

    prods = []

    for entry in result['allProducts']['edges']:
        row = []

        entry_id = entry['node']['nacelleEntryId']
        handle = entry['node']['content']['handle']

        row.append(space_id)
        row.append(token)
        row.append(entry_id)
        row.append(handle)

        prods.append(row)
    
    # Pagination:
    has_next_page = result['allProducts']['pageInfo']['hasNextPage']
    end_cursor = result['allProducts']['pageInfo']['endCursor']

    while has_next_page:
        params = {"endCursor": end_cursor}

        result = client.execute(query, variable_values=params)

        for entry in result['allProducts']['edges']:
            row = []

            entry_id = entry['node']['nacelleEntryId']
            handle = entry['node']['content']['handle']

            row.append(space_id)
            row.append(token)
            row.append(entry_id)
            row.append(handle)

            prods.append(row)
        
        has_next_page = result['allProducts']['pageInfo']['hasNextPage']
        end_cursor = result['allProducts']['pageInfo']['endCursor']

    return prods

def get_prod_by_id(space_id, token, entry_id):
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
        query GetProduct($entryID: [String!]) { 
            allProducts(filter: {nacelleEntryIds: $entryID}) {
                edges {
                    node {
                        content {
                            handle
                        }
                        variants {
                            price
                            quantityAvailable
                            content {
                                title
                            }
                        }
                    }
                }
            }
        }      
        """
    )

    params = {"entryID": entry_id}
    result = client.execute(query, variable_values=params)    

    return result

def get_prod_by_handle(space_id, token, handle):
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
        query GetProduct($handle: [String!]) { 
            allProducts(filter: {handles: $handle}) {
                edges {
                    node {
                        content {
                            handle
                        }
                        variants {
                            price
                            quantityAvailable
                            content {
                                title
                            }
                        }
                    }
                }
            }
        }      
        """
    )

    params = {"handle": handle}
    result = client.execute(query, variable_values=params)    

    return result    

def get_all_collections(space_id, token, end_cursor=''):
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
        query GetAllCollections($endCursor: String!) { 
            allProductCollections(filter: {first: 500, after: $endCursor}) {
                pageInfo {
                    hasNextPage
                    endCursor
                }
                edges {
                    node {
                        nacelleEntryId
                        content {
                            handle
                        }
                    }
                }
            }
        }        
        """
    )


    params = {"endCursor": end_cursor}

    result = client.execute(query, variable_values=params)

    collections_list = []

    for entry in result['allProductCollections']['edges']:
        row = []

        entry_id = entry['node']['nacelleEntryId']
        handle = entry['node']['content']['handle']

        row.append(space_id)
        row.append(token)
        row.append(entry_id)
        row.append(handle)

        collections_list.append(row)
    
    # Pagination:
    has_next_page = result['allProductCollections']['pageInfo']['hasNextPage']
    end_cursor = result['allProductCollections']['pageInfo']['endCursor']

    while has_next_page:
        params = {"endCursor": end_cursor}

        result = client.execute(query, variable_values=params)

        for entry in result['allProductCollections']['edges']:
            row = []

            entry_id = entry['node']['nacelleEntryId']
            handle = entry['node']['content']['handle']

            row.append(space_id)
            row.append(token)
            row.append(entry_id)
            row.append(handle)

            collections_list.append(row)
        
        has_next_page = result['allProductCollections']['pageInfo']['hasNextPage']
        end_cursor = result['allProductCollections']['pageInfo']['endCursor']

    return collections_list

def get_collection_by_id(space_id, token, entry_id):
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
        query GetProduct($entryID: [String!]) { 
            allProductCollections(filter: {nacelleEntryIds: $entryID}) {
                edges {
                    node {
                        content {
                            handle
                        }
                        productConnection {
					        totalCount
				        }
                    }
                }
            }
        }      
        """
    )

    params = {"entryID": entry_id}
    result = client.execute(query, variable_values=params)    

    return result

def get_collection_by_handle(space_id, token, handle):
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
        query allProductCollections($handle: [String!]) { 
            allProductCollections(filter: {handles: $handle}) {
                edges {
                    node {
                        content {
                            handle
                        }
                        productConnection {
					        totalCount
				        }
                    }
                }
            }
        }      
        """
    )

    params = {"handle": handle}
    result = client.execute(query, variable_values=params)    

    return result    