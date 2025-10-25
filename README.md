# Ecommerce Sales Analysis

## Data Acquisition
- **Source**: Brazilian E-Commerce Public Dataset by Olist on Kaggle (https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- **License**: ODBL (Open Database License)
- **Description**: Anonymized data from 2016-2018 Brazilian e-commerce (100k+ orders). 9 CSV files (~130 MB total).
- **Key Files and Schemas**:
  | File | Rows/Cols | Primary Key | Foreign Keys |
  |------|-----------|--------------|--------------|
  |olist_customers_dataset.csv|99441/5|customer_id|None|
  |olist_geolocation_dataset.csv|1000163/5|geolocation_zip_code_prefix|None|
  |olist_orders_dataset.csv|99441/8|order_id|customer_id|
  |olist_order_items_dataset.csv|112650/7|order_item_id|order_id, product_id, seller_id|
  |olist_order_payments_dataset.csv|103886/5|order_id|order_id|
  |olist_order_reviews_dataset.csv|99224/7|review_id|order_id|
  |olist_products_dataset.csv|32951/9|product_id|None|
  |olist_sellers_dataset.csv|3095/4|seller_id|None|
- **Initial Verification Observations**:
- **Download Instructions**:
  1. Install: `pip install kaggle`
  2. Setup API key (from Kaggle account(.
  3. Run: `kaggle datasets download -d olistbr/brazilian-ecommerce -p data --unzip`
- **Sample Usage** (Python join for sales view):
  ```python
  import pandas as pd
  orders = pd.read_csv('data/olist_orders_dataset.csv')
  items = pd.read_csv('data/olist_order_items_dataset.csv')
  payments = pd.read_csv('data/olist_order_payments_dataset.csv')
  sales_df = orders.merge(items, on='order_id').merge(payments, on='order_id')
  print(sales_df.head())
