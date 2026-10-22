"""
I cheated and built this part in python not javascript
I did try like cheerio and puppeteer and a couple other combonations and I just couldnt get it to work
I blame Javascript since I was able to do this in python rather quickly ~20 minutes
And that 20 minutes included testing everything and a full 5 minutes of api calls so I didnt accidentally DDOS pokeapi
"""
def importer():
    import requests as r
    import json
    import time
    import os

    if not os.path.isdir("pokeJson/"):
        os.mkdir("pokeJson/")
    if not os.path.isdir("pokemon/"):
            os.mkdir("pokemon/")
    
    baseLink = "https://pokeapi.co/api/v2/pokemon/"
    for i in range(1,1026):
        data = json.loads(r.get(baseLink+str(i)).text)
        with open("pokeJson/"+data["name"]+".json", "w") as f:
            json.dump(data, f, indent = 2)
        with open("pokemon/"+data["name"]+".png", "wb") as img:
            img.write(r.get(data["sprites"]["front_default"]).content)
        time.sleep(0.1)

def main():
    importer()


if __name__ == "__main__":
    # main()
    pass
