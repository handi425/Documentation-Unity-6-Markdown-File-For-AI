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

#  [GL](GL.html).GetGPUProjectionMatrix

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

public static [Matrix4x4](Matrix4x4.html)
GetGPUProjectionMatrix([Matrix4x4](Matrix4x4.html) proj, bool
renderIntoTexture);

### Parameters

proj | Source projection matrix.  
---|---  
renderIntoTexture | Will this projection be used for rendering into a RenderTexture?  
  
### Returns

**Matrix4x4** Adjusted projection matrix for the current graphics API.

### Description

Compute GPU projection matrix from camera's projection matrix.

In Unity, projection matrices follow OpenGL convention. However on some
platforms they have to be transformed a bit to match the native API
requirements. Use this function to calculate how the final projection matrix
will be like. The value will match what comes as `UNITY_MATRIX_P` matrix in a
shader.  
  
The `renderIntoTexture` value should be set to true if you intend to render
into a [RenderTexture](RenderTexture.html) with this projection matrix. On
some platforms it affects how the final matrix will look like.  
  
Additional resources: [Camera.projectionMatrix](Camera-projectionMatrix.html),
[Matrix4x4.Perspective](Matrix4x4.Perspective.html), [Platform
differences](../Manual/SL-PlatformDifferences.html), [Built-in shader
variables](../Manual/SL-UnityShaderVariables.html).

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

