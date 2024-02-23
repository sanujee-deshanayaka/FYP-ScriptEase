import shutil


def compress_folder(folder_path, archive_format='zip'):
    """
    Compress a folder using shutil.make_archive.

    Parameters:
    - folder_path: The path of the folder to compress.
    - archive_format: The format of the archive (default is 'zip').

    Returns:
    - archive_path: The path of the compressed archive file.
    """
    # Generate the archive path
    archive_path = shutil.make_archive(folder_path, archive_format, folder_path)

    print(f"Folder '{folder_path}' compressed successfully. Archive file: {archive_path}")
    return folder_path
