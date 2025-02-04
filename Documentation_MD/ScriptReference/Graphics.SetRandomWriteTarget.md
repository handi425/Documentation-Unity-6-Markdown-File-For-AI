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

#  [Graphics](Graphics.html).SetRandomWriteTarget

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

public static void SetRandomWriteTarget(int index,
[ComputeBuffer](ComputeBuffer.html) uav, bool preserveCounterValue = false);

## Declaration

public static void SetRandomWriteTarget(int index,
[GraphicsBuffer](GraphicsBuffer.html) uav, bool preserveCounterValue = false);

## Declaration

public static void SetRandomWriteTarget(int index,
[RenderTexture](RenderTexture.html) uav);

### Parameters

index | The index of the random write target.  
---|---  
uav | Buffer or texture to set as the write target.  
preserveCounterValue | Whether to leave the append/consume counter value unchanged.  
  
### Description

Set random write target for [Shader Model 4.5](../Manual/SL-
ShaderCompileTargets.html) level pixel shaders.

Shader Model 4.5 and above level pixel shaders can write into arbitrary
locations of some textures and buffers, called "unordered access views" (UAV)
in [UsingDX11GL3Features](../Manual/UsingDX11GL3Features.html). These "random
write" targets are set similarly to how multiple render targets are set. You
can either use a [RenderTexture](RenderTexture.html) with `enableRandomWrite`
flag set, or a [ComputeBuffer](ComputeBuffer.html) as target.  
  
Offset the index value given to `SetRandomWriteTarget` by adding the number of
render targets used. This value might not correspond exactly to the fixed
register index set in the shaders as the UAV indexing value can vary between
different platforms. Refer to the platform-specific documentation for details
of these differences. On DX11, the first valid UAV index is the number of
active render targets, so in the common case of a single render target, the
UAV indexing will start from 1. Platforms using automatically translated HLSL
shaders will match this behavior, however, with hand-written GLSL shaders the
indexes will match the bindings.  
  
When setting a [ComputeBuffer](ComputeBuffer.html), the `preserveCounterValue`
parameter indicates whether to leave the counter value unchanged, or reset it
to 0 (the default behaviour).  
  
The targets stay set until you manually clear them with
[ClearRandomWriteTargets](Graphics.ClearRandomWriteTargets.html). It is best
practice to call ClearRandomWriteTargets after your rendering is complete. If
you do not do this, rendering issues can occur and some built-in Unity
rendering passes may crash.  
  
Additional resources: [RenderTexture.enableRandomWrite](RenderTexture-
enableRandomWrite.html), [ComputeBuffer](ComputeBuffer.html),
[ComputeBuffer.SetCounterValue](ComputeBuffer.SetCounterValue.html),
[UsingDX11GL3Features](../Manual/UsingDX11GL3Features.html).

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

