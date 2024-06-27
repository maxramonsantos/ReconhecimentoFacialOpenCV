import cv2
import os
import numpy as np

# Criar reconhecedor facial LBPH
lbph = cv2.face.LBPHFaceRecognizer_create()

# Função para criar a pasta "fotos" se ela não existir
def criar_pasta_fotos():
    if not os.path.exists("fotos"):
        os.makedirs("fotos")

# Cria a pasta "fotos"
criar_pasta_fotos()

# Carrega o classificador dos olhos
classificadorOlho = cv2.CascadeClassifier("haarcascade_eye.xml")

# Carrega o classificador de faces
classificador = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Inicia a captura de vídeo
camera = cv2.VideoCapture(0)

# Inicializa variáveis de controle
amostra = 1
numeroAmostras = 25
id = input("Digite seu identificador: ")
largura, altura = 220, 220

print("Capturando as faces...")

while True:
    # Lê um frame da câmera
    conectado, imagem = camera.read()
    
    # Converte a imagem para escala de cinza
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # Detecta faces na imagem
    facesDetectadas = classificador.detectMultiScale(imagemCinza,
                                                     scaleFactor=1.5,
                                                     minSize=(150, 150))
    
    # Para cada face detectada, desenha um retângulo ao redor dela
    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

        # Detecta olhos na região da face
        regiao = imagem[y:y + a, x:x + l]
        regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)

        # Para cada olho detectado, desenha um retângulo ao redor dele
        for (ox, oy, ol, oa) in olhosDetectados:
            cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

    # Captura a imagem da face detectada e salva quando a tecla 'q' é pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        if np.average(imagemCinza) > 110:
            if amostra <= numeroAmostras:
                imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
                cv2.imwrite(f"fotos/pessoa.{id}.{amostra}.jpg", imagemFace)
                print(f"[foto {amostra} capturada com sucesso]")
                amostra += 1

    # Captura a tecla pressionada
    key = cv2.waitKey(1)
    if key & 0xFF == 27:  # 27 é o código ASCII da tecla 'ESC'
        break

    # Mostra a imagem com as detecções
    cv2.imshow("Face", imagem)
    
    # Verifica se o número de amostras desejado foi atingido
    if amostra > numeroAmostras:
        break

print("Faces capturadas com sucesso")
camera.release()
cv2.destroyAllWindows()
