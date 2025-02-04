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

#  [GL](GL.html).Clear

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

public static void Clear(bool clearDepth, bool clearColor, [Color](Color.html)
backgroundColor, float depth = 1.0f);

### Parameters

clearDepth | Should the depth buffer be cleared?  
---|---  
clearColor | Should the color buffer be cleared?  
backgroundColor | The color to clear with, used only if `clearColor` is `true`.  
depth | The depth to clear the z-buffer with, used only if `clearDepth` is `true`. The valid range is from 0 (near plane) to 1 (far plane). The value is graphics API agnostic: the abstraction layer will convert the value to match the convention of the current graphics API.  
  
### Description

Clear the current render buffer.

This clears the screen or the active [RenderTexture](RenderTexture.html) you
are drawing into. The cleared area is limited by the active viewport. This
operation might alter the model/view/projection matrices.  
  
In most cases, a Camera will already be configured to clear the screen or
[RenderTexture](RenderTexture.html) and you will not need to perform this
operation manually.  
  
Additional resources: [GL.ClearWithSkybox](GL.ClearWithSkybox.html).

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

