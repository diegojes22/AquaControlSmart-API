import Utils

exampleFromESP32 : dict = {
    "description" : "Data from ESP32",
    "date" : Utils.date(),
    "time" : Utils.time(),
    "data" : {
        "pin" : 1,
        "value" : 55
    }
}