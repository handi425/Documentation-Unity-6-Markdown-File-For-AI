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

# DrawingSettings

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

Settings for ScriptableRenderContext.DrawRenderers.

DrawingSettings describes how to sort visible objects
([sortingSettings](Rendering.DrawingSettings-sortingSettings.html)) and which
shader passes to use ([shaderPassName](Rendering.DrawingSettings-
shaderPassName.html)).  
  
Additional resources: ScriptableRenderContext.DrawRenderers,
[ScriptableRenderContext.Cull](Rendering.ScriptableRenderContext.Cull.html),
[FilteringSettings](Rendering.FilteringSettings.html).  
  
OverrideMaterial vs. OverrideShader: Using the overrideMaterial parameter will
override all rendered materials and their properties. The overrideShader
property will force the renderers to use a different shader while preserving
current material properties. Properties on the overriden material can then be
accessed in the override shader. The use of override shaders is currently not
supported with SRPBatcher and BatchRendererGroups. Override Shaders will have
an impact on performance and should be avoided where overrideMaterial can be
used. OverrideShader and OverrideMaterial can't both be used in the same
drawRenderers call.

### Static Properties

[maxShaderPasses](Rendering.DrawingSettings-maxShaderPasses.html)| The
maxiumum number of passes that can be rendered in 1 DrawRenderers call.  
---|---  
  
### Properties

[enableDynamicBatching](Rendering.DrawingSettings-enableDynamicBatching.html)|
Controls whether dynamic batching is enabled.  
---|---  
[enableInstancing](Rendering.DrawingSettings-enableInstancing.html)| Controls
whether instancing is enabled.  
[fallbackMaterial](Rendering.DrawingSettings-fallbackMaterial.html)| Sets the
Material to use for any drawers in this group that don't meet the
requirements.  
[mainLightIndex](Rendering.DrawingSettings-mainLightIndex.html)| Configures
what light should be used as main light.  
[overrideMaterial](Rendering.DrawingSettings-overrideMaterial.html)| Sets the
Material to use for all drawers that would render in this group.  
[overrideMaterialPassIndex](Rendering.DrawingSettings-
overrideMaterialPassIndex.html)| Selects which pass of the override material
to use.  
[overrideShader](Rendering.DrawingSettings-overrideShader.html)| Sets the
shader to use for all drawers that would render in this group. Override
shaders do not override existing material properties.  
[overrideShaderPassIndex](Rendering.DrawingSettings-
overrideShaderPassIndex.html)| Selects which pass of the override shader to
use.  
[perObjectData](Rendering.DrawingSettings-perObjectData.html)| What kind of
per-object data to setup during rendering.  
[sortingSettings](Rendering.DrawingSettings-sortingSettings.html)| How to sort
objects during rendering.  
  
### Constructors

[DrawingSettings](Rendering.DrawingSettings-ctor.html)| Create a draw settings
struct.  
---|---  
  
### Public Methods

[GetShaderPassName](Rendering.DrawingSettings.GetShaderPassName.html)| Get the
name of the shader pass.  
---|---  
[SetShaderPassName](Rendering.DrawingSettings.SetShaderPassName.html)| Set the
name of the shader pass.  
  
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

