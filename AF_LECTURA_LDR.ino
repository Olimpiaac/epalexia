void setup() {
  Serial.begin(9600);
}

void loop() {
  int ldrValue = analogRead(A4); // Este es el pin de mi LDR de la placa de Arduino

  if (ldrValue < 100) {
    Serial.println(0);
    Serial.println("LDR_OFF");
  }
  else {
    Serial.println(1);
    Serial.println("LDR_ON");
  }

  delay(1000);
}