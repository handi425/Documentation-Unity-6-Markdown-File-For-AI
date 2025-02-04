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

# ShadowDrawingSettings

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

Settings for ScriptableRenderContext.DrawShadows.

This structure describes which shadow light to render
([lightIndex](Rendering.ShadowDrawingSettings-lightIndex.html)) with what
split settings ([splitData](Rendering.ShadowDrawingSettings-splitData.html)).  
  
Additional resources: [ShadowSplitData](Rendering.ShadowSplitData.html).

### Properties

[batchLayerMask](Rendering.ShadowDrawingSettings-batchLayerMask.html)| Unity
renders objects whose BatchFilterSettings.batchLayer value is enabled in this
bit mask.  
---|---  
[cullingResults](Rendering.ShadowDrawingSettings-cullingResults.html)| Culling
results to use.  
[lightIndex](Rendering.ShadowDrawingSettings-lightIndex.html)| The index of
the shadow-casting light to be rendered.  
[objectsFilter](Rendering.ShadowDrawingSettings-objectsFilter.html)| Specifies
the filter Unity applies to GameObjects that it renders in the shadow pass.  
[splitIndex](Rendering.ShadowDrawingSettings-splitIndex.html)| The split index
of the shadow-casting light to be rendered. With the default value of -1,
Unity increments the split index from 0 for shadow renderer lists that are
created consecutively for the same light index with matching filtering and
masking settings.  
[useRenderingLayerMaskTest](Rendering.ShadowDrawingSettings-
useRenderingLayerMaskTest.html)| Set this to true to make Unity filter
Renderers during shadow rendering. Unity filters Renderers based on the
Rendering Layer Mask of the Renderer itself, and the Rendering Layer Mask of
each shadow casting Light.  
  
### Constructors

[ShadowDrawingSettings](Rendering.ShadowDrawingSettings-ctor.html)| Create a
shadow settings object.  
---|---  
  
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

