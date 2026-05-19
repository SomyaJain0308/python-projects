# 13 — Password Generator

A terminal password generator that takes a desired length from the user and generates a random password guaranteed to contain at least one letter, digit, and special character.

## How to Run

```bash
python password_generator.py
```

No external dependencies — uses Python's built-in `random` and `string` modules.

## Example

```
How many characters do you want it to be? 12
aG3$kLm9!xQp
```

## What I Learned

- `string.ascii_letters`, `string.digits`, `string.punctuation` for building character pools
- `random.choices(pool, k=n)` to generate a list of random characters in one line
- `any()` as a Pythonic way to check if a condition is met for any element in a list
- Validation loop to keep regenerating until the password meets all requirements (letter + digit + symbol)

## What I'd Improve

- Wrap logic into functions (`get_length()`, `generate_password()`) for reusability — the flat script structure is a step back from projects 03 and 12
- Remove the hardcoded 8–16 character limit — a real password generator shouldn't cap at 16
- Let the user choose whether to include symbols or digits (optional parameters)