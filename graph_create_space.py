# %%
import json
import time

from nebula3.Config import Config, SessionPoolConfig
from nebula3.gclient.net import ConnectionPool
from nebula3.gclient.net.SessionPool import SessionPool

with open("secrets.json") as f:
    secrets = json.loads(f.read())

space_name = "players"

# %%
# for data insert
connection_pool = ConnectionPool()
connection_pool.init(
    [
        (
            secrets.get("nebula_graph").get("host"),
            secrets.get("nebula_graph").get("port"),
        )
    ],
    Config(),
)
with connection_pool.session_context(
    secrets.get("nebula_graph").get("user"),
    secrets.get("nebula_graph").get("password"),
) as session:
    result = session.execute(
        stmt=f"""
        drop space {space_name};
        create space if not exists {space_name}(partition_num=10,replica_factor=1,vid_type=fixed_string(32));
        """
    )
    time.sleep(20)
    session.execute(
        stmt=f"""
        use {space_name};
        create tag player(name string,age int);
        create tag team(name string);
        create edge serve(start_year int,end_year int);
        create edge follow(degree int);
    """
    )
    time.sleep(20)
    session.execute(
        stmt=f"""
        create tag index idx_player_name on player(name(20));
    """
    )
    time.sleep(20)
    session.execute(
        stmt="""
        insert vertex player(name,age) values "player100":("Tim Duncan", 42);
        insert vertex player(name,age) values "player101":("Tony Parker", 36);
        insert vertex player(name,age) values "player102":("LaMarcus Aldridge", 33);
        insert vertex player(name,age) values "player103":("Rudy Gay", 32);
        insert vertex player(name,age) values "player104":("Marco Belinelli", 32);
        insert vertex player(name,age) values "player105":("Danny Green", 31);
        insert vertex player(name,age) values "player106":("Kyle Anderson", 25);
        insert vertex player(name,age) values "player107":("Aron Baynes", 32);
        insert vertex player(name,age) values "player108":("Boris Diaw", 36);
        insert vertex player(name,age) values "player109":("Tiago Splitter", 34);
        insert vertex player(name,age) values "player110":("Cory Joseph", 27);
        insert vertex player(name,age) values "player111":("David West", 38);
        insert vertex player(name,age) values "player112":("Jonathon Simmons", 29);
        insert vertex player(name,age) values "player113":("Dejounte Murray", 29);
        insert vertex player(name,age) values "player114":("Tracy McGrady", 39);
        insert vertex player(name,age) values "player115":("Kobe Bryant", 40);
        insert vertex player(name,age) values "player116":("LeBron James", 34);
        insert vertex player(name,age) values "player117":("Stephen Curry", 31);
        insert vertex player(name,age) values "player118":("Russell Westbrook", 30);
        insert vertex player(name,age) values "player119":("Kevin Durant", 30);
        insert vertex player(name,age) values "player120":("James Harden", 29);
        insert vertex player(name,age) values "player121":("Chris Paul", 33);
        insert vertex player(name,age) values "player122":("DeAndre Jordan", 30);
        insert vertex player(name,age) values "player123":("Ricky Rubio", 28);
        insert vertex player(name,age) values "player124":("Rajon Rondo", 33);
        insert vertex player(name,age) values "player125":("Manu Ginobili", 41);
        insert vertex player(name,age) values "player126":("Kyrie Irving", 26);
        insert vertex player(name,age) values "player127":("Vince Carter", 42);
        insert vertex player(name,age) values "player128":("Carmelo Anthony", 34);
        insert vertex player(name,age) values "player129":("Dwyane Wade", 37);
        insert vertex player(name,age) values "player130":("Joel Embiid", 25);
        insert vertex player(name,age) values "player131":("Paul George", 28);
        insert vertex player(name,age) values "player132":("Giannis Antetokounmpo", 24);
        insert vertex player(name,age) values "player133":("Yao Ming", 38);
        insert vertex player(name,age) values "player134":("Blake Griffin", 30);
        insert vertex player(name,age) values "player135":("Damian Lillard", 28);
        insert vertex player(name,age) values "player136":("Steve Nash", 45);
        insert vertex player(name,age) values "player137":("Dirk Nowitzki", 40);
        insert vertex player(name,age) values "player138":("Paul Gasol", 38);
        insert vertex player(name,age) values "player139":("Marc Gasol", 34);
        insert vertex player(name,age) values "player140":("Grant Hill", 46);
        insert vertex player(name,age) values "player141":("Ray Allen", 43);
        insert vertex player(name,age) values "player142":("Klay Thompson", 29);
        insert vertex player(name,age) values "player143":("Kristaps Porzingis", 23);
        insert vertex player(name,age) values "player144":("Shaquille O'Neal", 47);
        insert vertex player(name,age) values "player145":("JaVale McGee", 31);
        insert vertex player(name,age) values "player146":("Dwight Howard", 33);
        insert vertex player(name,age) values "player147":("Amar'e Stoudemire", 36);
        insert vertex player(name,age) values "player148":("Jason Kidd", 45);
        insert vertex player(name,age) values "player149":("Ben Simmons", 22);
        insert vertex player(name,age) values "player150":("Luka Doncic", 20);
        insert vertex team(name) values "team200":("Warriors");
        insert vertex team(name) values "team201":("Nuggets");
        insert vertex team(name) values "team202":("Rockets");
        insert vertex team(name) values "team203":("Trail Blazers");
        insert vertex team(name) values "team204":("Spurs");
        insert vertex team(name) values "team205":("Thunders");
        insert vertex team(name) values "team206":("Jazz");
        insert vertex team(name) values "team207":("Clippers");
        insert vertex team(name) values "team208":("Kings");
        insert vertex team(name) values "team209":("Timberwolves");
        insert vertex team(name) values "team210":("Lakers");
        insert vertex team(name) values "team211":("Pelicans");
        insert vertex team(name) values "team212":("Grizzlies");
        insert vertex team(name) values "team213":("Mavericks");
        insert vertex team(name) values "team214":("Suns");
        insert vertex team(name) values "team215":("Hornets");
        insert vertex team(name) values "team216":("Cavaliers");
        insert vertex team(name) values "team217":("Celtics");
        insert vertex team(name) values "team218":("Raptors");
        insert vertex team(name) values "team219":("76ers");
        insert vertex team(name) values "team220":("Pacers");
        insert vertex team(name) values "team221":("Bulls");
        insert vertex team(name) values "team222":("Hawks");
        insert vertex team(name) values "team223":("Knicks");
        insert vertex team(name) values "team224":("Pistons");
        insert vertex team(name) values "team225":("Bucks");
        insert vertex team(name) values "team226":("Magic");
        insert vertex team(name) values "team227":("Nets");
        insert vertex team(name) values "team228":("Wizards");
        insert vertex team(name) values "team229":("Heat");
        insert edge follow(degree) values "player100"->"player101":(95);
        insert edge follow(degree) values "player100"->"player125":(95);
        insert edge follow(degree) values "player101"->"player100":(95);
        insert edge follow(degree) values "player101"->"player125":(95);
        insert edge follow(degree) values "player101"->"player102":(90);
        insert edge follow(degree) values "player125"->"player100":(90);
        insert edge follow(degree) values "player102"->"player101":(75);
        insert edge follow(degree) values "player102"->"player100":(75);
        insert edge follow(degree) values "player103"->"player102":(70);
        insert edge follow(degree) values "player104"->"player101":(50);
        insert edge follow(degree) values "player104"->"player100":(55);
        insert edge follow(degree) values "player104"->"player105":(60);
        insert edge follow(degree) values "player105"->"player104":(83);
        insert edge follow(degree) values "player105"->"player100":(70);
        insert edge follow(degree) values "player105"->"player116":(80);
        insert edge follow(degree) values "player107"->"player100":(80);
        insert edge follow(degree) values "player108"->"player101":(80);
        insert edge follow(degree) values "player108"->"player100":(80);
        insert edge follow(degree) values "player109"->"player100":(80);
        insert edge follow(degree) values "player109"->"player125":(90);
        insert edge follow(degree) values "player113"->"player100":(99);
        insert edge follow(degree) values "player113"->"player101":(99);
        insert edge follow(degree) values "player113"->"player125":(99);
        insert edge follow(degree) values "player113"->"player104":(99);
        insert edge follow(degree) values "player113"->"player105":(99);
        insert edge follow(degree) values "player113"->"player116":(99);
        insert edge follow(degree) values "player113"->"player118":(99);
        insert edge follow(degree) values "player113"->"player121":(99);
        insert edge follow(degree) values "player113"->"player106":(99);
        insert edge follow(degree) values "player113"->"player119":(99);
        insert edge follow(degree) values "player113"->"player120":(99);
        insert edge follow(degree) values "player114"->"player115":(90);
        insert edge follow(degree) values "player114"->"player140":(90);
        insert edge follow(degree) values "player114"->"player103":(90);
        insert edge follow(degree) values "player116"->"player141":(100);
        insert edge follow(degree) values "player118"->"player131":(90);
        insert edge follow(degree) values "player118"->"player120":(90);
        insert edge follow(degree) values "player120"->"player118":(80);
        insert edge follow(degree) values "player121"->"player116":(90);
        insert edge follow(degree) values "player121"->"player128":(90);
        insert edge follow(degree) values "player121"->"player129":(90);
        insert edge follow(degree) values "player124"->"player141":(-1);
        insert edge follow(degree) values "player126"->"player116":(13);
        insert edge follow(degree) values "player127"->"player114":(90);
        insert edge follow(degree) values "player127"->"player148":(70);
        insert edge follow(degree) values "player128"->"player116":(90);
        insert edge follow(degree) values "player128"->"player121":(90);
        insert edge follow(degree) values "player128"->"player129":(90);
        insert edge follow(degree) values "player129"->"player116":(90);
        insert edge follow(degree) values "player129"->"player121":(90);
        insert edge follow(degree) values "player129"->"player128":(90);
        insert edge follow(degree) values "player130"->"player149":(80);
        insert edge follow(degree) values "player131"->"player118":(95);
        insert edge follow(degree) values "player133"->"player114":(90);
        insert edge follow(degree) values "player133"->"player144":(90);
        insert edge follow(degree) values "player134"->"player121":(-1);
        insert edge follow(degree) values "player135"->"player102":(80);
        insert edge follow(degree) values "player136"->"player147":(90);
        insert edge follow(degree) values "player136"->"player137":(88);
        insert edge follow(degree) values "player136"->"player117":(90);
        insert edge follow(degree) values "player136"->"player148":(85);
        insert edge follow(degree) values "player137"->"player136":(80);
        insert edge follow(degree) values "player137"->"player148":(80);
        insert edge follow(degree) values "player137"->"player129":(10);
        insert edge follow(degree) values "player138"->"player115":(90);
        insert edge follow(degree) values "player138"->"player139":(99);
        insert edge follow(degree) values "player139"->"player138":(99);
        insert edge follow(degree) values "player140"->"player114":(90);
        insert edge follow(degree) values "player141"->"player124":(9);
        insert edge follow(degree) values "player142"->"player117":(90);
        insert edge follow(degree) values "player143"->"player150":(90);
        insert edge follow(degree) values "player144"->"player145":(100);
        insert edge follow(degree) values "player144"->"player100":(80);
        insert edge follow(degree) values "player147"->"player136":(90);
        insert edge follow(degree) values "player148"->"player127":(80);
        insert edge follow(degree) values "player148"->"player136":(90);
        insert edge follow(degree) values "player148"->"player137":(85);
        insert edge follow(degree) values "player149"->"player130":(80);
        insert edge follow(degree) values "player150"->"player137":(90);
        insert edge follow(degree) values "player150"->"player143":(90);
        insert edge follow(degree) values "player150"->"player120":(80);
        insert edge serve(start_year,end_year) values "player100"->"team204":(1997, 2016);
        insert edge serve(start_year,end_year) values "player101"->"team204":(1999, 2018);
        insert edge serve(start_year,end_year) values "player101"->"team215":(2018, 2019);
        insert edge serve(start_year,end_year) values "player102"->"team203":(2006, 2015);
        insert edge serve(start_year,end_year) values "player102"->"team204":(2015, 2019);
        insert edge serve(start_year,end_year) values "player103"->"team212":(2006, 2013);
        insert edge serve(start_year,end_year) values "player103"->"team218":(2013, 2013);
        insert edge serve(start_year,end_year) values "player103"->"team208":(2013, 2017);
        insert edge serve(start_year,end_year) values "player103"->"team204":(2017, 2019);
        insert edge serve(start_year,end_year) values "player104"->"team200":(2007, 2009);
        insert edge serve(start_year,end_year) values "player104"->"team218":(2009, 2010);
        insert edge serve(start_year,end_year) values "player104"->"team215"@20102012:(2010, 2012);
        insert edge serve(start_year,end_year) values "player104"->"team221":(2012, 2013);
        insert edge serve(start_year,end_year) values "player104"->"team204"@20132015:(2013, 2015);
        insert edge serve(start_year,end_year) values "player104"->"team208":(2015, 2016);
        insert edge serve(start_year,end_year) values "player104"->"team215"@20162017:(2016, 2017);
        insert edge serve(start_year,end_year) values "player104"->"team222":(2017, 2018);
        insert edge serve(start_year,end_year) values "player104"->"team219":(2018, 2018);
        insert edge serve(start_year,end_year) values "player104"->"team204"@20182019:(2018, 2019);
        insert edge serve(start_year,end_year) values "player105"->"team216":(2009, 2010);
        insert edge serve(start_year,end_year) values "player105"->"team204":(2010, 2018);
        insert edge serve(start_year,end_year) values "player105"->"team218":(2018, 2019);
        insert edge serve(start_year,end_year) values "player106"->"team204":(2014, 2018);
        insert edge serve(start_year,end_year) values "player106"->"team212":(2018, 2019);
        insert edge serve(start_year,end_year) values "player107"->"team204":(2013, 2015);
        insert edge serve(start_year,end_year) values "player107"->"team224":(2015, 2017);
        insert edge serve(start_year,end_year) values "player107"->"team217":(2017, 2019);
        insert edge serve(start_year,end_year) values "player108"->"team222":(2003, 2005);
        insert edge serve(start_year,end_year) values "player108"->"team214":(2005, 2008);
        insert edge serve(start_year,end_year) values "player108"->"team215":(2008, 2012);
        insert edge serve(start_year,end_year) values "player108"->"team204":(2012, 2016);
        insert edge serve(start_year,end_year) values "player108"->"team206":(2016, 2017);
        insert edge serve(start_year,end_year) values "player109"->"team204":(2010, 2015);
        insert edge serve(start_year,end_year) values "player109"->"team222":(2015, 2017);
        insert edge serve(start_year,end_year) values "player109"->"team219":(2017, 2017);
        insert edge serve(start_year,end_year) values "player110"->"team204":(2011, 2015);
        insert edge serve(start_year,end_year) values "player110"->"team218":(2015, 2017);
        insert edge serve(start_year,end_year) values "player110"->"team220":(2017, 2019);
        insert edge serve(start_year,end_year) values "player111"->"team215":(2003, 2011);
        insert edge serve(start_year,end_year) values "player111"->"team220":(2011, 2015);
        insert edge serve(start_year,end_year) values "player111"->"team204":(2015, 2016);
        insert edge serve(start_year,end_year) values "player111"->"team200":(2016, 2018);
        insert edge serve(start_year,end_year) values "player112"->"team204":(2015, 2017);
        insert edge serve(start_year,end_year) values "player112"->"team226":(2017, 2019);
        insert edge serve(start_year,end_year) values "player112"->"team219":(2019, 2019);
        insert edge serve(start_year,end_year) values "player113"->"team204":(2016, 2019);
        insert edge serve(start_year,end_year) values "player114"->"team218":(1997, 2000);
        insert edge serve(start_year,end_year) values "player114"->"team226":(2000, 2004);
        insert edge serve(start_year,end_year) values "player114"->"team202":(2004, 2010);
        insert edge serve(start_year,end_year) values "player114"->"team204":(2013, 2013);
        insert edge serve(start_year,end_year) values "player115"->"team210":(1996, 2016);
        insert edge serve(start_year,end_year) values "player116"->"team216"@20032010:(2003, 2010);
        insert edge serve(start_year,end_year) values "player116"->"team229":(2010, 2014);
        insert edge serve(start_year,end_year) values "player116"->"team216"@20142018:(2014, 2018);
        insert edge serve(start_year,end_year) values "player116"->"team210":(2018, 2019);
        insert edge serve(start_year,end_year) values "player117"->"team200":(2009, 2019);;
        insert edge serve(start_year,end_year) values "player118"->"team205":(2008, 2019);
        insert edge serve(start_year,end_year) values "player119"->"team205":(2007, 2016);
        insert edge serve(start_year,end_year) values "player119"->"team200":(2016, 2019);
        insert edge serve(start_year,end_year) values "player120"->"team205":(2009, 2012);
        insert edge serve(start_year,end_year) values "player120"->"team202":(2012, 2019);
        insert edge serve(start_year,end_year) values "player121"->"team215":(2005, 2011);
        insert edge serve(start_year,end_year) values "player121"->"team207":(2011, 2017);
        insert edge serve(start_year,end_year) values "player121"->"team202":(2017, 2021);
        insert edge serve(start_year,end_year) values "player122"->"team207":(2008, 2018);
        insert edge serve(start_year,end_year) values "player122"->"team213":(2018, 2019);
        insert edge serve(start_year,end_year) values "player122"->"team223":(2019, 2019);
        insert edge serve(start_year,end_year) values "player123"->"team209":(2011, 2017);
        insert edge serve(start_year,end_year) values "player123"->"team206":(2017, 2019);
        insert edge serve(start_year,end_year) values "player124"->"team217":(2006, 2014);
        insert edge serve(start_year,end_year) values "player124"->"team213":(2014, 2015);
        insert edge serve(start_year,end_year) values "player124"->"team208":(2015, 2016);
        insert edge serve(start_year,end_year) values "player124"->"team221":(2016, 2017);
        insert edge serve(start_year,end_year) values "player124"->"team211":(2017, 2018);
        insert edge serve(start_year,end_year) values "player124"->"team210":(2018, 2019);
        insert edge serve(start_year,end_year) values "player125"->"team204":(2002, 2018);
        insert edge serve(start_year,end_year) values "player126"->"team216":(2011, 2017);
        insert edge serve(start_year,end_year) values "player126"->"team217":(2017, 2019);
        insert edge serve(start_year,end_year) values "player127"->"team218":(1998, 2004);
        insert edge serve(start_year,end_year) values "player127"->"team227":(2004, 2009);
        insert edge serve(start_year,end_year) values "player127"->"team226":(2009, 2010);
        insert edge serve(start_year,end_year) values "player127"->"team214":(2010, 2011);
        insert edge serve(start_year,end_year) values "player127"->"team213":(2011, 2014);
        insert edge serve(start_year,end_year) values "player127"->"team212":(2014, 2017);
        insert edge serve(start_year,end_year) values "player127"->"team208":(2017, 2018);
        insert edge serve(start_year,end_year) values "player127"->"team222":(2018, 2019);
        insert edge serve(start_year,end_year) values "player128"->"team201":(2003, 2011);
        insert edge serve(start_year,end_year) values "player128"->"team223":(2011, 2017);
        insert edge serve(start_year,end_year) values "player128"->"team205":(2017, 2018);
        insert edge serve(start_year,end_year) values "player128"->"team202":(2018, 2019);
        insert edge serve(start_year,end_year) values "player129"->"team229"@20032016:(2003, 2016);
        insert edge serve(start_year,end_year) values "player129"->"team221":(2016, 2017);
        insert edge serve(start_year,end_year) values "player129"->"team216":(2017, 2018);
        insert edge serve(start_year,end_year) values "player129"->"team229"@20182019:(2018, 2019);
        insert edge serve(start_year,end_year) values "player130"->"team219":(2014, 2019);
        insert edge serve(start_year,end_year) values "player131"->"team220":(2010, 2017);
        insert edge serve(start_year,end_year) values "player131"->"team205":(2017, 2019);
        insert edge serve(start_year,end_year) values "player132"->"team225":(2013, 2019);
        insert edge serve(start_year,end_year) values "player133"->"team202":(2002, 2011);
        insert edge serve(start_year,end_year) values "player134"->"team207":(2009, 2018);
        insert edge serve(start_year,end_year) values "player134"->"team224":(2018, 2019);
        insert edge serve(start_year,end_year) values "player135"->"team203":(2012, 2019);
        insert edge serve(start_year,end_year) values "player136"->"team214"@19961998:(1996, 1998);
        insert edge serve(start_year,end_year) values "player136"->"team213":(1998, 2004);
        insert edge serve(start_year,end_year) values "player136"->"team214"@20042012:(2004, 2012);
        insert edge serve(start_year,end_year) values "player136"->"team210":(2012, 2015);
        insert edge serve(start_year,end_year) values "player137"->"team213":(1998, 2019);
        insert edge serve(start_year,end_year) values "player138"->"team212":(2001, 2008);
        insert edge serve(start_year,end_year) values "player138"->"team210":(2008, 2014);
        insert edge serve(start_year,end_year) values "player138"->"team221":(2014, 2016);
        insert edge serve(start_year,end_year) values "player138"->"team204":(2016, 2019);
        insert edge serve(start_year,end_year) values "player138"->"team225":(2019, 2020);
        insert edge serve(start_year,end_year) values "player139"->"team212":(2008, 2019);
        insert edge serve(start_year,end_year) values "player139"->"team218":(2019, 2019);
        insert edge serve(start_year,end_year) values "player140"->"team224":(1994, 2000);
        insert edge serve(start_year,end_year) values "player140"->"team226":(2000, 2007);
        insert edge serve(start_year,end_year) values "player140"->"team214":(2007, 2012);
        insert edge serve(start_year,end_year) values "player140"->"team207":(2012, 2013);
        insert edge serve(start_year,end_year) values "player141"->"team225":(1996, 2003);
        insert edge serve(start_year,end_year) values "player141"->"team205":(2003, 2007);
        insert edge serve(start_year,end_year) values "player141"->"team217":(2007, 2012);
        insert edge serve(start_year,end_year) values "player141"->"team229":(2012, 2014);
        insert edge serve(start_year,end_year) values "player142"->"team200":(2011, 2019);
        insert edge serve(start_year,end_year) values "player143"->"team223":(2015, 2019);
        insert edge serve(start_year,end_year) values "player143"->"team213":(2019, 2020);
        insert edge serve(start_year,end_year) values "player144"->"team226":(1992, 1996);
        insert edge serve(start_year,end_year) values "player144"->"team210":(1996, 2004);
        insert edge serve(start_year,end_year) values "player144"->"team229":(2004, 2008);
        insert edge serve(start_year,end_year) values "player144"->"team214":(2008, 2009);
        insert edge serve(start_year,end_year) values "player144"->"team216":(2009, 2010);
        insert edge serve(start_year,end_year) values "player144"->"team217":(2010, 2011);
        insert edge serve(start_year,end_year) values "player145"->"team228":(2008, 2012);
        insert edge serve(start_year,end_year) values "player145"->"team201":(2012, 2015);
        insert edge serve(start_year,end_year) values "player145"->"team213":(2015, 2016);
        insert edge serve(start_year,end_year) values "player145"->"team200":(2016, 2018);
        insert edge serve(start_year,end_year) values "player145"->"team210":(2018, 2019);
        insert edge serve(start_year,end_year) values "player146"->"team226":(2004, 2012);
        insert edge serve(start_year,end_year) values "player146"->"team210":(2012, 2013);
        insert edge serve(start_year,end_year) values "player146"->"team202":(2013, 2016);
        insert edge serve(start_year,end_year) values "player146"->"team222":(2016, 2017);
        insert edge serve(start_year,end_year) values "player146"->"team215":(2017, 2018);
        insert edge serve(start_year,end_year) values "player146"->"team228":(2018, 2019);
        insert edge serve(start_year,end_year) values "player147"->"team214":(2002, 2010);
        insert edge serve(start_year,end_year) values "player147"->"team223":(2010, 2015);
        insert edge serve(start_year,end_year) values "player147"->"team229":(2015, 2016);
        insert edge serve(start_year,end_year) values "player148"->"team213"@19941996:(1994, 1996);
        insert edge serve(start_year,end_year) values "player148"->"team214":(1996, 2001);
        insert edge serve(start_year,end_year) values "player148"->"team227":(2001, 2008);
        insert edge serve(start_year,end_year) values "player148"->"team213"@20082012:(2008, 2012);
        insert edge serve(start_year,end_year) values "player148"->"team223":(2012, 2013);
        insert edge serve(start_year,end_year) values "player149"->"team219":(2016, 2019);
        insert edge serve(start_year,end_year) values "player150"->"team213":(2018, 2019);
    """,
    )
