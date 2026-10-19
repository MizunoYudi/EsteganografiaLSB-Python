import PIL.Image as pimage
import pathlib as plib
import numpy as np

def EsconderPorLSB(mensagem, imagem):
    pimagem = pimage.open(imagem)
    pimagem = pimagem.convert("RGB")
    pixels = np.array(pimagem.getdata())
    mensagemb = ""
    
    for i in mensagem:
        mensagemb = mensagemb + f'{ord(i):08b}'

    tam_mensagem = len(mensagemb)
    cabecalho = f'{(tam_mensagem):032b}'
    bits_totais = cabecalho + mensagemb
    tamanho_total = len(bits_totais)
    bits_disponiveis = (len(pixels) * 3)

    if(bits_disponiveis >= tamanho_total):
        for posicao, bit in enumerate(bits_totais):
            pixel = posicao // 3
            canal = posicao % 3
            if(pixels[pixel][canal] % 2 == 0 and (int(bit) == 1)):
                pixels[pixel][canal] += 1
            elif(pixels[pixel][canal] % 2 != 0 and (int(bit) == 0)):
                pixels[pixel][canal] -= 1
        pimagemcopia = pimagem.copy()
        pimagemcopia.putdata(tuple(map(tuple, pixels)))
        pimagemcopia.save(plib.Path(imagem).stem+"-codificado"+plib.Path(imagem).suffix)
    else:
        print("A mensagem não cabe na imagem")