## Propagation data script

This script helps to propagate data to prepare Bitbucket instance for performance tests https://github.com/atlassian/dc-app-performance-toolkit

#### Install
1. Clone to the `app` folder (close to the `bitbucket.yml` config file)

#### Usage
1. Set all necessary params in the config file
2. Run script
```bash
    python3 prepare_dataset.py
```

It will create 20 repositories in the PROJECT_1 project, push example dataset into each repo and creates one PR


