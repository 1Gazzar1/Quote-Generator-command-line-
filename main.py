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


font = ImageFont.truetype("fonts\\Play-Bold.ttf",40)
text_color = (255,255,255)

while True : 
    
    inp = input("do you want a random quote ?(y/n)").strip().lower()
    if inp == "y" :
        # loading the image
        image = Image.open(BytesIO(Generate_random_image_without_path(blur= 5))).convert("RGBA")
        
        # loading the quote and author 
        quote , author = get_quote()
        full_quote = f"{quote}\nBy {author}"
        # drawing the text to the image
        draw = ImageDraw.Draw(image)
        
        text_pos = (50,50)
        padding = 10

        box_pos = draw.textbbox(text_pos,full_quote,font)
         
        box = (box_pos[0] - padding,  box_pos[1] - padding, box_pos[2] + padding, box_pos[3] + padding)
        draw.rectangle(box, fill=(0, 0, 0,128))
        draw.multiline_text(text_pos,full_quote,text_color,font= font)
        
        image.show()
    elif inp == "n" :
        break
    else : 
        print("Invalid input")
                

