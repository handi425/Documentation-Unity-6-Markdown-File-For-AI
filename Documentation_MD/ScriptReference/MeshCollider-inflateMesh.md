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

#  [MeshCollider](MeshCollider.html).inflateMesh

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

[Switch to Manual](../Manual/class-MeshCollider.html "Go to MeshCollider
Component in the Manual")

**Obsolete** MeshCollider.inflateMesh is no longer supported. The new cooking
algorithm doesn't need inflation to be used. public bool inflateMesh;

### Description

Allow the physics engine to increase the volume of the input mesh in attempt
to generate a valid convex mesh.

The physics engine imposes restrictions on the number of vertices and faces of
convex meshes used for collisions. For that reason, the minimum-volume convex
mesh automatically generated from the original non-convex mesh may not be
suitable for use in physics. In order to address that, the mesh inflation can
be used. It effectively extends the source data by a margin of
[skinWidth](MeshCollider-skinWidth.html) and bevels the sharp edges so that
the resulting mesh suits physics better.  
  
**Note** : Setting this to true can decrease the accuracy of the collision
mesh. Inflating a MeshCollider creates a new instance of the input mesh. This
takes additional memory.

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

