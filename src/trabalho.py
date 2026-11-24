import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

foto = Image.open("imagens/foto.jpg").convert("RGB")
img = np.array(foto)
altura, largura = img.shape[:2]

st.header("2. Brilho")
brilho = st.slider("Ajuste do brilho", -100, 100, 0)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
hsv[:, :, 2] = np.clip(hsv[:, :, 2].astype(int) + brilho, 0, 255).astype(np.uint8)
imagem_brilho = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
st.image(imagem_brilho, caption="Imagem com brilho ajustado")

st.header("8. Negativo")
negativo = 255 - img
st.image(negativo, caption="Negativo da imagem")

st.header("11. Espelhamento")
horizontal = cv2.flip(img, 1)
vertical = cv2.flip(img, 0)
st.image(horizontal, caption="Espelhamento horizontal")
st.image(vertical, caption="Espelhamento vertical")

st.header("9. Recorte")
lado_maximo = min(altura, largura)
lado = st.slider("Tamanho do recorte", 1, lado_maximo, lado_maximo)

if largura - lado > 0:
    x = st.slider("Posição horizontal do recorte", 0, largura - lado, 0)
else:
    x = 0

if altura - lado > 0:
    y = st.slider("Posição vertical do recorte", 0, altura - lado, 0)
else:
    y = 0

recorte = img[y:y + lado, x:x + lado]
st.image(recorte, caption="Imagem recortada")

st.header("20. Pixel art")
passo = st.slider("Tamanho dos pixels", 2, 50, 10)
nova_largura = max(1, largura // passo)
nova_altura = max(1, altura // passo)
reduzida = cv2.resize(img, (nova_largura, nova_altura), interpolation=cv2.INTER_NEAREST)
pixel_art = cv2.resize(reduzida, (largura, altura), interpolation=cv2.INTER_NEAREST)
st.image(pixel_art, caption="Efeito pixel art")
