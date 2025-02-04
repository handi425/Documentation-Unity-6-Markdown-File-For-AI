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

#  [Camera](Camera.html).CalculateFrustumCorners

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

[Switch to Manual](../Manual/class-Camera.html "Go to Camera Component in the
Manual")

## Declaration

public void CalculateFrustumCorners([Rect](Rect.html) viewport, float z,
[Camera.MonoOrStereoscopicEye](Camera.MonoOrStereoscopicEye.html) eye,
Vector3[] outCorners);

### Parameters

viewport | Normalized viewport coordinates to use for the frustum calculation.  
---|---  
z | Z-depth from the camera origin at which the corners will be calculated.  
eye | Camera eye projection matrix to use.  
outCorners | Output array for the frustum corner vectors. Cannot be null and length must be >= 4.  
  
### Description

Given viewport coordinates, calculates the view space vectors pointing to the
four frustum corners at the specified camera depth.

The order of the corners is lower left, upper left, upper right, lower right.  
  
`CalculateFrustumCorners` can be used to efficiently calculate the world space
position of a pixel in an image effect shader. See standard assets
implementation of global fog.

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            // this example shows the different camera frustums when using asymmetric projection matrices (like those used by OpenVR).  
      
            var camera = GetComponent<[Camera](Camera.html)>();
            [Vector3](Vector3.html)[] frustumCorners = new [Vector3](Vector3.html)[4];
            camera.CalculateFrustumCorners(new [Rect](Rect.html)(0, 0, 1, 1), camera.farClipPlane, [Camera.MonoOrStereoscopicEye.Mono](Camera.MonoOrStereoscopicEye.Mono.html), frustumCorners);  
      
            for (int i = 0; i < 4; i++)
            {
                var worldSpaceCorner = camera.transform.TransformVector(frustumCorners[i]);
                [Debug.DrawRay](Debug.DrawRay.html)(camera.transform.position, worldSpaceCorner, [Color.blue](Color-blue.html));
            }  
      
            camera.CalculateFrustumCorners(new [Rect](Rect.html)(0, 0, 1, 1), camera.farClipPlane, [Camera.MonoOrStereoscopicEye.Left](Camera.MonoOrStereoscopicEye.Left.html), frustumCorners);  
      
            for (int i = 0; i < 4; i++)
            {
                var worldSpaceCorner = camera.transform.TransformVector(frustumCorners[i]);
                [Debug.DrawRay](Debug.DrawRay.html)(camera.transform.position, worldSpaceCorner, [Color.green](Color-green.html));
            }  
      
            camera.CalculateFrustumCorners(new [Rect](Rect.html)(0, 0, 1, 1), camera.farClipPlane, [Camera.MonoOrStereoscopicEye.Right](Camera.MonoOrStereoscopicEye.Right.html), frustumCorners);  
      
            for (int i = 0; i < 4; i++)
            {
                var worldSpaceCorner = camera.transform.TransformVector(frustumCorners[i]);
                [Debug.DrawRay](Debug.DrawRay.html)(camera.transform.position, worldSpaceCorner, [Color.red](Color-red.html));
            }
        }
    }
    

Which can be seen in the following image:
![](../StaticFiles/ScriptRefImages/FrustumCorners.PNG).

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

