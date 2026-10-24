import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("KEY")

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json",
}

while True:
    try:
        user = input("Enter The Github Username: ")
        url = "https://api.github.com/users/" + user

        response = requests.get(url, headers=headers)
        data = response.json()

        #print(data)

        keys = [
            "followers_url",
            "following_url",
            "starred_url",
            "repos_url",
            "name",
            "public_repos",
            "company",
            "location",
            "email",
            "bio",
            "created_at"
        ]

        followers_url, following_url, starred_url, repos_url, name, public_repos, company, location, email, bio, created_at = [
            data.get(k) for k in keys
        ]

        print("=====================================================")
        print("Name:", name)
        print("Email:", email)
        print("Location:", location)
        print("Bio:", bio)
        print("Account Created:", created_at)
        print("=====================================================")

        followers = requests.get(followers_url, headers=headers).json()

        print("Followers: ")
        for i in followers:
            print(i.get("login"))

        print("=====================================================")

        clean_following_url = following_url.replace("{/other_user}", "")
        following = requests.get(clean_following_url, headers=headers).json()

        print("Following:")
        for i in following:
            print(i.get("login"))

        print("=====================================================")

        clean_starred_url = starred_url.replace("{/owner}{/repo}", "")
        starred = requests.get(clean_starred_url, headers=headers).json()
        print("Starred Repositories:")
        for i in starred:
            print(i.get("name"))

        print("======================================================")

        repos = requests.get(repos_url, headers=headers).json()
        print("Repositories:")
        for i in repos:
            print(i.get("name"))

    except:
        print("Error...")
        break