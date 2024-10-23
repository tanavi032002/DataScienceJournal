import json
import pymongo

def read_json(file_path):
    """Read JSON data from a file."""
    try:
        with open(file_path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file {file_path}.")
        return {}

def create_city_to_country_map():
    """Generate a mapping of cities to their respective countries."""
    return {
        "newyork": "usa",
        "dallas": "usa",
        "beijing": "china",
        "colombo": "sri_lanka",
        "hongkong": "china",
        "kandy": "sri_lanka",
        "wuhan": "china",
        "chicago": "usa"
    }

def mongo_connection(database, collection):
    """Connect to a specified MongoDB database and collection."""
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client[database]
        return db[collection]
    except pymongo.errors.ConnectionError:
        print(f"Error: Unable to connect to MongoDB at {database}/{collection}.")
        return None

def compute_total_cost(ticket_info, visa_fees, city_country_map):
    """Compute the total cost associated with a ticket."""
    last_location = ticket_info['visa_stamped_location'][-1]
    associated_country = city_country_map.get(last_location)
    if associated_country:
        visa_fee = visa_fees.get(associated_country, 0)  # Default to 0 if no fee found
        return visa_fee + int(ticket_info['ticket_price'])
    return None

def display_passenger_info(ticket_list, visa_fees, city_country_map):
    """Display the information for each passenger along with total cost."""
    print('Passenger Information:')
    for ticket_info in ticket_list:
        total_cost = compute_total_cost(ticket_info, visa_fees, city_country_map)
        if total_cost is not None:
            print(f"Passenger ID {ticket_info['ticket_id']}: Name: {ticket_info['passenger_name']}, Total Cost: {total_cost}")
        else:
            print(f"Passenger ID {ticket_info['ticket_id']}: Name: {ticket_info['passenger_name']}, Total Cost: Not available")

def execute():
    json_data = read_json("data.json")
    if not json_data:
        return  # Exit if JSON data could not be read
    city_country_map = create_city_to_country_map()
    ticket_collection = mongo_connection("Passenger_Management_System", "tickets")

    if ticket_collection is not None:
        ticket_list = list(ticket_collection.find({}))
        display_passenger_info(ticket_list, json_data.get('visa_rates', {}), city_country_map)

if __name__ == "__main__":
    execute()
