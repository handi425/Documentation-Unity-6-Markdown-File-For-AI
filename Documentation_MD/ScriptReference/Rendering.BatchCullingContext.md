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

# BatchCullingContext

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

Culling context for a batch.

Specifies the data required to perform culling. Additional resources:
[OnPerformCulling](Rendering.BatchRendererGroup.OnPerformCulling.html).

### Properties

[cullingFlags](Rendering.BatchCullingContext-cullingFlags.html)| Additional
culling information for the current context.  
---|---  
[cullingLayerMask](Rendering.BatchCullingContext-cullingLayerMask.html)| The
cullingLayerMask value of the object from which the culling is invoked. The
draw command is discarded by the internal culling if the expression (1 <<
layer) & cullingLayerMask is false. Using this field is optional, use it for
performance or other optimization purposes.  
[cullingPlanes](Rendering.BatchCullingContext-cullingPlanes.html)| Planes to
cull against.  
[cullingSplits](Rendering.BatchCullingContext-cullingSplits.html)| The array
of CullingSplit structs.  
[localToWorldMatrix](Rendering.BatchCullingContext-localToWorldMatrix.html)|
Local to world matrix.  
[lodParameters](Rendering.BatchCullingContext-lodParameters.html)| Additional
resources: LODParameters.  
[projectionType](Rendering.BatchCullingContext-projectionType.html)| The
projection of the view from which the culling is invoked. Usage example: take
different culling paths for orthographic vs perspective views.  
[receiverPlaneCount](Rendering.BatchCullingContext-receiverPlaneCount.html)|
The number of receiver planes.  
[receiverPlaneOffset](Rendering.BatchCullingContext-receiverPlaneOffset.html)|
The index of the first receiver plane in the BatchCullingContext.cullingPlanes
array.  
[sceneCullingMask](Rendering.BatchCullingContext-sceneCullingMask.html)| Use
this bit mask to discard the draw commands in a particular context. A draw
command is not discarded if the expression (1 << layer) & sceneCullingMask is
true. This field is typically used when rendering Editor previews.  
[splitExclusionMask](Rendering.BatchCullingContext-splitExclusionMask.html)| A
bitmask that represents the BatchCullingContext.cullingSplits Unity ignores in
a BatchDrawCommand struct.  
[viewID](Rendering.BatchCullingContext-viewID.html)| The ID of the object from
which the culling is invoked. Usage example: store culling-related data for
each object.  
[viewType](Rendering.BatchCullingContext-viewType.html)| The type of the view
from which the culling is invoked. Usage examples: skip culling, take
different culling paths depending on the view type, etc.  
  
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

