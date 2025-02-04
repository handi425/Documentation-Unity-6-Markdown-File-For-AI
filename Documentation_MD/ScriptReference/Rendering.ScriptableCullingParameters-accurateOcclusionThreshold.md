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

#
[ScriptableCullingParameters](Rendering.ScriptableCullingParameters.html).accurateOcclusionThreshold

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

public float accurateOcclusionThreshold;

### Description

This parameter determines query distance for occlusion culling.

The accurateOcclusionThreshold controls the distance where the level of detail
(LOD) changes.  
  
The default value of this parameter is -1, and any value less than 0 has the
same effect. Default values result in automatic calculation of the LOD.  
  
When you use occlusion culling, the occlusion data of the world varies in
level of detail. In the occlusion data, there are tiles of various sizes. Each
tile contains a cells-and-portals graph. In each cell, visibility is the same.
This means that any two points are visible within the cell. Portals are the
openings between the cells, which determine the visibility between them.  
  
The tiles are in a k-d tree. The tree contains different sized tiles, where
each tile represents a level of detail. When you query a small tile, you get
accurate culling results at the price of query time.  
  
During the culling, the tile size varies with the distance from the camera.
This gives finer detail closer to the camera, and coarser detail at further
distance.  
  
The higher the value is, the higher the accuracy is far away form the camera.
High values can have a negative impact on performance.

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

