# 🛡️ MIF Encryption v2 — Mathematical Indexing Function

### 🔐 Invented by Dhanwanth

> *"Everything started with a normal thought in the classroom."*

---

## 📜 What is MIF Encryption?

**MIF Encryption v2** is a customizable encryption system built from scratch using original mathematical logic and randomness. It converts each character into a numerical representation, applies key-driven transformations, and obfuscates the output using seeded randomness and modular arithmetic.

---

## 🚀 What's New in v2?

| Feature                     | MIF 1        | MIF 2 ✅                    |
| --------------------------- | ------------ | -------------------------- |
| Key-based logic             | ❌ No         | ✅ Yes                      |
| Modular transformation      | ❌ No         | ✅ Uses (x + key)² % mod    |
| Local seeded randomness     | ❌ Global RNG | ✅ Per-stage random control |
| Customizable mutation rules | ⚠️ Fixed     | ✅ Based on key             |
| Output reproducibility      | ❌            | ✅ Fully seed-based         |
| Compatible with decryption  | ✅            | ✅ (if key + seed known)    |

---

## 🧪 How It Works

**Input:** `"Dhanwanth"`
**Key:** `17`
**Seed:** `42`
**Mod:** `997` (prime number for modular operations)

### Encryption Pipeline:

1. **Character Indexing**
   Each character is converted to an index using a custom `char_set`.
   Example: `'D'` → `29`

2. **Mathematical Transformation**
   Formula:

   ```
   ((index + key)²) % mod
   ```

3. **Random Integer Mutation**
   Adds a seeded random number (1–50) to each transformed value.
   This step is reproducible thanks to seeded local RNG.

4. **Digit Mutation Based on Key**
   Each digit is optionally mutated to another character using:

   ```
   char_set[(digit + key) % len(char_set)]
   ```

5. **Random Separators**
   Multi-digit numbers are broken up with random symbols (seeded again), such as:
   `/`, `<`, `|`, `;`, `_`, `{`, etc.

---

## 💻 Example Output

```python
encrypt_mif("HI", key=17, seed=42)
# Output: w-4-7x{s{w
```

---

## 🔓 Decryption

Decryption is possible only if:

* The **key** is known
* The **seed** is preserved
* The exact **char\_set** and **mutation rules** are used
* The same `mod` value is used

---

## ⚙️ Customization Options

* Use any **math function** (e.g., `(x+key)**2`, `3x + key`)
* Adjust **mutation probability**
* Change **mod** for a different encryption space
* Modify or extend the **character set**
* Add irreversible **hashing mode** (future feature)

---

## ✨ Quote from the Creator

> *"Everything started with a normal thought in the classroom."*
> — **Dhanwanth**, Inventor of MIF, 12-year-old 8th grader from India

---

## 👨‍💼 Project Structure

```
MIF_Encryption/
├── main.py                 # Encryption driver
├── utils.py                # Core MIF logic and mutations
├── separator.py            # Separator randomizer
└── README.md               # This file
```

---

## 🧎 License

This project is open-source. Feel free to fork, modify, and build on top of MIF.

---

## 🧠 Next Version: MIF 3?

* ↻ Chained encryption (next char depends on previous)
* 🔐 Public/private key layer (hybrid with asymmetric logic)
* 🔒 Irreversible MIF hashing
* 🧪 Mutation controlled by key-derived noise functions

---
