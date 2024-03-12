import os
import tempfile
import pytest
from file_info import get_files_info

@pytest.fixture
def sample_dir_structure():
    with tempfile.TemporaryDirectory() as tmp_dir:
        os.makedirs(os.path.join(tmp_dir, 'subdir'))
        with open(os.path.join(tmp_dir, 'file1.txt'), 'w') as f:
            f.write('Hello, World!')
        with open(os.path.join(tmp_dir, 'file2.py'), 'w') as f:
            f.write('print("Python")')
        yield tmp_dir

def test_get_files_info(sample_dir_structure):
    files_info = get_files_info(sample_dir_structure)
    assert len(files_info) == 3
    assert files_info[0].name == 'subdir'
    assert files_info[0].extension == ''
    assert files_info[0].is_directory is True
    assert files_info[0].parent_directory == os.path.basename(sample_dir_structure)