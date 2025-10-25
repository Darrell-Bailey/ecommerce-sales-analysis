# Ecommerce Sales Analysis

## Data Acquisition
- **Source**:
- **License**:
- **Description**:
- **Key Files and Schemas**:

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
