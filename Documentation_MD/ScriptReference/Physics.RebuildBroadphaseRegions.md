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

**Method group is Obsolete**  

#  [Physics](Physics.html).RebuildBroadphaseRegions

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

**Obsolete** Physics.RebuildBroadphaseRegions has been deprecated alongside
Multi Box Pruning. Use Automatic Box Pruning instead.

## Declaration

public static void RebuildBroadphaseRegions([Bounds](Bounds.html) worldBounds,
int subdivisions);

### Parameters

worldBounds | Boundaries of the physics world.  
---|---  
subdivisions | How many cells to create along x and z axis.  
  
### Description

Rebuild the broadphase interest regions as well as set the world boundaries.

Effective only when the Multi-box Pruning Broadphase is used.  
  
In this mode, the boundaries of the world have to be set and then the physics
engine would subdivide the volume into a flat grid in the XZ plane, with each
cell containing a set of objects that belong to the cell. One may think that
each cell contains an instance of the regular sweep-and-prune broadphase. The
main benefit of having a grid is to be able to avoid the typical sweep-and-
prune locality problem where in a flat world all the objects overlap each
other along the Y axis thus causing excess rebuilding of the SAP projections
lists along each axis even for the objects that are far apart.  
  
Note that the physics objects located outside of the world boundaries will not
detect collisions at all.  
  
There is a limit of 256 on the total amount of world cells currently, so the
maximum number you can set to subdivisions is 16.  
  
This function is useful to make the broadphase settings per-scene, not per-
project.

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

