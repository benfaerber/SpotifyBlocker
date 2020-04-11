# Spotfiy Ad-blocker
#This is all the nerd stuff
import os, platform

print("Spotify Permanent Ad-blocker")

#This maps all of Spotify's AD urls to 127.0.0.1 which means the local system
#Basically it just makes all the sites impossible to reach
#When Spotify tries to load an ad it thinks it's offline, however the music data isn't blocked so it still plays
payload = '''
\n
# Start Block Spotify Ads URLS
127.0.0.1 media-match.com
127.0.0.1 adclick.g.doublecklick.net
127.0.0.1 http://www.googleadservices.com
127.0.0.1 open.spotify.com
127.0.0.1 pagead2.googlesyndication.com
127.0.0.1 desktop.spotify.com
127.0.0.1 googleads.g.doubleclick.net
127.0.0.1 pubads.g.doubleclick.net
127.0.0.1 securepubads.g.doubleclick.net
127.0.0.1 audio2.spotify.com
127.0.0.1 http://audio2.spotify.com
127.0.0.1 http://www.audio2.spotify.com
127.0.0.1 http://www.omaze.com
127.0.0.1 omaze.com
127.0.0.1 bounceexchange.com
127.0.0.1 core.insightexpressai.com
127.0.0.1 content.bitsontherun.com
127.0.0.1 s0.2mdn.net
127.0.0.1 v.jwpcdn.com
127.0.0.1 d2gi7ultltnc2u.cloudfront.net
127.0.0.1 crashdump.spotify.com
127.0.0.1 adeventtracker.spotify.com
127.0.0.1 log.spotify.com
127.0.0.1 analytics.spotify.com
127.0.0.1 ads-fa.spotify.com
127.0.0.1 cs283.wpc.teliasoneracdn.net
127.0.0.1 audio-ec.spotify.com
127.0.0.1 cs126.wpc.teliasoneracdn.net
127.0.0.1 heads-ec.spotify.com
127.0.0.1 u.scdn.co
127.0.0.1 cs126.wpc.edgecastcdn.net
127.0.0.1 pagead46.l.doubleclick.net
127.0.0.1 pagead.l.doubleclick.net
127.0.0.1 video-ad-stats.googlesyndication.com
127.0.0.1 pagead-googlehosted.l.google.com
127.0.0.1 partnerad.l.doubleclick.net
127.0.0.1 prod.spotify.map.fastlylb.net
127.0.0.1 adserver.adtechus.com
127.0.0.1 na.gmtdmp.com
127.0.0.1 anycast.pixel.adsafeprotected.com
127.0.0.1 ads.pubmatic.com
127.0.0.1 idsync-ext.rlcdn.com
127.0.0.1 http://www.googletagservices.com
127.0.0.1 sto3.spotify.com
127.0.0.1 spclient.wg.spotify.com
127.0.0.1 d361oi6ppvq2ym.cloudfront.net
127.0.0.1 gads.pubmatic.com
127.0.0.1 ads-west-colo.adsymptotic.com
127.0.0.1 geo3.ggpht.com
127.0.0.1 showads33000.pubmatic.com
127.0.0.1 spclient.wg.spotify.com
# End Block Spotify Ads URLS
'''

# This detects your os and if you have a Mac it maps that data
op = platform.system()

if (op == "Darwin"):
	op = "Mac"

# This sets the location of your host file, It's different on different OSes
ho = ""
if (op == "Linux"):
	ho = "/etc/hosts"
	raw_input("Push any enter to start.\n")
elif (op == "Mac"):
	ho = "/private/etc/hosts"
	raw_input("Push any enter to start.\n")
elif (op == "Windows"):
	ho = "C:\Windows\System32\drivers\etc\hosts"
	input("Push any enter to start.\n")

# Last but not least, it attempts to inject the payload
try:
	with open(ho, "a") as f:
		f.write(payload)
		print("Success!")
		print("You may need to either reboot your computer or reopen Spotify for this to work.")
		print("You don't need to run this program again and can delete it if you choose.")
except:
	print("There was an error! This is likley due to limited permissions.")
	if (op == "Linux" or op == "Mac"):
		print("Are you using sudo to execute the program?")
	elif (op == "Windows"):
		print("Are you using an admin CMD?")
