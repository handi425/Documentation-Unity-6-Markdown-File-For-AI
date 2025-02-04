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

# DefaultFormat

enumeration

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

Use a default format to create either Textures or RenderTextures from scripts
based on platform specific capability.

    
    
    using UnityEngine;
    using UnityEngine.Experimental.Rendering;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Create a new texture and assign it to the material of the renderer.
            [Texture2D](Texture2D.html) texture = new [Texture2D](Texture2D.html)(1, 1, [DefaultFormat.LDR](Experimental.Rendering.DefaultFormat.LDR.html), [TextureCreationFlags.None](Experimental.Rendering.TextureCreationFlags.None.html));
            GetComponent<[Renderer](Renderer.html)>().material.mainTexture = texture;
        }
    }
    

Each graphics card may not support all usages across formats. Use
[SystemInfo.IsFormatSupported](SystemInfo.IsFormatSupported.html) to check
which usages the graphics card supports.  
  
Additional resources:
[SystemInfo.GetGraphicsFormat](SystemInfo.GetGraphicsFormat.html),
[Texture2D](Texture2D.html), [texture assets](../Manual/Textures.html).

### Properties

[LDR](Experimental.Rendering.DefaultFormat.LDR.html)| Represents the default
platform-specific LDR format. If the project uses the linear rendering mode,
the actual format is sRGB. If the project uses the gamma rendering mode, the
actual format is UNorm.  
---|---  
[HDR](Experimental.Rendering.DefaultFormat.HDR.html)| Represents the default
platform specific HDR format.  
[DepthStencil](Experimental.Rendering.DefaultFormat.DepthStencil.html)|
Represents the default platform-specific depth stencil format.  
[Shadow](Experimental.Rendering.DefaultFormat.Shadow.html)| Represents the
default platform specific shadow format.  
[Video](Experimental.Rendering.DefaultFormat.Video.html)| Represents the
default platform specific video format.  
  
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

