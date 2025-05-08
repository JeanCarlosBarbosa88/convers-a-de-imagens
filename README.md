Conversão de Imagens para Tons de Cinza e Preto e Branco com Python
Este script Python utiliza a biblioteca Pillow para converter imagens coloridas em versões em tons de cinza e preto e branco. Ele oferece uma maneira simples de transformar imagens para análise visual ou processamento posterior.

Requisitos
Python 3.x

Biblioteca Pillow (PIL Fork)

Para instalar a biblioteca Pillow, execute o seguinte comando:

bash
Copiar
Editar
pip install pillow
Funções Implementadas
1. converter_para_cinza(imagem)
Converte uma imagem colorida para tons de cinza utilizando a fórmula de luminância:

ini
Copiar
Editar
L = 0.3 * R + 0.59 * G + 0.11 * B
Onde:

R, G, B são os valores das cores vermelha, verde e azul do pixel.

2. converter_para_preto_branco(imagem, limiar=128)
Converte a imagem em tons de cinza para preto e branco, aplicando um limiar:

Pixels com valor de luminância maior ou igual ao limiar são convertidos para branco (255).

Pixels com valor de luminância menor que o limiar são convertidos para preto (0).

O valor padrão do limiar é 128, mas pode ser ajustado conforme necessário.

3. gerar_copias(imagem_original)
Gera e salva duas cópias da imagem original:

Uma em tons de cinza: salva como imagem_tons_de_cinza.jpg.

Uma em preto e branco: salva como imagem_preto_branco.jpg.

Como Usar
Substitua 'jean.jpg' pelo caminho da sua imagem no código:

python
Copiar
Editar
imagem_original = 'jean.jpg'
Execute o script Python:

bash
Copiar
Editar
python nome_do_arquivo.py
As imagens convertidas serão salvas no mesmo diretório com os nomes especificados.

Exemplo de Uso
python
Copiar
Editar
from PIL import Image

Caminho da imagem original
imagem_original = 'jean.jpg'

Gerar cópias convertidas
gerar_copias(imagem_original)
Observações
A biblioteca Pillow é uma poderosa ferramenta para manipulação de imagens em Python. Ela oferece funcionalidades como abertura, salvamento, conversão e aplicação de filtros em imagens. Para mais informações, consulte a documentação oficial.

O método convert('L') da Pillow é utilizado para converter a imagem para escala de cinza. O modo 'L' representa uma imagem em escala de cinza de 8 bits.

A conversão para preto e branco é realizada aplicando um limiar sobre a imagem em escala de cinza. Isso resulta em uma imagem binária, onde os pixels são apenas preto ou branco.
