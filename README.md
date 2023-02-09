
![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)


# UAF! Cli

CLI app to never forget which command use to extract or compress archives in different formats


## Installation


```sh
   wget https://raw.githubusercontent.com/kalak-io/archives_extractor/master/uaf!.py
   # Move file in your local python path
   # Think to add execution rights with chmod
```
## Usage/Examples

### Create an alias in your shell config
```sh
    alias uaf="<path-to-script>"
```

### Usage

The default extension archive is `.tar`

#### Compact archive
```sh
touch file.txt && echo "Lorem Ipsum" >> file.txt
uaf compact file.txt
```
A archive.tar is created with `file.txt`


## Roadmap

- Additional files archiver programs

- Add more compression tools

- Add more tests

- Installation with pip


## Running Tests

To run tests, run the following command

```bash
  pytest -n auto -vv
```


## Authors

- [@kalakio](https://github.com/kalak-io)

