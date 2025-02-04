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

#  [NavMeshObstacle](AI.NavMeshObstacle.html).carving

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

public bool carving;

### Description

Should this obstacle make a cut-out in the navmesh.

When enabled, this changes the navmesh by cutting out a hole. The shape of the
hole is based on the size and shape set on
[NavMeshObstacle](AI.NavMeshObstacle.html) and the navmesh bake settings for
radius and height.  
  
When the obstacle moves, the carved hole will also move but to reduce CPU
overhead the hole is only recalculated when necessary. The recalculation logic
has two options: 1) carve when stationary, 2) carve when moved.  
  
"Carve when stationary" is the default behavior and is used when
[carveOnlyStationary](AI.NavMeshObstacle-carveOnlyStationary.html) is set to
true. The obstacle is treated as moving when it has moved more than the
distance set by [carvingMoveThreshold](AI.NavMeshObstacle-
carvingMoveThreshold.html). At this time, the carved hole is removed. When the
obstacle has stopped moving, and has been stationary more than
[carvingTimeToStationary](AI.NavMeshObstacle-carvingTimeToStationary.html)
seconds, the obstacles is treated stationary and carving is updated again.
While the obstacle is moving, the agents will avoid it using the collision
avoidance, but will not plan paths around it. This mode is generally the best
choice in terms of performance. It is good match when the game object is
controlled by physics (i.e. crates and barrels).  
  
"Carve when moved" behavior is used when
[carveOnlyStationary](AI.NavMeshObstacle-carveOnlyStationary.html) is set to
false. In this mode the carved hole is updated when the obstacle has moved
more than the distance set by [carvingMoveThreshold](AI.NavMeshObstacle-
carvingMoveThreshold.html). This mode is well suited for large slowly moving
obstacles, for example a tank that is being avoided by infantry.

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

