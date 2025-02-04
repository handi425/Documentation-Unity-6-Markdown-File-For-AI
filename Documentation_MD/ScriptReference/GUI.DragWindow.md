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

#  [GUI](GUI.html).DragWindow

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

public static void DragWindow([Rect](Rect.html) position);

### Parameters

position | The part of the window that can be dragged. This is clipped to the actual window.  
---|---  
  
### Description

Make a window draggable.

Insert a call to this function inside your window code to make a window
draggable.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Rect](Rect.html) windowRect = new [Rect](Rect.html)(20, 20, 120, 50);  
      
        void OnGUI()
        {
            // Register the window.
            windowRect = [GUI.Window](GUI.Window.html)(0, windowRect, DoMyWindow, "My Window");
        }  
      
        // Make the contents of the window
        void DoMyWindow(int windowID)
        {
            // Make a very long rect that is 20 pixels tall.
            // This will make the window be resizable by the top
            // title bar - no matter how wide it gets.
            [GUI.DragWindow](GUI.DragWindow.html)(new [Rect](Rect.html)(0, 0, 10000, 20));
        }
    }
    

* * *

## Declaration

public static void DragWindow();

### Description

If you want to have the entire window background to act as a drag area, use
the version of DragWindow that takes no parameters and put it at the end of
the window function.

This will mean that any other controls will get precedence and the dragging
will only be activated if nothing else has mouse focus. Additional resources:
[DragWindow](GUI.DragWindow.html),
[BringWindowToFront](GUI.BringWindowToFront.html),
[BringWindowToBack](GUI.BringWindowToBack.html).

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Rect](Rect.html) windowRect = new [Rect](Rect.html)(20, 20, 120, 50);  
      
        void OnGUI()
        {
            windowRect = [GUI.Window](GUI.Window.html)(0, windowRect, DoMyWindow, "My Window");
        }  
      
        // Make the contents of the window
        void DoMyWindow(int windowID)
        {
            [GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 20, 100, 20), "Can't drag me");
            // Insert a huge dragging area at the end.
            // This gets clipped to the window (like all other controls) so you can never
            //  drag the window from outside it.
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

