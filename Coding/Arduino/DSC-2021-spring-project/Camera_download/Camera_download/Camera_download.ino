#include "esp_camera.h"
#include <WiFi.h>
#define CAMERA_MODEL_AI_THINKER
#include "cameraconfig.h"

//와이파이 아이디&비밀번호
const char* ssid = "*********";
const char* password = "*********";

void startCameraServer();




void setup() {
  Serial.begin(115200);
  Serial.setDebugOutput(true);
  Serial.println();

  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;
  
  if(psramFound()){
    config.frame_size = FRAMESIZE_UXGA;
    config.jpeg_quality = 10;
    config.fb_count = 2;
  } else {
    config.frame_size = FRAMESIZE_SVGA;
    config.jpeg_quality = 12;
    config.fb_count = 1;
  }


  //init
  
  // camera init
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }

  // SD camera init
  card_err = init_sdcard();
  if (card_err != ESP_OK)
  {
    Serial.printf("SD Card init failed with error 0x%x", card_err);
    return;
  }



  //drop down frame size for higher initial frame rate
  sensor_t * s = esp_camera_sensor_get();
  s->set_framesize(s, FRAMESIZE_QVGA);

  //와이파이 연결
  WiFi.begin(ssid, password);

  //와이파이 연결시까지 ... 출력, 연결되면 신호 출력
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");

  startCameraServer();

  //연결된 주소 출력
  Serial.print("Camera Ready! Use 'http://");
  Serial.print(WiFi.localIP());
  Serial.println("' to connect");

  // ftp 서버용 아이디&비밀번호 세팅
  ftpSrv.begin("esp", "esp");
  digitalWrite(33, HIGH);
}

















void setup2() {
  print_local_address();
  
  if (init_wifi())
  { // Connected to WiFi
    internet_connected = true;
    Serial.println("Internet connected");
    init_time();
    time(&now);
  }

  //init with high specs to pre-allocate larger buffers
  if (psramFound())
  {
    config.frame_size = FRAMESIZE_UXGA;
    config.jpeg_quality = 1;
    config.fb_count = 2;
  }
  else
  {
    config.frame_size = FRAMESIZE_SVGA; // svga 12 fails due to jpg 60000
    config.jpeg_quality = 12;
    config.fb_count = 1;
  }

  // 200 ms x 150 frames = 30 seconds     is 3 MB indoors
  // 200 ms x 300 frames = 1 minute       is about 6MD indoor
  // 20 ms x 3000 frames = 10 minute      is 60 MB indoor
  // burst 1000 frames gives 8 fps rather than 5, so 2 minutues 20 MB indoor

  startCameraServer();


  sprintf(localip, "%s", WiFi.localIP().toString().c_str());
  Serial.print("localip ");
  Serial.println(localip);

  //
  //  startup defaults  -- EDIT HERE
  //  zzz

  sensor_t *s = esp_camera_sensor_get();
  s->set_framesize(s, FRAMESIZE_VGA);
  s->set_quality(s, 10);
  do_fb(); // do a couple captures to make sure camera has new config
  do_fb();

  framesize = 6; // vga
  repeat = 100;  // 100 videos
  xspeed = 1;    // playback at 1 x realtime
  gray = 0;      // not gray

  quality = 10;           // quality 10 - pretty good.  Goes from 0..63, but 0-5 sometimes fails on bright scenery (jpg too big for ESP32CAM system)
  capture_interval = 200; // 200 milli-secconds per frame
  total_frames = 9000;    // 9000 frames x 200 ms = 1800 sec = 30 min

  xlength = total_frames * capture_interval / 1000;

  newfile = 0;   // no file is open  // don't fiddle with this!
  recording = 1; // start recording on reboot without sending a command
}

void loop() {
  delay(10000);
}
