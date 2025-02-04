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

#  [CommandBuffer](Rendering.CommandBuffer.html).SetInstanceMultiplier

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

## Declaration

public void SetInstanceMultiplier(uint multiplier);

### Description

Adds a command to multiply the instance count of every draw call by a specific
multiplier.

Changing the instance multiplier is useful for stereo rendering optimizations
such as single pass instanced rendering. For example, if you set the
multiplier to 2, a command that draws one instance, instead draws two, and a
command that draws two instances, draws four. See [Single Pass Instanced
Rendering](../Manual/SinglePassInstancing.html) for more information.  
  
The multiplier is used until you reset it by calling this function again with
a new value. The default multiplier is 1. Passing a parameter value of 0 to
this function also sets the instance multiplier to 1.  
  
The instance multiplier affects draw calls submitted by internal Unity Engine
functions as well as
[CommandBuffer.DrawMesh](Rendering.CommandBuffer.DrawMesh.html),
[CommandBuffer.DrawMeshInstanced](Rendering.CommandBuffer.DrawMeshInstanced.html),
[Graphics.DrawMeshInstanced](Graphics.DrawMeshInstanced.html),
[CommandBuffer.DrawProcedural](Rendering.CommandBuffer.DrawProcedural.html),
and [Graphics.DrawProcedural](Graphics.DrawProcedural.html)  
  
Note that the multiplier is not used for the indirect commands,
[CommandBuffer.DrawMeshInstancedIndirect](Rendering.CommandBuffer.DrawMeshInstancedIndirect.html),
[Graphics.DrawMeshInstancedIndirect](Graphics.DrawMeshInstancedIndirect.html),
[CommandBuffer.DrawProceduralIndirect](Rendering.CommandBuffer.DrawProceduralIndirect.html),
[Graphics.DrawProceduralIndirect](Graphics.DrawProceduralIndirect.html).

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

