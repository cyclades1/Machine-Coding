from player import Player_dir
from team import Team_dir


from service import create_player, create_team ,create_bid, auction_end,\
                        getplayerbids,getteambids, auction_start

getnum = lambda: int(input())
getnums = lambda : map(int, input().split())
getvals = lambda: input().split()



def main():
    Auction_player = None

    value= getvals()
    while value[0]!="exit":
        if value[0]=="createplayer":
            try:
                value[2] = int(value[2])
                create_player(value[1],value[2] )
            except Exception as e:
                print(e)

        if value[0]=="createteam":
            try:
                value[2] = int(value[2])
                create_team(value[1],value[2] )
            except Exception as e:
                print(e)
        if value[0]=="startauction":
            if not Auction_player:
                Auction_player= auction_start(value[1])
            else:
                print("Another auction running")

        if value[0]=="endauction":
            if not Auction_player:
                pass
            else:
                auction_end(Auction_player)
                Auction_player=None
        if value[0]=="createbid":
            if not Auction_player:
                pass
            else:
                try:
                    value[2] = int(value[2])
                    create_bid(value[1],Auction_player, value[2] )
                except Exception as e:
                    print(e)

        if value[0]=="teamoverview":
            for team in Team_dir:
                print(Team_dir[team].get_overview())
        
        if value[0]=="playeroverview":
            for player in Player_dir:
                print(Player_dir[player].get_overview())
           
        
        if value[0]=="bidhistory":
            print(value[2],": ")
            if value[1]=="player":
                getplayerbids(value[2])
            if value[1]=="team":

                getteambids(value[2])
        value= getvals()
        
    

if __name__=="__main__":
    main()