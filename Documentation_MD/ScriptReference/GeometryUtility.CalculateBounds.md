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

#  [GeometryUtility](GeometryUtility.html).CalculateBounds

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

public static [Bounds](Bounds.html) CalculateBounds(Vector3[] positions,
[Matrix4x4](Matrix4x4.html) transform);

### Parameters

positions | An array that stores the location of 3d positions.  
---|---  
transform | A matrix that changes the position, rotation and size of the bounds calculation.  
  
### Returns

**Bounds** Calculates the axis-aligned bounding box.

### Description

Calculates the bounding box from the given array of
[positions](GeometryUtility-positions.html) and the transformation matrix.

[GeometryUtility.CalculateBounds](GeometryUtility.CalculateBounds.html)
generates a [Bounds](Bounds.html) bounding box. The positions parameter stores
a 3d point array. Each point is inside the generated axis-aligned bounding
box. The transform parameter provides a transformation
[Matrix4x4](Matrix4x4.html) that uses a Vector3 position, Quaternion rotation,
and Vector3 scale.  
  
The example below shows how to use
[CalculateBounds](GeometryUtility.CalculateBounds.html). A
[LightProbeGroup](LightProbeGroup.html) passes [positions](GeometryUtility-
positions.html) into [CalculateBounds](GeometryUtility.CalculateBounds.html).
The example code creates a bounding box with eight Light Probes. By default,
the Light Probes are one unit from each corner of a unit cube.  
  
To run the example:

  1. Create a Project and add an empty [GameObject](GameObject.html) called `GameObject`.
  2. Add a 3D cube as a child of `GameObject` and call it `Cube`.
  3. Add a [LightProbeGroup](LightProbeGroup.html) component to `Cube`.
  4. Add the script below to `Cube`.
  5. Run the `Project` and switch back to the `Scene` view.

In the `Scene` view, you can see the [LightProbeGroup](LightProbeGroup.html).
When the game runs, the rotation changes in `Awake`. The eight yellow spheres
that indicate the [LightProbeGroup](LightProbeGroup.html) change position and
the Cube appears rotated. `Scene` mode shows the `Cube` rotated in the x, y
and z axes, and shows in the `Local tool handle`. Rotating the `Cube` changes
the positions of the eight [LightProbeGroup](LightProbeGroup.html) Light
Probes. The `Scene` mode rotates and zooms to show the Light Probes. Also, the
`Cube` rotates and the [LightProbeGroup](LightProbeGroup.html) updates. If you
rescale the `Cube`, the [LightProbeGroup](LightProbeGroup.html) changes size.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // [GeometryUtility.CalculateBounds](GeometryUtility.CalculateBounds.html) - example  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Awake()
        {
            transform.position = new [Vector3](Vector3.html)(0.0f, 0.0f, 0.0f);
            transform.Rotate(10.0f, 30.0f, -50.0f, [Space.Self](Space.Self.html));  
      
            [Debug.Log](Debug.Log.html)(transform.localToWorldMatrix);
        }  
      
        void OnDrawGizmosSelected()
        {
            [LightProbeGroup](LightProbeGroup.html) lightProbeGroup = GetComponent<[LightProbeGroup](LightProbeGroup.html)>();  
      
            [Vector3](Vector3.html) center = transform.position;
            [Bounds](Bounds.html) bounds = [GeometryUtility.CalculateBounds](GeometryUtility.CalculateBounds.html)(lightProbeGroup.probePositions, transform.localToWorldMatrix);
            [Gizmos.color](Gizmos-color.html) = new [Color](Color.html)(1, 1, 1, 0.25f);
            [Gizmos.DrawCube](Gizmos.DrawCube.html)(center, bounds.size);
            [Gizmos.DrawWireCube](Gizmos.DrawWireCube.html)(center, bounds.size);
        }
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

