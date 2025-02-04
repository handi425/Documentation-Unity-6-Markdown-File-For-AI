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

#  [Handles](Handles.html).DrawWireArc

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

public static void DrawWireArc([Vector3](Vector3.html) center,
[Vector3](Vector3.html) normal, [Vector3](Vector3.html) from, float angle,
float radius, float thickness = 0.0f);

### Parameters

center | The center of the circle in world space.  
---|---  
normal | The normal of the circle in world space.  
from | The direction of the point on the circle circumference, relative to the center, where the arc begins.  
angle | The angle of the arc, in degrees.  
radius | The radius of the circle in world space units.  
thickness | Line thickness in UI points (zero thickness draws single-pixel line).  
  
### Description

Draws a circular arc in 3D space.

The [Handles.color](Handles-color.html) and [Handles.matrix](Handles-
matrix.html) properties colorize and additionally transform the arc position.
Unity ignores `DrawWireArc` (that is, nothing happens) when the current GUI
event type is not [Repaint](EventType.Repaint.html).  
  
![](../StaticFiles/ScriptRefImages/DrawWireArc.png)  
_Wire Arc in the Scene View._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;  
      
    //this class should exist somewhere in your project
    public class WireArcExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public float shieldArea;
    }  
      
    // Create a 180 degrees wire arc with a ScaleValueHandle attached to the disc
    // that lets you modify the "shieldArea" value in the WireArcExample
    [[CustomEditor](CustomEditor.html)(typeof(WireArcExample))]
    public class DrawWireArc : [Editor](Editor.html)
    {
        void OnSceneGUI()
        {
            [Handles.color](Handles-color.html) = [Color.red](Color-red.html);
            WireArcExample myObj = (WireArcExample)target;
            [Handles.DrawWireArc](Handles.DrawWireArc.html)(myObj.transform.position, myObj.transform.up, -myObj.transform.right, 180, myObj.shieldArea);
            myObj.shieldArea = (float)[Handles.ScaleValueHandle](Handles.ScaleValueHandle.html)(myObj.shieldArea, myObj.transform.position + myObj.transform.forward * myObj.shieldArea, myObj.transform.rotation, 1, [Handles.ConeHandleCap](Handles.ConeHandleCap.html), 1);
        }
    }
    

You can use [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html) to
calculate a suitable size for a manipulator handle.  
  
Arc line `thickness` can be optionally set. Zero thickness draws a one-pixel
line. Larger thickness values express line thickness in UI points. For
example, a thickness of 1.0 could be two pixels wide on screen if the display
zoom is 200% (see [EditorGUIUtility.pixelsPerPoint](EditorGUIUtility-
pixelsPerPoint.html)).  
  
![](../StaticFiles/ScriptRefImages/HandlesDrawWireArcThickness.png)  
_Arcs of varying thickness._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
    }  
      
    // [Display](Display.html) arcs of various angles and thickness in the scene view
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
                var center = position;
                var start = [Vector3.left](Vector3-left.html);
                var normal = [Vector3.forward](Vector3-forward.html);
                var radius = 3 - i * 0.3f;
                var angle = 40 + 30 * i;
                [Handles.DrawWireArc](Handles.DrawWireArc.html)(center, normal, start, angle, radius, i);
            }
        }
    }
    

Additional resources: [Handles.lineThickness](Handles-lineThickness.html),
[Handles.DrawLine](Handles.DrawLine.html),
[Handles.DrawSolidArc](Handles.DrawSolidArc.html),
[Handles.DrawWireDisc](Handles.DrawWireDisc.html).

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

