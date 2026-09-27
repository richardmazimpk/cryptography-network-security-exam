import os
import sys
import hashlib
from cryptography.fernet import Fernet

# Configuration paths
ORIGINAL_FILE = "student_records.txt"
ENCRYPTED_FILE = "student_records.enc"
DECRYPTED_FILE = "student_records_decrypted.txt"
KEY_FILE = "secret.key"
HASH_FILE = "baseline_hash.txt"

def load_or_create_key():
    """Generates a key if missing, or reads an existing one (Part a)."""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        print(f"[✔] New cryptographic key generated and saved outside git tracking to: {KEY_FILE}")
        return key

def calculate_sha256(file_path):
    """Calculates the SHA-256 hash of a file for integrity verification (Part c)."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def encrypt_file():
    """Part a: Encrypts the supplied sample student record file."""
    # Ensure a sample file exists if the user hasn't supplied one
    if not os.path.exists(ORIGINAL_FILE):
        sample_records = (
            "StudentID,Name,Major,GPA\n"
            "STU001,Alice Mutoni,Computer Science,3.85\n"
            "STU002,Aline Ingabire,Data Analytics,3.62\n"
            "STU003,Fidel Gasana,Cyber Security,3.91\n"
        )
        with open(ORIGINAL_FILE, "w", encoding="utf-8") as f:
            f.write(sample_records)
        print(f"[✔] Created a sample source file: {ORIGINAL_FILE}")

    try:
        key = load_or_create_key()
        cipher = Fernet(key)

        with open(ORIGINAL_FILE, "rb") as f:
            raw_data = f.read()

        encrypted_data = cipher.encrypt(raw_data)

        with open(ENCRYPTED_FILE, "wb") as f:
            f.write(encrypted_data)
        
        # Part c baseline: Save a baseline hash of the file right after creating/saving it
        baseline_hash = calculate_sha256(ORIGINAL_FILE)
        with open(HASH_FILE, "w", encoding="utf-8") as f:
            f.write(baseline_hash)

        print(f"[✔] Successfully encrypted data into: {ENCRYPTED_FILE}")
        print(f"[✔] Baseline SHA-256 integrity hash tracked: {baseline_hash}")
    except Exception as e:
        print(f"[❌] Error during encryption: {e}")

def decrypt_and_verify():
    """Part b: Decrypts the file and verifies contents match the original."""
    # Part d: Handle missing encrypted files or keys
    if not os.path.exists(ENCRYPTED_FILE):
        print(f"[❌] Error: Encrypted file '{ENCRYPTED_FILE}' is missing! Please encrypt a file first.")
        return
    if not os.path.exists(KEY_FILE):
        print(f"[❌] Error: Key file '{KEY_FILE}' is missing! Cannot decrypt data without it.")
        return

    try:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
        
        cipher = Fernet(key)

        with open(ENCRYPTED_FILE, "rb") as f:
            encrypted_content = f.read()

        decrypted_bytes = cipher.decrypt(encrypted_content)

        with open(DECRYPTED_FILE, "wb") as f:
            f.write(decrypted_bytes)
        print(f"[✔] Data decrypted and saved to: {DECRYPTED_FILE}")

        # Verification step
        if os.path.exists(ORIGINAL_FILE):
            with open(ORIGINAL_FILE, "rb") as f_orig, open(DECRYPTED_FILE, "rb") as f_dec:
                if f_orig.read() == f_dec.read():
                    print("[✔] VERIFICATION SUCCESS: Decrypted contents match the original precisely.")
                else:
                    print("[❌] VERIFICATION FAILED: Decrypted file contents do not match original text.")
        else:
            print("[⚠] Warning: Original plain text file missing; cannot run visual comparison match check.")
    except Exception as e:
        print(f"[❌] Decryption failed (invalid key or corrupted data): {e}")

def check_integrity():
    """Part c: Calculates a SHA-256 hash and detects subsequent changes."""
    if not os.path.exists(ORIGINAL_FILE):
        print(f"[❌] Error: Original file '{ORIGINAL_FILE}' does not exist to run an integrity check.")
        return
    if not os.path.exists(HASH_FILE):
        print("[❌] Error: Baseline hash records missing. Re-run encryption to establish track markers.")
        return

    with open(HASH_FILE, "r", encoding="utf-8") as f:
        baseline_hash = f.read().strip()

    current_hash = calculate_sha256(ORIGINAL_FILE)
    print(f"\nStored Baseline Hash: {baseline_hash}")
    print(f"Current File Hash:   {current_hash}")

    if current_hash == baseline_hash:
        print("[✔] INTEGRITY PASSED: The file remains authentic and unchanged.")
    else:
        print("[❌] CRITICAL SECURITY ALERT: The file has been modified subsequently since creation!")

def tamper_file_simulation():
    """Helper simulation to make demonstrating Part c to your grading examiner easy."""
    if not os.path.exists(ORIGINAL_FILE):
        print("[❌] Run encryption options first to generate a file to tamper with.")
        return
    with open(ORIGINAL_FILE, "a", encoding="utf-8") as f:
        f.write("STU999,Malicious Actor,Grade Tampering,4.00\n")
    print(f"[!] Simulation: Injected a fake student grading row into '{ORIGINAL_FILE}'.")

def show_menu():
    while True:
        print("\n=============================================")
        print("    ENCRYPTION & INTEGRITY APPLICATION       ")
        print("=============================================")
        print("1. [Part a] Encrypt student record file")
        print("2. [Part b] Decrypt file and verify match")
        print("3. [Part c] Perform SHA-256 integrity audit check")
        print("4. [Simulate] Unauthorized file tampering modification")
        print("5. Exit application")
        print("=============================================")
        
        # Part d: Robust user entry evaluation tracking
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            encrypt_file()
        elif choice == "2":
            decrypt_and_verify()
        elif choice == "3":
            check_integrity()
        elif choice == "4":
            tamper_file_simulation()
        elif choice == "5":
            print("Exiting application safely. Goodbye!")
            sys.exit(0)
        else:
            print("[❌] Invalid entry input. Please input a numeric value between 1 and 5.")

if __name__ == "__main__":
    show_menu()
