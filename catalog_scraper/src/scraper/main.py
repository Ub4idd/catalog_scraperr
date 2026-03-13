from scraper.crawler import get_product_links
from scraper.parsers import scrape_product_details
from scraper.utils import remove_duplicates
from scraper.exporters import save_to_csv, save_summary

def run_project():
    print("Starting the Perfect Scraper Project...")
    base_website = "https://webscraper.io/test-sites/e-commerce/static"
    
    # 1. Get raw links with categories attached
    raw_products_info = get_product_links(base_website)
    
    # 2. Remove duplicates and get the exact count
    unique_products_info, duplicate_count = remove_duplicates(raw_products_info)
    print(f"Found {len(unique_products_info)} unique products. Removed {duplicate_count} duplicates.")
    
    # 3. Read the details for every single product
    all_products_data = []
    for info in unique_products_info:
        print(f"Reading details for: {info['product url']}")
        data = scrape_product_details(info)
        all_products_data.append(data)
        
    # 4. Save both required CSV files
    save_to_csv(all_products_data, "data/products.csv")
    save_summary(all_products_data, duplicate_count, "data/category_summary.csv")
    print("Project finished 100% successfully!")

if __name__ == "__main__":
    run_project()