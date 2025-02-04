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

#  [GraphicsTexture](Rendering.GraphicsTexture.html).active

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

public static [Rendering.GraphicsTexture](Rendering.GraphicsTexture.html)
active;

### Description

Currently active graphics texture.

All rendering goes into the active GraphicsTexture. If the active
GraphicsTexture is `null`, everything renders in the main window. If the
active render target is a [RenderTexture](RenderTexture.html),
`GraphicsTexture.active` returns the [graphicsTexture](Texture-
graphicsTexture.html) of [RenderTexture.active](RenderTexture-active.html).  
  
In order to set the active render target to a GraphicsTexture, it must have
[GraphicsTextureDescriptorFlags.RenderTarget](Rendering.GraphicsTextureDescriptorFlags.RenderTarget.html)
enabled in
[GraphicsTextureDescriptor.flags](Rendering.GraphicsTextureDescriptor-
flags.html) on texture creation.  
  
Setting `GraphicsTexture.active` is the same as calling
[Graphics.SetRenderTarget](Graphics.SetRenderTarget.html) with a single
GraphicsTexture. Typically you change or query the active render target when
implementing custom graphics effects; if all you need is to make a Camera
render into a texture, then use [Camera.targetTexture](Camera-
targetTexture.html) with a [RenderTexture](RenderTexture.html) instead.  
  
Additional resources:
[GraphicsTextureDescriptorFlags.RenderTarget](Rendering.GraphicsTextureDescriptorFlags.RenderTarget.html),
[Graphics.SetRenderTarget](Graphics.SetRenderTarget.html),
[RenderTexture.active](RenderTexture-active.html).

    
    
    using UnityEngine;
    using UnityEngine.Rendering;
    using System.Collections;  
      
    // Get the contents of a [GraphicsTexture](Rendering.GraphicsTexture.html) into a [Texture2D](Texture2D.html)
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        static public [Texture2D](Texture2D.html) GetGfxTexPixels([GraphicsTexture](Rendering.GraphicsTexture.html) gfxTex)
        {
            // Remember currently active render target
            [GraphicsTexture](Rendering.GraphicsTexture.html) currentActiveRT = [GraphicsTexture.active](Rendering.GraphicsTexture-active.html);  
      
            // Set the supplied [GraphicsTexture](Rendering.GraphicsTexture.html) as the active one
            [GraphicsTexture.active](Rendering.GraphicsTexture-active.html) = gfxTex;  
      
            // Create a new [Texture2D](Texture2D.html) and read the [GraphicsTexture](Rendering.GraphicsTexture.html) image into it
            [Texture2D](Texture2D.html) tex = new [Texture2D](Texture2D.html)(gfxTex.descriptor.width, gfxTex.descriptor.height);
            tex.ReadPixels(new [Rect](Rect.html)(0, 0, tex.width, tex.height), 0, 0);
            tex.Apply();  
      
            // Restore previously active render texture
            [GraphicsTexture.active](Rendering.GraphicsTexture-active.html) = currentActiveRT;
            return tex;
        }
    }
    

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

