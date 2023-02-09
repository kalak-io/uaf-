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
        "compact": {
            "package": "tar",
            "options": "cvzf",
            "pattern": "{package} {options} {destination} {sources}"
        },
        "extract": {
            "package": "tar",
            "options": "xvzf",
            "pattern": "{package} {options} {sources}"
        },
        "suffix": [".tar.gz", ".tgz"]
    }

TAR_BZ = {
        "compact": {
            "package": "tar",
            "options": "cvjf",
            "pattern": "{package} {options} {destination} {sources}"
        },
        "extract": {
            "package": "tar",
            "options": "xvjf",
            "pattern": "{package} {options} {sources}"
        },
        "suffix": [".tar.tbz2", ".tar.bz2"]
    }

ZIP = {
    "compact": {
        "package": "zip",
        "options": "",
        "pattern": "{package} {options} {destination} {sources}"
    },
    "extract": {
        "package": "unzip",
        "options": "-d",
        "pattern": "{package} {options} {destination} {sources}"
    },
    "suffix": [".zip"]
}

CONFIG_MIME_TYPE = {
    ('application/x-tar', None): TAR,
    ('application/x-tar', 'xz'): TAR,
    ('application/x-tar', 'gzip'): TAR_GZ,
    ('application/x-tar', 'bzip2'): TAR_BZ,
    ('application/zip', None): ZIP
}
 