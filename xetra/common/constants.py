""" file to store constants"""
from enum import Enum
"""kieu du lieu hang so"""
class S3FileTypes(Enum):
    """support file type for s3bucketconnector"""
    CSV='csv'
    PARQUET='parquet'

class MetaProcessFormat(Enum):

    META_DATE_FORMAT='%Y-%m-%d'
    META_PROCESS_FORMAT='%Y-%m-%d %H:%M:$S'
    META_SOURCE_COL='source_date'
    META_PROCESS_COL='date_processing'
    META_FILE_FORMAT='csv'