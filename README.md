# 🏄 surfops 🏄‍♀️

Surfops is a small repo with all the tools that help me manage my day-to-day surf tasks like **creating polls**, **keeping track of who goes to surf** and **generating the leaderboards**.

## How It Works

Simply put, this project gathers all the commands that I use to run all those tasks. Below is the complete list with a brief description:

* 📊 **Create the "Surf Poll"**
  * Every week on Tuesday, we create a slack `/poll` so people can sign up for this week's surf.
* 📝 **Keep track of who goes to surf and who falls asleep**
  * Every year we organize the "Surf Retreat". The top 10 surfers (that go regularly to surf) are automatically signed up! This is why we keep track of who goes to surf.
* 🥇 **Generate leaderboard** 
  * Consists of the ranking of how many time did someone go to surf over the last year. 
* 🏥 `WIP` **Healthcheck** 
  * Report on all configurations to healthcheck functionality. 


> To understand more about each command and how they work, check the [/docs](/docs) folder for detailed information.

## Usage

This project runs on `python3.6` and you can run it using Docker. There is a simple **Makefile** that contains all commands to run this project locally.

> Note that you don't have to clone this repo. Pulling the latest image of `andreffs/surfops` would be enough.


Lets start by pulling the latest image of this repo:
```bash
# Pull image to local registry
$ make pull
```

Now that you already have the image locally, just open a shell into the docker container and run the command that you need:

```bash
# Start python shell on container
$ make shell
```

### Configuration 

Only 3 environments variables are required to run all commands, which are:

| Variable | Description |
| ----- | ----- |  
| `SLACK_API_TOKEN=` | This is what allows your script to run the `/poll` command on any particular channel |
| `ZAPIER_CREATE_LOG_ENTRY_HOOK=` | Web hook for Zapier "Create new entry" on the "Surf History" spreadsheet | 
| `ZAPIER_UPDATE_LOG_ENTRY_HOOK=` | Web hook for Zapier "Update last entry" on the "Surf History" spreadsheet | 


You need to create a local `.env` file, with those secrets inside, for the project to work.

## Cronjobs

The cronjobs under `~/surfops/cronjobs/` are simply running the following python command:

```shell
$ python surf.py <COMMAND> <ARGUMENTS>
```


#### K8S Cluster.

Of course that you don't need a kubernetes cluster to run these commands, but since we have one at our disposal, why not 😁.

There is one cronjob for each command. The sequence of cronjobs translates to the workflow that we manually do every week.

| Time of execution | Cronjob | Description | 
| ----- | ----- | ----- | 
| At 10:30 on Tuesdays | `surfops-generate-poll.yaml` | Creates `/poll` on "#surfing channel to let people sign up for this weeks surf. |
| At 20:00 on Wednesdays | `surfops-create-new-log-entry.yaml` | Adds list of people of replied "Yes" to "Surf History" spreadsheet.  |
| At 9:30 on Thursday | `surfops-update-last-log-entry.yaml` | Updates last entry on "Surf History" with updated list of people that went to surf. |

Note that those cronjobs rely on a secret by the name `surfops-secrets`. You can create them by running the following script on a terminal.

```bash
# On a terminal tab, replace those environments and then copy&paste the snippet below:
$ cat <<EOF | kubectl apply -f -
apiVersion: v1
stringData:
  SLACK_API_TOKEN: xoxp-12345-....
  ZAPIER_CREATE_LOG_ENTRY_HOOK: https://hooks.zapier.com/hooks/catch/123...
  ZAPIER_UPDATE_LOG_ENTRY_HOOK: https://hooks.zapier.com/hooks/catch/456...
kind: Secret
metadata:
  name: surfops-secrets
  namespace: default
type: Opaque
EOF
````

Just need to replace with the correct environments.