def crc32(file_path):
    try:
        with open(file_path, "rb") as file:
            data = file.read()
            # Import zlib for CRC calculation (CRC-32)
            import zlib
            crc_value = zlib.crc32(data) & 0xFFFFFFFF  # Ensure 32-bit
            return crc_value
    except FileNotFoundError:
        print("File not found")
        return None

def verify_crc(file_path, original_crc):
    calculated_crc = crc32(file_path)
    return calculated_crc == original_crc

# Example Usage:
file_path = "demo.jpg"
original_crc = crc32(file_path)
print(f"Original CRC: {original_crc}")

# To verify after transmission
if verify_crc(file_path, original_crc):
    print("File is intact (CRC matches)")
else:
    print("File is corrupted (CRC mismatch)")
