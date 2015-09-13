#coding=utf-8
import json, os, base64, sys

path = os.path.dirname(__file__)
emojis = json.load(open(os.path.join(path, "emojis.json")))
chars = json.load(open(os.path.join(path, "mime.json")))


encode_dict = dict(zip(chars, emojis))
decode_dict = dict(zip(emojis, chars))

if sys.version_info.major == 2:
	emojisize = 2
	fastrange = xrange
	requiredtype = str
	charconvert = str
else:
	emojisize = 1
	fastrange = range
	def requiredtype(buf):
		return bytes(buf, 'utf8')
	charconvert = chr



def encode(buf):
	buf = requiredtype(buf)
	b64buf = base64.b64encode(buf)
	return "".join(map(lambda x: encode_dict[charconvert(x)], b64buf))

def decode(buf):
	splitbuf = [buf[i*emojisize:i*emojisize+emojisize] for i in fastrange(int(len(buf)/emojisize))]
	b64buf = "".join(map(lambda x: decode_dict[x], splitbuf))
	return base64.b64decode(requiredtype(b64buf)).decode()