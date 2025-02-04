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

#  [Application](Application.html).unloading

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

Unity raises this event when the Player is unloading.

Add an event handler to this event if you want to trigger events to
[Application.Unload](Application.Unload.html) calls. The event is raised after
a call to [Application.Unload](Application.Unload.html) is made, right before
the unloading starts.  
  
**Note:** The `Application.unloading` event is only supported on iOS, Android,
and Universal Windows Platform.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Unload Unity when the user clicks the button. Exit is not applied to the application.  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 10, 200, 75), "Unload"))
                [Application.Unload](Application.Unload.html)();
        }  
      
        static void OnUnload()
        {
            [Debug.Log](Debug.Log.html)("Unloading the Player");
        }  
      
        [RuntimeInitializeOnLoadMethod]
        static void RunOnStart()
        {
            [Application.unloading](Application-unloading.html) += OnUnload;
        }
    }
    

Additional resources: [Application.Unload](Application.Unload.html).

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

