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

# GraphicsTexture

class in UnityEngine.Rendering

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

Represents the view on a single texture resource that is uploaded to the
graphics device.

A GraphicsTexture specifically represents the actual resource that a
[Texture](Texture.html) object uploads to the GPU. A Texture may create
several different GraphicsTextures in its lifetime (such as to represent
different mipmap levels or the color and depth buffers in a
[RenderTexture](RenderTexture.html)) and will recreate GraphicsTextures when
certain changes are made to the Texture (such as resizing). Use
[Texture.graphicsTexture](Texture-graphicsTexture.html) to get a Texture's
current GraphicsTexture.  
  
GraphicsTextures are useful for getting the current uploaded state of a
texture on the graphics device.
[GraphicsTextureDescriptor.mipCount](Rendering.GraphicsTextureDescriptor-
mipCount.html) represents only the uploaded mipmap levels when using texture
streaming or [mipmap limit settings](Texture2D-activeMipmapLimit.html).
Consequently,
[GraphicsTextureDescriptor.width](Rendering.GraphicsTextureDescriptor-
width.html) and
[GraphicsTextureDescriptor.height](Rendering.GraphicsTextureDescriptor-
height.html) represent the width and height of the maximum uploaded mipmap
level.  
  
GraphicsTextures are purely run-time objects and cannot be saved as assets.  
  
To use a GraphicsTexture as a render target, it must have
[GraphicsTextureDescriptorFlags.RenderTarget](Rendering.GraphicsTextureDescriptorFlags.RenderTarget.html)
enabled in its
[GraphicsTextureDescriptor.flags](Rendering.GraphicsTextureDescriptor-
flags.html).  
  
Additional resources: [Texture.graphicsTexture](Texture-graphicsTexture.html),
[Graphics.SetRenderTarget](Graphics.SetRenderTarget.html).

### Static Properties

[active](Rendering.GraphicsTexture-active.html)| Currently active graphics
texture.  
---|---  
  
### Properties

[descriptor](Rendering.GraphicsTexture-descriptor.html)| Contains all the
information Unity uses to create a GraphicsTexture.  
---|---  
[state](Rendering.GraphicsTexture-state.html)| The current state of a
GraphicsTexture.  
  
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

