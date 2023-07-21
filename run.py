import logging
import logging.config
import yaml


def main():
    """entry point to run the xetra ETL job"""
    #parsing YAML file
    config_path='C:/Users/pnhtu/xetra_project/xetra_1234/configs/xetra_report1_config.yml'
    config=yaml.safe_load(open(config_path))
    #CONFIGURE LOGGING
    log_config=config['logging']
    logging.config.dictConfig(log_config)
    logger=logging.getLogger(__name__)
    logger.info('this is my test')

if __name__=='__main__':
    main()