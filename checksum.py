def calculate_checksum(file_path):
    try:
        with open(file_path, "rb") as file:
            data = file.read()
            checksum = sum(data) % 256  # Modulo 256 for 8-bit checksum
            return checksum
    except FileNotFoundError:
        print("File not found")
        return None

def verify_checksum(file_path, original_checksum):
    calculated_checksum = calculate_checksum(file_path)
    return calculated_checksum == original_checksum

# Example Usage:
file_path = "./testcsv.csv"  
original_checksum = calculate_checksum(file_path)
print(f"Original Checksum: {original_checksum}")

# To verify after transmission
if verify_checksum(file_path, original_checksum):
    print("File is intact (Checksum matches)")
else:
    print("File is corrupted (Checksum mismatch)")
