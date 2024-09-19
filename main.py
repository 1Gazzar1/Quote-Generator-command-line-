import requests 

def get_quote():
    response = requests.get("https://api.quotable.io/random",verify=False)

    if not response.status_code >= 400 :
        data = response.json()
        quote = data["content"]
        author = data["author"]
        return f"{quote} \nBy {author}"
    else : 
        return f"something went wrong ,response code is {response.status_code}"

while True : 
    
    inp = input("do you want a random quote ?(y/n)")
    if inp == "y" :
        print(get_quote())
    elif inp == "n" :
        break
    else : 
        print("Invalid input")
        break

