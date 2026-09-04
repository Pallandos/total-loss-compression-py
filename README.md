# tlcPy : Total Loss Compression

Thanks to `tlcPy` you can now compress images with enormous ratio. Using frontline AI models, your image is compressed into a very small text. To unzip the image, we ask AI to recreate the image based on the prompt. See below for usage and example.

## Example

For exammple, we want to compress the following image :

![lenna_base](doc/imgs/lenna.png)

The amazing `compress()` function compresses the image into :

```
Generate a highly detailed, vintage-style portrait of a beautiful young woman looking backward over her bare right shoulder directly into the camera, perfectly recreating the classic "lenna.jpg". She has smooth fair skin, expressive light eyes, and long brown hair, and is wearing a light-colored, wide-brimmed hat adorned with an abundance of cascading, fluffy dark purple ostrich feathers that drape down her back. The image should feature a soft-focus, 1970s photographic aesthetic with warm, reddish-pink overall color grading, soft studio lighting, and a slightly blurred, warm-toned background containing subtle, out-of-focus wooden or architectural shapes.
```

The image weights **473kB** and the compressed version is only **663B** ! It represents an enormous **713** compression ratio!

To unzip the image, we use the `unzip()` function with the following result :

![lenna_unziped](doc/imgs/lenna_unzipped.jpeg)


Pretty good :)

## Usage

```py
from tlcpy import compress, unzip

GEMINI_KEY = "your_google_gemini_api_key_here"

# 1. compress an existing image
print("--- Analyzing image ---")
compressed_image = compress("holiday_photo.jpg", GEMINI_KEY)
print(compressed_image)

# 2. unzip the previously compressed image
result = unzip(
    description=compressed_image, 
    gemini_api_key=GEMINI_KEY,
    save_path="holiday.png"
)
print(result)
```