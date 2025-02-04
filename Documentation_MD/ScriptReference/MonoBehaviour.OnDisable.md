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

#  [MonoBehaviour](MonoBehaviour.html).OnDisable()

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

### Description

This function is called when the behaviour becomes disabled.

This is also called when the object is destroyed and can be used for any
cleanup code. When scripts are reloaded after compilation has finished,
OnDisable will be called, followed by an OnEnable after the script has been
loaded.

    
    
    // Implement OnDisable and OnEnable script functions.
    // These functions will be called when the attached [GameObject](GameObject.html)
    // is toggled.
    // This example also supports the [Editor](Editor.html).  The [Update](PlayerLoop.Update.html) function
    // will be called, for example, when the position of the
    // [GameObject](GameObject.html) is changed.  
      
    using UnityEngine;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class PrintOnOff : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnDisable()
        {
            [Debug.Log](Debug.Log.html)("PrintOnDisable: script was disabled");
        }  
      
        void OnEnable()
        {
            [Debug.Log](Debug.Log.html)("PrintOnEnable: script was enabled");
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
    #if UNITY_EDITOR
            [Debug.Log](Debug.Log.html)("[Editor](Editor.html) causes this [Update](PlayerLoop.Update.html)");
    #endif
        }
    }
    

**Note:** [OnDisable](MonoBehaviour.OnDisable.html) cannot be a co-routine.  
Additional resources: [OnEnable](MonoBehaviour.OnEnable.html).

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

