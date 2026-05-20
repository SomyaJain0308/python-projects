# 05 — Password Manager

A terminal-based encrypted password manager using the `cryptography` library. Supports a master password gate, adding new credentials, and reading decrypted passwords from an encrypted file.

## How to Run

```bash
pip install cryptography
python password_manager.py
```

On first run, manually call `gen_key()` once to generate `secret.key`, or add an auto-generation check in `main()`.

## Example

```
Password: ****
Do you want to Read a Password or Add a Password? add
Username: netflix
Password: mypassword123

Do you want to Read a Password or Add a Password? read
Username: netflix
Password: mypassword123
```

## What I Learned

- `cryptography.fernet` for symmetric encryption — encrypting and decrypting strings
- Separating key generation (`gen_key`) and key loading (`load_key`) into distinct functions
- File handling — appending credentials with `"a"` mode, reading back with `readlines()`
- Parsing specific lines from a file to selectively decrypt only the password field
- Basic master password gate using `sys.exit()` on failure

## What I'd Improve

- **Hardcoded master password** — `"file@123"` in plain text is a security flaw; should use `hashlib.sha256` to store and compare a hash instead
- **No auto key generation** — if `secret.key` doesn't exist, the program crashes; add `os.path.exists()` check in `main()`
- **No error handling for missing `pass.txt`** — first `read()` call crashes with `FileNotFoundError`
- **Fragile `~~~` separator** — a password containing `~~~` would break parsing; a blank line or JSON format would be more robust
- **No option to delete or update** an existing password entry