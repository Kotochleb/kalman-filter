# kalman-filter

The project was made for statistics course at university. It's goal was to simulate one of simplest
mobile robot's model. In this case robot was driving only in straight line. System input was it's acceleration
and observed state was velocity.

## State space matrices

Robot was represented with following matrices:

![equation](http://www.sciweavers.org/upload/Tex2Img_1591663436/render.png)


![equation](http://www.sciweavers.org/upload/Tex2Img_1591663496/render.png)


![equation](http://www.sciweavers.org/upload/Tex2Img_1591663511/render.png)

## Usage

To start simulation run `kalman.py`

Each sensor has its parameters inside class.
Class `DummySensor` can be used to represent any sensor with given noise covariance and sample time.

## Conclusions

`IMU`, `GPS` and `Encoder` sensor implementation doesn't work as it is intended for usage with Kalman filter.
They were designed to show thinks such as accelerometer drift. Sensor that works as it is intended for Kalman filter is `DummySensor` which have true white noise with known standard deqiation.
