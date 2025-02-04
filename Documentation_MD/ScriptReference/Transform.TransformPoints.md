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

#  [Transform](Transform.html).TransformPoints

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

[Switch to Manual](../Manual/class-Transform.html "Go to Transform Component
in the Manual")

## Declaration

public void TransformPoints(Span<Vector3> positions);

### Parameters

positions | The positions of the points to be transformed, each is replaced by the transformed version.  
---|---  
  
### Description

Transforms multiple points from local space to world space overwriting each
original point with the transformed version.

Note that the positions of the returned points are affected by scale. Use
[Transform.TransformDirections](Transform.TransformDirections.html) if you are
dealing with direction vectors.  
  
You can perform the opposite conversion, from world to local space using
[Transform.InverseTransformPoints](Transform.InverseTransformPoints.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) someObject;  
      
        const int kNumPoints = 100;  
      
        void Start()
        {
            // Instantiate 100 objects to the right of the current object
            [Vector3](Vector3.html)[] points = new [Vector3](Vector3.html)[kNumPoints];
            for (int pointNum = 0; pointNum < kNumPoints; pointNum++)
            {
                points[pointNum] = [Vector3.right](Vector3-right.html) * pointNum;
            }
            transform.TransformPoints(points);
            for (int pointNum = 0; pointNum < kNumPoints; pointNum++)
            {
                Instantiate(someObject, points[pointNum], someObject.transform.rotation);
            }
        }
    }
    

Additional
resources:[Transform.TransformPoint](Transform.TransformPoint.html),
[Transform.InverseTransformPoints](Transform.InverseTransformPoints.html),
[Transform.TransformDirections](Transform.TransformDirections.html),
[Transform.TransformVectors](Transform.TransformVectors.html).

* * *

## Declaration

public void TransformPoints(ReadOnlySpan<Vector3> positions, Span<Vector3>
transformedPositions);

### Parameters

positions | The positions of the points to be transformed, these vectors are not modified by the function unless the `transformedPositions` span overlaps.  
---|---  
transformedPositions | Receives the transformed positions of each point, must be the same length as `positions` otherwise an exception will be thrown. If this span overlaps `positions` other than representing the exact same elements the behaviour is undefined.  
  
### Description

Transforms multiple points from local space to world space writing the
transformed points to a possibly different location.

Note that the positions of the returned points are affected by scale. Use
[Transform.TransformDirections](Transform.TransformDirections.html) if you are
dealing with directions.  
  
You can perform the opposite conversion, from world to local space using
[Transform.InverseTransformPoints](Transform.InverseTransformPoints.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) someObject;  
      
        const int kNumPoints = 100;  
      
        void Start()
        {
            // Instantiate 100 objects to the right of the current object
            [Vector3](Vector3.html)[] points = new [Vector3](Vector3.html)[kNumPoints];
            for (int pointNum = 0; pointNum < kNumPoints; pointNum++)
            {
                points[pointNum] = [Vector3.right](Vector3-right.html) * pointNum;
            }
            [Vector3](Vector3.html)[] transformedPoints = new [Vector3](Vector3.html)[kNumPoints];
            transform.TransformPoints(points, transformedPoints);
            for (int pointNum = 0; pointNum < kNumPoints; pointNum++)
            {
                Instantiate(someObject, transformedPoints[pointNum], someObject.transform.rotation);
            }
        }
    }
    

Additional
resources:[Transform.TransformPoint](Transform.TransformPoint.html),
[Transform.InverseTransformPoints](Transform.InverseTransformPoints.html),
[Transform.TransformDirections](Transform.TransformDirections.html),
[Transform.TransformVectors](Transform.TransformVectors.html).

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

