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

#  [GeometryUtility](GeometryUtility.html).CalculateFrustumPlanes

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

public static Plane[] CalculateFrustumPlanes([Camera](Camera.html) camera);

### Parameters

camera | The camera with the view frustum that you want to calculate planes from.  
---|---  
  
### Returns

**Plane[]** The planes that form the camera's view frustum.

### Description

Calculates frustum planes.

This function takes the given camera's view frustum and returns six planes
that form it.  
  
Ordering: [0] = Left, [1] = Right, [2] = Down, [3] = Up, [4] = Near, [5] = Far  
  
Additional resources: [Plane](Plane.html),
[GeometryUtility.TestPlanesAABB](GeometryUtility.TestPlanesAABB.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Calculate the planes from the main camera's view frustum
            [Plane](Plane.html)[] planes = [GeometryUtility.CalculateFrustumPlanes](GeometryUtility.CalculateFrustumPlanes.html)([Camera.main](Camera-main.html));  
      
            // Create a "[Plane](Plane.html)" [GameObject](GameObject.html) aligned to each of the calculated planes
            for (int i = 0; i < 6; ++i)
            {
                [GameObject](GameObject.html) p = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Plane](PrimitiveType.Plane.html));
                p.name = "[Plane](Plane.html) " + i.ToString();
                p.transform.position = -planes[i].normal * planes[i].distance;
                p.transform.rotation = [Quaternion.FromToRotation](Quaternion.FromToRotation.html)([Vector3.up](Vector3-up.html), planes[i].normal);
            }
        }
    }
    

* * *

## Declaration

public static void CalculateFrustumPlanes([Camera](Camera.html) camera,
Plane[] planes);

### Parameters

camera | The camera with the view frustum that you want to calculate planes from.  
---|---  
planes | An array of 6 Planes that will be overwritten with the calculated plane values.  
  
### Description

Calculates frustum planes.

This function takes the given camera's view frustum and returns six planes
that form it. This is similar to the previous overload, except that instead of
allocating a new array for the calculated planes, the function will use an
array that you have provided. This array must always be exactly of length 6.  
  
Ordering: [0] = Left, [1] = Right, [2] = Down, [3] = Up, [4] = Near, [5] = Far  
  
Additional resources: [Plane](Plane.html),
[GeometryUtility.TestPlanesAABB](GeometryUtility.TestPlanesAABB.html).

* * *

## Declaration

public static Plane[] CalculateFrustumPlanes([Matrix4x4](Matrix4x4.html)
worldToProjectionMatrix);

### Parameters

worldToProjectionMatrix | A matrix that transforms from world space to projection space, from which the planes will be calculated.  
---|---  
  
### Returns

**Plane[]** The planes that enclose the projection space described by the
matrix.

### Description

Calculates frustum planes.

This function returns six planes of a frustum defined by the given view &
projection matrix.  
  
Additional resources: [Plane](Plane.html),
[GeometryUtility.TestPlanesAABB](GeometryUtility.TestPlanesAABB.html).

* * *

## Declaration

public static void CalculateFrustumPlanes([Matrix4x4](Matrix4x4.html)
worldToProjectionMatrix, Plane[] planes);

### Parameters

worldToProjectionMatrix | A matrix that transforms from world space to projection space, from which the planes will be calculated.  
---|---  
planes | An array of 6 Planes that will be overwritten with the calculated plane values.  
  
### Description

Calculates frustum planes.

This function returns six planes of a frustum defined by the given view &
projection matrix. This is similar to the previous overload, except that
instead of allocating a new array for the calculated planes, the function will
use an array that you have provided. This array must always be exactly of
length 6.  
  
Additional resources: [Plane](Plane.html),
[GeometryUtility.TestPlanesAABB](GeometryUtility.TestPlanesAABB.html).

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

