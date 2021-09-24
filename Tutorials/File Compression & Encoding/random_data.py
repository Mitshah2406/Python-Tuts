# Two libraries
import zlib
import base64
# open a random text file

data = open('randomdata.txt', 'r').read()
# convert string data into bytes using bytes fn.  ----NOTE:: utf-8 is the file format.
data_bytes = bytes(data, 'utf-8')
# compressing data using compress fn of zlib library upto max level and then encoding it using b64encode of base64 library
compressed_data = base64.b64encode(zlib.compress(data_bytes, 9))
# decoding the  compressed data
decoded_data = compressed_data.decode('utf-8')
# opening a new file amd saving the decoded data to it.
compressed_file = open('compressed.txt', 'w')
compressed_file.write(decoded_data)

decompressed_data = zlib.decompress(base64.b64decode(compressed_data))
print(decompressed_data)
