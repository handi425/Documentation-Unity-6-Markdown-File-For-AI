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

#  [Handles](Handles.html).DrawSolidRectangleWithOutline

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

public static void DrawSolidRectangleWithOutline(Vector3[] verts,
[Color](Color.html) faceColor, [Color](Color.html) outlineColor);

### Parameters

verts | The 4 vertices of the rectangle in world coordinates.  
---|---  
faceColor | The color of the rectangle's face.  
outlineColor | The outline color of the rectangle.  
  
### Description

Draw a solid outlined rectangle in 3D space.

![](../StaticFiles/ScriptRefImages/DrawSolidRectangle.png)  
_Solid rectangle with a black outline in the Scene View._

    
    
    // Create a semi transparent rectangle that lets you modify
    // the "range" that resides in "SolidRectangleExample.cs"  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    [[CustomEditor](CustomEditor.html)(typeof(SolidRectangleExample))]
    public class DrawSolidRectangle : [Editor](Editor.html)
    {
        void OnSceneGUI()
        {
            SolidRectangleExample t = target as SolidRectangleExample;
            [Vector3](Vector3.html) pos = t.transform.position;  
      
            [Vector3](Vector3.html)[] verts = new [Vector3](Vector3.html)[]
            {
                new [Vector3](Vector3.html)(pos.x - t.range, pos.y, pos.z - t.range),
                new [Vector3](Vector3.html)(pos.x - t.range, pos.y, pos.z + t.range),
                new [Vector3](Vector3.html)(pos.x + t.range, pos.y, pos.z + t.range),
                new [Vector3](Vector3.html)(pos.x + t.range, pos.y, pos.z - t.range)
            };  
      
            [Handles.DrawSolidRectangleWithOutline](Handles.DrawSolidRectangleWithOutline.html)(verts, new [Color](Color.html)(0.5f, 0.5f, 0.5f, 0.1f), new [Color](Color.html)(0, 0, 0, 1));  
      
            foreach ([Vector3](Vector3.html) posCube in verts)
            {
                t.range = [Handles.ScaleValueHandle](Handles.ScaleValueHandle.html)(t.range,
                    posCube,
                    [Quaternion.identity](Quaternion-identity.html),
                    1.0f,
                    [Handles.CubeHandleCap](Handles.CubeHandleCap.html),
                    1.0f);
            }
        }
    }
    

And the script attached to this Handle:

    
    
    using UnityEngine;  
      
    public class SolidRectangleExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public float range = 5.0f;
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

