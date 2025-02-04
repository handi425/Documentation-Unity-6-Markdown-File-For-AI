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

#  [Mesh](Mesh.html).AddBlendShapeFrame

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

[Switch to Manual](../Manual/class-Mesh.html "Go to Mesh Component in the
Manual")

## Declaration

public void AddBlendShapeFrame(string shapeName, float frameWeight, Vector3[]
deltaVertices, Vector3[] deltaNormals, Vector3[] deltaTangents);

### Parameters

shapeName | Name of the blend shape to add a frame to.  
---|---  
frameWeight | Weight for the frame being added.  
deltaVertices | Delta vertices for the frame being added.  
deltaNormals | Delta normals for the frame being added.  
deltaTangents | Delta tangents for the frame being added.  
  
### Description

Adds a new blend shape frame.

If blend shape name does not exist, then a new blend shape is created. Blend
shape frames can only be added to a new blend shape, or the last blend shape.
Usually there will be a single frame for a blend shape, but the range of
blending [0-100%] may be split into multiple frames. Weight is assumed to be
100% when a shape only has one frame. Frame must be added in an increasing
weight order for blend shapes having multiple frames. `deltaVertices`,
`deltaNormals` and `deltaTangents` arrays must be of size =
[Mesh.vertexCount](Mesh-vertexCount.html). Subtract Mesh vertices, normals or
tangents to convert from frame full vectors to get deltas. `deltaNormals` or
`deltaTangents` may be set to null if there are no normals or tangents for a
frame.

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

