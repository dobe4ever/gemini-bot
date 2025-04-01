# db.py

import os
import psycopg2

# Database constants
DATABASE_URL = os.environ['DATABASE_URL']

# Create database connection
def create_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn, conn.cursor()

# Initialize database
def init_database():
    conn, cur = create_connection()
    
    # cur.execute("DROP TABLE IF EXISTS users;")

    # Create users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id BIGINT PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

    # Create messages table with user_id foreign key
    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            user_id BIGINT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    cur.close()
    conn.close()
    return True


def add_user(user):
    conn, cur = create_connection()
    cur.execute("""
        INSERT INTO users (user_id, username, first_name, last_name)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (user_id) DO UPDATE SET
            username = EXCLUDED.username,
            first_name = EXCLUDED.first_name,
            last_name = EXCLUDED.last_name
    """, (user.id, user.username, user.first_name, user.last_name))
    
    conn.commit()
    cur.close()
    conn.close()
    return user

# Message
def add_message(user_id, role, content):
    conn, cur = create_connection()
    cur.execute(
        "INSERT INTO messages (user_id, role, content) VALUES (%s, %s, %s)",
        (user_id, role, content)
    )
    conn.commit()
    cur.close()
    conn.close()
    return True

def get_messages(user_id, limit=25):
    conn, cur = create_connection()
    cur.execute(
        "SELECT role, content FROM messages WHERE user_id = %s ORDER BY id ASC LIMIT %s",
        (user_id, limit)
    )
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result
