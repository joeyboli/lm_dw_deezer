from enum import StrEnum


class QUALITS(StrEnum):
	NICE = 'MP3_320'
	GOOD = 'FLAC'
	OK = 'MP3_128'


class COMPRESSION(StrEnum):
	ZSTD = 'ZSTD'
	ZIP = 'ZIP'
	GZIP = 'GZIP'


class BE_DW(StrEnum):
	C = 'C'
	RUST = 'RUST'


DEFAULT_FILE_FORMATS = [
	'{artist} - {title}',
	'{artist} - {title}',
	'{artist} - {title}',
	'{artist} - {title}',
	'{artist} - {title}',
	'{artist} - {title}',
	'{artist} {title}',
	'{album} {n_track}:{n_disk}',
	'{title} - {artists}'
]


DEFAULT_FOLDER_FORMATS = [
	'{album} - {artists}',
	'{artist} - {album}'
]
