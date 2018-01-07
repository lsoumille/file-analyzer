class Constants:
    VIRUSTOTAL_SENDING_URL = "https://www.virustotal.com/vtapi/v2/file/scan"
    VIRUSTOTAL_REPORT_URL = "https://www.virustotal.com/vtapi/v2/file/report"

    METADEFENDER_URL = "https://scan.metadefender.com"
    METADEFENDER_SENDING_URL = METADEFENDER_URL + "/v2/file"
    METADEFENDER_REPORT_URL = METADEFENDER_URL + "/v2/file/"

    COMMON_CLEAN_MESSAGE = "[*] Scan terminated, nothing evil was detected"
    COMMON_MALICIOUS_MESSAGE = "### Malicious content detected ###"
    COMMON_INVESTIGATION_REPORT = "# Investigation Report #"

    CONFIG_PATH = "config.yml"

    SHORT_REPORTING = 0
    MEDIUM_REPORTING = 1
    COMPREHENSIVE_REPORTING = 2