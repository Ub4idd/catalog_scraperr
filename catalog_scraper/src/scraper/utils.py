def remove_duplicates(items_list):
    unique_items = {}
    duplicates_removed = 0
    
    for item in items_list:
        url = item['product url']
        if url not in unique_items:
            unique_items[url] = item
        else:
            duplicates_removed += 1
            
    # We return both the cleaned list AND the count of duplicates removed
    return list(unique_items.values()), duplicates_removed