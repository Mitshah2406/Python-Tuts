import zlib
import base64


def compress(input, output):
    data = open(input, 'r').read()
    data_bytes = bytes(data, 'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes, 9))
    decoded_data = compressed_data.decode('utf-8')
    compressed_file = open(output, 'w')
    compressed_file.write(decoded_data)


def decompress(input,output):
    file__content = open(input, 'r').read()
    encoded_data = file__content.encode('utf-8')
    decompressed_data = zlib.decompress(base64.b64decode(encoded_data))
    decoding = decompressed_data.decode()
    otfile = open(output,'w')
    otfile.write(decoding)


