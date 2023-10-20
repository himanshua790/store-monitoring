import csv
from app import db
from app.models import Store
from datetime import datetime


def import_csv_to_db(csv_file):
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                store_id = row['store_id']
                status = row['status']
                timestamp_utc = datetime.strptime(
                    row['timestamp_utc'], '%Y-%m-%d %H:%M:%S.%f UTC')

                store = Store(store_id=store_id, status=status,
                              timestamp_utc=timestamp_utc)
                db.session.add(store)
            db.session.commit()
        print("Data imported successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.session.rollback()


if __name__ == '__main__':
    import_csv_to_db('store_data.csv')
