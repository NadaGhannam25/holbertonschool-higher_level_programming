#!/usr/bin/python3
import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder and print their titles
    """
    response = requests.get(URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder and save them into a CSV file
    """
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        data = []
        for post in posts:
            data.append({
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            })

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "title", "body"]
            )
            writer.writeheader()
            writer.writerows(data)

