# Arthur Cohen
# 07/10/2016
# AWS Lambda event-driven script to resize a image (icon auto generator)
from PIL import Image
import boto3 as boto

region = 'us-east-1'
# buckets for read and write images
source = 'original-icon'
destination = 'resized-icon'


def lambda_handler(event, context):
    original = event['Records'][0]['s3']['object']['key']  # lambda event-driven call from a S3 by PUT method (upload)

    session = boto.Session(region_name=region)
    s3 = session.resource('s3')

    s3.meta.client.download_file(source, original, '/tmp/' + original)  # download the uploaded image

    with open('/tmp/' + original, 'r+b') as buff:
        with Image.open(buff) as image:
            image.thumbnail((64, 64))  # resize image
            image.save('/tmp/64' + original)  # write
            s3.meta.client.upload_file('/tmp/64' + original, destination, original[:-4] + '_64.png')  # upload to the destinationination bucket

# you can repeat this to any size you want

            image.thumbnail((32, 32))
            image.save('/tmp/32' + original)
            s3.meta.client.upload_file('/tmp/32' + original, destination, original[:-4] + '_32.png')

            image.thumbnail((16, 16))
            image.save('/tmp/16' + original)
            s3.meta.client.upload_file('/tmp/16' + original, destination, original[:-4] + '_16.png')
