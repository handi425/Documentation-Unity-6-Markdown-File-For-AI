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

# RasterState

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

Values for the raster state.

Use this with [RenderStateBlock](Rendering.RenderStateBlock.html) and
ScriptableRenderContext.DrawRenderers to override the GPU's render state.  
  
Corresponds to the `Conservative`, `Cull`, `ZClip`, and `Offset` commands in
[ShaderLab](../Manual/SL-Reference.html).  
  
Additional resources: [RenderStateBlock](Rendering.RenderStateBlock.html),
[[ScriptableRenderContext.DrawRenderers], [ShaderLab command:
Stencil](../Manual/SL-Stencil.html).

### Static Properties

[defaultValue](Rendering.RasterState-defaultValue.html)| Default values for
the raster state.  
---|---  
  
### Properties

[conservative](Rendering.RasterState-conservative.html)| Enables conservative
rasterization. Before using check for support via
SystemInfo.supportsConservativeRaster property.  
---|---  
[cullingMode](Rendering.RasterState-cullingMode.html)| Controls which sides of
polygons should be culled (not drawn).  
[depthClip](Rendering.RasterState-depthClip.html)| Enable clipping based on
depth.  
[offsetFactor](Rendering.RasterState-offsetFactor.html)| Scales the maximum Z
slope in the GPU's depth bias setting.  
[offsetUnits](Rendering.RasterState-offsetUnits.html)| Scales the minimum
resolvable depth buffer value in the GPU's depth bias setting.  
  
### Constructors

[RasterState](Rendering.RasterState-ctor.html)| Creates a new raster state
with the given values.  
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

