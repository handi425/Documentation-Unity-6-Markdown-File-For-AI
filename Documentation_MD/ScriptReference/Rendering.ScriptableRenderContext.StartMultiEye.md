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
[ScriptableRenderContext](Rendering.ScriptableRenderContext.html).StartMultiEye

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

public void StartMultiEye([Camera](Camera.html) camera);

## Declaration

public void StartMultiEye([Camera](Camera.html) camera, int eye);

### Parameters

camera | Camera to enable stereo rendering on.  
---|---  
eye | The current eye to be rendered.  
  
### Description

Schedules a fine-grained beginning of stereo rendering on the
ScriptableRenderContext.

Activates stereo rendering on the
[ScriptableRenderContext](Rendering.ScriptableRenderContext.html) and
`camera`. When used in conjunction with
[StopMultiEye](Rendering.ScriptableRenderContext.StopMultiEye.html), these
APIs provide fine-grained control of which draw calls are multi-plexed for
stereo purposes. For example, you would wrap your opaque and transparent
passes with
[StartMultiEye](Rendering.ScriptableRenderContext.StartMultiEye.html) and
[StopMultiEye](Rendering.ScriptableRenderContext.StopMultiEye.html), but you
could exclude your shadow rendering.  
  
Note that only draws are affected by this API. Compute work is not
automatically adjusted for stereo, therefore, per-eye compute work must be
manually generated.  
  
Additional resources:
[StopMultiEye](Rendering.ScriptableRenderContext.StopMultiEye.html),
[SetupCameraProperties](Rendering.ScriptableRenderContext.SetupCameraProperties.html),
[StereoEndRender](Rendering.ScriptableRenderContext.StereoEndRender.html),
CullingResults.GetCullingParameters.

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

