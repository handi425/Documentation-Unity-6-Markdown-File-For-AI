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

#  [Gizmos](Gizmos.html).DrawLineStrip

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

public static void DrawLineStrip(ReadOnlySpan<Vector3> points, bool looped);

### Parameters

points | The points that define the sequence of lines to draw. The function draws a line between each point and the one that follows it.  
---|---  
looped | Whether to draw an additional line between the last point and the first. When this is `true`, Unity draws an additional line between `points[points.Length - 1]` and `points[0]`. When this is `false`, the lines terminate at the last point.  
  
### Description

Draws a line between each point in the supplied span.

This function provides a more efficient way to draw multiple lines than
repeatedly calling the [Gizmos.DrawLine](Gizmos.DrawLine.html) function for
each one.  
  
Unity draws the first line from `points[0]` to `points[1]`, the next from
`points[1]` to `points[2]`, and so on.

    
    
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
                new [Vector3](Vector3.html)(100, 100, 0),
                new [Vector3](Vector3.html)(-100, 100, 0)
            };
        }  
      
        void OnDrawGizmosSelected()
        {
            // Draws four lines making a square
            [Gizmos.color](Gizmos-color.html) = [Color.blue](Color-blue.html);
            [Gizmos.DrawLineStrip](Gizmos.DrawLineStrip.html)(points, true);
        }
    }
    

Additional resources: [Gizmos.DrawLine](Gizmos.DrawLine.html),
[Gizmos.DrawLineList](Gizmos.DrawLineList.html).

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

