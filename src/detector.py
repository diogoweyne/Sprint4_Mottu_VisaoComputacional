from ultralytics import YOLO
import cv2

class MotoDetector:
    def __init__(self, model_path="yolov8n.pt"):
        # Carrega o modelo YOLO (pré-treinado no COCO)
        self.model = YOLO(model_path)

    def detectar_motos(self, frame):
        # Predição
        results = self.model.predict(frame, conf=0.5, verbose=False)

        # Filtra somente motos (classe 3 = "motorbike" no dataset COCO)
        motos = []
        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                if cls_id == 3:  # 3 = motorbike
                    motos.append(box)

        return motos, results


from ultralytics import YOLO
import cv2, datetime

model = YOLO('yolov8n.pt')

def detectar_motos():
    cap = cv2.VideoCapture(0)
    resultado_deteccao = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        for r in results:
            for box in r.boxes:
                cls = model.names[int(box.cls)]
                if cls == 'motorcycle':
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
                    cv2.putText(frame, f"Moto detectada", (x1, y1-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

                    resultado_deteccao = {
                        "classe": cls,
                        "data_hora": datetime.datetime.now().isoformat()
                    }

        cv2.imshow("Detecção de Motos", frame)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    return resultado_deteccao
