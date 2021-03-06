import io
import os
from dotenv import load_dotenv

from fss3wrap.afs_interface import Afs

import pytest


# [x] FS [x] S3 : test_bytes_write
# [x] FS [x] S3 : test_directory_list
# [x] FS_BIN [x] FS_TXT [x] S3_BIN [x] S3_TXT : test_file_copy
# [x] FS_BIN [x] FS_TXT [x] S3_BIN [x] S3_TXT : test_file_descriptor_copy
# [x] FS_BIN [x] S3_BIN : test_file_fd_bin
# [x] FS_TXT [x] S3_TXT : test_file_fd_text
# [x] FS_BIN [x] S3_BIN : test_file_fd_custom_bucket_bin
# [x] FS_BIN [x] S3_BIN : test_file_md5
# [x] FS_BIN [x] S3_BIN : test_file_read_bin
# [x] FS_BIN [x] S3_BIN : test_file_read_text
# [x] FS_BIN [x] S3_BIN : test_file_remove
# [x] FS_BIN [x] S3_BIN : test_reinit

load_dotenv(override=True)

pytest.aws_bucket_1 = os.getenv('AWS_BUCKET_1')
pytest.aws_bucket_2 = os.getenv('AWS_BUCKET_2')

pytest.fs_path_local = os.getenv('FS_PATH_LOCAL')
pytest.fs_path_remote = os.getenv('FS_PATH_REMOTE')

pytest.s3_parameters = {
    'access_key_id': os.getenv('AWS_ACCESS_KEY_ID'),
    'secret_access_key': os.getenv('AWS_SECRET_ACCESS_KEY'),
    'bucket': pytest.aws_bucket_1
}

pytest.s3_used = (os.getenv('AWS_S3_USED') == 'True')

pytest.afs = Afs(pytest.s3_used, pytest.s3_parameters, pytest.aws_bucket_1, pytest.fs_path_remote)

def test_bytes_write():
    try:
        destination_path = 'extra_sub_folder'
        destination_file = 'destination_file'
        mbytes = b"some initial binary data: \x00\x01"

        pytest.afs.bytes_write(destination_path, destination_file, mbytes)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_directory_list():
    try:
        destination_path = 'extra_sub_folder'

        print(pytest.afs.directory_list(destination_path))
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_file_copy():
    try:
        source_path = pytest.fs_path_local
        source_file = 'LICENSE'
        destination_path = 'extra_sub_folder'
        destination_file = 'out_LICENSE'

        pytest.afs.file_copy(
            source_path,
            source_file,
            destination_path,
            destination_file)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_file_descriptor_copy():
    try:
        source_path = pytest.fs_path_local
        source_file = 'LICENSE'
        destination_path = 'extra_sub_folder'
        destination_file = 'out_LICENSE'

        with open("{}/{}".format(source_path, source_file), "rb") as fd:
            pytest.afs.file_descriptor_copy(fd, destination_path, destination_file)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))

def test_filelike_copy():
    try:

        destination_path = 'extra_sub_folder'
        destination_file = 'foo'
        b = io.BytesIO(b'bar')

        pytest.afs.file_descriptor_copy(b, destination_path, destination_file)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))

def test_file_fd_bin():
    try:
        destination_path = 'extra_sub_folder'
        destination_file = '4x4.jpg'

        fd_bin = pytest.afs.file_fd_bin(destination_path, destination_file)
        print(fd_bin.read().hex())
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_file_fd_text():
    try:
        destination_path = 'extra_sub_folder'
        destination_file = 'out_LICENSE'

        print(
            pytest.afs.file_fd(
                destination_path,
                destination_file).read())
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_file_fd_custom_bucket_bin():
    try:
        custom_bucket = pytest.aws_bucket_2


        destination_path = 'extra_sub_folder'
        destination_file = '4x4.jpg'
        pytest.afs = Afs(pytest.s3_used, pytest.s3_parameters, custom_bucket, pytest.fs_path_remote)

        fd_bin = pytest.afs.file_fd_bin(destination_path, destination_file)
        print(fd_bin.read().hex())

        # reset
        pytest.afs = Afs(pytest.s3_used, pytest.s3_parameters, pytest.aws_bucket_1, pytest.fs_path_remote)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_file_md5():
    try:
        file_path = 'extra_sub_folder'
        file_name = '4x4.jpg'

        print(pytest.afs.file_md5(file_path, file_name))
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_file_read_bin():
    try:
        destination_path = 'extra_sub_folder'
        destination_file = '4x4.jpg'

        fread = pytest.afs.file_read_bin(destination_path, destination_file)
        print(fread)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_file_read_text():
    try:
        destination_path = 'extra_sub_folder'
        destination_file = 'out_LICENSE'

        fread = pytest.afs.file_read(destination_path, destination_file)
        print(fread)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_file_remove():
    try:
        file_path = 'extra_sub_folder'
        file_name = 'out_LICENSE'

        pytest.afs.file_remove(file_path, file_name)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))


def test_reinit():
    try:
        pytest.afs.reinit(pytest.s3_used, pytest.s3_parameters, pytest.aws_bucket_2, pytest.fs_path_remote)

        source_path = pytest.fs_path_local
        source_file = 'LICENSE'
        destination_path = 'extra_sub_folder'
        destination_file = 'out_LICENSE'

        pytest.afs.file_copy(
            source_path,
            source_file,
            destination_path,
            destination_file)
    except BaseException as e:
        pytest.fail("BaseException => {}".format(str(e)))