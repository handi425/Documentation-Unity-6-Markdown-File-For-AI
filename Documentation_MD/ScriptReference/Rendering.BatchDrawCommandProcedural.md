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

# BatchDrawCommandProcedural

struct in UnityEngine.Rendering

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

Represents a procedural draw command for a
[BatchRendererGroup](Rendering.BatchRendererGroup.html).

This type of draw command has a reference to a material, but all vertex data
is fetched procedurally by the shader.

### Properties

[baseVertex](Rendering.BatchDrawCommandProcedural-baseVertex.html)| Base
vertex  
---|---  
[batchID](Rendering.BatchDrawCommandProcedural-batchID.html)| The batch ID
that this draw command uses. Determines the metadata values that are available
to a shader.  
[elementCount](Rendering.BatchDrawCommandProcedural-elementCount.html)| Number
of elements (indices or vertices) to draw  
[flags](Rendering.BatchDrawCommandProcedural-flags.html)| Specifies rendering
options for the draw command.  
[indexBufferHandle](Rendering.BatchDrawCommandProcedural-
indexBufferHandle.html)| Handle of an index buffer to use for indexed drawing.  
[indexOffsetBytes](Rendering.BatchDrawCommandProcedural-
indexOffsetBytes.html)| Offset into the index buffer where indices will be
read from, when issuing indexed draws.  
[lightmapIndex](Rendering.BatchDrawCommandProcedural-lightmapIndex.html)| The
index of the baked lightmap used in this draw command. If lightmap texture
arrays are enabled, this value is always -1 (0xFFFF).  
[materialID](Rendering.BatchDrawCommandProcedural-materialID.html)| Identifies
which Material to use to render the instances in this draw command.  
[sortingPosition](Rendering.BatchDrawCommandProcedural-sortingPosition.html)|
Together with BatchDrawCommand.flags, this specifies how to depth sort the
instances in this draw command.  
[splitVisibilityMask](Rendering.BatchDrawCommandProcedural-
splitVisibilityMask.html)| Indicates which splits that the draw command is
visible in.  
[topology](Rendering.BatchDrawCommandProcedural-topology.html)| The primitive
topology to use when executing the draw command.  
[visibleCount](Rendering.BatchDrawCommandProcedural-visibleCount.html)| The
number of instances to draw with this draw command. This must be a value
greater than 1.  
[visibleOffset](Rendering.BatchDrawCommandProcedural-visibleOffset.html)| The
index of the element in BatchCullingOutputDrawCommands.visibleInstances that
matches the first instance in this draw command.  
  
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

