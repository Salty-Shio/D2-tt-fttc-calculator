# Destiny 2 Triple Tap / Fourth Times The Charm Calculator

This is an overengineered solution meant to solve a simple problem. Perks like triple tap and fourth times the charm can have some interesting interactions with weapons, especially if they are both on the same weapon. The amount of shots in a single magaizine can seemingly exponentially grow and I found myself sitting down and trying to count out how many shots would result from these perks. The resulting shots in a magazine, the amount of ammunation refunded, how many times a perk would be proced, were all annoying to figure out. Finally I decided to write this to make my life easier.

## Use

You'll need Python 3.10 or higher installed to run this. It runs in the terminal and will prompt you for the relevant information. Just clone the repo and you'll be good to go.

## About

Like I said, this is super overengineered in comparison to solving this problem. If you want a simple calculator that works on the web, I'll have one up on (my website)[https://shio.me] soon.

### The Perks

If you don't know what this is, I'll give a quick explanation. Destiny 2 is a space magic first person looter shooter rage game. As it is a first person shooter, there are guns, and lots of them. Each weapon in the game is a unique drop, where the stats will vary based on what perks appear on that weapon. In this specific case, there are two perks that weapons can roll with that have a unique interaction.

### Triple Tap

When a player lands three precision hits on an enemy each within two seconds of each other, a round is refunded from thin air (meaning it is not drawn from your ammo reserves) to the magazine.

This means that if you have a magazine with size 6 and you get all 6 precision hits, the weapon with be refunded, two shots to the magazine making the overall magazine size 8. If you have a magazine size of 9 rounds, you will be refunded 3 shots. Those three rounds will then proc the perk a fourth time, making your total rounds in the magazine 13.

### Fourth Times the Charm

Similar to Triple Tap, fourth times refunds two rounds to the magazine for every four precision hits. This means that. With a magazine of 4, 2 rounds will be returned for a total of 6 shots, and with a magazine of 8, 4 will be refunded allowing for one extra proc for a total of 14 shots.

### Together

This is where it becomes somewhat of a pain to figure out how many bullets will end up in your magazine. When you have a weapon with both perks on it, the number of shots goes up rapidly. With a magazine of 4, you get 11 shots, and with a magazine of 10 you get 47 shots. It becomes apparent that counting out the shots gets out of hand quickly. Hence the creation of this calculator

### Why this approach?

There are a number of ways to solve this problem. The easiest is probably through math. Once again, I'll go more in to depth on that on my website. Here, I've opted for a more flexible solution. This simulates the process of actually firing the weapon. The reason I opted for this is to allow for the potential for this to account for other perks or weapon simulation. It also allows for the potential to measure things other than ammo when it comes to weapons. For instance, in the future I could allow for the program to figure out exactly how many shots from a weapon are possible during a DPS phase of a boss. Essentially, this is overengineered to leave the possibilities open.
