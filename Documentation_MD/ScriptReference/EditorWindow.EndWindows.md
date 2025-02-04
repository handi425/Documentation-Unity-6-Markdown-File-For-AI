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

#  [EditorWindow](EditorWindow.html).EndWindows

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

public void EndWindows();

### Description

Close a window group started with
[EditorWindow.BeginWindows](EditorWindow.BeginWindows.html).

![](../StaticFiles/ScriptRefImages/GUIWindowDemo.png)  
_Simple editor Window with a window and a button inside._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;
    
    public class IMGUIWindowDemo : [EditorWindow](EditorWindow.html)
    {
        // The position of the window
        public [Rect](Rect.html) windowRect = new [Rect](Rect.html)(100, 100, 200, 200);
        void OnGUI()
        {
            BeginWindows();
    
            // All [GUI.Window](GUI.Window.html) or [GUILayout.Window](GUILayout.Window.html) must come inside here
            windowRect = [GUILayout.Window](GUILayout.Window.html)(1, windowRect, DoWindow, "Hi There");
    
            EndWindows();
        }
    
        // The window function. This works just like ingame [GUI.Window](GUI.Window.html)
        void DoWindow(int unusedWindowID)
        {
            [GUILayout.Button](GUILayout.Button.html)("Hi");
            [GUI.DragWindow](GUI.DragWindow.html)();
        }
    
        // Add menu item to show this demo.
        [[MenuItem](MenuItem.html)("Test/GUIWindow Demo")]
        static void Init()
        {
            [EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(IMGUIWindowDemo));
        }
    }
    

The placement of the [BeginWindows](EditorWindow.BeginWindows.html) /
[EndWindows](EditorWindow.EndWindows.html) pair determines where popup windows
will appear; all windows are clipped to the clipping area defined by
[GUI.BeginGroup](GUI.BeginGroup.html) or
[GUI.BeginScrollView](GUI.BeginScrollView.html). A small example of that:  
  
![](../StaticFiles/ScriptRefImages/GUIWindowDemo2.png)  
_Simple editor window with a window and a button inside using scroll bars._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;
    
    public class IMGUIWindowDemo2 : [EditorWindow](EditorWindow.html)
    {
        // The position of the window
        public [Rect](Rect.html) windowRect = new [Rect](Rect.html)(100, 100, 200, 200);
    
        // Scroll position
        public [Vector2](Vector2.html) scrollPos = [Vector2.zero](Vector2-zero.html);
    
        void OnGUI()
        {
            // Set up a scroll view
            scrollPos = [GUI.BeginScrollView](GUI.BeginScrollView.html)(new [Rect](Rect.html)(0, 0, position.width, position.height), scrollPos, new [Rect](Rect.html)(0, 0, 1000, 1000));
    
            // Same code as before - make a window. Only now, it's INSIDE the scrollview
            BeginWindows();
            windowRect = [GUILayout.Window](GUILayout.Window.html)(1, windowRect, DoWindow, "Hi There");
            EndWindows();
            // Close the scroll view
            [GUI.EndScrollView](GUI.EndScrollView.html)();
        }
    
        void DoWindow(int unusedWindowID)
        {
            [GUILayout.Button](GUILayout.Button.html)("Hi");
            [GUI.DragWindow](GUI.DragWindow.html)();
        }
    
        [[MenuItem](MenuItem.html)("Test/GUIWindow Demo 2")]
        static void Init()
        {
            [EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(IMGUIWindowDemo2));
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

