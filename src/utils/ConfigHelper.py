

class ConfigHelper:

    @staticmethod
    def getVirusTotalAPIKey(config_content):
        return config_content['virustotal']['api_key']

    @staticmethod
    def getMetadefenderCloud(config_content):
        return config_content['metadefendercloud']['api_key']