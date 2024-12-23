#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "";
const char* password = "";
String apiRoute="https://mlew-api-iot.onrender.com/store?label=";
String alertRoute="https://mlew-api-iot.onrender.com/alert?type=";

bool isSent=false;
int moisture=34;

void setup() {
  Serial.begin(9600);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("Connected to WiFi");
  pinMode(moisture,INPUT);
}

void sendDataToDashboard(String api){
  if(WiFi.status()==WL_CONNECTED){
    HTTPClient http;
    http.begin(api);
    int responseCode=http.GET();
    if(responseCode>0){
      String response=http.getString();
      Serial.println(response);
      http.end();
    }
  }
}
void loop() {
    int m=analogRead(moisture);
    Serial.print("Moisture: ");
    Serial.println(m);
    
    sendDataToDashboard(apiRoute+"Moisture"+"&value="+String(m));
    delay(2000);
    

    if(m<500 && !isSent){
      sendDataToDashboard(alertRoute+"danger"+"&message=Heavy Water in the Field");
      isSent=true;
    } 
    if(m>4000){
      isSent=false;
    }
}