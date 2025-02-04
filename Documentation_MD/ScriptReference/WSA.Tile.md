[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# Tile

class in UnityEngine.WSA

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Represents tile on Windows start screen

This class can be used to create or update secondary tiles on start screen and
get instances of tiles to send notifications to them.

### Static Properties

[main](WSA.Tile-main.html)| Returns applications main tile  
---|---  
  
### Properties

[exists](WSA.Tile-exists.html)| Whether secondary tile is pinned to start
screen.  
---|---  
[hasUserConsent](WSA.Tile-hasUserConsent.html)| Whether secondary tile was
approved (pinned to start screen) or rejected by user.  
[id](WSA.Tile-id.html)| A unique string, identifying secondary tile  
  
### Public Methods

[Delete](WSA.Tile.Delete.html)| Show a request to unpin secondary tile from
start screen.  
---|---  
[PeriodicBadgeUpdate](WSA.Tile.PeriodicBadgeUpdate.html)| Starts periodic
update of a badge on a tile.  
[PeriodicUpdate](WSA.Tile.PeriodicUpdate.html)| Starts periodic update of a
tile.  
[RemoveBadge](WSA.Tile.RemoveBadge.html)| Remove badge from tile.  
[StopPeriodicBadgeUpdate](WSA.Tile.StopPeriodicBadgeUpdate.html)| Stops
previously started periodic update of a tile.  
[StopPeriodicUpdate](WSA.Tile.StopPeriodicUpdate.html)| Stops previously
started periodic update of a tile.  
[Update](WSA.Tile.Update.html)| Send a notification for tile (update tiles
look).  
[UpdateBadgeImage](WSA.Tile.UpdateBadgeImage.html)| Sets or updates badge on a
tile to an image.  
[UpdateBadgeNumber](WSA.Tile.UpdateBadgeNumber.html)| Set or update a badge on
a tile to a number.  
  
### Static Methods

[CreateOrUpdateSecondary](WSA.Tile.CreateOrUpdateSecondary.html)| Creates new
or updates existing secondary tile.  
---|---  
[DeleteSecondary](WSA.Tile.DeleteSecondary.html)| Show a request to unpin
secondary tile from start screen.  
[Exists](WSA.Tile.Exists.html)| Whether secondary tile is pinned to start
screen.  
[GetSecondaries](WSA.Tile.GetSecondaries.html)| Gets all secondary tiles.  
[GetSecondary](WSA.Tile.GetSecondary.html)| Returns the secondary tile,
identified by tile id.  
[GetTemplate](WSA.Tile.GetTemplate.html)| Get template XML for tile
notification.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

