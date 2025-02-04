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

#  [HandleUtility](HandleUtility.html).DistanceToCone

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

public static float DistanceToCone([Vector3](Vector3.html) position,
[Quaternion](Quaternion.html) rotation, float size);

### Parameters

position | Position of the cone.  
---|---  
rotation | Rotation of the cone.  
size | Size of the cone.  
  
### Returns

**float** Distance from mouse to cone in pixels.

### Description

Returns the distance in pixels from the mouse pointer to a cone.

Calculates the screen space distance from the mouse pointer to a cone at given
world space `position` with the given `rotation` and `size`.  
  
Returns zero when mouse pointer is directly over the cone.  
  
Uses the current camera to determine the distance.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
    }  
      
    // Displays cone in scene view, and distance from mouse
    // to the cone.
    [[CustomEditor](CustomEditor.html)(typeof(ExampleScript))]
    public class ExampleEditor : [Editor](Editor.html)
    {
        public void OnSceneGUI()
        {
            var t = target as ExampleScript;
            var tr = t.transform;
            var position = tr.position;
            var rotation = tr.rotation;
            var size = 1.0f;
            // draw a cone in scene
            [Handles.color](Handles-color.html) = [Color.yellow](Color-yellow.html);
            [Handles.ConeHandleCap](Handles.ConeHandleCap.html)(0, position, rotation, size, Event.current.type);
            // calculate distance from mouse to cone, and display it
            var distance = [HandleUtility.DistanceToCone](HandleUtility.DistanceToCone.html)(position, rotation, size);
            [GUI.color](GUI-color.html) = [Color.black](Color-black.html);
            [Handles.Label](Handles.Label.html)(position, distance.ToString("F0"));
            // make scene view repaint on mouse move
            if (Event.current.type == [EventType.MouseMove](EventType.MouseMove.html))
                Event.current.Use();
        }
    }
    

![](../StaticFiles/ScriptRefImages/HandleUtilityDistanceToCone.png).  
  
Additional resources: [DistanceToCircle](HandleUtility.DistanceToCircle.html),
[DistanceToCube](HandleUtility.DistanceToCube.html),
[DistanceToLine](HandleUtility.DistanceToLine.html).

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

