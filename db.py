import os
import psycopg2
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Database constants - Using direct access as requested
try:
    # This will RAISE KeyError immediately if not set in Railway env vars
    DATABASE_URL = os.environ['DATABASE_URL']
    logger.info("DATABASE_URL retrieved from environment.")
except KeyError:
    logger.critical("FATAL: DATABASE_URL environment variable not set!")
    # Optionally raise it again to ensure the app stops if this module is imported
    raise ValueError("DATABASE_URL is mandatory and was not found in environment variables.")

# Create database connection
def create_connection():
    """Creates and returns a database connection and cursor."""
    # DATABASE_URL existence is checked at module load time now
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        # Removed the redundant info log from here, it's noisy on every call
        # logger.info("Database connection established successfully.")
        return conn, cursor
    except psycopg2.OperationalError as e:
        logger.error(f"Database connection failed: {e}")
        return None, None
    except Exception as e:
        logger.error(f"An unexpected error occurred during DB connection: {e}")
        return None, None

def close_connection(conn, cursor):
    """Closes the database cursor and connection."""
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    # logger.info("Database connection closed.") # Can be noisy

def test_db_connection():
    """Tests the database connection by executing a simple query."""
    logger.info("Attempting database connection test...")
    conn, cursor = create_connection()
    if conn and cursor:
        try:
            cursor.execute("SELECT 1;") # Simple query to test
            logger.info("Database test query executed successfully.")
            close_connection(conn, cursor) # Close connection after successful test
            return True
        except Exception as e:
            logger.error(f"Database test query failed: {e}")
            close_connection(conn, cursor) # Still close connection on failure
            return False
    else:
        # create_connection already logged the error
        logger.error("Database test connection failed: Could not establish connection.")
        return False
        