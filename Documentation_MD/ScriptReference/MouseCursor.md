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

# MouseCursor

enumeration

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

Custom mouse cursor shapes used with EditorGUIUtility.AddCursorRect.

    
    
    //Create a folder and name it “[Editor](Editor.html)” if this doesn’t already exist
    //Put this script in the folder  
      
    //This script creates a new menu (“Examples”) and a menu item (“Mouse [Cursor](Cursor.html)”). Click on this option. This displays a small window that has a color box in it.
    //Hover over the colored box to cause an Orbit mouse cursor to appear.  
      
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class MouseCursorExample : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/MouseCursorRect Example")]
        static void AddCursorRectExample()
        {
            MouseCursorExample window =
                [EditorWindow.GetWindowWithRect](EditorWindow.GetWindowWithRect.html)<MouseCursorExample>(new [Rect](Rect.html)(0, 0, 180, 80));
            window.Show();
        }  
      
        void OnGUI()
        {
            [EditorGUI.DrawRect](EditorGUI.DrawRect.html)(new [Rect](Rect.html)(10, 10, 160, 60), new [Color](Color.html)(0.5f, 0.5f, 0.85f));
            [EditorGUI.DrawRect](EditorGUI.DrawRect.html)(new [Rect](Rect.html)(20, 20, 140, 40), new [Color](Color.html)(0.9f, 0.9f, 0.9f));
            [EditorGUIUtility.AddCursorRect](EditorGUIUtility.AddCursorRect.html)(new [Rect](Rect.html)(20, 20, 140, 40), [MouseCursor.Orbit](MouseCursor.Orbit.html));
        }
    }
    

### Properties

[Arrow](MouseCursor.Arrow.html)| Normal pointer arrow.  
---|---  
[Text](MouseCursor.Text.html)| Text cursor.  
[ResizeVertical](MouseCursor.ResizeVertical.html)| Vertical resize arrows.  
[ResizeHorizontal](MouseCursor.ResizeHorizontal.html)| Horizontal resize
arrows.  
[Link](MouseCursor.Link.html)| Arrow with a Link badge (for assigning
pointers).  
[SlideArrow](MouseCursor.SlideArrow.html)| Arrow with small arrows for
indicating sliding at number fields.  
[ResizeUpRight](MouseCursor.ResizeUpRight.html)| Resize up-right for window
edges.  
[ResizeUpLeft](MouseCursor.ResizeUpLeft.html)| Resize up-Left for window
edges.  
[MoveArrow](MouseCursor.MoveArrow.html)| Arrow with the move symbol next to it
for the sceneview.  
[RotateArrow](MouseCursor.RotateArrow.html)| Arrow with the rotate symbol next
to it for the sceneview.  
[ScaleArrow](MouseCursor.ScaleArrow.html)| Arrow with the scale symbol next to
it for the sceneview.  
[ArrowPlus](MouseCursor.ArrowPlus.html)| Arrow with the plus symbol next to
it.  
[ArrowMinus](MouseCursor.ArrowMinus.html)| Arrow with the minus symbol next to
it.  
[Pan](MouseCursor.Pan.html)| Cursor with a dragging hand for pan.  
[Orbit](MouseCursor.Orbit.html)| Cursor with an eye for orbit.  
[Zoom](MouseCursor.Zoom.html)| Cursor with a magnifying glass for zoom.  
[FPS](MouseCursor.FPS.html)| Cursor with an eye and stylized arrow keys for
FPS navigation.  
[CustomCursor](MouseCursor.CustomCursor.html)| The current user defined
cursor.  
[SplitResizeUpDown](MouseCursor.SplitResizeUpDown.html)| Up-Down resize arrows
for window splitters.  
[SplitResizeLeftRight](MouseCursor.SplitResizeLeftRight.html)| Left-Right
resize arrows for window splitters.  
  
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

