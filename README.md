# CInfo

Making CI/CD triaging little bit easier

## Configuration

```
input:
  prod_jenkins:
    type: jenkins
    url: https://some.jenkins.com
    jobs:
      - jobX
      - jobY
output:
  some_spreadsheet:
    type: google_spreadsheet
    url: https://docs.google.com/spreadsheets/d/some.spreadsheet
```

## Usage

To run full triaging process of pulling and publishing the data: `cinfo triage`

## Contributions

Contributions are made by submitting pull requests
