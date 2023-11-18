import os, secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from base64 import  b64decode, b64encode
from cryptography.hazmat.backends import default_backend
from opentotp import OpenTOTP
from uuid import uuid4
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
import hashlib
import random
from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO
from django.core.files import File
import sys
class DataEncryption():


    def encrypt(key, plaintext):
        iv                  = os.urandom(16)
        cipher              = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor           = cipher.encryptor()
        padder              = PKCS7(128).padder()
        padded_plaintext    = padder.update(plaintext.encode("utf-8")) + padder.finalize()
        ciphertext          = encryptor.update(padded_plaintext) + encryptor.finalize()
        return b64encode(iv + ciphertext).decode("utf-8")


    def decrypt(key, ciphertext):
        ciphertext = b64decode(ciphertext.encode("utf-8"))
        iv = ciphertext[:16]
        ciphertext = ciphertext[16:]
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

        unpadder = PKCS7(128).unpadder()
        decrypted_plaintext_padded = unpadder.update(decrypted_padded) + unpadder.finalize()

        plaintext = decrypted_plaintext_padded.decode("utf-8")
        return plaintext

        


otp_method = OpenTOTP(secret=uuid4().hex,
               alphabet="0123456789",
               otp_length=6,
               otp_change_interval=60,
               otp_drift=5)


class OTPHandler():

    def generate():
        otp_value = otp_method.generate()
        return otp_value
    
    

    def verify(otp :str):
 
        if otp_method.verify(otp):
            return True
        return False
    
    
def get_token_user_or_none(request):
    User = get_user_model()
    try:
        instance = User.objects.get(id=request.user.id)
    except Exception:
        instance = None
    finally:
        return instance
    

def get_object_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None
    

def generate_avatar(username, size=200, text_color=(255, 255, 255), font_size=50):

    initials = ''.join(name[0] for name in username.split())

    background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    hashed_username = hashlib.md5(username.encode('utf-8')).hexdigest()


    image = Image.new('RGB', (size, size), background_color)
    draw = ImageDraw.Draw(image)


    font = ImageFont.truetype("arial.ttf", font_size)


    text_width, text_height = draw.textsize(initials, font=font)
    text_x = (size - text_width) // 2
    text_y = (size - text_height) // 2


    draw.text((text_x, text_y), initials, fill=text_color, font=font)


    image.save(f'{hashed_username}_avatar.png')
    
    return image



    
    
class ConvertBase64File():
    
    def base64toImage(image_data:str):
      
        if image_data:
            image_format, imgstr = image_data.split(';base64,')
        ext = image_format.split('/')[-1]
        return ContentFile(base64.b64decode(imgstr), name=f'image.{ext}')
    
    def base64toFile(file_field:str):
        
        if file_field:
            pdf_format, pdfstr = file_field.split(';base64,')
        pdf_ext = pdf_format.split('/')[-1]
        pdf_content = base64.b64decode(pdfstr)

        pdf_file = ContentFile(pdf_content, name=f'document.{pdf_ext}')
        return pdf_file
    
    def save_base64_file_to_db(base64_data, file_name):
        
        if base64_data.startswith("data:application/pdf;base64,"):
            _, base64_data = base64_data.split(',', 1)

        
        decoded_data = base64.b64decode(base64_data)
        content_file = ContentFile(decoded_data, name=file_name)
      
        return content_file
            
    def base64toFiledata(file_field: str):
        if file_field:
            file_format, file_data = file_field.split(';base64,')
            file_ext = file_format.split('/')[-1]

            # Decode the base64 data
            file_content = base64.b64decode(file_data)

            # Determine the file name based on the original format
            file_name = f'document.{file_ext}'

            # Create a ContentFile with the decoded content and original file name
            file = ContentFile(file_content, name=file_name)
            return file
        return None        
