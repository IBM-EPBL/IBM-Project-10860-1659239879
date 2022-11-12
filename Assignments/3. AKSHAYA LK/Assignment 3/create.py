import ibm_boto3
from ibm_botocore.client import Config
COS_ENDPOINT = "https://s3.ap.cloud-object-storage.appdomain.cloud"
COS_API_KEY_ID = "AmJGyvvLokxmS3pijauUv5G0vAyesRp0rNsRkdgybb7O"
COS_INSTANCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/b73d958a094b4bf9a2dbe4fac5ff884b:b0a3d87e-7850-483f-8b22-ffbc3b02613b::"
COS_STORAGE_CLASS = "ap-geo"
cos = ibm_boto3.client("s3", ibm_api_key_id=COS_API_KEY_ID, ibm_service_instance_id=COS_INSTANCE_CRN, config=Config(signature_version="oauth"), endpoint_url=COS_ENDPOINT)
cos.create_bucket(
    Bucket="flaskone",
    CreateBucketConfiguration={
        "LocationConstraint":COS_STORAGE_CLASS
    }
)