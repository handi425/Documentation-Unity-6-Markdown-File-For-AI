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

#  [Handles](Handles.html).DrawLine

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

public static void DrawLine([Vector3](Vector3.html) p1,
[Vector3](Vector3.html) p2, float thickness = 0.0f);

### Parameters

p1 | The position of the first line's end point in world space.  
---|---  
p2 | The position of the second line's end point in world space.  
thickness | Line thickness in UI points (zero thickness draws single-pixel line).  
  
### Description

Draws a line from `p1` to `p2`.

The [Handles.color](Handles-color.html) and [Handles.matrix](Handles-
matrix.html) properties colorize and additionally transform the line position.
Unity ignores `DrawLine` (that is, nothing happens) when the current GUI event
type is not [Repaint](EventType.Repaint.html).  
  
![](../StaticFiles/ScriptRefImages/DrawLine.png)  
_Draw Line in the Scene View._  
  
Below is an example of an Editor script that draws lines in SceneView to
GameObjects listed in a script.

    
    
    // Draw lines to the connected game objects that a script has.
    // If the target object doesnt have any game objects attached
    // then it draws a line from the object to (0, 0, 0).  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [[CustomEditor](CustomEditor.html)(typeof(ConnectedObjectsExampleScript))]
    class ConnectLineHandleExampleScript : [Editor](Editor.html)
    {
        void OnSceneGUI()
        {
            ConnectedObjectsExampleScript connectedObjects = target as ConnectedObjectsExampleScript;
            if (connectedObjects.objs == null)
                return;  
      
            [Vector3](Vector3.html) center = connectedObjects.transform.position;
            for (int i = 0; i < connectedObjects.objs.Length; i++)
            {
                [GameObject](GameObject.html) connectedObject = connectedObjects.objs[i];
                if (connectedObject)
                {
                    [Handles.DrawLine](Handles.DrawLine.html)(center, connectedObject.transform.position);
                }
                else
                {
                    [Handles.DrawLine](Handles.DrawLine.html)(center, [Vector3.zero](Vector3-zero.html));
                }
            }
        }
    }
    

Example script to attach to a GameObject that will act as a handle:

    
    
    using UnityEngine;  
      
    public class ConnectedObjectsExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html)[] objs = null;
    }
    

Line `thickness` can be optionally set. Zero thickness draws a one-pixel line.
Larger thickness values express line thickness in UI points. For example, a
thickness of 1.0 could be two pixels wide on screen if the display zoom is
200% (see [EditorGUIUtility.pixelsPerPoint](EditorGUIUtility-
pixelsPerPoint.html)).  
  
![](../StaticFiles/ScriptRefImages/HandlesDrawLineThickness.png)  
_Lines of varying thickness._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
    }  
      
    // Displays lines of various thickness in the scene view
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
                var linePos = position + [Vector3.right](Vector3-right.html) * (i * 0.5f);
                [Handles.DrawLine](Handles.DrawLine.html)(linePos, linePos + [Vector3.up](Vector3-up.html), i);
            }
        }
    }
    

Additional resources: [Handles.lineThickness](Handles-lineThickness.html),
[Handles.DrawLines](Handles.DrawLines.html),
[Handles.DrawPolyLine](Handles.DrawPolyLine.html),
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

