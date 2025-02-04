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

#  [MonoBehaviour](MonoBehaviour.html).OnApplicationPause(bool)

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

[Switch to Manual](../Manual/class-MonoBehaviour.html "Go to MonoBehaviour
Component in the Manual")

### Parameters

pauseStatus | True if the application is paused, False if playing.  
---|---  
  
### Description

Sent to all GameObjects when the playing application pauses or resumes on
losing or regaining focus.

When [Run In Background](PlayerSettings-runInBackground.html) (**Edit >
Project Settings > Player > Resolution and Presentation**) is disabled, a game
running in the Editor's Play mode or in a standalone Player will pause any
time the Editor or Player application loses focus. In these cases Unity sends
`OnApplicationPause(true)` to all MonoBehaviours.  
  
The `pauseStatus` parameter is either `true` (paused) or `false` (running).
All MonoBehaviours receive this event while they are initializing, just after
`Awake`, so it will be called (with status `false`) on first entering Play
mode. They receive it again whenever the application pauses or unpauses on
losing or regaining focus.  
  
**Note** : Unity does **not** call `OnApplicationPause` in response to
toggling the Pause button in the [Editor toolbar](../Manual/Toolbar.html). The
status of the pause button in the Editor is tracked by the
[PauseState](PauseState.html) enum.  
  
For `OnApplicationPause` to trigger in a Player application running separately
from the Editor, the running Player must be windowed and smaller than the full
screen. If the game is hidden (fully or partly) by another application then it
pauses and Unity calls `OnApplicationPause` with `true`. When the game regains
focus, Unity calls `OnApplicationPause` with `false`.  
  
`OnApplicationPause` can be a co-routine; to do this use the `yield` statement
in the function. Implemented this way, it is evaluated twice during the
initial frame: first as an early notification, and secondly during the normal
co-routine update step.  
  
On **Android** , enabling the on-screen keyboard causes an
[OnApplicationFocus](MonoBehaviour.OnApplicationFocus.html) event with the
value `false`. However, if you press "Home" at the moment the keyboard is
enabled, the `OnApplicationFocus` event is not called and `OnApplicationPause`
is called instead.

    
    
    using UnityEngine;  
      
    public class AppPaused : [MonoBehaviour](MonoBehaviour.html)
    {
        bool isPaused = false;  
      
        void OnGUI()
        {
            if (isPaused)
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(100, 100, 50, 30), "Game paused");
        }  
      
        void OnApplicationFocus(bool hasFocus)
        {
            isPaused = !hasFocus;
        }  
      
        void OnApplicationPause(bool pauseStatus)
        {
            isPaused = pauseStatus;
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

