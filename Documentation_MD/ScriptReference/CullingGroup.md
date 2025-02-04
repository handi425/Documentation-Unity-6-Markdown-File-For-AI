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

# CullingGroup

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

### Description

Describes a set of bounding spheres that should have their visibility and
distances maintained.

### Properties

[enabled](CullingGroup-enabled.html)| Pauses culling group execution.  
---|---  
[onStateChanged](CullingGroup-onStateChanged.html)| Sets the callback that
will be called when a sphere's visibility and/or distance state has changed.  
[targetCamera](CullingGroup-targetCamera.html)| Locks the CullingGroup to a
specific camera.  
  
### Constructors

[CullingGroup](CullingGroup-ctor.html)| Create a CullingGroup.  
---|---  
  
### Public Methods

[Dispose](CullingGroup.Dispose.html)| Clean up all memory used by the
CullingGroup immediately.  
---|---  
[EraseSwapBack](CullingGroup.EraseSwapBack.html)| Erase a given bounding
sphere by moving the final sphere on top of it.  
[GetDistance](CullingGroup.GetDistance.html)| Get the current distance band
index of a given sphere.  
[IsVisible](CullingGroup.IsVisible.html)| Returns true if the bounding sphere
at index is currently visible from any of the contributing cameras.  
[QueryIndices](CullingGroup.QueryIndices.html)| Retrieve the indices of
spheres that have particular visibility and/or distance states.  
[SetBoundingDistances](CullingGroup.SetBoundingDistances.html)| Set bounding
distances for 'distance bands' the group should compute, as well as options
for how spheres falling into each distance band should be treated.  
[SetBoundingSphereCount](CullingGroup.SetBoundingSphereCount.html)| Sets the
number of bounding spheres in the bounding spheres array that are actually
being used.  
[SetBoundingSpheres](CullingGroup.SetBoundingSpheres.html)| Sets the array of
bounding sphere definitions that the CullingGroup should compute culling for.  
[SetDistanceReferencePoint](CullingGroup.SetDistanceReferencePoint.html)| Set
the reference point from which distance bands are measured.  
  
### Delegates

[StateChanged](CullingGroup.StateChanged.html)| This delegate is used for
recieving a callback when a sphere's distance or visibility state has changed.  
---|---  
  
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

