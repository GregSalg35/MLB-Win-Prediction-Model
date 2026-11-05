WITH

teamstats AS (
	SELECT 
    yearID,
    lgID,
    teamID,
    G,
    W,
    L,
    R,
    R / G AS RperGame,
    AB,
    AB + BB + HBP + SF AS PA,
    H,
    (H - `2B` - `3B` - HR) AS `1B`,
    `2B`,
    `3B`,
    HR,
    BB,
    SO,
    SB,
    CS,
    HBP,
    SF,
    RA,
    ER,
    CG,
    SHO,
    SV,
    HA,
    HRA,
    BBA,
    SOA,
    E,
    DP
    
    FROM teams
    
    WHERE yearID > 1989
    AND yearID != 1994 AND yearID != 1995 AND yearID != 2020
),

detailedstats AS (
    SELECT *,
        (1*`1B` + 2*`2B` + 3*`3B` + 4*HR) AS TB,
        ROUND(H / AB, 3) AS Average,
        ROUND((H + BB + HBP) / (AB + BB + HBP + SF), 3) AS OBP,
        ROUND((1*`1B` + 2*`2B` + 3*`3B` + 4*HR) / AB, 3) AS SLG,
        ROUND((H + BB + HBP) / (AB + BB + HBP + SF) + (1*`1B` + 2*`2B` + 3*`3B` + 4*HR) / AB,3) AS OPS,
        BB / PA AS BBpercent,
        SO / PA AS KPercent,
        BB / SO AS BBtoKratio,
        HR / PA AS HRrate,
        `2B` + `3B` + HR AS XBH,
        HR / G AS HRperGame,
        RA / G AS RAperGame
        
        
    FROM teamstats
),

finerstats AS (
	SELECT *,
    SLG - Average AS ISO,
    XBH / PA AS XBHrate,
    (H - HR) / (AB - SO - HR + SF) AS BattedBalls
    
    FROM detailedstats
)
	

SELECT *
FROM finerstats

    