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

#### Links
* https://developer.atlassian.com/platform/marketplace/testing-your-app-with-a-large-data-set/#dimensions-of-a-large-bitbucket-dc
* https://developer.atlassian.com/platform/marketplace/dc-apps-performance-toolkit-user-guide-bitbucket/
* https://developer.atlassian.com/platform/marketplace/dc-apps-performance-and-scale-testing/
* https://developer.atlassian.com/platform/marketplace/dc-apps-performance-toolkit-user-guide-bitbucket/
* https://developer.atlassian.com/platform/marketplace/dc-apps-security-scanner/
* https://developer.atlassian.com/platform/marketplace/dc-apps-security-scanner/#how-to-get-a-dependency-tree-for-dc-apps-security-scanner-analysis
* https://developer.atlassian.com/platform/marketplace/dc-apps-performance-and-scale-testing/