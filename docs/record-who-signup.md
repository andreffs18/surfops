# Who Signup?

On top of our **Weekly surf** we have the **Yearly Surf Retreat** where _only the best surfers go_ 😎.

Okay, that's not entirely true! Everybody can go, but we have rules!

The idea is simple: 
- We can take 16 people to the yearly surf retreat!
- The top half will be the most frequent people going to our **weekly surf**
- The bottom half will be randomly selected from all the people that went to the **weekly surf** 

To make this idea come to life we need to keep track of who signs up, as well who ends up actually going

## How is it done?

We have a spreadsheet (yup 🙄) that saves some information regarding that week's surf, and one of the columns is **Who Singup**.

Simply copy&pasting the people that replied "Yes" from the poll, remove the "@" simbol and any white spaces, and that's it.

> All this pre-processing would guarantee that we dont have any mistakes when generating the Leaderboard

Here is an example of that spreadsheet:

![](/resources/surf-history-spreadsheet.png)

To automatize this step we created this spreadsheet on Google Spreadsheets and created a Zapier "Zap" that would add a new row to this spreadsheet every time we make a POST request to a specific Web hook.

## Cronjob

This started to become a pain because we usually would forget to save this information before the surf day.
And since we penalize people that skip surf, we would end up with no way of confirming who actually said "Yes" but didn't go. 
To record that information we run the cronjob at 20h on the day before surf.
 
Cronjob [/surfops/cronjobs/surfops-create-new-log-entry.yaml](/surfops/cronjobs/surfops-create-new-log-entry.yaml) takes care of this.
👍  

# Who actually went?

Alright, now it's all fun when on Tuesday during lunch I say:

- "Yes, I will go to this weeks surf!"

But then end up falling asleep and not showing up!

> Right, I forgot to mention that Weekly Surf means you need to be at the Office at 7AM Sharp! <br/>
> (Transportation to the beach is around 30~40 minutes, depends on traffic + 1 hour of surfing and you will be back to the office around 10h30!)

So, in order to congratulate the ones that woke up early and went, and penalize the ones that skipped, we record that difference!

> Penalize in the sense of the Leaderboard 😅

The idea is simple: 
- Pick up the final list of people that said "Yes" from the "/poll"
- Update last entry of our "Surf History" spreadsheet 


## How is it done?

This step is pretty much piggy-backing on the ["Who signup"](#who-signup).

We also have a Zapier "Zap" that provides a specific Web hook that updates the last row of that spreadsheet with the information given on the POST. 

## Cronjob

This one runs on the day of the weekly surf, at 10h30. 

Cronjob [/surfops/cronjobs/surfops-update-last-log-entry.yaml](/surfops/cronjobs/surfops-update-last-log-entry.yaml) takes care of this.
👍  

