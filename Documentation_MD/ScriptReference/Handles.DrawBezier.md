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

#  [Handles](Handles.html).DrawBezier

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

public static void DrawBezier([Vector3](Vector3.html) startPosition,
[Vector3](Vector3.html) endPosition, [Vector3](Vector3.html) startTangent,
[Vector3](Vector3.html) endTangent, [Color](Color.html) color,
[Texture2D](Texture2D.html) texture, float width);

### Parameters

startPosition | The start point of the bezier line.  
---|---  
endPosition | The end point of the bezier line.  
startTangent | The start tangent of the bezier line.  
endTangent | The end tangent of the bezier line.  
color | The color to use for the bezier line.  
texture | The texture to use for drawing the bezier line.  
width | The width of the bezier line.  
  
### Description

Draw textured bezier line through start and end points with the given
tangents.

To get an anti-aliased effect use a texture that is 1x2 pixels with one
transparent white pixel and one opaque white pixel. The bezier curve will be
swept using this texture.  
  
**Note:** Use [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html)
where you might want to have constant screen-sized handles.  
  
![](../StaticFiles/ScriptRefImages/DrawBezier.png)  
_Bezier Line in the Scene View._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [[CustomEditor](CustomEditor.html)(typeof(BezierExample))]
    public class DrawBezierExample : [Editor](Editor.html)
    {
        void OnSceneGUI()
        {
            BezierExample be = target as BezierExample;  
      
            be.startPoint = [Handles.PositionHandle](Handles.PositionHandle.html)(be.startPoint, [Quaternion.identity](Quaternion-identity.html));
            be.endPoint = [Handles.PositionHandle](Handles.PositionHandle.html)(be.endPoint, [Quaternion.identity](Quaternion-identity.html));
            be.startTangent = [Handles.PositionHandle](Handles.PositionHandle.html)(be.startTangent, [Quaternion.identity](Quaternion-identity.html));
            be.endTangent = [Handles.PositionHandle](Handles.PositionHandle.html)(be.endTangent, [Quaternion.identity](Quaternion-identity.html));  
      
            // Visualize the tangent lines
            [Handles.DrawDottedLine](Handles.DrawDottedLine.html)(be.startPoint, be.startTangent, 5);
            [Handles.DrawDottedLine](Handles.DrawDottedLine.html)(be.endPoint, be.endTangent, 5);  
      
            [Handles.DrawBezier](Handles.DrawBezier.html)(be.startPoint, be.endPoint, be.startTangent, be.endTangent, [Color.red](Color-red.html), null, 5f);
        }
    }

And the script attached to this Handle:

    
    
    using UnityEngine;  
      
    public class BezierExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector3](Vector3.html) startPoint = new [Vector3](Vector3.html)(-5f, 2f, 0f);
        public [Vector3](Vector3.html) endPoint = new [Vector3](Vector3.html)(5f, -2f, 0f);
        public [Vector3](Vector3.html) startTangent = new [Vector3](Vector3.html)(0f, 2f, 0f);
        public [Vector3](Vector3.html) endTangent = new [Vector3](Vector3.html)(0f, -2f, 0f);
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

