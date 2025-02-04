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

# RendererListDesc

struct in UnityEngine.Rendering.RendererUtils

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

Represents the set of GameObjects that a RendererList contains.

### Properties

[batchLayerMask](Rendering.RendererUtils.RendererListDesc-
batchLayerMask.html)| The batch layer mask to use for filtering this
RendererList.  
---|---  
[excludeObjectMotionVectors](Rendering.RendererUtils.RendererListDesc-
excludeObjectMotionVectors.html)| Indicates whether to exclude dynamic
GameObjects from the RendererList.  
[layerMask](Rendering.RendererUtils.RendererListDesc-layerMask.html)| The
layer mask to use for filtering this RendererList.  
[overrideMaterial](Rendering.RendererUtils.RendererListDesc-
overrideMaterial.html)| The material to render the RendererList's GameObjects
with. This overrides the material for each GameObject.  
[overrideMaterialPassIndex](Rendering.RendererUtils.RendererListDesc-
overrideMaterialPassIndex.html)| Pass index for the override material.  
[overrideShader](Rendering.RendererUtils.RendererListDesc-
overrideShader.html)| The shader to render the RendererList's GameObjects
with. This overrides the shader for each GameObject. Override shaders do not
override existing material properties.  
[overrideShaderPassIndex](Rendering.RendererUtils.RendererListDesc-
overrideShaderPassIndex.html)| Selects which pass of the override shader to
use.  
[rendererConfiguration](Rendering.RendererUtils.RendererListDesc-
rendererConfiguration.html)| The renderer configuration for the RendererList.
For more information, see PerObjectData.  
[renderingLayerMask](Rendering.RendererUtils.RendererListDesc-
renderingLayerMask.html)| The rendering layer mask to use for filtering this
RendererList.  
[renderQueueRange](Rendering.RendererUtils.RendererListDesc-
renderQueueRange.html)| The material render queue range to use for the
RendererList. For more information, see RenderQueueRange.  
[sortingCriteria](Rendering.RendererUtils.RendererListDesc-
sortingCriteria.html)| The method Unity uses to sort the GameObjects in the
RendererList. For more information, see SortingCriteria.  
[stateBlock](Rendering.RendererUtils.RendererListDesc-stateBlock.html)| An
optional set of values to override the RendererLists render state. For more
information, see RenderStateBlock.  
  
### Constructors

[RendererListDesc](Rendering.RendererUtils.RendererListDesc-ctor.html)|
Initializes and returns an instance of RendererListDesc.  
---|---  
  
### Public Methods

[IsValid](Rendering.RendererUtils.RendererListDesc.IsValid.html)| Checks
whether the RendererListDesc is valid.  
---|---  
  
### Static Methods

[ConvertToParameters](Rendering.RendererUtils.RendererListDesc.ConvertToParameters.html)|
Convert a given RendererListDesc to a RendererListParams struct with
equivalent parameters.  
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

