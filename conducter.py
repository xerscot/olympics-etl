from os import listdir
import scout
import load

file_list = []
# I would like this list of files to be processed for analytics later
for f in listdir("raw"):
    file_location = "raw/" + f
    file_list.append(file_location)

# We can use this file to construct the SQL Database with.
file_with_highest = ""

# Working with the worst case here below so that I maximise the fields of data I can capture
# This way I won't have to dynamically update the DB structure if someone had one or more fields of data
def scout_ahead():
    global file_with_highest
    highest_number = 0
    count = 1 
    for f in file_list:
        msg = "Processing file {0} of {1}".format(count, len(file_list))
        update_user(msg)
        obj = scout.Scout(f)
        obj.get_number_of_columns()
        if highest_number < obj._column_number:
            highest_number = obj._column_number
            file_with_highest = f
        count = count + 1
    print("File with highest number: " + file_with_highest)
    print("File has {0} columns".format(highest_number))

def database_check():
    print("Initialising and seeding database.")
    dc = load.Load(file_with_highest)
    dc.first_database_check()

def process_remaining_rows():    
    print("Processing all files now.")
    count = 2
    for f in file_list:
        if f == file_with_highest:
            continue
        msg = "Processing file {0} of {1}".format(count, len(file_list))
        update_user(msg)
        ll = load.Load(f)
        ll.insert_competitor_data()

def update_user(msg):
    print(msg, end='\r')

def main():
    scout_ahead()
    database_check()
    process_remaining_rows()
    print("All done! Good bye.")

if __name__ == "__main__":
    main()