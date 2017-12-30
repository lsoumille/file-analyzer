class Constants:
    VIRUSTOTAL_SENDING_URL = "https://www.virustotal.com/vtapi/v2/file/scan"

    VIRUSTOTAL_REPORT_URL = "https://www.virustotal.com/vtapi/v2/file/report"

    COMMON_CLEAN_MESSAGE = "[*] Scan terminated, nothing evil was detected"

    CONFIG_PATH = "config.yml"

    SHORT_REPORTING = 0
    MEDIUM_REPORTING = 1
    COMPREHENSIVE_REPORTING = 2