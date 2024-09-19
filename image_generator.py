import requests 

def Generate_random_customizable_image(file_path : str ,
                                        width : int = 1920 , height : int = 1080 ,
                                        blur : int = False , grayscale : bool = False ,
                                        img_id : int = None):
    # Cofiguring the Url as intended for the user 
    if img_id == None :
        url = f"https://picsum.photos/{width}/{height}/"
    else : 
        url = f"https://picsum.photos/id/{img_id}/{width}/{height}/"

    params = []
    if blur :
         params.append(f"blur={blur}")
    if grayscale :
        params.append(f"grayscale")

    url += "?" + "&".join(params)

    # making the request from the api 
    response = requests.get(url)

    # generating the image
    if response.status_code == 200 :

        content = response.content 
        with open(file_path,"wb") as file :
            file.write(content)
        print(f"image saved")

    else : 
        print(f"process failed , status code = {response.status_code}")

#Generate_random_customizable_image("Data\\image_2.jpg",1360,720,blur=0,img_id=667,grayscale=True)