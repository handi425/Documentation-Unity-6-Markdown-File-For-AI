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

**Experimental** : this API is experimental and might be changed or removed in
the future.

# GraphicsState

struct in UnityEngine.Experimental.Rendering

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

A graphics state identifies a specific rendering configuration.

Modern graphics APIs (i.e. Metal, D3D12, Vulkan) use both the active shader
variant and rendering configuration to create the accurate GPU representation
of a shader.

### Properties

[attachments](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
attachments.html)| Array of color attachments used in this rendering
configuration.  
---|---  
[depthAttachmentIndex](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
depthAttachmentIndex.html)| The index of the attachment to be used as the
depth/stencil buffer for this rendering configuration.  
[depthBias](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
depthBias.html)| The global depth bias value for this rendering configuration.  
[forceCullMode](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
forceCullMode.html)| The forced cull mode in this rendering configuration.  
[invertCulling](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
invertCulling.html)| Flag indicating if backface culling is inverted in this
rendering configuration.  
[invertProjection](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
invertProjection.html)| Flag indicating if the projection matrix is inverted
in this rendering configuration.  
[multiviewCount](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
multiviewCount.html)| The number of VR views used in this rendering
configuration.  
[negativeScale](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
negativeScale.html)| Flag indicating if the mesh has inverted scale in this
rendering configuration.  
[renderState](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
renderState.html)| The render state used in this rendering configuration.  
[sampleCount](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
sampleCount.html)| The number of samples per pixel in this rendering
configuration.  
[shadingRateIndex](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
shadingRateIndex.html)| Index of attachment used as shading rate image.  
[slopeDepthBias](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
slopeDepthBias.html)| The global slope depth bias value for this rendering
configuration.  
[subPasses](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
subPasses.html)| Array containing information of each subpass.  
[subPassIndex](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
subPassIndex.html)| Index of the active subpass in this rendering
configuration.  
[topology](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
topology.html)| The topology of the Mesh, e.g: Triangles, Lines, Quads,
Points, etc. used in this rendering configuration.  
[vertexAttributes](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
vertexAttributes.html)| Array containing information of vertex attributes.  
[wireframe](Experimental.Rendering.GraphicsStateCollection.GraphicsState-
wireframe.html)| Is wireframe mode enabled for this rendering configuration.  
  
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

