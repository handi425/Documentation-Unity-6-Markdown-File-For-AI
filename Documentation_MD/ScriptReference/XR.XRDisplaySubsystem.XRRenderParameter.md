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

# XRRenderParameter

struct in UnityEngine.XR

/

Implemented in:[UnityEngine.XRModule](UnityEngine.XRModule.html)

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

A single viewpoint that must be rendered by the render pipeline. Contains a
target viewport and texture array slice within a corresponding
[renderTarget](XR.XRDisplaySubsystem.XRRenderPass-renderTarget.html).

### Properties

[isPreviousViewValid](XR.XRDisplaySubsystem.XRRenderParameter-
isPreviousViewValid.html)| Determines whether
XRDisplaySubsystem.XRRenderParameter.previousView is valid for use in a frame.  
---|---  
[occlusionMesh](XR.XRDisplaySubsystem.XRRenderParameter-occlusionMesh.html)|
Represents the area in screen-space that is not visible on the XR Display.  
[previousView](XR.XRDisplaySubsystem.XRRenderParameter-previousView.html)|
Previous frame view matrix for use in motion vector calculation. Use
XRDisplaySubsystem.XRRenderParameter.isPreviousViewValid to determine if
previous view is valid for use. When late latching is enabled, previous view
is also adjusted for late latching.  
[projection](XR.XRDisplaySubsystem.XRRenderParameter-projection.html)| The
projection matrix that the render pipeline should use to render to the
renderTarget.  
[textureArraySlice](XR.XRDisplaySubsystem.XRRenderParameter-
textureArraySlice.html)| The slice of the output texture array that the render
pipeline should render to.  
[view](XR.XRDisplaySubsystem.XRRenderParameter-view.html)| World transform
that the render pipeline should use to render to the renderTarget.  
[viewport](XR.XRDisplaySubsystem.XRRenderParameter-viewport.html)| Selects the
viewport of the output texture renderTarget.  
  
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

