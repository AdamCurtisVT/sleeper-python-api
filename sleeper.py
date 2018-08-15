#-------------------------------------------------
# Imports
#-------------------------------------------------
import sys
import json
import requests

#-------------------------------------------------
# Classes - User
#-------------------------------------------------

# Represents a Sleeper.app user.
class User(object):
    Username = ''
    UserId = ''
    DisplayName = ''    
    AvatarId = ''

    # Initializes a new instance of the User class.
    def __init__(self, jsonText):
        self.Username = jsonText['username']
        self.UserId = jsonText['user_id']
        self.DisplayName = jsonText['display_name']
        self.AvatarId = jsonText['avatar']

#-------------------------------------------------
# Classes - Leagues
#-------------------------------------------------

# Represents a Sleeper.app league.
class League(object):
    TotalRosters = 0;
    Status = ''
    Sport = ''
    Settings = ''
    SeasonType = ''
    Season = ''
    ScoringSettings = ''
    RosterPositions = ''
    PreviousLeagueId = ''
    Name = ''
    LeagueId = ''
    DraftId = ''
    AvatarId = ''

    # Initializes a new instance of the League class.
    def __init__(self, jsonText):
        self.TotalRosters = jsonText['total_rosters']
        self.Status = jsonText['status']
        self.Sport = jsonText['sport']
        self.Settings = LeagueSettings(jsonText['settings'])
        self.SeasonType = jsonText['season_type']
        self.Season = jsonText['season']
        self.ScoringSettings = ScoringSettings(jsonText['scoring_settings'])
        self.RosterPositions = jsonText['roster_positions']
        self.PreviousLeagueId = jsonText['previous_league_id']
        self.Name = jsonText['name']
        self.LeagueId = jsonText['league_id']
        self.DraftId = jsonText['draft_id']
        self.Avatar = jsonText['avatar']

# Represents Sleeper.app league settings.
class LeagueSettings(object):
    WaiverType = 0
    WaiverDayOfWeek = 0
    WaiverClearDays = 0
    WaiverBudget = 0
    Type = 0
    TradeReviewDays = 0
    TradeDeadline = 0
    TaxiYears = 0
    TaxiSlots = 0
    TaxiDeadline = 0
    TaxiAllowVets = 0
    StartWeek = 0
    ReserveSlots = 0
    PlayoffWeekStart = '0
    PlayoffTeams = 0
    PickTrading = 0
    OffseasonAdds = 0
    NumberOfTeams = 0
    MaxKeepers = 0
    Leg = 0
    DraftRounds = 0
    DailyWaiversLastRan = 0
    DailyWaiversHour = 0
    DailyWaivers = 0

    # Initializes a new instance of the LeagueSettings class.
    def __init__(self, jsonText):
        self.WaiverType = jsonText['waiver_type']
        self.WaiverDayOfWeek = jsonText['waiver_day_of_week']
        self.WaiverClearDays = jsonText['waiver_clear_days']
        self.WaiverBudget = jsonText['waiver_budget']
        self.Type = jsonText['type']
        self.TradeReviewDays = jsonText['trade_review_days']
        self.TradeDeadline = jsonText['trade_deadline']
        self.TaxiYears = jsonText['taxi_years']
        self.TaxiSlots = jsonText['taxi_slots']
        self.TaxiDeadline = jsonText['taxi_deadline']
        self.TaxiAllowVets = jsonText['taxi_allow_vets']
        self.StartWeek = jsonText['start_week']
        self.ReserveSlots = jsonText['reserve_slots']
        self.PlayoffWeekStart = jsonText['playoff_week_start']
        self.PlayoffTeams = jsonText['playoff_teams']
        self.PickTrading = jsonText['pick_trading']
        self.OffseasonAdds = jsonText['offseason_adds']
        self.NumberOfTeams = jsonText['num_teams']
        self.MaxKeepers = jsonText['max_keepers']
        self.Leg = jsonText['leg']
        self.DraftRounds = jsonText['draft_rounds']
        self.DailyWaiversLastRan = jsonText['daily_waivers_last_ran']
        self.DailyWaiversHour = jsonText['daily_waivers_hour']
        self.DailyWaivers = jsonText['daily_waivers']
        
# Represents a Sleeper.app league user.
class LeagueUser(object):
    UserId = ''
    Settings = ''
    TeamName = ''  
    MentionPn = ''  
    AllowPn = ''  
    LeagueId = ''  
    IsOwner = False
    IsBot = False
    DisplayName = ''    
    AvatarId = ''

    # Initializes a new instance of the LeagueUser class.
    def __init__(self, jsonText):
        self.UserId = jsonText['user_id']
        self.Settings = jsonText['settings']
        self.MentionPn = jsonText['metadata']['mention_pn']
        self.AllowPn = jsonText['metadata']['allow_pn']
        self.LeagueId = jsonText['league_id']
        self.IsOwner = jsonText['is_owner']
        self.IsBot = jsonText['is_bot']
        self.DisplayName = jsonText['display_name']
        self.AvatarId = jsonText['avatar']
        if 'team_name' in jsonText:
            self.TeamName = jsonText['metadata']['team_name']

# Represents a Sleeper.app roster.
class Roster(object):
    Taxi = ''
    Starters = []
    Settings = ''        
    RosterId = ''
    Reserve = []
    Players = []
    PlayerMap = ''
    OwnerId = ''
    Metadata = ''
    LeagueId = ''

    # Initializes a new instance of the Roster class.
    def __init__(self, jsonText):
        self.Taxi = jsonText['taxi']
        self.Starters = jsonText['starters']
        self.Settings = RosterSettings(jsonText['settings'])
        self.RosterId = jsonText['roster_id']
        self.Reserve = jsonText['reserve']
        self.Players = jsonText['players']
        self.PlayerMap = jsonText['player_map']
        self.OwnerId = jsonText['owner_id']
        self.Metadata = jsonText['metadata']
        self.LeagueId = jsonText['league_id']

# Represents Sleeper.app roster settings.
class RosterSettings(object):
    Wins = 0
    WaiverPosition = 0
    WaiverBudgetUsed = 0
    TotalMoves = 0
    Ties = 0
    Losses = 0
    FantasyPoints = 0
    FantasyPointsAgainst = 0
    FantasyPointsDecimal = 0
    FantasyPointsAgainstDecimal = 0

    # Initializes a new instance of the RosterSettings class.
    def __init__(self, jsonText):
        self.Wins = jsonText['wins']
        self.WaiverPosition = jsonText['waiver_position']
        self.WaiverBudgetUsed = jsonText['waiver_budget_used']
        self.TotalMoves = jsonText['total_moves']
        self.Ties = jsonText['ties']
        self.Losses = jsonText['losses']
        if 'fpts' in jsonText:
            self.FantasyPoints = jsonText['fpts']
        if 'fpts_against' in jsonText:
            self.FantasyPointsAgainst = jsonText['fpts_against']
        if 'fpts_decimal' in jsonText:
            self.FantasyPointsDecimal = jsonText['fpts_decimal']
        if 'fpts_against_decimal' in jsonText:
            self.FantasyPointsAgainstDecimal = jsonText['fpts_against_decimal']

class ScoringSettings(object):
    Fumble = 0
    FumbleLost = 0
    RushingTouchdown = 0
    RushingYard = 0
    PassingTouchdown = 0
    PassingYard = 0
    ReceivingTouchdown = 0     
    ReceivingYard = 0
    Reception = 0
    TwoPointReception = 0
    FumbleRecovery = 0    
    ForcedFumble = 0     
    PassingInterception = 0
    PassingTwoPointConversion = 0
    ExtraPointMissed = 0
    ExtraPointMade = 0
    FieldGoalMissed = 0
    FieldGoalMade = 0
    FieldGoalMadeBetween0And19 = 0
    FieldGoalMadeBetween20And29 = 0
    FieldGoalMadeBetween30And39 = 0
    FieldGoalMadeBetween40And49 = 0
    FieldGoalMadeOver50 = 0
    Interception = 0
    DefensiveTouchdown = 0
    Sack = 0
    Safety = 0
    BlockedKick = 0
    PointsAllowed0 = 0
    PointsAllowedBetween1And6 = 0
    PointsAllowedBetween7And13 = 0
    PointsAllowedBetween14And20 = 0
    PointsAllowedBetween21And27 = 0
    PointsAllowedBetween28And34 = 0
    PointsAllowedOver35 = 0
    SpecialTeamsForcedFumble = 0
    SpecialTeamsFumbleRecovery = 0
    SpecialTeamsTouchdown = 0

    # Initializes a new instance of the ScoringSettings class.
    def __init__(self, jsonText):        
        self.Fumble = jsonText['fum']
        self.FumbleLost = jsonText['fum_lost']
        self.RushingTouchdown = jsonText['rush_td']
        self.RushingYard = jsonText['rush_yd']
        self.PassingTouchdown = jsonText['pass_td']
        self.PassingYard = jsonText['pass_yd']
        self.ReceivingTouchdown = jsonText['rec_td']        
        self.ReceivingYard = jsonText['rec_yd']
        self.Reception = jsonText['rec']
        self.TwoPointReception = jsonText['rec_2pt']
        self.FumbleRecovery = jsonText['fum_rec']        
        self.ForcedFumble = jsonText['ff']       
        self.PassingInterception = jsonText['pass_int']
        self.PassingTwoPointConversion = jsonText['pass_2pt']
        self.ExtraPointMissed = jsonText['xpmiss']
        self.ExtraPointMade = jsonText['xpm']
        self.FieldGoalMissed = jsonText['fgmiss']
        self.FieldGoalMade = jsonText['fgm']
        self.FieldGoalMadeBetween0And19 = jsonText['fgm_0_19']
        self.FieldGoalMadeBetween20And29 = jsonText['fgm_20_29']
        self.FieldGoalMadeBetween30And39 = jsonText['fgm_30_39']
        self.FieldGoalMadeBetween40And49 = jsonText['fgm_40_49']
        self.FieldGoalMadeOver50 = jsonText['fgm_50p']
        self.Interception = jsonText['int']
        self.DefensiveTouchdown = jsonText['def_td']
        self.Sack = jsonText['sack']  
        self.Safety = jsonText['safe']
        self.BlockedKick = jsonText['blk_kick']
        self.PointsAllowed0 = jsonText['pts_allow_0']
        self.PointsAllowedBetween1And6 = jsonText['pts_allow_1_6']
        self.PointsAllowedBetween7And13 = jsonText['pts_allow_7_13']
        self.PointsAllowedBetween14And20 = jsonText['pts_allow_14_20']
        self.PointsAllowedBetween21And27 = jsonText['pts_allow_21_27']
        self.PointsAllowedBetween28And34 = jsonText['pts_allow_28_34'] 
        self.PointsAllowedOver35 = jsonText['pts_allow_35p']
        self.SpecialTeamsForcedFumble = jsonText['st_ff']
        self.SpecialTeamsFumbleRecovery = jsonText['st_fum_rec']
        self.SpecialTeamsTouchdown = jsonText['st_td']
        
#-------------------------------------------------
# Functions - User - API
#-------------------------------------------------

# Call the Sleeper API to retrieve a user.
def GetUser(userId):
    if not userId:
        raise ValueError('The User ID must not be null.') 
    endpoint = ('https://api.sleeper.app/v1/user/{}'.format(userId))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        return User(responseJson)
    else:
        return null
    
#-------------------------------------------------
# Functions - Leagues - API
#-------------------------------------------------

# Call the Sleeper API to retrieve a specific league.
def GetLeague(leagueId):
    if not leagueId:
        raise ValueError('The League ID must not be null.') 
    endpoint = ('https://api.sleeper.app/v1/league/{}'.format(leagueId))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        return League(responseJson)
    else:
        return None

# Call the Sleeper API to retrieve all league for a specific user in a season.
def GetLeaguesForUser(userId, season):
    if not userId:
        raise ValueError('The User ID must not be null.')
    if not season:
        raise ValueError('The season must not be null.') 
    endpoint = ('https://api.sleeper.app/v1/user/{}/leagues/nfl/{}'.format(userId, season))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        leagues = list()
        for leagueJson in responseJson:
            leagues.append(League(leagueJson))
        return leagues
    else:
        return None

# Call the Sleeper API to retrieve all rosters in a specific league.
def GetLeagueRosters(leagueId):
    if not leagueId:
        raise ValueError('The League ID must not be null.') 
    endpoint = ('https://api.sleeper.app/v1/league/{}/rosters'.format(leagueId))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        rosters = list()
        for rosterJson in responseJson:
            rosters.append(Roster(rosterJson))
        return rosters
    else:
        return None

# Call the Sleeper API to retrieve all users in a specific league.
def GetLeagueUsers(leagueId):
    if not leagueId:
        raise ValueError('The League ID must not be null.') 
    endpoint = ('https://api.sleeper.app/v1/league/{}/users'.format(leagueId))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        users = list()
        for userJson in responseJson:
            users.append(LeagueUser(userJson))
        return users
    else:
        return None
