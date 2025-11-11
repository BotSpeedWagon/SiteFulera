import asyncio
import websockets
import cv2
import base64

async def enviar_frames():
    uri = "ws://187.75.79.34:8765"  # mesmo servidor WebSocket do seu projeto
    print("[INFO] Conectando ao servidor WebSocket...")
    ws = await websockets.connect(uri)
    await ws.send("CameraSender")
    print("[INFO] Identificado como CameraSender")  

    # Abre webcam padrão (índice 0)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("[ERRO] Não foi possível acessar a webcam")
        return

    print("[INFO] Iniciando envio de frames...")
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("[WARN] Falha ao capturar frame")
                await asyncio.sleep(0.1)
                continue

            # Codifica o frame em JPEG
            _, jpeg = cv2.imencode(".jpg", frame)

            # Codifica em Base64 para enviar via WebSocket
            frame_b64 = base64.b64encode(jpeg).decode("utf-8")
            await ws.send("FRAME:" + frame_b64)

            await asyncio.sleep(1 / 30)  # 30 FPS

    except Exception as e:
        print("[ERRO]", e)

    finally:
        cap.release()
        await ws.close()
        print("[INFO] Encerrando conexão e liberando recursos")

if __name__ == "__main__":
    asyncio.run(enviar_frames())
