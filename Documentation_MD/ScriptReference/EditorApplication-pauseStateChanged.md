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

#  [EditorApplication](EditorApplication.html).pauseStateChanged

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

Event that is raised whenever the Editor's pause state changes.

Add an event handler to this event to receive a notification that the pause
state has changed, as well as information about the state it has changed into.  
  
Note that the Editor may be paused or unpaused in both edit mode and play
mode, so you should test [isPlaying](EditorApplication-isPlaying.html) inside
your event handler if you need to discriminate between these two conditions.  
  
The following example script logs the Editor's pause state to the console
whenever if changes. Copy it into a file called PauseStateChangedExample.cs
and put it in a folder called Editor.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // ensure class initializer is called whenever scripts recompile
    [[InitializeOnLoadAttribute](InitializeOnLoadAttribute.html)]
    public static class PauseStateChangedExample
    {
        // register an event handler when the class is initialized
        static PauseStateChangedExample()
        {
            [EditorApplication.pauseStateChanged](EditorApplication-pauseStateChanged.html) += LogPauseState;
        }  
      
        private static void LogPauseState([PauseState](PauseState.html) state)
        {
            [Debug.Log](Debug.Log.html)(state);
        }
    }
    

Additional resources: [PauseState](PauseState.html),
[EditorApplication.isPaused](EditorApplication-isPaused.html),
[EditorApplication.playModeStateChanged](EditorApplication-
playModeStateChanged.html).

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

