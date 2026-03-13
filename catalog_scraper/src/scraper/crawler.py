import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_page(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def get_product_links(base_website):
    print("Scouting for categories, subcategories, and paginated links...")
    products_info = []
    
    main_page = get_page(base_website)
    # The website's sidebar menu holds the categories
    sidebar = main_page.find(id='side-menu')
    if not sidebar:
        return products_info
        
    category_links = sidebar.find_all('a', class_='category-link')
    
    for cat_link in category_links:
        cat_name = cat_link.text.strip()
        cat_url = urljoin(base_website, cat_link.get('href'))
        cat_page = get_page(cat_url)
        
        # Find subcategories inside the specific category
        sub_menu = cat_page.find(id='side-menu')
        sub_links = sub_menu.find_all('a', class_='subcategory-link')
        
        for sub_link in sub_links:
            sub_name = sub_link.text.strip()
            current_page_url = urljoin(base_website, sub_link.get('href'))
            
            while current_page_url:
                page_data = get_page(current_page_url)
                items = page_data.find_all('a', class_='title')
                
                for item in items:
                    products_info.append({
                        'category': cat_name,
                        'subcategory': sub_name,
                        'product url': urljoin(base_website, item.get('href'))
                    })
                
                # Check for pagination (Next button)
                next_button = page_data.find('a', rel='next')
                if next_button:
                    current_page_url = urljoin(base_website, next_button.get('href'))
                else:
                    current_page_url = None
                    
    return products_info