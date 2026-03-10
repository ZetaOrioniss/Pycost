# Costs CLI

A small command-line tool to **track and view your expenses** using a simple JSON file.

The goal of this script is to stay **lightweight and easy to use**, with **no external dependencies**. All expenses are stored locally in a `costs.json` file.

---

## Features

* Add a new expense
* List recorded expenses
* Sort expenses by date
* Store everything locally in a JSON file
* Possibility of using git to keep a history 

---

## Installation

Clone the repository or simply copy the script:

```bash
git clone <repo>
cd <repo>
```

Make the script executable:

```bash
chmod +x main.py
```

Then run it with:

```bash
./main.py
```

or

```bash
python3 main.py
```

---

## Usage

The program works with **commands** (`add`, `list`).

### Add an expense

```bash
./main.py add -p 10 -d 2026-03-10 -a pizza
```

Arguments:

* `-p`, `--price` : price of the item
* `-d`, `--date` : date in `YYYY-MM-DD` format
* `-a`, `--article` : name of the item

Example:

```bash
./main.py add -p 4.5 -d 2026-03-10 -a coffee
```

---

### List expenses

```bash
./main.py list
```

Example output:

```
1. 2026-03-10 | coffee | 4.5€
2. 2026-03-10 | pizza | 10€
```

---

### Sort expenses

By default, expenses are displayed **from oldest to newest**.

You can reverse the order:

```bash
./main.py list -o desc
```

Available options:

* `asc` → oldest → newest
* `desc` → newest → oldest

---

## Data structure

Expenses are stored in `costs.json` like this:

```json
[
    {
        "price": 10.0,
        "date": "2026-03-10",
        "article": "pizza"
    }
]
```

---

## Notes

* If `costs.json` does not exist, it will be created automatically.
* If the file is empty or corrupted, the program will simply start with an empty list.

---

## Possible improvements

Some ideas to extend the project:

* Add a **total expenses** command
* Filter by **date**
* Delete an expense
* Add **categories**
* Export data (for example to CSV)

---

## License

Free to use and modify.