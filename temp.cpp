// -------- PIN DEFINITIONS --------
int sensorPin = A0;   // Soil moisture sensor (AO)
int buzzerPin = 8;    // Buzzer
int relayPin  = 7;    // Relay (motor control)

// Adjust threshold after testing values in Serial Monitor
int dryThreshold = 600;

// -------- SETUP --------
void setup()
{
  pinMode(buzzerPin, OUTPUT);
  pinMode(relayPin, OUTPUT);

  digitalWrite(relayPin, HIGH);   // Relay OFF initially (active LOW)

  Serial.begin(9600);
}

// -------- LOOP --------
void loop()
{
  int moistureValue = analogRead(sensorPin);

  Serial.print("Moisture Value: ");
  Serial.println(moistureValue);

  // If soil is DRY
  if (moistureValue > dryThreshold)
  {
    digitalWrite(relayPin, LOW);  // Motor ON
    tone(buzzerPin, 1000);        // Buzzer ON
    Serial.println("DRY - Motor & Buzzer ON");
  }
  else // Soil is WET
  {
    digitalWrite(relayPin, HIGH); // Motor OFF
    noTone(buzzerPin);            // Buzzer OFF
    Serial.println("WET - Motor & Buzzer OFF");
  }

  delay(1000);
}