"""connector and method accessing s3 bucket"""
import os
import logging
import boto3

class S3BucketConnector():
    """class interacting with s3"""
    def __init__(self,access_key:str,secret_key:str,endpoint_url:str,bucket_name:str):
        """
        access_key: param access_key for accessing s3
        secret_key: param secret_key for accessing s3
        endpoint_url : enpoint url to s3
        """
        self._logger=logging.getLogger(__name__)
        self.endpoint_url=endpoint_url
        self.session=boto3.Session(aws_access_key_id=os.environ[access_key],aws_secret_access_key=os.environ[secret_key])
        self._s3=self.session.resource(service_name='s3',endpoint_url=endpoint_url)
        self._bucket=self._s3.Bucket(bucket_name)

    def list_files_in_prefix(self,prefix):
        files = [obj.key for obj in self._bucket.objects.filter(Prefix=prefix)]
        return files

    def read_csv_to_df(self):
        pass

    def write_df_to_s3(self):
        pass
        
