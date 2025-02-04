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

#  [GUI](GUI.html).BringWindowToFront

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

public static void BringWindowToFront(int windowID);

### Parameters

windowID | The identifier used when you created the window in the [Window](GUI.Window.html) call.  
---|---  
  
### Description

Bring a specific window to front of the floating windows.

    
    
    // Draws 2 overlapped windows and when clicked on 1 window's button
    // Brings the other window to the front.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Rect](Rect.html) windowRect = new [Rect](Rect.html)(20, 20, 120, 50);
        private [Rect](Rect.html) windowRect2 = new [Rect](Rect.html)(80, 20, 120, 50);  
      
        void OnGUI()
        {
            windowRect = [GUI.Window](GUI.Window.html)(0, windowRect, DoMyFirstWindow, "First");
            windowRect2 = [GUI.Window](GUI.Window.html)(1, windowRect2, DoMySecondWindow, "Second");
        }  
      
        void DoMyFirstWindow(int windowID)
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 20, 100, 20), "Bring to front"))
                [GUI.BringWindowToFront](GUI.BringWindowToFront.html)(1); // Bring the 2nd window to front  
      
            [GUI.DragWindow](GUI.DragWindow.html)(new [Rect](Rect.html)(0, 0, 10000, 20));
        }  
      
        void DoMySecondWindow(int windowID)
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 20, 100, 20), "Bring to front"))
                [GUI.BringWindowToFront](GUI.BringWindowToFront.html)(0); // Bring the 1rst window to front  
      
            [GUI.DragWindow](GUI.DragWindow.html)(new [Rect](Rect.html)(0, 0, 10000, 20));
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

