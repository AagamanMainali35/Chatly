from datetime import timedelta

from fastapi import UploadFile
import boto3
from botocore.exceptions import ClientError
from  app.config.settings import settings
class StorageClient:
    def __init__(self):
        self.max_file_size = 5 * 1024 * 1024
        self.region="aap-southeast-1"
        self.client=boto3.client(
            "s3",
            endpoint_url=str(settings.s3_endpoint),
            aws_access_key_id=settings.s3_access_key,
            aws_secret_access_key=settings.s3_secret_key,
            region_name=self.region
        )
        
        self.public_client=boto3.client(
            "s3",
            endpoint_url=str(settings.s3_public_endpoint or settings.s3_endpoint),
            aws_access_key_id=settings.s3_access_key,
            aws_secret_access_key=settings.s3_secret_key,
            region_name=self.region
        )
        
    def check_bucket(self,name:str)-> None:
        try:
            self.client.head_bucket(Bucket=name)
        except ClientError as e:
            status=e.response["ResponseMetadata"]["HTTPStatusCode"]
            if status == 404:
                self.client.create_bucket(Bucket=name)
            else: 
                raise
                
    def validate_file(self, file: UploadFile,context_types:list[str])->None:
        file.file.seek(0,2) 
        file_size=file.file.tell()
        file.file.seek(0) # move cursor to start of the file if moved by other instances .
        
        if not file.filename:
            raise ValueError("Filename is required")

        if len(file.filename) > 255:
            raise ValueError("Filename is too long")
        
        if file_size > self.max_file_size:
            raise ValueError("Invalid file size only file with 5MB is allowed")
        
        if file.content_type not in context_types:
            raise ValueError("Invalid file type provided.")
        
    def create_bucket(self,bucket_name:str):
        return self.client.create_bucket(Bucket=bucket_name)
    
    def retrieve_file(self,file_name:str)->str:
        try:
            return self.public_client.generate_presigned_url(
                ClientMethod="get_object",
                Params={
                    "Bucket": "media",
                    "Key": file_name,
                },
                ExpiresIn=3600,  # seconds
            )
        except ClientError as e:
            raise
        
    
    def uploadfiles(self,bucket_name:str,bucket_key:str,file:UploadFile):
        self.validate_file(file , context_types=["image/jpeg",
                    "image/png"])
        self.client.upload_fileobj(
            file.file,
            bucket_name,
            bucket_key,
            ExtraArgs={
                "ContentType": file.content_type,
                "ContentDisposition": "inline",
            },
        )
        
    def delete_file(self,file_name:str,bucket_name:str)-> bool:
        result=self.client.delete_object(Bucket=bucket_name,Key=file_name)
        return result['ResponseMetadata']['HTTPStatusCode']
       
client=StorageClient()