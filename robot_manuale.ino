int E1 = 6;   //controllo potenza motore
int M1 = 7;  //controllo direzione motore
int E2 = 5;
int M2 = 4;
int value = 128;  //velocità motori
int cmd;  //comando inserito
char verso_M1 = LOW;
char verso_M2 = LOW;

void setup() {
  Serial.begin(9600);
  pinMode(M1, OUTPUT);   
  pinMode(M2, OUTPUT); 
}

void loop() {

    if (Serial.available() > 0) {
      cmd = Serial.read();
      Serial.flush();
      
      switch(cmd) {

        case 'w': {  //Avanti
          digitalWrite(M1, LOW);    //imposta direzione rotazione motore
          digitalWrite(M2, LOW);
          analogWrite(E1, value);   //Controllo velocità PWM
          analogWrite(E2, value);
          verso_M1 = LOW;
          verso_M2 = LOW;
          delay(100);
        } break;

        case 'd': {  //Destra
          digitalWrite(M1, verso_M1);
          analogWrite(E1, value);   
          analogWrite(E2, '0');
          delay(100);
        } break;

        case 'a': {  //Sinistra
          digitalWrite(M2, verso_M2);
          analogWrite(E2, value);   
          analogWrite(E1, '0');
          delay(100);
        } break;

        case 's': {  //Indietro
          digitalWrite(M1, HIGH);
          digitalWrite(M2, HIGH);
          analogWrite(E2, value);   
          analogWrite(E1, value);
          verso_M1 = HIGH;
          verso_M2 = HIGH;
          delay(100);
        } break;
        
        case 'q': {  //Ruota Sinistra
          digitalWrite(M1, HIGH);
          digitalWrite(M2, LOW);
          analogWrite(E1, value);   
          analogWrite(E2, value);
          delay(100);
        } break;

        case 'e': {  //Ruota Destra
          digitalWrite(M1, LOW);
          digitalWrite(M2, HIGH);
          analogWrite(E1, value);   
          analogWrite(E2, value);
          delay(100);
        } break;

        case '1': {  //velocità 1 = 35%
          value = 89;
        } break;

        case '2': {  //velocità 2 = 50%
          value = 128;
        } break;

        case '3': {  //velocità 2 = 75%
          value = 192;
        } break;

        case '4': {  //velocità 2 = 100%
          value = 255;
        } break;      

        case '0': case 'c': {  //Stop
          analogWrite(E1, 0);  
          analogWrite(E2, 0);
          delay(100);
        } break;

      }  //fine switch

    }  //fine if

}  //fine loop
