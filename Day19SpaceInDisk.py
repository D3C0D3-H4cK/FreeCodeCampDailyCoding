def number_of_photos(photo_size_mb, drive_size_gb):
    sizeGb = drive_size_gb * 1000
    totalSpace = sizeGb // photo_size_mb
    return int(totalSpace)
number_of_photos(3.5, 750)