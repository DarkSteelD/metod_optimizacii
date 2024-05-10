from faker import Faker
import psycopg2
import random
from datetime import datetime, timedelta

# Initialize Faker with Russian localization
fake = Faker('ru_RU')

# Database connection
conn = psycopg2.connect("dbname=ShopTest user=postgres password=Goklk666")
cur = conn.cursor()

# Generate data for 'client'
for _ in range(20):
    name = fake.name()[:50]  # Truncate to 50 characters
    address = fake.address()[:50]  # Truncate to 50 characters
    phone = fake.phone_number()[:50]  # Truncate to 50 characters
    cur.execute("INSERT INTO public.client (name, address, phone) VALUES (%s, %s, %s)", (name, address, phone))


# Generate data for 'product'
for _ in range(20):
    name = fake.word()
    ed = 'шт.'
    selling_price = random.randint(100, 1000)  # Random price between 100 and 1000
    expiration_date = fake.date_between(start_date='+1y', end_date='+5y')
    cur.execute("INSERT INTO public.product (name, ed, selling_price, expiration_date) VALUES (%s, %s, %s, %s)", (name, ed, selling_price, expiration_date))

# Generate data for 'futura', 'futurainfo', 'discardedproducts', 'payment'
cur.execute("SELECT id FROM public.client")
client_ids = cur.fetchall()

cur.execute("SELECT id FROM public.product")
product_ids = cur.fetchall()

for _ in range(20):
    id_client = random.choice(client_ids)[0]
    date = fake.date_between(start_date='-1y', end_date='today')
    totalsum = random.randint(500, 5000)
    status = random.choice([0, 1])  # Status as 0 or 1

    # Insert into futura and retrieve the generated id
    cur.execute("INSERT INTO public.futura (id_client, data, totalsum, status) VALUES (%s, %s, %s, %s) RETURNING id", (id_client, date, totalsum, status))
    futura_id = cur.fetchone()[0]  # Fetch the returned id

    # Insert into futurainfo
    id_product = random.choice(product_ids)[0]
    quantity = random.randint(1, 10)
    price = random.randint(100, 500)
    cur.execute("INSERT INTO public.futurainfo (id_futura, id_product, quantity, price) VALUES (%s, %s, %s, %s)", (futura_id, id_product, quantity, price))

    # Payment
    date_pay = date + timedelta(days=random.randint(1, 30))
    paynum = random.randint(100, totalsum)
    cur.execute("INSERT INTO public.payment (id_futura, date_pay, paynum) VALUES (%s, %s, %s)", (futura_id, date_pay, paynum))
    
    # Discarded products
    discarded_date = date - timedelta(days=random.randint(1, 365))
    reason = random.choice(['истек срок годности', 'повреждение'])
    cur.execute("INSERT INTO public.discardedproducts (id_product, discarded_date, quantity, reason) VALUES (%s, %s, %s, %s)", (id_product, discarded_date, quantity, reason))

# Commit transactions
conn.commit()

# Close connections
cur.close()
conn.close()
