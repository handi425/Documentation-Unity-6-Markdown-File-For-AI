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

#  [Application](Application.html).CancelQuit

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

**Obsolete** CancelQuit is deprecated. Use the wantsToQuit event instead.

## Declaration

public static void CancelQuit();

### Description

Cancels quitting the application. This is used for showing a splash screen at
the end of a game.

This function only works in the Player.  
  
**Note:** [CancelQuit](Application.CancelQuit.html) is deprecated. Use
[Application.wantsToQuit](Application-wantsToQuit.html) instead.  
  
**Note:** This function has no effect on iPhone. Application cannot prevent
termination under iPhone OS.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Delays quitting for 2 seconds and
        // loads the finalsplash level during that time.  
      
        float showSplashTimeout = 2.0f;
        bool  allowQuitting = false;  
      
        void Awake()
        {
            // This game object needs to survive multiple levels
            Application.DontDestroyOnLoad(this.gameObject);
        }  
      
        void OnApplicationQuit()
        {
            // If we haven't already load up the final splash screen level
            if (Application.loadedLevelName.ToLower() != "finalsplash")
            {
                StartCoroutine("DelayedQuit");
            }  
      
            // Don't allow the user to exit until we got permission in
            if (!allowQuitting)
            {
                Application.CancelQuit();
            }
        }  
      
        IEnumerator DelayedQuit()
        {
            Application.LoadLevel("finalsplash");  
      
            // Wait for showSplashTimeout
            yield return new [WaitForSeconds](WaitForSeconds.html)(showSplashTimeout);  
      
            // then quit for real
            allowQuitting = true;
            [Application.Quit](Application.Quit.html)();
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

