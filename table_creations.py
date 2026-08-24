from sqlfunc import createtable

# ==========================================
# DATABASE CREDENTIALS (UPDATE THESE)
# ==========================================
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Hussain13620_root"  # Put your MySQL password here
DB_NAME = "file_organizer_db"  # Make sure you created this database in MySQL first!

# ==========================================
# TABLE INITIALIZATION SCRIPT
# ==========================================
def initialize_database():
    print("Starting database initialization...")

    # 1. Users Table
    users_structure = {
        "user_id": "INT AUTO_INCREMENT PRIMARY KEY",
        "username": "VARCHAR(50) UNIQUE NOT NULL",
        "password": "VARCHAR(255) NOT NULL", 
        "created_at": "DATETIME DEFAULT CURRENT_TIMESTAMP"
    }
    createtable(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, "users", users_structure)

    # 2. File Logs Table (Tracks all moved/organized files)
    file_logs_structure = {
        "log_id": "INT AUTO_INCREMENT PRIMARY KEY",
        "user_id": "INT NOT NULL", 
        "file_name": "VARCHAR(255) NOT NULL",
        "file_extension": "VARCHAR(50)",
        "old_path": "TEXT NOT NULL",
        "new_path": "TEXT NOT NULL",
        "action_type": "VARCHAR(50) NOT NULL",
        "timestamp": "DATETIME DEFAULT CURRENT_TIMESTAMP",
        "FOREIGN KEY (user_id)": "REFERENCES users(user_id) ON DELETE CASCADE"
    }
    createtable(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, "file_logs", file_logs_structure)

    # 3. Categories Table (e.g., 'Images', 'Documents')
    categories_structure = {
        "category_id": "INT AUTO_INCREMENT PRIMARY KEY",
        "category_name": "VARCHAR(100) NOT NULL",
        "target_folder_name": "VARCHAR(255) NOT NULL"
    }
    createtable(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, "categories", categories_structure)

    # 4. Extension Rules Table (e.g., linking '.jpg' to 'Images' category)
    rules_structure = {
        "rule_id": "INT AUTO_INCREMENT PRIMARY KEY",
        "extension": "VARCHAR(50) NOT NULL UNIQUE",
        "category_id": "INT NOT NULL",
        "FOREIGN KEY (category_id)": "REFERENCES categories(category_id) ON DELETE CASCADE"
    }
    createtable(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, "extension_rules", rules_structure)

    print("All tables successfully initialized in the database!")

# ==========================================
# RUN THE SCRIPT
# ==========================================
if __name__ == "__main__":
    initialize_database()