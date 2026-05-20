# 07 — Madlibs Generator

A terminal Madlibs game that reads a story template from a file, extracts placeholders, prompts the user to fill them in, and prints the completed story.

## How to Run

```bash
python madlibs.py
```

No external dependencies — uses Python's built-in `re` module.

Make sure `story.txt` is in the same folder. Placeholders in the story use angle brackets like `<adjective>` or `<noun>`.

## Example `story.txt`

```
Once upon a time, a <adjective> <noun> went to the <place>.
It was a very <adjective> day and everyone was feeling <emotion>.
```

## Example Run

```
Write words for these placeholders:
adjective: spooky
noun: cat
place: library
emotion: confused

Once upon a time, a spooky cat went to the library.
It was a very spooky day and everyone was feeling confused.
```

## What I Learned

- `re.findall()` with a regex pattern to extract placeholders from a string
- `dict.fromkeys()` to deduplicate a list while preserving insertion order
- Reading a full file with `file.read()` vs line by line
- In-place string replacement by reassigning the `story` variable each iteration

## What I'd Improve

- Wrap logic into functions (`load_story`, `get_placeholders`, `fill_story`) for reusability
- Add error handling for missing `story.txt` with a clear message instead of a crash
- Include a sample `story.txt` in the repo so it runs out of the box
- Add support for multiple story files with a menu to choose between them