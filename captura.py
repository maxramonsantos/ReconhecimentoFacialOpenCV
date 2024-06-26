import cv2
import os

# Função para criar a pasta "fotos" se ela não existir
def criar_pasta_fotos():
    if not os.path.exists("fotos"):
        os.makedirs("fotos")

# Cria a pasta "fotos"
criar_pasta_fotos()

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
        
        # Captura a imagem da face detectada e salva quando a tecla 'q' é pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            if amostra <= numeroAmostras:
                imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
                cv2.imwrite(f"fotos/pessoa.{id}.{amostra}.jpg", imagemFace)
                print(f"[foto {amostra} capturada com sucesso]")
                amostra += 1
    
    # Mostra a imagem com as detecções
    cv2.imshow("Face", imagem)
    
    # Verifica se o número de amostras desejado foi atingido
    if amostra > numeroAmostras:
        break
    
    # Captura a tecla pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        continue

print("Faces capturadas com sucesso")
camera.release()
cv2.destroyAllWindows

