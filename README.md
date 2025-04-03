# Image-to-Pdf-Converter

Converting images into pdf, using python script.

On a random day, I wanted to convert some of my Personal Documents which were images and want to convert them into pdf. I could have used the online websites to convert it but a sense of insecurity strike me. So, I searched for tools which I can download and use it any time I want. However, those tools leave a watermark on the pdf which I dont want and to remove the water mark I need to purchase their premium vesion.

As a programmer, that hurts me. Why I have to pay for something that I can do it by myself.

Here is a python script to convert the images into pdf.

**No need to pay :)**

It is a very simple program. However, I might update it again and agian with some more dynamic features or I am also open to suggestions!!

**Feel free to drop any idea of your :)**

---

## **How it works?**

Store all the images you want to convert into pdf into the `images_to_pds` folder.

### **Featues**

> If you want to combine the multiple images into one pdf, then label the images with numbers. Like: 1.png, 2.jpg, 3.jpeg,....
>
> If you dont want to combine them then set the `--order` to `False`
>
> If you store the images with different name then each images will be converted into separate pdfs.

**Note:** All the pdf will be saved into the `images_to_pds` folder.

Dont worry :), If you want to save them into a different folder then use the `--pdf_folder` argument followed by the path.

---
## Commands to be ran on terminal

1. Merge labeled images + save PDFs in image folder (default):
  `python image_to_pdf.py`

2. Same behavior, but save all PDFs into a custom folder:
  `python image_to_pdf.py --pdf_folder ./pdf_outputs/`

3. Don’t merge anything → every image gets its own PDF (in same folder as image):
  `python image_to_pdf.py --order False`

4. Don’t merge, and save all PDFs in a separate folder:
  `python image_to_pdf.py --order False --pdf_folder ./pdf_outputs/`
