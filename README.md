# lambda_icon-generator
AWS Lambda **event-driven** script to resize a image (icon auto generator)

Here is a simple script using 'Pillow' that recive a event-driven call from Amazon 'S3' by PUT method and process into other(s) images like a automatic icon generator

___

in order to use this you have to integrate the library *PIL/Pillow*, but not from 'pip install ...'

You need to use the Pillow from this repository.
Here is why: [Lambda-packages](https://github.com/arthurcohen/lambda-packages)