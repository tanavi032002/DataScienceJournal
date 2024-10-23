import pymysql
from pymongo import MongoClient
from pymongo.errors import BulkWriteError
from bson import ObjectId

# MySQL database connection details
mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = 'root'
mysql_db = 'Anup'

# MongoDB database connection details
mongo_host = 'localhost'
mongo_port = 27017
mongo_db = 'ANup'

# Connect to MySQL database
mysql_conn = pymysql.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    db=mysql_db
)

# Connect to MongoDB
mongo_client = MongoClient(mongo_host, mongo_port)
mongo_database = mongo_client[mongo_db]

try:
    with mysql_conn.cursor(pymysql.cursors.DictCursor) as cursor:
        # Fetch data from MySQL category table
        cursor.execute("SELECT * FROM category")
        categories = cursor.fetchall()

        print("Categories from MySQL:", categories)  # Debug print

        # Check for missing keys in categories
        for category in categories:
            if 'category_id' not in category or 'category_name' not in category:
                print("Missing keys in category:", category)

        # Fetch data from MySQL product table
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()

        print("Products from MySQL:", products)  # Debug print

        # Check for missing keys in products
        for product in products:
            if 'product_id' not in product or 'product_name' not in product or 'category_id' not in product:
                print("Missing keys in product:", product)

        # Create a mapping from category_id to list of products
        category_products_mapping = {}
        for product in products:
            category_id = product['category_id']
            product_info = {
                "product_id": product['product_id'],
                "product_name": product['product_name']
            }
            category_products_mapping.setdefault(category_id, []).append(product_info)

        print("Category Products Mapping:", category_products_mapping)

        # Prepare category documents with embedded products
        categories_with_products = []
        for category in categories:
            category_id = category['category_id']
            products_list = category_products_mapping.get(category_id, [])
            category_document = {
                "_id": ObjectId(),  # MongoDB will auto-generate ObjectId for _id
                "category_id": category['category_id'],
                "category_name": category['category_name'],
                "products": products_list
            }
            categories_with_products.append(category_document)

        # Clear existing MongoDB category collection to avoid duplicates
        category_collection = mongo_database['category']
        category_collection.delete_many({})  # Deletes all documents in the collection

        try:
            # Insert data into MongoDB category collection
            category_collection.insert_many(categories_with_products, ordered=False)
        except BulkWriteError as bwe:
            print("Bulk Write Error:", bwe.details)

        # Display migrated data
        print("\n=== Categories and Products Migrated to MongoDB ===\n")
        for category in categories_with_products:
            print(f"Category ID: {category['category_id']} | Name: {category['category_name']}")
            for product in category['products']:
                print(f"    Product ID: {product['product_id']} | Name: {product['product_name']}")

finally:
    mysql_conn.close()
    mongo_client.close()

print("\nData migration from MySQL to MongoDB completed successfully.\n")
