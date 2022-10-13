import csv
import sys
import json
import hashlib
import nacelle 
from tqdm import tqdm

selected_option = input('Scan products or collections (P/C): ')
selected_option = selected_option.lower()

if (selected_option != 'p') and (selected_option != 'c'):
    print("Invalid selection")
    sys.exit()

# --------------------------------------
# Get all PRODUCTS in a space
# --------------------------------------

print('Step 1: Get a list of all products')

prods_list = []

with open('./data/spaces.csv', 'r') as spaces_file:
    reader = csv.reader(spaces_file)

    for row in reader:
        space_id = row[0]
        token = row[1]
        
        if selected_option == 'p':
            prods = nacelle.get_all_products(space_id, token)
        else:
            prods = nacelle.get_all_collections(space_id, token)
    
        for p in prods:
            prods_list.append(p)

# --------------------------------------
# Get a product's hash
# --------------------------------------

print('Step 2: Getting API response for each product')

n = 0
for row in tqdm(prods_list):
    # nacelle entry id
    if selected_option == 'p':
        entry_id_result = nacelle.get_prod_by_id(space_id=row[0], token=row[1], entry_id=row[2])
    else:
        entry_id_result = nacelle.get_collection_by_id(space_id=row[0], token=row[1], entry_id=row[2])

    entry_id_json = json.dumps(entry_id_result)
    entry_id_hash = hashlib.md5(entry_id_json.encode("utf-8")).hexdigest()

    # handle
    if selected_option == 'p':
        handle_result = nacelle.get_prod_by_handle(space_id=row[0], token=row[1], handle=row[3])
    else:
        handle_result = nacelle.get_collection_by_handle(space_id=row[0], token=row[1], handle=row[3])

    handle_json = json.dumps(handle_result)
    handle_hash = hashlib.md5(handle_json.encode("utf-8")).hexdigest()

    # append to prod_list:
    prods_list[n].append(entry_id_hash)
    prods_list[n].append(handle_hash)

    # compare hashes:
    if entry_id_hash == handle_hash:
        prods_list[n].append(0) # hashes match
    else:
        prods_list[n].append(1) # we've got a problem

    n+=1
     
# --------------------------------------
# Save CSV
# --------------------------------------

print('Step 3: Saving to output.csv')

with open('./data/output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(prods_list)