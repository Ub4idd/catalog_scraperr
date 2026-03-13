import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_product_details(info_dict):
    # 1. Take the exact URL OUT of the backpack
    product_url = info_dict['product url']
    
    # 2. Now it is safe to go to the internet!
    response = requests.get(product_url)
    page = BeautifulSoup(response.text, 'html.parser')
    
    # 3. Set up the exact 7 columns you requested
    product_data = {
        'category': info_dict['category'],
        'subcategory': info_dict['subcategory'],
        'product title': 'No Title Found',
        'price': 0.0,
        'description': 'Missing Description',
        'image url': 'No Image Found',
        'product url': product_url
    }
    
    # 4. Find all the details on the page
    title = page.find(class_='title')
    if title:
        product_data['product title'] = title.text.strip()
        
    price = page.find(class_='price')
    if price:
        try:
            clean_price = price.text.strip().replace('$', '').replace(',', '')
            product_data['price'] = float(clean_price)
        except ValueError:
            pass
            
    desc = page.find(class_='description')
    if desc:
        product_data['description'] = desc.text.strip()
        
    img_tag = page.find('img', class_='img-responsive')
    if img_tag and img_tag.get('src'):
        product_data['image url'] = urljoin(product_url, img_tag.get('src'))
        
    return product_data