# base64_emoji

Inspired by [base64-emoji](https://github.com/watson/base64-emoji), this python module
allows for encoding of string objects into emoji and back.

![emojo-all-the-things](https://cloud.githubusercontent.com/assets/10602/8368864/31a7982c-1b7e-11e5-8731-d1728ddfbafa.jpg)

## Usage

```python
import base64_emoji

encoded = base64_emoji.encode('Hello World')
decoded = base64_emoji.decode(encoded)

print(encoded) # => 🍕📙🕡🌵🎎📙🚢😮🕡🐗🏦🕤🎎📙🕖📫
print(decoded) # => Hello World
```

## License

MIT
