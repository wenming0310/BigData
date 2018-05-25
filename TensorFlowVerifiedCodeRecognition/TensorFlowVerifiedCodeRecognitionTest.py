from PIL import Image
from captcha.image import ImageCaptcha
import numpy as np
def generate_captcha(captcha_text):
   """
   get captcha text and np array
   :param captcha_text: source text
   :return: captcha image and array
   """
   image = ImageCaptcha()
   captcha = image.generate(captcha_text)
   captcha_image = Image.open(captcha)
   captcha_array = np.array(captcha_image)
   return captcha_array

captcha = generate_captcha('1234')
print(captcha, captcha.shape)