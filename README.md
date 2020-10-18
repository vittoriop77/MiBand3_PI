# Xiaomi MiBand
Library to work with Xiaomi MiBand 2/3 (Support Python3)
[Read the Article here](https://medium.com/@a.nikishaev/how-i-hacked-xiaomi-miband-2-to-control-it-from-linux-a5bd2f36d3ad)

# Contributors & Info Sources
1) Base lib provided by [Leo Soares](https://github.com/leojrfs/miband2)
2) Additional debug & fixes was made by my friend [Volodymyr Shymanskyy](https://github.com/vshymanskyy/miband2-python-test). Also see his [cool JS library](https://github.com/vshymanskyy/miband-js)
3) Some info that really helped i got from [Freeyourgadget team](https://github.com/Freeyourgadget/Gadgetbridge/tree/master/app/src/main/java/nodomain/freeyourgadget/gadgetbridge/service/devices/huami/miband2)

# Run

1) Install dependencies
```sh
pip install -r requirements.txt
```
2) Turn on your Bluetooth
3) Unpair you MiBand from current mobile apps
4) Find out you MiBand MAC address
```sh
sudo hcitool lescan
```
5) Run this to auth device
```sh
python main.py MAC_ADDRESS --init
```
6) If you having problems(BLE can glitch sometimes) try this and repeat from 4)
```sh
sudo hciconfig hci0 reset
```

### If you have trouble installing bluepy

```sudo apt-get install libglib2-dev  ```

# Donate
If you like what im doing, you can send me some money for pepsi(i dont drink alcohol). https://www.paypal.me/creotiv
