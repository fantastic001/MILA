
# MILA - Modular integration and lightweight adaptability 

## How to use

Copy `config.py` into your project and change variables in the beginning of the file to your project name. 

## Documenting your configuration parameters

In order to get configuration parameters you can modify, execute:

    python scripts/detect_function_calls.py  my_project/ get_config_ --exclude get_config_location

Every configuration parameter can be changed in configuration file and overwritten by using 
environment variable. 

For instance, `url` can be specified in configuration file and can be modified using `<<MY_PROJECT>>_URL` environment variable. 

Configuration file is specified using `<<MY_PROJECT>>_CONFIG` and default location is at `~/.config/<<my_project>>.json`
