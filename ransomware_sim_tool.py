# ransomware_sim_tool.py
import os
from cryptography.fernet import Fernet

KEY_FILE = "key.key"
TARGET_FOLDER = "test_folder"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_key():
    if not os.path.exists(KEY_FILE):
        print("[-] Key file not found. You must encrypt first.")
        return None
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_files():
    if not os.path.exists(TARGET_FOLDER):
        print(f"[-] Folder '{TARGET_FOLDER}' not found.")
        return

    key = generate_key()
    fernet = Fernet(key)

    print(f"[*] Encrypting .txt files in '{TARGET_FOLDER}'...")
    for filename in os.listdir(TARGET_FOLDER):
        filepath = os.path.join(TARGET_FOLDER, filename)
        if filename.endswith(".txt"):
            with open(filepath, "rb") as file:
                data = file.read()
            encrypted = fernet.encrypt(data)
            with open(filepath, "wb") as file:
                file.write(encrypted)
            print(f"[+] Encrypted: {filename}")
    print(f"[✓] Encryption complete. Key saved to '{KEY_FILE}'.")

def decrypt_files():
    if not os.path.exists(TARGET_FOLDER):
        print(f"[-] Folder '{TARGET_FOLDER}' not found.")
        return

    key = load_key()
    if not key:
        return

    fernet = Fernet(key)

    print(f"[*] Decrypting .txt files in '{TARGET_FOLDER}'...")
    for filename in os.listdir(TARGET_FOLDER):
        filepath = os.path.join(TARGET_FOLDER, filename)
        if filename.endswith(".txt"):
            with open(filepath, "rb") as file:
                data = file.read()
            try:
                decrypted = fernet.decrypt(data)
                with open(filepath, "wb") as file:
                    file.write(decrypted)
                print(f"[+] Decrypted: {filename}")
            except Exception as e:
                print(f"[-] Failed to decrypt {filename}: {e}")
    print("[✓] Decryption complete.")

def main():
    while True:
        print("\n=== Ransomware Simulator Tool (Safe Demo) ===")
        print("1. Encrypt test files")
        print("2. Decrypt test files")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            encrypt_files()
        elif choice == "2":
            decrypt_files()
        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
