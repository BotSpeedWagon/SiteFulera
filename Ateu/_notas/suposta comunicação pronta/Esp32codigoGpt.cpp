/*
#include <WiFi.h>
#include <WebSocketsClient.h>

const char* ssid = "NOME_DO_WIFI";
const char* senha = "SENHA_DO_WIFI";

WebSocketsClient webSocket;

void webSocketEvent(WStype_t type, uint8_t * payload, size_t length) {
  switch(type) {
    case WStype_CONNECTED:
      Serial.println("✅ Conectado ao servidor WebSocket!");
      webSocket.sendTXT("esp32"); // Identifica-se
      break;

    case WStype_TEXT:
      Serial.printf("📩 Mensagem recebida: %s\n", payload);
      if (strcmp((char*)payload, "girar") == 0) {
        Serial.println("➡️ Girando motor...");
      } else if (strcmp((char*)payload, "parar") == 0) {
        Serial.println("🛑 Parando motor...");
      }
      break;

    case WStype_DISCONNECTED:
      Serial.println("❌ Desconectado!");
      break;
  }
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, senha);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado!");

  webSocket.begin("192.168.x.x", 8765, "/"); // IP do PC que roda servidor_ws.py
  webSocket.onEvent(webSocketEvent);
  webSocket.setReconnectInterval(5000);
}

void loop() {
  webSocket.loop();
}
*/