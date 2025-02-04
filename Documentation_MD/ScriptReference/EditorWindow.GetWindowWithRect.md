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

#  [EditorWindow](EditorWindow.html).GetWindowWithRect

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

public static [EditorWindow](EditorWindow.html) GetWindowWithRect(Type
windowType, [Rect](Rect.html) rect, bool utility = false, string title =
null);

### Parameters

windowType | The type of the window. Must derive from EditorWindow.  
---|---  
rect | The position on the screen where a newly created window will show.  
utility | Set this to true, to create a floating utility window, false to create a normal window.  
title | If GetWindow creates a new window, it will get this title. If this value is null, use the class name as title.  
  
### Description

Returns the first EditorWindow of type `t` which is currently on the screen.

If there is none, creates and shows new window at the position `rect` and
returns the instance of it.  
  
![](../StaticFiles/ScriptRefImages/GetWindowRectEx.png)  
_Create an empty 100x150px window at the upper left corner of the screen._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    
    // Create a dockable empty window at the top left corner of the screen
    // with 100px width and 150px height.
    
    public class EditorWindowTestRect : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/[Display](Display.html) simple sized Window")]
        static void Initialize()
        {
            EditorWindowTestRect window = (EditorWindowTestRect)[EditorWindow.GetWindowWithRect](EditorWindow.GetWindowWithRect.html)(typeof(EditorWindowTestRect), new [Rect](Rect.html)(0, 0, 100, 150));
        }
    }
    

* * *

## Declaration

public static T GetWindowWithRect([Rect](Rect.html) rect);

## Declaration

public static T GetWindowWithRect([Rect](Rect.html) rect, bool utility);

## Declaration

public static T GetWindowWithRect([Rect](Rect.html) rect, bool utility, string
title);

## Declaration

public static T GetWindowWithRect([Rect](Rect.html) rect, bool utility, string
title, bool focus);

### Parameters

T | The type of the window. Must derive from EditorWindow.  
---|---  
rect | The position on the screen where a newly created window will show.  
utility | Set this to true, to create a floating utility window, false to create a normal window.  
title | If GetWindow creates a new window, it will get this title. If this value is null, use the class name as title.  
focus | Whether to give the window focus, if it already exists. (If GetWindow creates a new window, it will always get focus).  
  
### Returns

**T** An EditorWindow instance of type `T`.

### Description

Returns the first EditorWindow of type `t` which is currently on the screen.

If there is none, creates and shows new window at the position `rect` and
returns the instance of it.

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

