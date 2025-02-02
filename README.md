# In Stock NVIDIA

This is a script that checks the NVIDIA store for available products and sends an email notification if any products are in stock.

### Steps to run

1. Create the virtual env

    - python -m venv .venv
    - source .venv/bin/activate

2. Install the requirements
    - python -m pip install -r requirements.txt

### Steps to clone repo in linux

-   git config --global user.name "name user"
-   git config --global user.email "email user"
-   git config --global credential.helper store
-   git clone [repo url]

## Crontabs

Crontab configured for in stock script

### Configuration

```
*/10 * * * *  $HOME/repo/in-clock/run.sh
```
