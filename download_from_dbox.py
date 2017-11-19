import urllib.request
import io
import gzip

def download_from_dbox(url,out_file):
    """ Downloading file from dropbox url, decompress and write it to out_file """

    response = urllib.request.urlopen(url)
    compressed_file = io.BytesIO(response.read())
    decompressed_file = gzip.GzipFile(fileobj=compressed_file)

    with open(out_file, 'wb') as outfile:
        outfile.write(decompressed_file.read())

    print("Download " + out_file[:-4] + " from dropbox succeed.")
