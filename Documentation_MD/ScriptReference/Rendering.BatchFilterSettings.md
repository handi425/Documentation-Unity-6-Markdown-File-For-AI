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

# BatchFilterSettings

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

Represents settings that Unity applies to draw commands in this [draw
range](Rendering.BatchDrawRange.html).

For more information, see [BatchRendererGroup](../Manual/batch-renderer-
group.html).

### Properties

[allDepthSorted](Rendering.BatchFilterSettings-allDepthSorted.html)| Indicates
whether all draw commands in the current draw range have the
BatchDrawCommandFlags.HasSortingPosition flag set.  
---|---  
[batchLayer](Rendering.BatchFilterSettings-batchLayer.html)| The batch layer
to use for draw commands in this draw range.  
[layer](Rendering.BatchFilterSettings-layer.html)| The layer to use for draw
commands in this draw range.  
[motionMode](Rendering.BatchFilterSettings-motionMode.html)| Specifies how to
generate motion vectors in this draw range.  
[receiveShadows](Rendering.BatchFilterSettings-receiveShadows.html)| Indicates
whether instances from draw commands in this draw range should receive
shadows.  
[rendererPriority](Rendering.BatchFilterSettings-rendererPriority.html)| The
sorting priority to use for draw commands in this draw range.  
[renderingLayerMask](Rendering.BatchFilterSettings-renderingLayerMask.html)|
The rendering layer mask to use for draw commands in this draw range.  
[sceneCullingMask](Rendering.BatchFilterSettings-sceneCullingMask.html)| Use
this bit mask to discard the draw commands in a particular context. A draw
command is not discarded if the expression (1 << layer) & sceneCullingMask is
true. This field is typically used when rendering Editor previews.  
[shadowCastingMode](Rendering.BatchFilterSettings-shadowCastingMode.html)|
Specifies how instances from the draw commands in this draw range cast
shadows.  
[staticShadowCaster](Rendering.BatchFilterSettings-staticShadowCaster.html)|
Indicates whether instances from the draw commands in this draw range render
into cached shadow maps.  
  
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

