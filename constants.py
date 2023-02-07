TAR = {
        "compact": {
            "package": "tar",
            "options": "cvfP",
            "pattern": "{package} {options} {destination} {sources}"
        },
        "extract": {
            "package": "tar",
            "options": "xvf",
            "pattern": "{package} {options} {sources}"
        },
        "suffix": ".tar"
    }

# TAR_GZ = {
#         "extract": {
#             "package": "tar",
#             "options": "xvzf",
#             "pattern": "{package} {options} {sources}"
#         },
#         "compact": {
#             "package": "tar",
#             "options": "cvzf",
#             "pattern": "{package} {options} {destination} {sources}"
#         }
#     }

# TAR_BZ = {
#         "extract": {
#             "package": "tar",
#             "options": "xvjf",
#             "pattern": "{package} {options} {sources}"
#         },
#         "compact": {
#             "package": "tar",
#             "options": "cvjf",
#             "pattern": "{package} {options} {destination} {sources}"
#         }
#     }

CONFIG_MIME_TYPE = {
    "application/x-tar": TAR,
    # ".tar": TAR,
    # ".tar.xz": TAR,
    # ".xz": TAR,
    # ".tbz": TAR_BZ,
    # ".tbz2": TAR_BZ,
    # ".tar.bz2": TAR_BZ,
    # ".tgz": TAR_GZ,
    # ".tar.gz": TAR_GZ
}
 