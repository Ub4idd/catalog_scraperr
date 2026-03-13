import csv

def save_to_csv(data_list, filename):
    if not data_list:
        return
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data_list[0].keys())
        writer.writeheader()
        writer.writerows(data_list)
    print(f"Successfully saved {filename}")

def save_summary(data_list, duplicate_count, filename):
    # Group the data by Category and Subcategory
    summary_groups = {}
    
    for row in data_list:
        key = (row['category'], row['subcategory'])
        if key not in summary_groups:
            summary_groups[key] = {
                'category': row['category'],
                'subcategory': row['subcategory'],
                'prices': [],
                'missing_desc': 0
            }
        
        summary_groups[key]['prices'].append(row['price'])
        if row['description'] == 'Missing Description' or not row['description'].strip():
            summary_groups[key]['missing_desc'] += 1

    # Calculate the math for each subcategory group
    summary_rows = []
    for key, stats in summary_groups.items():
        prices = stats['prices']
        avg_p = sum(prices) / len(prices) if prices else 0
        min_p = min(prices) if prices else 0
        max_p = max(prices) if prices else 0
        
        summary_rows.append({
            'category': stats['category'],
            'subcategory': stats['subcategory'],
            'avg price': round(avg_p, 2),
            'lowest price': min_p,
            'highest price': max_p,
            'missing description': stats['missing_desc'],
            'duplications removed': duplicate_count # Applies the global duplicate count
        })
        
    if summary_rows:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=summary_rows[0].keys())
            writer.writeheader()
            writer.writerows(summary_rows)
        print(f"Successfully saved {filename}")