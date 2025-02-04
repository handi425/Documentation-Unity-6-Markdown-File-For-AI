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

#  [Gizmos](Gizmos.html).DrawLineList

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

public static void DrawLineList(ReadOnlySpan<Vector3> points);

### Parameters

points | Pairs of points to use as the beginning and end of each line to draw. Unity throws an exception if `points` contains an odd number of elements.  
---|---  
  
### Description

Draws multiple lines between pairs of points.

This function provides a more efficient way to draw multiple lines than
repeatedly calling the [Gizmos.DrawLine](Gizmos.DrawLine.html) function for
each one.  
  
Each pair of points from the `points` span represents the start and end of
each line, so Unity draws the first line from `points[0]` to `points[1]`, the
next from `points[2]` to `points[3]`, and so on.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        [Vector3](Vector3.html)[] points;  
      
        void Start()
        {
            points = new [Vector3](Vector3.html)[4]
            {
                new [Vector3](Vector3.html)(-100, 0, 0),
                new [Vector3](Vector3.html)(100, 0, 0),
                new [Vector3](Vector3.html)(-100, 100, 0),
                new [Vector3](Vector3.html)(100, 100, 0)
            };
        }  
      
        void OnDrawGizmosSelected()
        {
            // Draws two parallel blue lines
            [Gizmos.color](Gizmos-color.html) = [Color.blue](Color-blue.html);
            [Gizmos.DrawLineList](Gizmos.DrawLineList.html)(points);
        }
    }
    

Additional resources: [Gizmos.DrawLine](Gizmos.DrawLine.html),
[Gizmos.DrawLineStrip](Gizmos.DrawLineStrip.html).

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

