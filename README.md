# CInfo

Making CI/CD triaging little bit easier

## Installation

```
virtualenv ~/.cinfo_venv && source ~/.cinfo_venv/bin/activate
git clone git@github.com:bregman-arie/cinfo.git
cd cinfo
pipenv install .
```

## Configuration

```
sources:
  prod_jenkins:
    type: jenkins
    url: https://some.jenkins.com
    jobs:
      - jobX
      - jobY
targets:
  some_spreadsheet:
    type: google_spreadsheet
    url: https://docs.google.com/spreadsheets/d/some.spreadsheet
```

configuration file should be set in one of the following paths:
  * `/etc/cinfo/cinfo.yaml`
  * `~/.cinfo/cinfo.yaml`

Configuration can include multiple sources and targets.

## Usage

To run full triaging process of pulling and publishing the data: `cinfo triage`
To only pull data: `cinfo pull`
To only publish existing local data: `cinfo publish`

## Contributions

Contributions are made by submitting pull requests
