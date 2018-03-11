#include "gpio.h"

GPIO::GPIO() {

}

void GPIO::setup()
{
    if ( ! bcm2835_init()) {
        throw new HardwareException("Unable to init hardware GPIO");
    }
}

int GPIO::destroy()
{
    return bcm2835_close();
}

void GPIO::setMode(RPiGPIOPin pin, bcm2835FunctionSelect mode) { bcm2835_gpio_fsel(pin, mode); }
void GPIO::setInput(RPiGPIOPin pin) { bcm2835_gpio_fsel(pin, BCM2835_GPIO_FSEL_INPT); }
void GPIO::setOutput(RPiGPIOPin pin) { bcm2835_gpio_fsel(pin, BCM2835_GPIO_FSEL_OUTP); }
void GPIO::setPinsInput(uint32_t mask) { bcm2835_gpio_set_multi(mask); }
void GPIO::low(RPiGPIOPin pin) { bcm2835_gpio_clr(pin); }
void GPIO::lowMulti(uint32_t mask) { bcm2835_gpio_clr_multi(mask); }
void GPIO::high(RPiGPIOPin pin) { bcm2835_gpio_set(pin); }
void GPIO::highMulti(uint32_t mask) { bcm2835_gpio_set_multi(mask); }
uint8_t GPIO::digitalRead(RPiGPIOPin pin) { return bcm2835_gpio_lev(pin); }
uint8_t GPIO::eventRead(RPiGPIOPin pin) { return bcm2835_gpio_eds(pin); }
uint32_t GPIO::eventReadMulti(uint32_t mask) { return bcm2835_gpio_eds(mask); }
void GPIO::setDetectRisingEdge(RPiGPIOPin pin) { bcm2835_gpio_ren(pin); }
void GPIO::clearPinEvent(RPiGPIOPin pin) { bcm2835_gpio_set_eds(pin); }
void GPIO::clearPinEvents(uint32_t mask) { bcm2835_gpio_set_eds(mask); }

void GPIO::pwmSetClock(bcm2835PWMClockDivider divisor) { bcm2835_pwm_set_clock(divisor); }
///
/// GPIO::pwmSetPin(RPiGPIOPin, uint8_t, uint32_t, uint32_t)
///
///
/// To enable pwm for a pin precede this call with setting the pin mode
///   see bcm2835_gpio_fsel()
/// To disable pwm change the pin mode
///
/// param RPiGPIOPin pin
/// param uint8_t channel
/// param float dutyCycle
/// param uint32_t freq
///
void GPIO::pwmSetPin(RPiGPIOPin pin, uint8_t channel, float dutyCycle, uint32_t freq)
{
    // https://raspberrypi.stackexchange.com/a/53855
    // TODO finish
    // base clock is 19.2MHz PWM clock
    // Clock divider is set to 16.
    // With a divider of 16 and a RANGE of 1024, in MARKSPACE mode,
    // the pulse repetition frequency will be
    // 1.2MHz/1024 = 1171.875Hz, suitable for driving a DC motor with PWM
    bcm2835_pwm_set_mode(channel, GPIO_PWM_MARKSPACE, GPIO_PWM_ENABLE);
    uint32_t range;
    // data is the PWM Pulse ratio = Data/Range where Data must be <= Range
    // TODO handle >1 multiplier? or just change to enums?
    // if ( dutyCycle < 0 || dutyCycle > 1.0 ) { throw new HardwareException("Duty cycle must be between 0 and 1");}
    uint32_t data = static_cast<uint32_t> (dutyCycle * range);
    bcm2835_pwm_set_data(channel, data);
    bcm2835_pwm_set_range(channel, range);
}
