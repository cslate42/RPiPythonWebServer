#include <bcm2835.h>

#include <stdio.h>
#include <unistd.h>

#include "error.h"

// see http://www.hertaville.com/rpipwm.html
// http://www.iot-programmer.com/index.php/books/22-raspberry-pi-and-the-iot-in-c/chapters-raspberry-pi-and-the-iot-in-c/35-raspberry-pi-iot-in-c-introduction-to-the-gpio?showall=&start=1
// http://www.airspayce.com/mikem/bcm2835/bcm2835_8h_source.html
// http://www.airspayce.com/mikem/bcm2835/group__constants.html#ga63c029bd6500167152db4e57736d0939

#ifndef GPIO_H_
    #define GPIO_H_

    #define GPIO_PWM_MARKSPACE 1 // 1=mark space mode, 0 = balanced mode
    #define GPIO_PWM_ENABLE 1
    #define GPIO_PWM_DISABLE 0

    class GPIO {
    public:
        GPIO();
        void setup();
        int destroy();
        void setMode(RPiGPIOPin pin, bcm2835FunctionSelect mode);
        void setInput(RPiGPIOPin pin);
        void setOutput(RPiGPIOPin pin);
        void setPinsInput(uint32_t mask);
        void low(RPiGPIOPin pin);
        void lowMulti(uint32_t mask);
        void high(RPiGPIOPin pin);
        void highMulti(uint32_t mask);
        uint8_t digitalRead(RPiGPIOPin pin);
        uint8_t eventRead(RPiGPIOPin pin);
        uint32_t eventReadMulti(uint32_t mask);
        void setDetectRisingEdge(RPiGPIOPin pin);
        void clearPinEvent(RPiGPIOPin pin);
        void clearPinEvents(uint32_t mask);
        void pwmSetClock(bcm2835PWMClockDivider divisor);
        void pwmSetPin(RPiGPIOPin pin, uint8_t channel, float dutyCycle, uint32_t freq);
    private:

    };
#endif
