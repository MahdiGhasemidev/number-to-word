# Number to Word Converter

A simple yet powerful Python utility that converts numbers into their English word representation.  
For example, the input `12345` will output `"Twelve Thousand Three Hundred Forty Five"`.

---

## 📌 Features
- Converts any integer to its word format.
- Supports numbers from `0` up to `999,999,999,999` (999 billion).
- Handles edge cases such as `0`, round tens, and exact hundreds.
- Easy to use and extend.

---

## 🚀 Usage

### 1. Clone the Repository
```bash
git clone https://github.com/MahdiGhasemidev/number-to-word.git
cd number-to-word
```

### 2. Run the Script
```bash
python main.py
```

### 3. Example
```
Enter a Number : 12345
Twelve Thousand Three Hundred Forty Five
```

---

## 📂 Project Structure
```
number-to-word/
│── main.py          # Main script to run the converter
│── constance.py     # Contains constants for number names
└── README.md        # Project documentation
```

---

## 🧩 How It Works
1. **Numbers < 20** → Directly mapped using the `UNDER_TWENTY` list.  
2. **Numbers < 100** → Constructed using the `TENS` list and `UNDER_TWENTY` for the remainder.  
3. **Numbers >= 100** → The script finds the largest pivot (Hundred, Thousand, Million, Billion) from the `ABOVE_100` dictionary and recursively builds the word representation.

---

## ✅ Example Outputs
| Input     | Output                                 |
|-----------|-----------------------------------------|
| `0`       | Zero                                    |
| `19`      | Nineteen                                |
| `40`      | Forty                                   |
| `100`     | One Hundred                             |
| `123`     | One Hundred Twenty Three                |
| `123456`  | One Hundred Twenty Three Thousand Four Hundred Fifty Six |
| `1000000` | One Million                             |

---

## ⚠️ Limitations
- Only supports positive integers within the specified range.
- Does not handle negative numbers or decimals.

---

## 📌 Future Improvements
- Add support for negative numbers.
- Add support for decimal numbers.
- Option for different languages.

---

## 🛠 Requirements

- Python 3.6 or higher

Install the dependencies using:

```bash
pip install -r requirements.txt
### Requirements File
```


## 🧑‍💻 Author
**Mahdi Ghasemi**  
📧 Email: Mahdi.ghasemi.dev@gmail.com  
🌐 GitHub: [Mahdi Ghasemi](https://github.com/MahdiGhasemidev)  

---

### ⭐ If you find this project useful, consider giving it a star on GitHub!

---


## 📄 License

This project is licensed under the [MIT License](./LICENSE).