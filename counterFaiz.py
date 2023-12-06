import redis
import random

# Membuat koneksi ke Redis server yang berjalan dalam Docker
r = redis.Redis(host='localhost', port=6379, db=0)

# Key untuk data pengunjung
visitors_key = 'website_visitors'
# Key untuk counter
counter_key = 'program_counter'

# Fungsi untuk menampilkan menu
def display_menu():
    print("Choose an option:")
    print("1. Create a new visitor")
    print("2. Read visitor info")
    print("3. Update visitor page views")
    print("4. Delete a visitor")
    print("5. Show program counter")
    print("6. Exit")

# Fungsi untuk membuat data pengunjung baru
def create_visitor():
    visitor_data = generate_visitor_data()
    user_id = visitor_data['user_id']
    username = visitor_data['username']
    page_views = visitor_data['page_views']
    r.hset(visitors_key, user_id, f'Username: {username}, Page Views: {page_views}')
    print(f"Visitor (User {user_id}) created.")

# Fungsi untuk membaca data pengunjung
def read_visitor(user_id):
    visitor_info = r.hget(visitors_key, user_id)
    if visitor_info:
        print(f"Visitor Info (User {user_id}): {visitor_info.decode('utf-8')}")
    else:
        print(f"Visitor Info (User {user_id}) not found.")

# Fungsi untuk mengupdate data pengunjung
def update_visitor(user_id, new_page_views):
    r.hset(visitors_key, user_id, f'Username: user_{user_id}, Page Views: {new_page_views}')
    print(f"Visitor (User {user_id}) updated.")

# Fungsi untuk menghapus data pengunjung
def delete_visitor(user_id):
    r.hdel(visitors_key, user_id)
    print(f"Visitor (User {user_id}) deleted.")

# Fungsi untuk menampilkan program counter
def show_program_counter():
    counter_value = r.get(counter_key)
    if counter_value:
        print(f"Program Counter: {counter_value.decode('utf-8')}")
    else:
        print("Program Counter not found.")

# Fungsi untuk menghasilkan data pengunjung acak
def generate_visitor_data():
    user_id = random.randint(1, 1000)
    username = f'pengunjung_{user_id}'
    return {
        'user_id': user_id,
        'username': username,
        'page_views': random.randint(1, 10)
    }

# Main program
while True:
    display_menu()
    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        create_visitor()
    elif choice == '2':
        user_id = input("Enter user ID to read: ")
        read_visitor(int(user_id))
    elif choice == '3':
        user_id = input("Enter user ID to update: ")
        new_page_views = input("Enter new page views count: ")
        update_visitor(int(user_id), int(new_page_views))
    elif choice == '4':
        user_id = input("Enter user ID to delete: ")
        delete_visitor(int(user_id))
    elif choice == '5':
        show_program_counter()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please choose a valid option.")

# Increment program counter
current_counter = r.incr(counter_key)

# Menutup koneksi Redis
r.close()
