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

#  [Camera](Camera.html).RenderWithShader

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

[Switch to Manual](../Manual/class-Camera.html "Go to Camera Component in the
Manual")

## Declaration

public void RenderWithShader([Shader](Shader.html) shader, string
replacementTag);

### Description

Render the camera with shader replacement.

See [Rendering with Replaced Shaders](../Manual/SL-ShaderReplacement.html)
page for details.  
  
This will render the camera. It will use the camera's clear flags, target
texture and all other settings.  
  
If the replacementTag argument is not in use, pass an empty string as the
value.  
  
The camera will **not** send [OnPreCull](MonoBehaviour.OnPreCull.html),
[OnPreRender](MonoBehaviour.OnPreRender.html) or
[OnPostRender](MonoBehaviour.OnPostRender.html) to attached scripts. Image
filters will not be rendered either.  
  
This is used for special effects, e.g. rendering screen space normal buffer of
the whole Scene, heat vision and so on. To make use of this feature, usually
you create a camera and disable it. Then call RenderWithShader on it.  
  
You are not able to call the Render function from a camera that is currently
rendering. If you wish to do this create a copy of the camera, and make it
match the original one using [CopyFrom](Camera.CopyFrom.html).  
  
Additional resources: [Rendering with Replaced Shaders](../Manual/SL-
ShaderReplacement.html),
[SetReplacementShader](Camera.SetReplacementShader.html),
[Render](Camera.Render.html).

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

