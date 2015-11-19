import psycopg2

def insert_data():
    file_path = "reddit/subreddits.json"
    connection = psycopg2.connect(database="postgres", user="aleksander", password="12345abc")

    cursor = connection.cursor()
    print("Reading started")
    with open(file_path, "rb") as file:
        i = 1
        for r in file:
            cursor.execute("INSERT INTO subreddits (data) VALUES ('%s')" % (r))
            i = i + 1
            if  i % 10000 == 0:
                connection.commit()
                print("Inserted " + str(i) + " subreddits.")
        print("Inserting finished.")
    connection.commit()
    cursor.close()
    connection.close()

insert_data()