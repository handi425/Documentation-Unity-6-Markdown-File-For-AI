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

#  [Handles](Handles.html).DrawLines

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

public static void DrawLines(Vector3[] lineSegments);

### Parameters

lineSegments | A list of pairs of points that represent the start and end of line segments.  
---|---  
  
### Description

Draw a list of line segments.

![](../StaticFiles/ScriptRefImages/DrawLines.png) "Draw multiple lines in
sceneview.".  
  
Below is an example of an Editor script that draws lines in SceneView to
GameObjects listed in a script.

    
    
    // Draw lines to the connected game objects that a script has.
    // if the target object doesn't have any game objects attached
    // then it draws a line from the object to 0,0,0.  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections.Generic;  
      
    [[CustomEditor](CustomEditor.html)(typeof(ConnectedObjects))]
    class ConnectLineHandle : [Editor](Editor.html)
    {
        void OnSceneGUI()
        {
            ConnectedObjects connectedObjects = target as ConnectedObjects;
            if (connectedObjects.objs == null ||
                connectedObjects.objs.Length == 0)
                return;
            // we store the start and end points of the line segments in this array
            [Vector3](Vector3.html)[] lineSegments = new [Vector3](Vector3.html)[connectedObjects.objs.Length * 2];  
      
            int lastObject = connectedObjects.objs.Length - 1;
            [Vector3](Vector3.html) prevPoint;
            if (connectedObjects.objs[lastObject])
            {
                prevPoint = connectedObjects.objs[lastObject].transform.position;
            }
            else
            {
                prevPoint = [Vector3.zero](Vector3-zero.html);
            }
            int pointIndex = 0;
            for (int currObjectIndex = 0; currObjectIndex < connectedObjects.objs.Length; currObjectIndex++)
            {
                // find the position of our connected object and store it
                [Vector3](Vector3.html) currPoint;
                if (connectedObjects.objs[currObjectIndex])
                {
                    currPoint = connectedObjects.objs[currObjectIndex].transform.position;
                }
                else
                {
                    currPoint = [Vector3.zero](Vector3-zero.html);
                }  
      
                // store the starting point of the line segment
                lineSegments[pointIndex] = prevPoint;
                pointIndex++;  
      
                // store the ending point of the line segment
                lineSegments[pointIndex] = currPoint;
                pointIndex++;  
      
                prevPoint = currPoint;
            }
            [Handles.DrawLines](Handles.DrawLines.html)(lineSegments);
        }
    }
    

Example script to attach to a GameObject that will act as a handle:

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ConnectedObjects : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html)[] objs = null;
    }
    

* * *

## Declaration

public static void DrawLines(Vector3[] points, int[] segmentIndices);

### Parameters

points | A list of points.  
---|---  
segmentIndices | A list of pairs of indices to the start and end points of the line segments.  
  
### Description

Draw a list of indexed line segments.

    
    
    // Draw lines to the connected game objects that a script has.
    // if the target object doesn't have any game objects attached
    // then it draws a line from the object to 0,0,0.  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections.Generic;  
      
    [[CustomEditor](CustomEditor.html)(typeof(ConnectedLinePointsObjects))]
    class ConnectLinePointsHandle : [Editor](Editor.html)
    {
        void OnSceneGUI()
        {
            ConnectedLinePointsObjects connectedObjects = target as ConnectedLinePointsObjects;
            if (connectedObjects.objs == null ||
                connectedObjects.objs.Length == 0)
                return;  
      
            // we store the points of the line segments in this array
            [Vector3](Vector3.html)[] points = new [Vector3](Vector3.html)[connectedObjects.objs.Length];  
      
            // for each line segment we need two indices into the points array:
            // the index to the start and the end point
            int[] segmentIndices = new int[connectedObjects.objs.Length * 2];  
      
            // create the points and line segments indices
            int prevIndex = connectedObjects.objs.Length - 1;
            int pointIndex = 0;
            int segmentIndex = 0;
            for (int currIndex = 0; currIndex < connectedObjects.objs.Length; currIndex++)
            {
                // find the position of our connected object and store it
                if (connectedObjects.objs[pointIndex])
                {
                    points[pointIndex] = connectedObjects.objs[currIndex].transform.position;
                }
                else
                {
                    points[pointIndex] = [Vector3.zero](Vector3-zero.html);
                }  
      
                // the index to the start of the line segment
                segmentIndices[segmentIndex] = prevIndex;
                segmentIndex++;  
      
                // the index to the end of the line segment
                segmentIndices[segmentIndex] = pointIndex;
                segmentIndex++;  
      
                pointIndex++;
                prevIndex = currIndex;
            }
            [Handles.DrawLines](Handles.DrawLines.html)(points, segmentIndices);
        }
    }
    

And the script attached to this Handle:

    
    
    using UnityEngine;  
      
    using System.Collections;
    public class ConnectedLinePointsObjects : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html)[] objs = null;
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

