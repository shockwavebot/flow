*** Settings ***
Documentation
...    Read common config toml file and load vars and create dir structure 
...    
Library    ../../lib/toml_parser.py

*** Tasks ***
Task_001
    [Documentation]    Pars common config toml file
    ${config_data}=    Parse Toml File    projects/basic-flow/common-config.toml
