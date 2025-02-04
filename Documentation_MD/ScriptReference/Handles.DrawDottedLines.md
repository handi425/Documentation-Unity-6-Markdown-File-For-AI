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

#  [Handles](Handles.html).DrawDottedLines

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

public static void DrawDottedLines(Vector3[] lineSegments, float
screenSpaceSize);

### Parameters

lineSegments | A list of pairs of points that represent the start and end of line segments.  
---|---  
screenSpaceSize | The size in pixels for the lengths of the line segments and the gaps between them.  
  
### Description

Draw a list of dotted line segments.

![](../StaticFiles/ScriptRefImages/DrawDottedLines.png) "Draw multiple dotted
lines in sceneview.".

    
    
    // Draw lines to the connected game objects that a script has.
    // if the target object doesn't have any game objects attached
    // then it draws a line from the object to 0,0,0.  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections.Generic;  
      
    [[CustomEditor](CustomEditor.html)(typeof(ConnectedLineObjects))]
    class ConnectDottedLineHandle : [Editor](Editor.html)
    {
        float dashSize = 4.0f;
        void OnSceneGUI()
        {
            ConnectedLineObjects connectedObjects = target as ConnectedLineObjects;
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
            [Handles.DrawDottedLines](Handles.DrawDottedLines.html)(lineSegments, dashSize);
        }
    }
    

And the script attached to this Handle:

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ConnectedLineObjects : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html)[] objs = null;
    }
    

* * *

## Declaration

public static void DrawDottedLines(Vector3[] points, int[] segmentIndices,
float screenSpaceSize);

### Parameters

points | A list of points.  
---|---  
segmentIndices | A list of pairs of indices to the start and end points of the line segments.  
screenSpaceSize | The size in pixels for the lengths of the line segments and the gaps between them.  
  
### Description

Draw a list of indexed dotted line segments.

    
    
    // Draw lines to the connected game objects that a script has.
    // If the target object doesn't have any game objects attached
    // then it draws a line from the object to (0, 0, 0).  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections.Generic;  
      
    [[CustomEditor](CustomEditor.html)(typeof(ConnectedLinesObjects))]
    class ConnectDottedLinesHandle : [Editor](Editor.html)
    {
        float dashSize = 4.0f;
        void OnSceneGUI()
        {
            ConnectedLinesObjects connectedObjects = target as ConnectedLinesObjects;
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
            [Handles.DrawDottedLines](Handles.DrawDottedLines.html)(points, segmentIndices, dashSize);
        }
    }
    

And the script attached to this Handle:

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ConnectedLinesObjects : [MonoBehaviour](MonoBehaviour.html)
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

