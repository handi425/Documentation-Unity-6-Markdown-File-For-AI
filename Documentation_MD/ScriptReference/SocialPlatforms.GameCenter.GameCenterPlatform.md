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

**Method group is Obsolete**  

# GameCenterPlatform

class in UnityEngine.SocialPlatforms.GameCenter

/

Implemented
in:[UnityEngine.GameCenterModule](UnityEngine.GameCenterModule.html)

Leave feedback

  

Implements interfaces:[ISocialPlatform](SocialPlatforms.ISocialPlatform.html)

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

**Obsolete** GameCenterPlatform is deprecated and will be removed in a future
release.

### Description

iOS GameCenter implementation for network services.

An application bundle ID must be registered on iTunes Connect before it can
access GameCenter. This ID must be properly set in the iOS player properties
in Unity. When debugging you can use the GameCenter sandbox (a text displaying
this is shown when logging on). You must log on in the application to get into
sandbox mode, logging on in the GameCenter application will always use the
production version.  
  
When using the GameCenterPlatform class in C# you need to include the
UnityEngine.SocialPlatforms.GameCenter namespace.  
  
Some things to be aware of when using the generic API:  
  
**Authenticate()**  
If the user is not logged in, a standard GameKit UI is shown where they can
log on or create a new user. It is recommended this is done as early as
possible.  
  
**Achievement descriptions and Leaderboards**  
The achivements descriptions and leaderboard configurations can be configured
in the iTunes Connect portal. Achievements get unique identifiers and the
leaderboards use category names as identifiers.  
  
**GameCenter Sandbox**  
Development applications use the GameCenter Sandbox. This is a seperate
GameCenter than the live one, nothing is shared between them. It is
recommended that you create a seperate user for testing with the GameCenter
Sandbox, you should not use your real Apple ID for this. You can only log on
to the sandbox through a development application, make sure you are not logged
into GameCenter using the GameCenter app before testing begins. You should see
_*** Sandbox ***_ in the login dialog, if you don't see this then you are
logging on to the real one. Sometimes it happens that the OS forgets that the
application is using the sandbox and you will be logged on to the real one. If
the application has not been submitted to Apple already then this will
probably result in an error. To fix this all that needs to be done is to
delete the app and redeploy with Xcode. To make another Apple ID a friend of a
sandbox user it needs to be a sandbox user as well.  
  
If you start getting errors when accessing GameCenter stating that the
application is not recognized you'll need to delete the application completely
and re-deploy. Make sure you are not logged on when starting the newly
installed application again.

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

