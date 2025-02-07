import qrcode
import pickle
import os
import sys

# Define the file for storing QR code mappings
PICKLE_FILE = "qr_code_database.pkl"

def load_qr_database():
    """
    Load the QR code database from the pickle file. 
    If the file doesn't exist, return an empty dictionary.
    """
    if os.path.exists(PICKLE_FILE):
        with open(PICKLE_FILE, "rb") as file:
            return pickle.load(file)
    return {}

def save_qr_database(database):
    """
    Save the QR code database to the pickle file.
    """
    with open(PICKLE_FILE, "wb") as file:
        pickle.dump(database, file)

def generate_qr_code(data, filename, database):
    """
    Generate a QR Code and update the database.
    
    :param data: The information to encode in the QR code.
    :param filename: The filename to save the QR code image as.
    :param database: The current database mapping data to filenames.
    """
    if data in database:
        print(f"Data already processed. Existing QR Code: {database[data]}")
        return
    
    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image of the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to the specified file
        img.save(filename)
        print(f"QR Code generated and saved as {filename}")

        # Update the database
        database[data] = filename
        save_qr_database(database)
    except Exception as e:
        print(f"An error occurred: {e}")

def display_database(database):
    """
    Display all previously processed QR codes from the database.
    """
    if not database:
        print("No QR codes have been processed yet.")
    else:
        print("Previously processed QR codes:")
        for data, filename in database.items():
            print(f"Data: {data} -> File: {filename}")

if __name__ == "__main__":
    # Load the QR code database
    qr_database = load_qr_database()

    # Check command-line arguments
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <data> <filename>")
        display_database(qr_database)
    else:
        # Extract data and filename from command-line arguments
        input_data = sys.argv[1]
        output_filename = sys.argv[2]

        # Generate the QR code and update the database
        generate_qr_code(input_data, output_filename, qr_database)
