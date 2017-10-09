from boto3.s3.transfer import S3Transfer
import boto3
import os
import sys
import threading
from botocore.exceptions import ClientError
# Create an S3 client

class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()

class S3components(object):
 s3 = boto3.client('s3')
 s3_resource = boto3.resource('s3')
 transfer = S3Transfer(s3)
 # max size in bytes before uploading in parts. between 1 and 5 GB recommended
 MAX_SIZE = 20 * 1000 * 1000
 # size of parts when uploading in parts
 PART_SIZE = 6 * 1000 * 1000

 def __init__( self, bucket_name, file_dir,file_name,key_name):
    self.bucket_name = bucket_name
    self.file_dir = file_dir
    self.file_name = file_name
    self.key_name = key_name
    self.ProgressPercentage = []

 def S3_LIST_BUCKET(self):
 # Call S3 to list current buckets
    response = S3components.s3.list_buckets()
 # Get a list of all bucket names from the response
    buckets = [bucket['Name'] for bucket in response['Buckets']]
 # Print out the bucket list
    print("Bucket List: %s" % buckets)

 def S3_CREATE_BUCKET(self):
     print (self.bucket_name)
     try:
        S3components.s3.create_bucket(Bucket=self.bucket_name)
     except Exception as e:
      print (e)

 def S3_CREATE_BUCKET(self):
    try:
        S3components.s3.create_bucket(Bucket=self.bucket_name)
    except Exception as e:
        print(e)

 def S3_create_key(self):
     try:
         S3components.s3.put_object(Bucket=self.bucket_name, Key=self.key_name + '/')
     except Exception as e:
         print(e)

 def percent_cb(self,complete, total):
     self.complete = complete
     self.total = total
     sys.stdout.write('.')
     sys.stdout.flush()

 def S3_UPLOAD_FILE(self):
     try:
        if self.key_name != None:
            for root, dirs, files in os.walk(self.file_dir):
                for file in files:
                    S3components.transfer.upload_file(self.file_dir + file, self.bucket_name, self.key_name+'/'+file,callback=ProgressPercentage(self.file_dir + file))
        else:
                for root, dirs, files in os.walk(self.file_dir):
                    for file in files:
                        S3components.transfer.upload_file(self.file_dir + file, self.bucket_name, file,callback=ProgressPercentage(self.file_dir + file))
     except Exception as e:
        print(e)

 def S3_DOWNLOAD_FILE(self):
        try:
          if self.key_name != None:
              list = S3components.s3.list_objects(Bucket=self.bucket_name)['Contents']
              print (list)
              for s3_key in list:
                  s3_object = s3_key['Key']
                  if s3_object.startswith(self.key_name+"/"):
                    if not os.path.exists(self.file_dir+self.key_name):
                      os.makedirs(self.file_dir+self.key_name)
                    if not s3_object.endswith(self.key_name+"/"):
                      S3components.s3.download_file(self.bucket_name, s3_object, self.file_dir+s3_object)

          else:
              response = S3components.s3.list_buckets()
              bucket = S3components.s3_resource.Bucket(self.bucket_name)
              for object in bucket.objects.all():
                  bucket.download_file(self.file_name, self.file_dir + self.file_name)
                  # S3components.transfer.download_file(self.bucket_name,self.file_name,self.file_dir)
        except Exception as e:
                print(e)

 def S3_CREATE_DIR(self):
     try:
         for root, dirs, files in os.walk(self.file_dir):
             for file in files:
                S3components.s3.put_object(Bucket=self.bucket_name, Key=self.key_name + '/' + file )
     except Exception as e:
         print(e)

 def S3_DELETE(self):
    s3 = boto3.resource('s3')
    if self.key_name!= None and self.bucket_name != None:
        print('here1')
        bucket = s3.Bucket(self.bucket_name)
        objects_to_delete = []
        for obj in bucket.objects.filter(Prefix=self.key_name +'/'):
         objects_to_delete.append({'Key': obj.key})
        bucket.delete_objects(Delete={'Objects': objects_to_delete})

    if self.key_name!= None and self.bucket_name != None and self.file_name != None:
        print('here2')
        bucket = s3.Bucket(self.bucket_name)
        objects_to_delete = []
        for obj in bucket.objects.filter(Prefix=self.key_name + '/'+self.file_name):
         objects_to_delete.append({'Key': obj.key})
        bucket.delete_objects(Delete={'Objects': objects_to_delete})

    if self.key_name == None and self.bucket_name != None and self.file_name != None and  self.file_name != 'ALL':
        print('here3')
        bucket = s3.Bucket(self.bucket_name)
        objects_to_delete = []
        for obj in bucket.objects.filter(Prefix=self.file_name):
            objects_to_delete.append({'Key': obj.key})
        bucket.delete_objects(Delete={'Objects': objects_to_delete})

    if self.key_name == None and self.bucket_name != None and self.file_name == 'ALL':
        bucket = s3.Bucket(self.bucket_name)
        bucket.objects.all().delete()

    if self.key_name == None and self.bucket_name != None and self.file_name == None:
        S3components.s3.delete_bucket(Bucket=self.bucket_name)


#s3comp = S3components('pybucket1982','C:/','README.txt',None)
#s3comp.S3_LIST_BUCKET()
#s3comp.S3_CREATE_BUCKET()
#s3comp.S3_UPLOAD_FILE_BUCKET()
s3comp = S3components('pydevbucket','C:/Users/Jayanthi/Desktop/EC/','ALL',None)
#s3comp.S3_create_key()
#s3comp.S3_UPLOAD_FILE()
#s3comp.S3_DOWNLOAD_FILE()
#s3comp.S3_CREATE_DIR()
s3comp.S3_DELETE()



