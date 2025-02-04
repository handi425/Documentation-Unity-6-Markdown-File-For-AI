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

#  [GUILayout](GUILayout.html).MinHeight

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

public static [GUILayoutOption](GUILayoutOption.html) MinHeight(float
minHeight);

### Description

Option passed to a control to specify a minimum height.

![](../StaticFiles/ScriptRefImages/GUILayoutMinHeight.png)  
_Minimum height for a window._

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        // Draws a window you can resize between 80px and 200px height
        // Just click the box inside the window and move your mouse
        [Rect](Rect.html) windowRect = new [Rect](Rect.html)(10, 10, 100, 100);
        bool scaling = false;  
      
        void OnGUI()
        {
            windowRect = [GUILayout.Window](GUILayout.Window.html)(0, windowRect, ScalingWindow, "resizeable",
                [GUILayout.MinHeight](GUILayout.MinHeight.html)(80), [GUILayout.MaxHeight](GUILayout.MaxHeight.html)(200));
        }  
      
        void ScalingWindow(int windowID)
        {
            [GUILayout.Box](GUILayout.Box.html)("", [GUILayout.Width](GUILayout.Width.html)(20), [GUILayout.Height](GUILayout.Height.html)(20));
            if (Event.current.type == [EventType.MouseUp](EventType.MouseUp.html))
            {
                scaling = false;
            }
            else if (Event.current.type == [EventType.MouseDown](EventType.MouseDown.html) &&
                     [GUILayoutUtility.GetLastRect](GUILayoutUtility.GetLastRect.html)().Contains(Event.current.mousePosition))
            {
                scaling = true;
            }  
      
            if (scaling)
            {
                windowRect = new [Rect](Rect.html)(windowRect.x, windowRect.y,
                    windowRect.width + Event.current.delta.x, windowRect.height + Event.current.delta.y);
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

