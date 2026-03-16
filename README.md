\# Catalog Scraper Mini Project

## Project Purpose
This project is a comprehensive web scraper designed to navigate a structured static e-commerce site. It is built to fulfill the requirements of Quiz #1 for the "Tools & Tech. for DS" course at the University of Central Punjab. The scraper traverses categories and subcategories, follows paginated listing pages, and visits individual product detail pages to extract and clean data.

## Tech Stack & Tools
* **Python**: The core programming language used.
* **uv**: Used for project initialization, dependency management, and execution.
* **Beautiful Soup 4**: Used for parsing and extracting data from HTML.
* **Requests**: Used for handling HTTP page requests.
* **Git/GitHub**: Used for version control and workflow management.

## Installation & Setup
This project is managed entirely with `uv`. To set up the project:
1. Ensure `uv` is installed on your system.
2. Initialize the environment and install dependencies:
   ```bash
   uv sync
