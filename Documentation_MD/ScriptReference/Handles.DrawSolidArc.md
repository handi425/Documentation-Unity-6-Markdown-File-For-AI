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

#  [Handles](Handles.html).DrawSolidArc

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

public static void DrawSolidArc([Vector3](Vector3.html) center,
[Vector3](Vector3.html) normal, [Vector3](Vector3.html) from, float angle,
float radius);

### Parameters

center | The center of the circle.  
---|---  
normal | The normal of the circle.  
from | The direction of the point on the circumference, relative to the center, where the sector begins.  
angle | The angle of the sector, in degrees.  
radius | The radius of the circle  
  
**Note:** Use HandleUtility.GetHandleSize where you might want to have
constant screen-sized handles.  
  
### Description

Draw a circular sector (pie piece) in 3D space.

![](../StaticFiles/ScriptRefImages/DrawSolidArc.png)  
_Solid Arc in the Scene View._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    static class ArcExample
    {
        static [Vector3](Vector3.html) m_Angle = new [Vector3](Vector3.html)(1.5f, .66f, 0f);  
      
        // Create an arc at 0, 0, 0 in the [Scene](SceneManagement.Scene.html) view and a slider that changes thes angle of the arc.
        [InitializeOnLoadMethod]
        static void Init() => [SceneView.duringSceneGui](SceneView-duringSceneGui.html) += view =>
        {
            [Handles.DrawLine](Handles.DrawLine.html)(new [Vector3](Vector3.html)(1.5f, 0f, 0f), new [Vector3](Vector3.html)(1.5f, 1f, 0f));
            var handleSize = [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html)(m_Angle) * .1f;
            m_Angle = [Handles.Slider](Handles.Slider.html)(m_Angle, [Vector3.up](Vector3-up.html), handleSize, [Handles.DotHandleCap](Handles.DotHandleCap.html), EditorSnapSettings.move.x);
            m_Angle.y = [Mathf.Clamp](Mathf.Clamp.html)(m_Angle.y, 0f, 1f);
            [Handles.Label](Handles.Label.html)(m_Angle + [Vector3.right](Vector3-right.html) * handleSize * 2f, $"[Angle](UIElements.Angle.html) {m_Angle.y * 360f}");  
      
            [Handles.DrawSolidArc](Handles.DrawSolidArc.html)([Vector3.zero](Vector3-zero.html), [Vector3.forward](Vector3-forward.html), [Vector3.up](Vector3-up.html), m_Angle.y * -360f, 1f);
        };
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

