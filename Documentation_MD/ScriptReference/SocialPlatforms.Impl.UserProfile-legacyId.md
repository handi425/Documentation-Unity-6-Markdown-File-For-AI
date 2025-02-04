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

**Removed**  

#  [UserProfile](SocialPlatforms.Impl.UserProfile.html).legacyId

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

**Obsolete** legacyId returns playerID from GKPlayer, which became obsolete in
iOS 12.4 . id returns playerID for devices running versions before iOS 12.4,
and the newer teamPlayerID for later versions. Please use IUserProfile.id or
UserProfile.id instead.  
**Upgrade to[id](UserProfile-id.html)** public string legacyId;

### Description

Returns the ID provided in the Apple GameKit by GKPlayer.playerID (deprecated
and marked obsolete in iOS 12.4).

For devices running iOS version 12.4 and later, IUserProfile.id returns
[GKPlayer.teamPlayerID](https://developer.apple.com/documentation/gamekit/gkplayer/3174857-teamplayerid?language=objc).  
  
For devices running iOS version 12.3 and earlier, IUserProfile.id returns
[GKPlayer.playerID](https://developer.apple.com/documentation/gamekit/gkplayer/1521127-playerid?language=objc).  
  
Use IUserProfile.id instead of UserProfile.legacyId. Only use
UserProfile.legacyId if you need to access
[GKPlayer.playerID](https://developer.apple.com/documentation/gamekit/gkplayer/1521127-playerid?language=objc)
to migrate player data in your existing project.

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

