# Base Converter

### Inspired by **Obduction**'s Numerical Puzzle

I developed this simple base converter after learning about **base 4** while playing the game [**Obduction**](https://store.steampowered.com/app/306760/Obduction/). The game features an alien numerical system that uses base 4, and understanding it was a key challenge in solving some of its puzzles. I found the concept fascinating, so I created this small tool for fun!

---

## 📌 How It Works
This script converts numbers from **decimal** to any base (e.g., base 4). Simply enter your target number and the desired base, and it will display the converted result.

Here’s an example of how the script works in action:
```
> Your target number: 14
> Base number: 3
> =========================
>        RESULT = 112
> =========================
> 
> Your target number: 222
> Base number: 4
> =========================
>       RESULT = 3132
> =========================
```

---

## 🧩 **Base 4 in Obduction**
In *Obduction*, an alien race known as the **Villein** uses a **base 4 numbering system**. Instead of the familiar 0-9 digits in base 10, base 4 only uses **0, 1, 2, and 3**. Understanding this system is crucial for deciphering the game's puzzles.

For a deep dive into how base 4 is used in *Obduction*, check out this excellent community guide:

🔗 [**Villein Numbers Guide**](https://steamcommunity.com/sharedfiles/filedetails/?id=752679228)  
<img src="https://steamuserimages-a.akamaihd.net/ugc/478895272575397157/A39746A9CD3F485CBF51E871DE7807280681B119/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false"/>

---

## ⚙️ Code
This is the simple Python script used for conversion:

```python
while True:
    number = int(input("Your target number: "))
    base = int(input("Base number: "))

    result = ""
    while number > 0:
        result = str(number % base) + result
        number = number // base

    print("="*25)
    print(f"RESULT = {result}".center(25))
    print("="*25, end="\n\n")
```

---

## 🛠️ Features & Future Ideas
- Currently, this script converts from **decimal** to any base.
- Future improvements could include **support for fractional numbers** and **custom Villein-style symbols** for a more immersive experience.

---

### 🎮 Have you played *Obduction*?
If you're interested in puzzle games with **mystical worlds and deep lore**, *Obduction* is worth checking out. Let me know if you’ve solved its number-based challenges!

> Feel free to open an issue or contribute if you have ideas for improvements!