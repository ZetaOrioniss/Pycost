#! /usr/bin/python3
#! coding: utf-8

import sys
import json

json_base = """

{

  "cost" : [
    {

      "price" : {},
      "date" : "{}",
      "article" : "{}"
      
    }
  ]
  
}


"""

def isFileExist():

    try:
        json_file = open("costs.json", "r")
        print(json_file.read()); json_file.close()

    except FileNotFoundError:
        return False

def FileCreate():

    try:
        json_file = open("costs.json", "x"); json_file.close()

    except:

        return 1

def FileAppend(c_price, c_date, c_article):

    json_append = {
        "price": c_price,
        "date": c_date,
        "article": c_article
    }

    try:
        with open("costs.json", "a", encoding="utf-8") as json_file:
            print("opened")
            json_file.write(json.dumps(json_append, ensure_ascii=False) + ",\n")

    except Exception as e:
        print("Erreur :", e)




def main(option, price, date, article):
    
    if isFileExist() == False:
        FileCreate()

    if option == "add":

        FileAppend(price, date, article)



if __name__ == "__main__":

    option = sys.argv[1]
    price = sys.argv[2]
    date = sys.argv[3]
    article = sys.argv[4]

    print(option)


    main(option, price, date, article)