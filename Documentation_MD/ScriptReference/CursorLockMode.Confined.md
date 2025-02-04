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

#  [CursorLockMode](CursorLockMode.html).Confined

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

Confine cursor to the game window.

Note that confined cursor lock mode is only supported on the standalone player
platform on Windows and Linux. Confined cursor lock mode is not supported on
MacOS or Android.

    
    
    //This script makes Buttons that control the [Cursor](Cursor.html)'s lock state. Note that the Confined mode only works on Windows and Linux [Standalone](Unity.Android.Gradle.Manifest.Standalone.html) platform build.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            //Press the space bar to apply no locking to the [Cursor](Cursor.html)
            if ([Input.GetKey](Input.GetKey.html)([KeyCode.Space](KeyCode.Space.html)))
                [Cursor.lockState](Cursor-lockState.html) = [CursorLockMode.None](CursorLockMode.None.html);
        }  
      
        void OnGUI()
        {
            //Press this button to lock the [Cursor](Cursor.html)
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 0, 100, 50), "Lock [Cursor](Cursor.html)"))
            {
                [Cursor.lockState](Cursor-lockState.html) = [CursorLockMode.Locked](CursorLockMode.Locked.html);
            }  
      
            //Press this button to confine the [Cursor](Cursor.html) within the screen
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(125, 0, 100, 50), "Confine [Cursor](Cursor.html)"))
            {
                [Cursor.lockState](Cursor-lockState.html) = [CursorLockMode.Confined](CursorLockMode.Confined.html);
            }
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

