TAR = {
        "compact": {
            "package": "tar",
            "options": "cvf",
            "pattern": "{package} {options} {destination} {sources}"
        },
        "extract": {
            "package": "tar",
            "options": "xvf",
            "pattern": "{package} {options} {sources}"
        },
        "suffix": [".tar", ".tar.xz"]
    }

TAR_GZ = {
        "extract": {
            "package": "tar",
            "options": "xvzf",
            "pattern": "{package} {options} {sources}"
        },
        "compact": {
            "package": "tar",
            "options": "cvzf",
            "pattern": "{package} {options} {destination} {sources}"
        },
        "suffix": [".tar.gz", ".tgz"]
    }

TAR_BZ = {
        "extract": {
            "package": "tar",
            "options": "xvjf",
            "pattern": "{package} {options} {sources}"
        },
        "compact": {
            "package": "tar",
            "options": "cvjf",
            "pattern": "{package} {options} {destination} {sources}"
        },
        "suffix": [".tar.tbz2", ".tar.bz2"]
    }

CONFIG_MIME_TYPE = {
    ('application/x-tar', None): TAR,
    ('application/x-tar', 'xz'): TAR,
    ('application/x-tar', 'gzip'): TAR_GZ,
    ('application/x-tar', 'bzip2'): TAR_BZ
}
 