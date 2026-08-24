from sqlfunc import get_db_connection

# ==========================================
# DATABASE CREDENTIALS (UPDATE THESE)
# ==========================================
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Hussain13620_root"  # Update with your MySQL password
DB_NAME = "file_organizer_db"

def get_user_by_username(username):
    """Fetches user details for login validation."""
    connection = get_db_connection(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    # dictionary=True ensures we get data back as a dict, which FastAPI automatically turns into JSON
    cursor = connection.cursor(dictionary=True) 
    
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    
    cursor.close()
    connection.close()
    return user

def fetch_logs_by_filename(user_id, search_term):
    """Searches for moved files by their name (partial match supported)."""
    connection = get_db_connection(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    cursor = connection.cursor(dictionary=True)
    
    # The % wildcards allow for partial matching (e.g., searching "report" finds "q1_report.pdf")
    query = "SELECT * FROM file_logs WHERE user_id = %s AND file_name LIKE %s ORDER BY timestamp DESC"
    search_pattern = f"%{search_term}%"
    
    cursor.execute(query, (user_id, search_pattern))
    results = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return results

def fetch_logs_by_extension(user_id, extension):
    """Fetches all files moved that have a specific extension (e.g., '.pdf')."""
    connection = get_db_connection(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    cursor = connection.cursor(dictionary=True)
    
    query = "SELECT * FROM file_logs WHERE user_id = %s AND file_extension = %s ORDER BY timestamp DESC"
    cursor.execute(query, (user_id, extension))
    results = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return results

def fetch_logs_by_folder(user_id, folder_path):
    """Finds all files moved out of OR into a specific folder path."""
    connection = get_db_connection(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    cursor = connection.cursor(dictionary=True)
    
    query = """
        SELECT * FROM file_logs 
        WHERE user_id = %s AND (old_path LIKE %s OR new_path LIKE %s)
        ORDER BY timestamp DESC
    """
    search_pattern = f"%{folder_path}%"
    
    cursor.execute(query, (user_id, search_pattern, search_pattern))
    results = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return results