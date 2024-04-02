import requests
import hashlib
import base58

def download_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"Error downloading file: {e}")
        return None

def compute_double_sha_hash(file_content):
    # First SHA-256 hash
    first_hash = hashlib.sha256(file_content).digest()
    # Second SHA-256 hash, if you want to double hash
    double_hash = hashlib.sha256(first_hash).digest()
    return double_hash

def encode_to_cid(hash_bytes):
    # Convert the hash into a CIDv0 (example using base58)
    cid = base58.b58encode(hash_bytes).decode('utf-8')
    return cid

def main():
    url = input("Enter the URL of the file: ")

    file_content = download_file(url)
    if file_content is not None:
        double_hash = compute_double_sha_hash(file_content)
        cid = encode_to_cid(double_hash)
        print(f"CID-like string of downloaded file: {cid}")

if __name__ == "__main__":
    main()
