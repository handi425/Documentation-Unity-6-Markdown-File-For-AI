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

# RenderingLayerMask

struct in UnityEngine

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

The Render Pipeline allows you to use Rendering Layers, which are LayerMasks
to make Lights or effects only affect specific Renderers.

Rendering Layers are also supported on decal projectors, and can be sampled
from the ShaderGraph to implement custom effects.  
  
Rendering Layers are a Bitmask and it represents the 32 Layers and define them
as `true` or `false`. Each bitmask describes whether the `RenderingLayer` is
used. As an example, bit 5 can be set to 1 (`true`).  
  
`Edit->Settings->Tags and Layers` option shows the use of the 32 bitmasks.
Each `RenderingLayer` is shown with a string setting. As an example `Layer 0`
is set as `Default`. There is always at least one defined RenderingLayer.

### Static Properties

[defaultRenderingLayerMask](RenderingLayerMask-
defaultRenderingLayerMask.html)| Returns an instance of Default Rendering
Layer Mask.  
---|---  
  
### Properties

[value](RenderingLayerMask-value.html)| Converts a layer mask value to an
integer value.  
---|---  
  
### Static Methods

[GetDefinedRenderingLayerCount](RenderingLayerMask.GetDefinedRenderingLayerCount.html)|
Returns a number of Rendering Layers defined in the Tags and Layers manager.  
---|---  
[GetDefinedRenderingLayerNames](RenderingLayerMask.GetDefinedRenderingLayerNames.html)|
Returns a names of the defined Rendering Layers in the Tags and Layers
manager.  
[GetDefinedRenderingLayersCombinedMaskValue](RenderingLayerMask.GetDefinedRenderingLayersCombinedMaskValue.html)|
Returns value that represents all defined Rendering Layers in the Tags and
Layers manager.  
[GetDefinedRenderingLayerValues](RenderingLayerMask.GetDefinedRenderingLayerValues.html)|
Returns a values of the defined Rendering Layers in the Tags and Layers
manager.  
[GetLastDefinedRenderingLayerIndex](RenderingLayerMask.GetLastDefinedRenderingLayerIndex.html)|
Returns an index of the last defined Rendering Layer in the Tags and Layers
manager.  
[GetMask](RenderingLayerMask.GetMask.html)| Given a set of rendering layer
names as defined in the Tags and Layers manager, returns the equivalent
rendering layer mask for all of them.  
[GetRenderingLayerCount](RenderingLayerMask.GetRenderingLayerCount.html)|
Returns a number of Rendering Layers defined in the Tags and Layers manager
including empty ones.  
[NameToRenderingLayer](RenderingLayerMask.NameToRenderingLayer.html)| Given a
rendering layer name, returns the rendering layer index as defined in the Tags
and Layers manager.  
[RenderingLayerToName](RenderingLayerMask.RenderingLayerToName.html)| Given a
rendering layer index, returns the name of the layer as defined in the Tags
and Layers manager.  
  
### Operators

[RenderingLayerMask](RenderingLayerMask-operator_uint.html)| Implicitly
converts uint to a RenderingLayerMask.  
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

