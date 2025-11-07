# main.py
from ultralytics import YOLO
import cv2
import datetime
from utils import salvar_deteccao



# Carrega o modelo YOLO (certifique-se de que o arquivo yolov8n.pt está na pasta)
model = YOLO("yolov8n.pt")

print("🚀 Iniciando detecção de motos... Pressione ESC para sair.")

cap = cv2.VideoCapture(0)  # usa a webcam padrão
if not cap.isOpened():
    print("❌ Erro: não foi possível acessar a câmera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Erro: não foi possível capturar frame.")
        break

    # Executa o modelo YOLO no frame
    results = model(frame)

    for r in results:
        for box in r.boxes:
            cls = model.names[int(box.cls)]
            if cls == "motorcycle":  # só salva se for moto
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, "Moto detectada", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

                dados = {
                    "classe": cls,
                    "data_hora": datetime.datetime.now().isoformat()
                }
                salvar_deteccao(dados)

    cv2.imshow("Detecção de Motos", frame)

    # Pressione ESC para sair
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
print("✅ Detecção encerrada.")
