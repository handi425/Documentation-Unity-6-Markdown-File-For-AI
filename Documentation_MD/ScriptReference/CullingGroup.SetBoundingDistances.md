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

#  [CullingGroup](CullingGroup.html).SetBoundingDistances

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

public void SetBoundingDistances(float[] distances);

### Parameters

distances | An array of bounding distances. The distances should be sorted in increasing order.  
---|---  
  
### Description

Set bounding distances for 'distance bands' the group should compute, as well
as options for how spheres falling into each distance band should be treated.

Each distance value indicates a band that is 'up to' that distance; the array
[10, 20, 30] describes distance bands "from 0 to 10m", "from 10m to 20m" and
"from 20m to 30m."  
  
The distance from the reference point (set by
[CullingGroup.SetDistanceReferencePoint](CullingGroup.SetDistanceReferencePoint.html))
to the nearest edge of the sphere is used to calculate which distance band a
sphere is in. Therefore a sphere that covers multiple distance bands will be
considered to be in the nearest one to the reference point.  
  
In addition to forcing objects to be visible or invisible, you can use
distance bands to drive level-of-detail changes in your objects. For example,
you might define bands "from 0 to 40m" and "from 40m to 80m", and while you
might have both bands apply occlusion and frustum culling as normal, you could
have objects in the second band be animated with a less complex rig, or run a
less complex AI behaviour.  
  
By default, any spheres beyond the final bounding distance are implicitly
forced to be invisible. To avoid this, you can specify a final bounding
distance of float.PositiveInfinity.

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

