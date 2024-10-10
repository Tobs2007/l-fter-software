#include <FastLED.h>

FASTLED_USING_NAMESPACE


CRGB fan1[9];
CRGB fan2[9];
CRGB fan3[9];

#define BRIGHTNESS 100

void setup() {

  // tell FastLED about the LED strip configuration
  FastLED.addLeds<WS2811, 21, GRB>(fan1, 9).setCorrection(TypicalLEDStrip);
  FastLED.addLeds<WS2811, 22, GRB>(fan2, 9).setCorrection(TypicalLEDStrip);
  FastLED.addLeds<WS2811, 24, GRB>(fan3, 9).setCorrection(TypicalLEDStrip);

  // set master brightness control
  FastLED.setBrightness(BRIGHTNESS);
  delay(200);  // 3 second delay for recovery
  Serial.begin(9600);
  Serial.setTimeout(1);
  fan1[1] = CRGB(255, 255, 255);
  fan2[1] = CRGB(255, 255, 255);
  fan3[1] = CRGB(255, 255, 255);
  delay(200);
  FastLED.show();
  delay(2000);
}
void loop() {
  Serial.print("restart");
  while (!Serial.available()) {}
  int fan = Serial.readString().toInt();
  while (!Serial.available()) {}
  int index = Serial.readString().toInt();
  while (!Serial.available()) {}
  int R = Serial.readString().toInt();
  while (!Serial.available()) {}
  int G = Serial.readString().toInt();
  while (!Serial.available()) {}
  int B = Serial.readString().toInt();


  switch (fan) {
    case 0:
      fan1[index] = CRGB(R, G, B);
      break;
    case 1:
      fan2[index] = CRGB(R, G, B);
      break;
    case 2:
      fan3[index] = CRGB(R, G, B);
      break;
  }
  FastLED.show();
}