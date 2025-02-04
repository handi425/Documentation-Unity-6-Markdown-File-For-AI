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

#  [AndroidGame.Automatic](Android.AndroidGame.Automatic.html).SetGameState

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

## Declaration

public static void
SetGameState([Android.AndroidGameState](Android.AndroidGameState.html) mode);

### Parameters

mode |  [AndroidGameState](Android.AndroidGameState.html) value.  
---|---  
  
### Description

Sets the current [AndroidGameState](Android.AndroidGameState.html) to be used
for [Automated game state hinting in Unity](../Manual/android-game-state-
hinting.html). Requires API level 33 (Android 13).

You can set the mode parameter based on the current game state. For example,
you can use [AndroidGameState.None](Android.AndroidGameState.None.html) for
displaying the game menu and
[AndroidGameState.GamePlayInterruptible](Android.AndroidGameState.GamePlayInterruptible.html)
or
[AndroidGameState.GamePlayUninterruptible](Android.AndroidGameState.GamePlayUninterruptible.html)
during the gameplay.  
  
Once set, the mode remains unchanged until you call this method again.
However, if the game is interrupted by a full-screen video or a full-screen
ad, the mode automatically changes to
[AndroidGameState.Content](Android.AndroidGameState.Content.html).  
  
When target device does not support the required API level, no action is
taken.

    
    
    using UnityEngine;
    using UnityEngine.Android;  
      
    public class MainMenu : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [AndroidGame.Automatic.SetGameState](Android.AndroidGame.Automatic.SetGameState.html)([AndroidGameState.None](Android.AndroidGameState.None.html));
        }
    }
    

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

