def mediatype(extenssion):
    match extenssion:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg" | "heic":
            print("image/jpeg")
        case _:
            print("application/octet-stream")
            
                
filename = input()
ext = filename.split(".")[1]
mediatype(ext)