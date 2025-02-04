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

#  [GUIUtility](GUIUtility.html).GUIToScreenPoint

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

public static [Vector2](Vector2.html) GUIToScreenPoint([Vector2](Vector2.html)
guiPoint);

### Description

Convert a point from GUI position to screen space.

**Note:** In Unity the screen space **y** coordinate varies from zero at the
top edge of the window to a maximum at the bottom edge of the window. This is
different from what you might expect.  
  
Additional resources:
[GUIUtility.ScreenToGUIPoint](GUIUtility.ScreenToGUIPoint.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Converts a GUICoordinate (affected by a group) to a [Screen](Screen.html) coordinate.  
      
        void OnGUI()
        {
            [Vector2](Vector2.html) gPos = new [Vector2](Vector2.html)(10, 10);
            [GUI.BeginGroup](GUI.BeginGroup.html)(new [Rect](Rect.html)(10, 10, 100, 100));
            [Vector2](Vector2.html) convertedGUIPos = [GUIUtility.GUIToScreenPoint](GUIUtility.GUIToScreenPoint.html)(gPos);
            [GUI.EndGroup](GUI.EndGroup.html)();
            [Debug.Log](Debug.Log.html)("[GUI](GUI.html): " + gPos + " [Screen](Screen.html): " + convertedGUIPos);
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

