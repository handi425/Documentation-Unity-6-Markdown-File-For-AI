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

#  [MonoBehaviour](MonoBehaviour.html).OnApplicationFocus(bool)

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

hasFocus | True if the GameObjects have focus, else False.  
---|---  
  
### Description

Sent to all GameObjects when the player gets or loses focus.

[OnApplicationFocus](MonoBehaviour.OnApplicationFocus.html) is called when the
application loses or gains focus. Alt-tabbing or Cmd-tabbing can take focus
away from the Unity application to another desktop application. This causes
the GameObjects to receive an
[OnApplicationFocus](MonoBehaviour.OnApplicationFocus.html) call with the
argument set to false. When the user switches back to the Unity application,
the GameObjects receive an
[OnApplicationFocus](MonoBehaviour.OnApplicationFocus.html) call with the
argument set to true.  
  
[OnApplicationFocus](MonoBehaviour.OnApplicationFocus.html) can be a co-
routine; to do this, use the yield statement in the function. Implemented this
way, it is evaluated twice during the initial frame: first as an early
notification, and secondly during the normal co-routine update step.  
  
On Android, when the on-screen keyboard is enabled, it causes an
[OnApplicationFocus](MonoBehaviour.OnApplicationFocus.html)( false ) event. If
you press **Home** when the keyboard is enabled, the
[OnApplicationPause](MonoBehaviour.OnApplicationPause.html)() event is called
instead of the [OnApplicationFocus](MonoBehaviour.OnApplicationFocus.html)()
event.  
  
**Note** : If the Editor is in Play mode,
[OnApplicationFocus](MonoBehaviour.OnApplicationFocus.html) is called when the
Game view loses or gains focus. If an external application (meaning an
application other than Unity) has focus, and you click a different Editor tab,
::OnApplicationFocus is called twice in one frame. The first time,
[OnApplicationFocus](MonoBehaviour.OnApplicationFocus.html) is called with
hasFocus set to true because the Game view regains focus when Unity regains
focus. The second time,
[OnApplicationFocus](MonoBehaviour.OnApplicationFocus.html) is called with
hasFocus set to false because the Game view loses focus to the Editor tab that
was clicked.  
  
To minimize the number of times
[OnApplicationFocus](MonoBehaviour.OnApplicationFocus.html) is called when the
Editor is in Play mode, and you are using the rest of the Editor, drag the
Game view into a floating window.

    
    
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

