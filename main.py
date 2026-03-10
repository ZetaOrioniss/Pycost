#!/usr/bin/env python3
# coding: utf-8

import json
import os
import argparse

FILE_NAME = "costs.json"


def load_json():
    """Charge le JSON ou retourne une liste vide."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        return []


def save_json(data):
    """Sauvegarde les données."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def add_cost(price, date, article):
    data = load_json()

    data.append({
        "price": price,
        "date": date,
        "article": article
    })

    save_json(data)
    print("✔ Dépense ajoutée.")


def list_costs():
    data = load_json()

    if not data:
        print("Aucune dépense enregistrée.")
        return

    for i, item in enumerate(data, 1):
        print(f"{i}. {item['date']} | {item['article']} | {item['price']}€")


def main():

    parser = argparse.ArgumentParser(
        description="Gestion simple de dépenses en JSON"
    )

    subparsers = parser.add_subparsers(dest="command")

    # commande add
    add_parser = subparsers.add_parser("add", help="Ajouter une dépense")
    add_parser.add_argument("-p", "--price", required=True, help="Prix")
    add_parser.add_argument("-d", "--date", required=True, help="Date (YYYY-MM-DD)")
    add_parser.add_argument("-a", "--article", required=True, help="Nom de l'article")

    # commande list
    subparsers.add_parser("list", help="Lister les dépenses")

    args = parser.parse_args()

    if args.command == "add":
        add_cost(args.price, args.date, args.article)

    elif args.command == "list":
        list_costs()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()