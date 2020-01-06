# Create the Weekly Surf Poll

Every week we have our **Weekly Surf**, usually* on a Thursday.  

Since not everyone has surf equipment (suit/board) we need to know how many of us are going to surf, so we can rent surf equipment accordingly.
Also, depending on the amount of people that goes to surf, we need to have 1, 2 or even 3 professors with us.

So, in order to sign up to surf, we need to create a public slack **Poll** on our #surfing channel

![](/resources/surfing-poll.png)


This can be achieved by just installing the Poll slack app and running the following command:

```shell 
/poll "Who's ready for this week Weekly Surf?!" "Ohhh I am! 😎" "Nahh, it's cold! ❄️" 
```

## How is it done?

We use [slacker](https://pypi.org/project/slacker/) to send the "/poll" command over HTTP. 

The message and options are randomly selected from a pre-defined list. That is a simple .csv file that is on root of this project named `surfpolldata.csv`.

```csv
# small snippet of the file
Are you going to surf tomorrow?;Yes;No
Surf - Cold Edition;Yes;No
Paddling Session? - Cardio While Wet;Yes;No
(...)
```

All these messages were extracted from our #surfing channel by scraping all polls that were created during last year. 
Some tweaks happen to ensure the message is not specific to any particular day.


## Cronjob

Although it's not that big of a pain, but.. instead of manually creating this poll every week, we've configured a cronjob to run every monday, at 9h30 and do that for us.

Cronjob [/surfops/cronjobs/surfops-generate-poll.yaml](/surfops/cronjobs/surfops-generate-poll.yaml) takes care of this.
👍  

