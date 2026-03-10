#!/usr/bin/env python3
# coding: utf-8

import json
import os
import argparse

FILE_NAME = "costs.json"


def load_json():

    if not os.path.exists(FILE_NAME):

        return []

    try:

        with open(FILE_NAME, "r", encoding="utf-8") as f:

            return json.load(f)
        
    except (json.JSONDecodeError, ValueError):

        return []


def save_json(data):

    with open(FILE_NAME, "w", encoding="utf-8") as f:

        json.dump(data, f, indent=4, ensure_ascii=False)


def add_cost(price, date, article):

    data = load_json()

    data.append({
        "price": float(price),
        "date": date,
        "article": article
    })

    save_json(data)
    print("✔ Dépense ajoutée")


def list_costs(order="asc"):

    data = load_json()

    if not data:

        print("Aucune dépense enregistrée")
        return

    reverse = order == "desc"

    data = sorted(data, key=lambda x: x["date"], reverse=reverse)

    for i, item in enumerate(data, 1):

        print(f"{i}. {item['date']} | {item['article']} | {item['price']}€")


def main():

    parser = argparse.ArgumentParser(

        prog="costs",
        description="Gestionnaire simple de dépenses JSON",
        epilog="Exemple: costs add -p 10 -d 2026-03-10 -a pizza"

    )

    subparsers = parser.add_subparsers(dest="command")


    add_parser = subparsers.add_parser("add", help="Ajouter une dépense")

    add_parser.add_argument(

        "-p", "--price",
        required=True,
        help="prix de l'article"

    )

    add_parser.add_argument(

        "-d", "--date",
        required=True,
        help="date (YYYY-MM-DD)"

    )

    add_parser.add_argument(

        "-a", "--article",
        required=True,
        help="nom de l'article"

    )


    list_parser = subparsers.add_parser("list", help="Lister les dépenses")

    list_parser.add_argument(

        "-o", "--order",
        choices=["asc", "desc"],
        default="asc",
        help="ordre par date: asc (ancien → récent) ou desc (récent → ancien)"

    )

    args = parser.parse_args()

    if args.command == "add":

        add_cost(args.price, args.date, args.article)

    elif args.command == "list":

        list_costs(args.order)

    else:

        parser.print_help()


if __name__ == "__main__":
    
    main()  