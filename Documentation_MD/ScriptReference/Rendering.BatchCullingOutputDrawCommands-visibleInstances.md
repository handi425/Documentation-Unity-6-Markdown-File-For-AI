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
[BatchCullingOutputDrawCommands](Rendering.BatchCullingOutputDrawCommands.html).visibleInstances

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

public int* visibleInstances;

### Description

The indices of visible instances to render.

Because each draw command can have a different number of instances,
BatchRendererGroup stores the instance indices here, and each draw command
indexes them with the visibleOffset property. The instance indices are zero-
based indices that Unity passes directly to the shader which should use the
value to determine where to load instance data from.  
  
The culling callback must allocate the memory for this command using
[UnsafeUtility.Malloc](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Malloc.html)
with the [Allocator.TempJob](Unity.Collections.Allocator.TempJob.html)
parameter. Unity releases this memory when it finishes rendering the draw
commands.  
  
The visible instance indices only use the least significant 24 bits for the
actual instance index and use the highest 8 bits for the LOD crossfade factor.
In a future version of BatchRendererGroup, this restriction will only apply to
draw commands which actually set the LODCrossFade flag. This will enable you
to use all 32 bits which is useful if you want to encode data directly into
the index.

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

