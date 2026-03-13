# Catalog Scraper Mini Project

## Project Purpose
This project is a web scraper built to navigate a static e-commerce site, extract product details across multiple categories and paginated pages, and generate structured datasets.

## Setup and Run Instructions
1. This project uses `uv` for dependency management. 
2. To install dependencies, run: `uv sync`
3. To run the scraper, execute: `uv run python src/main.py`

## Branch Workflow
I followed the required Git workflow:
- `main` branch for final, stable code.
- `dev` branch for ongoing development.
- Feature branches (`feature/catalog-navigation`, `feature/product-details`) for adding new scraping capabilities.
- Fix branches for resolving URL issues and duplicates.

## Assumptions & Limitations
- Assumes the website structure (`class` names like `title` and `price`) does not change.
- Limit: Only scrapes the static test site provided in the instructions.