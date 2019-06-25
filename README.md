
# asana-view

This package allows you to view all of your Asana events (across workspaces) in one calendar. This feature is popularly requested but is not provided by Asana.

## Instructions

1. Get a personal access token from Asana:
    1. Visit [app.asana.com](https://app.asana.com)
    2. Click your icon in the top right corner.
    3. Select `My Profile Settings`.
    4. Choose the `Apps` tab
    5. Click `Manage Developer Apps` (bottom left)
    6. Select `+Create New Personal Access Token` (bottom left)
2. Copy the access token and paste it into your `~/.bash_profile`: 

    ```bash
    export ASANA_TOKEN="0/b25c048ff8e0cd498b1ac1d7b866c1d0"
    ```   

3. Install this Python package:

    ```python
    pip install git+https://github.com/sswatson/asana-view
    ```

4. Type `python` at the command line and run the following two lines of code:

    ```python
    from asanaview import showcalendar
    showcalendar()
    ```

![demo](https://raw.githubusercontent.com/sswatson/asana-view/master/images/asana.png)

