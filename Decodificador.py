import PIL.Image as pimage
import numpy as np

def LerMensagemPorLSB(imagem):
    pimagem = pimage.open(imagem)
    pimagem = pimagem.convert("RGB")
    pixels = np.array(pimagem.getdata())
    bits_disponiveis = len(pixels) * 3
    bits_lidos = ""

    for posicao in range(32):
        pixel = posicao // 3
        canal = posicao % 3
        if(pixels[pixel][canal] % 2 == 0):
            bits_lidos += "0"
        else:
            bits_lidos += "1"
    tamanho_mensagem = int(bits_lidos,2)

    if(tamanho_mensagem + 32 < bits_disponiveis):
        bits_mensagem = ""
        for posicao in range(32,tamanho_mensagem + 32):
            pixel = posicao // 3
            canal = posicao % 3
            if(pixels[pixel][canal] % 2 == 0):
                bits_mensagem += "0"
            else:
                bits_mensagem += "1"
        grupo_oculto = ""
        texto_oculto = ""
        for i in range(0,len(bits_mensagem),8):
            grupo_oculto = bits_mensagem[i: i + 8]
            valor = int(grupo_oculto,2)
            texto_oculto += chr(valor)
        print(texto_oculto)
    else:
        print("Mensagem maior do que o cabeçalho informado")