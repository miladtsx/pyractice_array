# 🔁 Similar String Grouper

A minimal Python tool to group similar strings based on circular rotations.
It identifies words that are rotations of each other and groups them into distinct sets.

## ✅ What it does

Given a list of strings, it groups words that are circularly similar.

For example, "abcd" and "cdab" are grouped together because one can be rotated into the other.

### Input

```python
["abcd", "cdab", "dabc", "bcda", "efgh", "ghfe"]
```

### Output

```python
{
  "abcd": ["abcd", "cdab", "dabc", "bcda"],
  "efgh": ["efgh"],
  "ghfe": ["ghfe"]
}
```

## 🚀 Installation

```bash
pip install rotate-group-words==0.3.0
```

## 📦 Usage

### In Code:

```python
from rotate-group-words import rotate_group_words

input = ["abcd", "cdab", "dabc", "bcda", "efgh", "ghfe"]
output = rotate_group_words(input)
print(output)

```

### As standalone cli application

```bash
rgw -h
rgw -w abcd,cdab,dabc,bcda,efgh,ghfe
```

## ⚙️ How it works

- Similarity Rule: Two words are similar if a rotation of one equals the other.

- Efficiency: The similarity check (is_similar) is optimized from O(n) to O(1).

- Grouping: Uses a visited set to avoid duplicate processing.

- Non-destructive: Does not mutate the input.

## 🛠️ Changelog & Improvements

[✔] Improved `is_similar()` from O(n) to O(1) by hashing normalized rotation forms.[6003...5a36](https://github.com/miladtsx/pyractice_array/commit/6003d69dbfc7990ee3f79fb6990a93efd4865a36)

[✔] Prevented duplicates using a visited `set`. [c7ca...c4e6](https://github.com/miladtsx/pyractice_array/commit/c7ca5f3ca0a0118c96a0d767726d013022cfc4e6)

[✔] Cleaned output formatting for easier reading. [118c...1b3a](https://github.com/miladtsx/pyractice_array/commit/118ce5917e32622ba2cd0a8b06bf53c739631b3a)

[✔] 100% test coverage and CI with GitHub Actions.[dd53...4a27](https://github.com/miladtsx/pyractice_array/commit/dd53efd0b1b09d4342f3586b2f66bcd4d7f14a27)

[✔] Packaged and published to [PyPI](https://pypi.org/project/rotate-group-words/)
