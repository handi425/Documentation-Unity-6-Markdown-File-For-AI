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

#  [Handles](Handles.html).DrawWireDisc

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

public static void DrawWireDisc([Vector3](Vector3.html) center,
[Vector3](Vector3.html) normal, float radius, float thickness = 0.0f);

### Parameters

center | The center of the disc in world space.  
---|---  
normal | The normal of the disc in world space.  
radius | The radius of the disc in world space units.  
thickness | Line thickness in UI points (zero thickness draws single-pixel line).  
  
### Description

Draws the outline of a flat disc in 3D space.

The [Handles.color](Handles-color.html) and [Handles.matrix](Handles-
matrix.html) properties colorize and additionally transform the disc position.
Unity ignores `DrawWireDisc` (that is, nothing happens) when the current GUI
event type is not [Repaint](EventType.Repaint.html).  
  
![](../StaticFiles/ScriptRefImages/DrawWireDisc.png)  
_Wire Disc in the Scene View._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // draw a red circle around the scene cube
    [[CustomEditor](CustomEditor.html)(typeof(CubeExample))]
    public class CubeEditor : [Editor](Editor.html)
    {
        void OnSceneGUI()
        {
            CubeExample cubeExample = (CubeExample)target;  
      
            [Handles.color](Handles-color.html) = [Color.red](Color-red.html);
            [Handles.DrawWireDisc](Handles.DrawWireDisc.html)(cubeExample.transform.position, new [Vector3](Vector3.html)(0, 1, 0), cubeExample.circleSize);
        }
    }
    

The cube:

    
    
    using UnityEngine;  
      
    public class CubeExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public float circleSize = 3.0f;
    }
    

You can use [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html) to
calculate a suitable size for a manipulator handle.  
  
Disc line `thickness` can be optionally set. Zero thickness draws a one-pixel
line. Larger thickness values express line thickness in UI points. For
example, a thickness of 1.0 could be two pixels wide on screen if the display
zoom is 200% (see [EditorGUIUtility.pixelsPerPoint](EditorGUIUtility-
pixelsPerPoint.html)).  
  
![](../StaticFiles/ScriptRefImages/HandlesDrawWireDiscThickness.png)  
_Discs of varying thickness._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
    }  
      
    // Displays circles of various thickness in the scene view
    [[CustomEditor](CustomEditor.html)(typeof(ExampleScript))]
    public class ExampleEditor : [Editor](Editor.html)
    {
        public void OnSceneGUI()
        {
            var t = target as ExampleScript;
            var tr = t.transform;
            var position = tr.position;
            [Handles.color](Handles-color.html) = [Color.yellow](Color-yellow.html);
            for (int i = 0; i < 10; ++i)
            {
                [Handles.DrawWireDisc](Handles.DrawWireDisc.html)(position + [Vector3.right](Vector3-right.html) * i, [Vector3.forward](Vector3-forward.html), 2, i);
            }
        }
    }
    

Additional resources: [Handles.lineThickness](Handles-lineThickness.html),
[Handles.DrawLine](Handles.DrawLine.html),
[Handles.DrawSolidDisc](Handles.DrawSolidDisc.html),
[Handles.DrawWireArc](Handles.DrawWireArc.html).

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

