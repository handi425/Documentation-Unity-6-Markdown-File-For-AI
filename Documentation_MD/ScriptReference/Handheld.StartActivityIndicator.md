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

#  [Handheld](Handheld.html).StartActivityIndicator

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

public static void StartActivityIndicator();

### Description

Starts os activity indicator.

Please be warned that this informs os ui system to start. For actual animation
to take effect you usually need to wait till the end of this frame. So if you
want activity indicator to be animated during synced operation, please use
coroutines. Note: You can't move the activity indicator invoked by this
method.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class Example2 : [MonoBehaviour](MonoBehaviour.html)
    {
        IEnumerator Load()
        {
            #if UNITY_IPHONE
            [Handheld.SetActivityIndicatorStyle](Handheld.SetActivityIndicatorStyle.html)(iOS.ActivityIndicatorStyle.Gray);
            #elif UNITY_ANDROID
            [Handheld.SetActivityIndicatorStyle](Handheld.SetActivityIndicatorStyle.html)([AndroidActivityIndicatorStyle.Small](AndroidActivityIndicatorStyle.Small.html));
            #endif  
      
            [Handheld.StartActivityIndicator](Handheld.StartActivityIndicator.html)();
            yield return new [WaitForSeconds](WaitForSeconds.html)(0);
            [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("My Next [Scene](SceneManagement.Scene.html)");
        }  
      
        void OnGUI()
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 10, 200, 200), "Load!"))
                StartCoroutine(Load());
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

