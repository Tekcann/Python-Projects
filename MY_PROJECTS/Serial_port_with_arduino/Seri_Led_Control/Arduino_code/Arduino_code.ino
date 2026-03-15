
#define led 13

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  if(Serial.available()){
    char a = Serial.read();

    if(a == '1'){
      digitalWrite(led, 1);
    }
    else if(a == '0'){
      digitalWrite(led, 0);
    }
  }
}
