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

#  [GUIUtility](GUIUtility.html).ScaleAroundPivot

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

public static void ScaleAroundPivot([Vector2](Vector2.html) scale,
[Vector2](Vector2.html) pivotPoint);

### Description

Helper function to scale the GUI around a point.

Modifies [GUI.matrix](GUI-matrix.html) to scale all GUI elements around a
`pivotPoint`.  
  
Additional resources: [GUI.matrix](GUI-matrix.html),
[RotateAroundPivot](GUIUtility.RotateAroundPivot.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    // [Scale](UIElements.Scale.html) a button by 1.5 times each time is pressed.  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Vector2](Vector2.html) scale = new [Vector2](Vector2.html)(1, 1);
        private [Vector2](Vector2.html) pivotPoint;  
      
        void OnGUI()
        {
            pivotPoint = new [Vector2](Vector2.html)([Screen.width](Screen-width.html) / 2, [Screen.height](Screen-height.html) / 2);
            [GUIUtility.ScaleAroundPivot](GUIUtility.ScaleAroundPivot.html)(scale, pivotPoint);  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)([Screen.width](Screen-width.html) / 2 - 25, [Screen.height](Screen-height.html) / 2 - 25, 50, 50), "Big!"))
            {
                scale += new [Vector2](Vector2.html)(0.5F, 0.5F);
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

