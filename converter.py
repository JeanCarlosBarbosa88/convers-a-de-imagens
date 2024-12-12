from PIL import Image

def converter_para_cinza(imagem):
    img = Image.open(imagem)
    
    largura, altura = img.size
    
    for x in range(largura):
        for y in range(altura):
            r, g, b = img.getpixel((x, y))
            
            cinza = int(0.3 * r + 0.59 * g + 0.11 * b)
    
            img.putpixel((x, y), (cinza, cinza, cinza))
    
    return img

def converter_para_preto_branco(imagem, limiar=128):
    img_cinza = converter_para_cinza(imagem)
    
    largura, altura = img_cinza.size
    
    # imagem em tons de cinza
    for x in range(largura):
        for y in range(altura):
            r, g, b = img_cinza.getpixel((x, y))
            
            if r >= limiar:
                img_cinza.putpixel((x, y), (255, 255, 255))  
            else:
                img_cinza.putpixel((x, y), (0, 0, 0))  
    
    return img_cinza

# gerar cópias e salvá-las
def gerar_copias(imagem_original):
    imagem_cinza = converter_para_cinza(imagem_original)
    imagem_cinza.save('imagem_tons_de_cinza.jpg')
    print("Imagem em tons de cinza salva como 'imagem_tons_de_cinza.jpg'.")
    

    imagem_pb = converter_para_preto_branco(imagem_original)

    imagem_pb.save('imagem_preto_branco.jpg')
    print("Imagem em preto e branco salva como 'imagem_preto_branco.jpg'.")


imagem_original = 'jean.jpg' 
gerar_copias(imagem_original)
