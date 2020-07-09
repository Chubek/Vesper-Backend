import datetime

prayerSchema = {
    "prayer_name": "Amy's Graduation",
    "prayer_dates": [datetime.datetime.now()]
}


def create_prayer_document(database):
    return database.insert_one(prayerSchema).inserted_id


