# dht-sensor

This node.js module supports querying air temperature and relative humidity from a compatible DHT sensor.

## Installation
``` bash
$ npm install rpi-dht-sensor
```

## Usage

This module uses the [BCM2835](http://www.airspayce.com/mikem/bcm2835/) library that requires access to 
/open/mem. Because of this, you will typically run node with admin privileges.

The library works for DHT11, DHT22 and AM2302 sensors. You should create a new class of the sensor type you have specifying the Pin number. After this, you can start reading. On the first read, the sensor will be initialized. If the initialization fails, the read will throw an error.

The module supports only physical PIN numbering, GPIO numbers are not supported yet.


### Example
#### DHT22

This sample queries the AM2302 sensor connected to the PIN 3 every 5 seconds and displays the result on the console. 

``` javascript
var rpiDhtSensor = require('rpi-dht-sensor');

var dht = new rpiDhtSensor.DHT22(2);

function read () {
  var readout = dht.read();

    console.log('Temperature: ' + readout.temperature.toFixed(2) + 'C, ' +
        'humidity: ' + readout.humidity.toFixed(2) + '%');
    setTimeout(read, 5000);
}
read();
```

#### DHT 11 example

``` javascript
var rpiDhtSensor = require('rpi-dht-sensor');

var dht = new rpiDhtSensor.DHT11(2);

function read () {
  var readout = dht.read();

    console.log('Temperature: ' + readout.temperature.toFixed(2) + 'C, ' +
        'humidity: ' + readout.humidity.toFixed(2) + '%');
    setTimeout(read, 5000);
}
read();
```

### Verbose output

Verbose output from the module can be enabled by defining ```VERBOSE``` during the module compilation. For example, this can be enabled via the binging.gyp file:

``` javascript
{
  'targets': [
    {
      ...,
      'defines': [ 'VERBOSE']
    }
  ]
}
```

### Appendix A: Quick Node.js installation guide

There are many ways you can get Node.js installed on your Raspberry Pi but the following method is very convenient for getting started on the latest version, very quickly.
``` shell
$ wget http://node-arm.herokuapp.com/node_latest_armhf.deb 
$ sudo dpkg -i node_latest_armhf.deb
```


### References

[1]: Node.js latest release - http://nodejs.org/dist/latest/

[2]: BCM2835 - http://www.airspayce.com/mikem/bcm2835/

[3]: Node.js native addon build tool - https://github.com/TooTallNate/node-gyp

