resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-terrform-hw-s3-is689"  
}

resource "aws_s3_bucket_versioning" "versioning_example" {
  bucket = aws_s3_bucket.my_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}
