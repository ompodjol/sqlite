import database

db_name = 'test.db'
user_data = [('France', 50), ('Jolly', 45), ('Grace', 43), ('Elena', 47)]
room_data = [('Mercury', 'Small size room'), ('Mars', 'Medium size room'), ('Venus', 'Large size room')]

if __name__ == "__main__":
    
    # database.create_connection(db_name)
    # database.create_user_table(db_name)
    # database.insert_user(db_name, user_data)
    # print(database.read_user(db_name))
    # database.delete_user(db_name, 'Elena')
    # print(database.read_user(db_name))
    # database.update_user_age(db_name, 'Jolly', 44)
    # print(database.read_user(db_name))
    # database.create_room_table(db_name)
    # database.insert_room(db_name, room_data)
    # print(database.read_room(db_name))
    # database.update_room_user(db_name, 'Mercury', 2)
    # database.update_room_user(db_name, 'Venus', 3)
    # print(database.read_room_user(db_name, 'Mercury'))
    # print(database.read_room_user(db_name, 'Venus'))
    print(database.read_room_by_room_name(db_name, 'Mars'))
