import requests 
from image_generator import Generate_random_image_without_path
from PIL import Image,ImageFont,ImageDraw
from io import BytesIO

def get_quote():
    response = requests.get("https://api.quotable.io/random/?maxLength=200",verify=False)

    if not response.status_code >= 400 :
        data = response.json()
        quote = data["content"]
        author = data["author"]
        return quote,author
    else : 
        return f"something went wrong ,response code is {response.status_code}"
def get_user_confirmation(prompt):
    """Gets a yes/no confirmation from the user."""
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'n']:
            return response == 'y'
        else:
            print("Invalid input, please enter 'y' or 'n'.")
def get_user_numeric_input(prompt, min_value=0, max_value=10):
    """Gets a numeric input from the user within a specified range."""
    while True:
        response = input(prompt).strip()
        if response.isnumeric():
            number = int(response)
            if min_value <= number <= max_value:
                return number
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        else:
            print("Invalid input, please enter a numeric value.")

font = ImageFont.truetype("fonts\\Play-Bold.ttf",40)
    
text_color = (255,255,255)

while True : 
    if get_user_confirmation("do you want a random quote ?(y/n) : ") :
        blur = get_user_numeric_input("do you want blur ? \n"
                                      "if yes enter a number (1-10) \n"
                                      "if no enter 0 : ")
        
        grayscaled = get_user_confirmation("do you want the photo grayscaled ? (y/n) ")
           
        # loading the image
        image = Image.open(BytesIO(
            Generate_random_image_without_path(blur= blur,grayscale=grayscaled))).convert("RGB")
        
        # loading the quote and author 
        quote , author = get_quote()
        full_quote = f"{quote}\nBy {author}"
        # drawing the text to the image
        draw = ImageDraw.Draw(image)
        
        text_pos = (50,50)
        padding = 10

        box_pos = draw.textbbox(text_pos,full_quote,font)

        if box_pos[2] + text_pos[0] > 1920 : 
            indx = quote.index(" ",len(quote)//2)
            quote = quote[:indx] +"\n" + quote[indx:]
            full_quote = f"{quote}\nBy {author}"
            box_pos = draw.textbbox(text_pos,full_quote,font)

        box = (box_pos[0] - padding,  box_pos[1] - padding, box_pos[2] + padding, box_pos[3] + padding)
        draw.rectangle(box, fill=(0, 0, 0,128))
        draw.multiline_text(text_pos,full_quote,text_color,font= font)
        
        image.show()
        image.save("Data\\imagetest0.jpg","JPEG")
    
                

