# ez_config

## Features

- Easy to use Configuration manager for python3
- Create and handle configuration files 
- Json compatibility

## 


## Setup and Working with 
Installation 
```sh
git clone https://github.com/Lainupcomputer/ez_config
```
move ez_config in project and import
```sh
import ez_config
```
Setting up:
```sh
cfg = ez_config()
cfg.initialise("file_path", seperator, debug) # defaults: seperator=#, debug=False 
```
add entry 
```sh
cfg.add("Config_Name", "config_data") # Note: config_data can be a list and spited by seperator
```

edit entry 
```sh
cfg.edit("Config_Name", "config_data", "value") 
```
Get entry 
```sh
cfg.get("Config_Name", "config_data") # Returns Value
```

