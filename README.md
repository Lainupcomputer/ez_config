# ez_config

## Features

- Easy to use Configuration manager for python3
- Create and handle configuration files 
- Json compatibility

## Installation 
```sh
git clone https://github.com/Lainupcomputer/ez_config
```


## Setup and Working with 
Setting up:
```sh
import ez_config

cfg = ez_config()

cfg.initialise("file_path", seperator, debug) # defaults: seperator=#, debug=False 
```
add entry 
```sh
cfg.add("Config_Name", "config_data") # Note: config_data can be a list and is spit with seperator
```

edit entry 
```sh
cfg.edit("Config_Name", "config_data", "value") 
```
Get entry 
```sh
cfg.get("Config_Name", "config_data") # Returns Value
```
## License

MIT

**Free Software, Hell Yeah!**
