import time
import Adafruit_DHT
import RPi.GPIO as GPIO

# Sensor setup
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # GPIO pin where the DHT sensor is connected

# GPIO setup for fan and heating pad
FAN_PIN = 17   # GPIO pin for the fan
HEATER_PIN = 27  # GPIO pin for the heating pad

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)
GPIO.setup(HEATER_PIN, GPIO.OUT)

# Threshold values for temperature and humidity
TEMP_THRESHOLD_HIGH = 30  # High temperature in Celsius
TEMP_THRESHOLD_LOW = 20   # Low temperature for heating
HUMIDITY_THRESHOLD_HIGH = 70  # High humidity percentage

# Function to read sensor data
def read_sensor_data():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
        print("Failed to retrieve data from sensor")
        return None, None

# Function to control the fan and heater
def control_environment(temp, humidity):
    # Cooling (turn on fan if too hot or humid)
    if temp > TEMP_THRESHOLD_HIGH or humidity > HUMIDITY_THRESHOLD_HIGH:
        GPIO.output(FAN_PIN, GPIO.HIGH)  # Turn on fan
        GPIO.output(HEATER_PIN, GPIO.LOW)  # Turn off heater
        print("Cooling: Fan On")
    
    # Heating (turn on heater if too cold)
    elif temp < TEMP_THRESHOLD_LOW:
        GPIO.output(FAN_PIN, GPIO.LOW)  # Turn off fan
        GPIO.output(HEATER_PIN, GPIO.HIGH)  # Turn on heater
        print("Heating: Heater On")
    
    # Ideal condition (turn off fan and heater)
    else:
        GPIO.output(FAN_PIN, GPIO.LOW)  # Turn off fan
        GPIO.output(HEATER_PIN, GPIO.LOW)  # Turn off heater
        print("Ideal Conditions: Fan and Heater Off")

# Main loop
try:
    while True:
        # Read sensor data
        temp, humidity = read_sensor_data()
        
        if temp is not None and humidity is not None:
            print(f"Temperature: {temp:.1f}C  Humidity: {humidity:.1f}%")
            
            # Control the environment based on sensor data
            control_environment(temp, humidity)
        
        # Wait before reading again
        time.sleep(2)

except KeyboardInterrupt:
    print("Program stopped by user")
finally:
    GPIO.cleanup()  # Clean up GPIO settings when program ends
