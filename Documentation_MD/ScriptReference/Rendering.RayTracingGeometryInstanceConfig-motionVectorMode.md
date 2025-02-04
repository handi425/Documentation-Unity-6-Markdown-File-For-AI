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
[RayTracingGeometryInstanceConfig](Rendering.RayTracingGeometryInstanceConfig.html).motionVectorMode

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

public [MotionVectorGenerationMode](MotionVectorGenerationMode.html)
motionVectorMode;

### Description

Motion vector mode.

Unity configures the following built-in shader uniforms to calculate motion
vectors in HLSL code: `unity_MotionVectorsParams`, `unity_MatrixPreviousM` and
`unity_MatrixPreviousMI`.  
  
For ray tracing instances, `unity_MotionVectorsParams` is a vector uniform.
Its component values are as follows:

  * the x and z components are 0
  * the y component is 0 if the motion vector mode is [MotionVectorGenerationMode.ForceNoMotion](MotionVectorGenerationMode.ForceNoMotion.html). Otherwise it is 1.
  * the w component is 0 if the motion vector mode is [MotionVectorGenerationMode.Camera](MotionVectorGenerationMode.Camera.html). Otherwise it is 1.

`unity_MatrixPreviousM` and `unity_MatrixPreviousMI` are the instance matrix
and its inverse respectively used in the previous frame. Note that Unity only
updates these matrices only when there's a [Camera](Camera.html) in the Scene
that's using the
[DepthTextureMode.MotionVectors](DepthTextureMode.MotionVectors.html) flag in
[Camera.depthTextureMode](Camera-depthTextureMode.html).  
  
To access the ray tracing instance matrix in closest hit, any hit, and
intersection shaders, use the `ObjectToWorld` or `WorldToObject` HLSL
functions.  
  
Additional resources:
[MotionVectorGenerationMode](MotionVectorGenerationMode.html).

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

