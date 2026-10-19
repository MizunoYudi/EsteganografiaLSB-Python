# Esteganografia LSB

Trabalho desenvolvido para a matéria Segurança da Informação, do 6° semestre do curso de Tecnologia em Análise e Desenvolvimento de Sistemas no IFSP Campus Boituva

Orientador: Daniel Cintra Cugler

Integrantes: Enzo Eiji Banin e João Victor Yudi Mizuno

## O que é

Programa de linha de comando em Python que "esconde" uma mensagem de texto dentro de uma imagem PNG usando a técnica LSB (Least Significant Bit) e que lê mensagens escondidas dessa forma.

## Como funciona

*Codificador*
Cada pixel da imagem tem três canais (R, G e B), e cada canal guarda um valor de 0 a 255. O programa troca apenas o **bit menos significativo** de cada canal por um bit da mensagem, o que altera a cor em no máximo 1 unidade e é imperceptível a olho nu.

Os bits são gravados nesta ordem, pixel a pixel (da esquerda para a direita, de cima para baixo), canal R, G e B de cada pixel:

1. **Cabeçalho:** 32 bits com o tamanho da mensagem, em bits.
2. **Mensagem:** 8 bits por caractere (código do caractere em binário).

Capacidade em bits: uma imagem com **largura * altura** pixels comporta **largura * altura * 3** bits, descontando os 32 do cabeçalho.

Capacidade em caracteres: uma imagem com **largura * altura * 3 - 32** bits ÷ 8 é a quantidade máxima de caracteres comportados.

*Decodificador*
O decodificador irá ler os 32 primeiros bits para obter o tamanho N da mensagem, a partir disso lê-se os N canais seguintes e agrupa de 8 em 8 bits,
convertendo cada grupo de 8 bits (um byte) em caractere. 
## Requisitos

- Python 3
- Pillow
- NumPy
- Pathlib

Instalação das dependências:

```
python -m pip install pillow numpy pathlib
```

Recomenda-se usar um ambiente virtual:

```
python -m venv .venv
.venv\Scripts\activate
python -m pip install pillow numpy pathlib
```

No Linux e no macOS, a ativação é **source .venv/bin/activate**

## Uso

Execute a partir da pasta do projeto.

### Esconder uma mensagem

```
python EsteganografiaLSB.py esconderMensagem <caminho-imagem> "<mensagem>"
```

Exemplo:

```
python EsteganografiaLSB.py esconderMensagem teste.png "Ninho de mafagafos"
```

A imagem é salva no diretório atual com o nome `<nome-da-imagem>-codificado.png`. A imagem original não é alterada. Use aspas na mensagem se ela tiver espaços.

### Ler uma mensagem

```
python EsteganografiaLSB.py lerMensagem <teste-codificado.png>
```

A mensagem escondida é exibida no terminal.

## Limitações conhecidas

- **Mensagem grande demais:** se a mensagem não couber na imagem, o programa exibe "A mensagem não cabe na imagem".
- **Caracteres acima do código 255** (por exemplo, emojis): não são suportados, pois cada caractere ocupa exatamente 8 bits. Letras acentuadas do português e letras maiúsculas e minúsculas funcionam.
- **Compatibilidade de arquivos:** o LSB pode ser aplicado idealmente nos formatos: PNG, BMP, TIFF, WebP lossless, QOI, TGA, PPM, PGM, PBM. Entretanto, a aplicação do LSB fará com que as imagens PNG percam a transparência, porque todas as imagens são convertidas para o formado RGB, perdendo o canal alfa caso a imagem possua.
- **Sem validação na leitura:** em uma imagem sem mensagem escondida, a saída é indefinida e o programa pode exibir lixo ou falhar.
