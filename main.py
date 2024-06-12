import database, month, invoice
import json

db_name = 'test.db'
user_data = [('France', 50), ('Jolly', 45), ('Grace', 43), ('Elena', 47)]
room_data = [('Mercury', 'Good for two person'), ('Mars', 'With Air-condition'), ('Venus', 'With TV')]
room_data_additional = [('Pluto', 'With Freezer'), ('Saturn', 'With Toilet'), ('Jupiter', 'With Kitchen')]
room_rate = [('Standard', 500), ('Deluxe', 1000), ('Suite', 3000)]
room_rate_assignment = [('Mercury', 'Standard'), ('Mars', 'Deluxe'), ('Venus', 'Suite'), ('Jupiter', 'Suite')]
calendar_data = [(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]

if __name__ == "__main__":
    
    # database.create_connection(db_name)
    # database.create_user_table(db_name)
    # database.insert_user(db_name, user_data)
    # print(database.read_user(db_name))
    # # database.delete_user(db_name, 'Elena')
    # print(database.read_user(db_name))
    # database.update_user_age(db_name, 'Jolly', 44)
    # print(database.read_user(db_name))
    # database.create_room_table(db_name)
    # database.insert_room(db_name, room_data)
    # print(database.read_room(db_name))
    # database.update_room_user(db_name, 'Mercury', 2)
    # database.update_room_user(db_name, 'Venus', 3)
    # database.update_room_user(db_name, 'Saturn', 1)
    # database.update_room_user(db_name, 'Jupiter', 4)
    # print(database.read_room_user(db_name, 'Mercury'))
    # print(database.read_room_user(db_name, 'Venus'))
    # print(database.read_room_by_room_name(db_name, 'Mars'))
    # database.insert_room(db_name, room_data_additional)
    # print(database.read_room(db_name))
    # database.create_rate_table(db_name)
    # database.insert_rate(db_name, room_rate)
    # database.update_room_type(db_name, 'Saturn', 'Suite')
    # database.update_room_type(db_name, 'Pluto', 'Standard')
    # print(database.read_room_rate_by_name(db_name, 'Venus'))
    # print(database.read_room_rate_by_name(db_name, 'Mercury'))
    # database.update_room_rate_by_variable(db_name, room_rate_assignment)
    # month.create_calendar_table(db_name)
    # month.insert_month(db_name, calendar_data)
    # invoice.create_invoice_table(db_name)
    # print(invoice.create_invoice_by_room(db_name, 'Mercury'))
    # print(invoice.create_invoice_by_room(db_name, 'Venus'))
    # print(invoice.query_invoice_all(db_name))
    # invoice.create_invoice_all_by_month_test(db_name, 'January', 2024)
    # invoice.create_invoice_all_by_month_test(db_name, 'February', 2024)
    # invoice.create_invoice_all_by_month_test(db_name, 'March', 2024)
    # print(json.dumps(invoice.query_invoice_all(db_name), indent=1))
    # print(json.dumps(invoice.query_invoice_all_with_date(db_name), indent=1))
    # print(invoice.query_invoice_all_with_date(db_name))
    # print(invoice.query_invoice_by_user(db_name, 'Elena'))
    print(json.dumps(invoice.query_invoice_by_user_with_date(db_name, 'Jolly', 'March', 2024), indent=1))