from PIL import Image
import numpy as np

def process_logo():
    # Load original image
    img = Image.open('logo.jpg').convert('L')
    img_np = np.array(img)

    # Create RGBA output (all white pixels)
    out = np.zeros((img_np.shape[0], img_np.shape[1], 4), dtype=np.uint8)
    out[:,:,0] = 255
    out[:,:,1] = 255
    out[:,:,2] = 255

    # Alpha channel mapping: dark pixels become opaque, light pixels become transparent.
    # img_np has values 0 (black) to 255 (white)
    # Background is light gray, maybe ~230-245
    # Text is black/dark gray, maybe ~0-50
    
    alpha = 255.0 - img_np
    
    # Anything lighter than 200 (alpha < 55) becomes fully transparent
    alpha[alpha < 55] = 0
    
    # Normalize the remaining alpha so the darkest part is fully opaque (255)
    max_a = np.max(alpha)
    if max_a > 0:
        alpha = alpha * (255.0 / max_a)
        
    out[:,:,3] = alpha.astype(np.uint8)

    final = Image.fromarray(out)
    
    # Crop to bounding box to remove excess transparent space
    bbox = final.getbbox()
    if bbox:
        final = final.crop(bbox)
        
    final.save('logo_white.png')
    print("Logo processed and saved as logo_white.png")

process_logo()
