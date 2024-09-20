import requests 
from image_generator import Generate_random_image_without_path
from PIL import Image,ImageFont,ImageDraw
from io import BytesIO

def get_quote():
    response = requests.get("https://api.quotable.io/random",verify=False)

    if not response.status_code >= 400 :
        data = response.json()
        quote = data["content"]
        author = data["author"]
        return quote,author
    else : 
        return f"something went wrong ,response code is {response.status_code}"


font = ImageFont.truetype("fonts\\LemonJellyPersonalUse-dEqR.ttf",70)
text_color = (0,0,0)

while True : 
    
    inp = input("do you want a random quote ?(y/n)").strip().lower()
    if inp == "y" :
        # loading the image
        image = Image.open(BytesIO(Generate_random_image_without_path(blur= 2)))
        text_pos = (300,image.size[1]//2-50)

        # loading the quote and author 
        quote , author = get_quote()

        # drawing the text to the image
        draw = ImageDraw.Draw(image)
        
        draw.multiline_text(text_pos,f"{quote}\nBy{author}",text_color,font= font)
        
        image.show()
    elif inp == "n" :
        break
    else : 
        print("Invalid input")
                

